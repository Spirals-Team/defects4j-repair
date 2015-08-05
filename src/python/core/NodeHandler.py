import os
import sys
import time
import subprocess

class NodeHandler(object):
	"""docstring for NodeHandler"""
	def __init__(self, tasks):
		self.maxNode = 50
		self.tasks = tasks
		self.running = 0

	def run(self, timeoutNode=None):
		totalTask = len(self.tasks)
		startTime = time.time()
		print "Execute %d tasks" % totalTask
		while(len(self.tasks) > 0):
			self.getRunning()
			if self.running < self.maxNode:
				task = self.tasks.pop()
				filename = task.project.name.lower() + '_' + str(task.id)
				stdoutlog =  os.path.join(task.project.logPath, str(task.id), task.tool.name, 'stdout.log')
				stderrlog =  os.path.join(task.project.logPath, str(task.id), task.tool.name, 'stderr.log')
				resultlog =  os.path.join(task.project.logPath, str(task.id), task.tool.name, 'results.json')

				if not os.path.exists(os.path.dirname(stdoutlog)):
					os.makedirs(os.path.dirname(stdoutlog))

				if not os.path.exists(os.path.dirname(stderrlog)):
					os.makedirs(os.path.dirname(stderrlog))

				cmd = 'rm %s; ' % stdoutlog
				cmd += 'rm %s; ' % stderrlog
				cmd += 'rm %s; ' % resultlog

				nodeCmdArgs = "%s -p %s -t %s -i %d" % (
					os.path.join(os.path.dirname(__file__), '..', 'defects4j-g5k-node.py'),
					task.project.name,
					task.tool.name,
					task.id
				)
				nodeCmd = "python %s" % nodeCmdArgs 

				# cmd += path
				cmd += "oarsub -l nodes=1,walltime=%s -O %s -E %s \"%s\"" % (
					timeoutNode if timeoutNode else task.tool.maxExecution,
					stdoutlog,
					stderrlog,
					nodeCmd
				)
				devnull = open('/dev/null', 'w')
				temp = subprocess.call(cmd, shell=True, stdin=None, stdout=devnull, stderr=devnull)
				self.running += 1
				self.printStatus(totalTask, startTime)
			else:
				time.sleep( 5 )
				self.getRunning()
				self.printStatus(totalTask, startTime)
		while(True):
			self.getRunning()
			self.printStatus(totalTask, startTime)
			if self.running > 0:
				time.sleep( 5 )
			else:
				break
		print "Execute %d tasks in %2.2f sec" % (totalTask, time.time() - startTime)
	def printStatus(self, totalTask, startTime):
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[K")
		print("%d tasks to run, %d tasks running, %2.2f%% completed (running for %2.2f sec)" % (len(self.tasks),self.running,(totalTask-len(self.tasks)-self.running)/float(totalTask)*100, time.time() - startTime))
	def getRunning(self):
		cmd = 'oarstat -u | grep `whoami` | wc -l'
		devnull = open('/dev/null', 'w')
		output = subprocess.check_output(cmd,shell=True, stdin=None, stderr=devnull)
		self.running = int(output)
