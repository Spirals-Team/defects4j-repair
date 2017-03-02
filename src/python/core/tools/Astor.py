import json
import re
import os
import subprocess
import datetime
from core.Tool import Tool
from core.Config import conf
from pprint import pprint

class Astor(Tool):
	"""docstring for Astor"""
	def __init__(self, name="Genprog"):
		super(Astor, self).__init__(name, "astor")
		self.maxExecution = "01:30:00"

	def runAstor(self, 
		project, 
		id,
		mode="statement",
		maxgen="1000000",
		population="1",
		seed="10"):
		source = None
		for index, src in project.src.iteritems():
			if id <= int(index):
				source = src
				break
		cmdInfo = 'export PATH="' + conf.defects4jRoot + '/framework/bin:$PATH";'
		cmdInfo += 'defects4j info -p ' + project.name + ' -b ' + str(id)
		info = subprocess.check_output(cmdInfo, shell=True)

		# extracts failing test cases
		failingTest = ""
		reg = re.compile('- (.*)::(.*)')
		m = reg.findall(info)
		for i in m:
			failingTest += i[0] + ":"    

		workdir = self.initTask(project, id)
		cmd = 'cd ' + workdir +  ';'
		cmd += 'export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8;'
		cmd += 'TZ="America/New_York"; export TZ'
		cmd += 'export PATH="' + conf.javaHome8 + ':$PATH";'
		cmd += 'time java %s -cp %s %s' % (conf.javaArgs, self.jar, self.main)
		cmd += ' -mode ' + mode
		cmd += ' -location .' 
		cmd += ' -dependencies lib/'
		cmd += ' -failing ' + failingTest
		cmd += ' -package ' + project.package
		cmd += ' -jvm4testexecution ' + conf.javaHome8
		cmd += ' -javacompliancelevel ' + str(project.complianceLevel[str(id)]['source'])
		cmd += ' -maxgen ' + maxgen
		cmd += ' -seed ' + seed
		cmd += ' -maxtime %d ' % (60)
		cmd += ' -scope local '
		cmd += ' -stopfirst false'
		cmd += ' -flthreshold 0'
		cmd += ' -population ' + population 
		cmd += ' -srcjavafolder ' + source['srcjava']
		cmd += ' -srctestfolder ' + source['srctest']
		cmd += ' -binjavafolder ' + source['binjava']
		cmd += ' -bintestfolder ' + source['bintest'] + ';'

		path = os.path.join(project.logPath, str(id), self.name, 'result')
		print path
		if not os.path.exists(os.path.dirname(path)):
			os.makedirs(os.path.dirname(path))
		#cmd += 'cp -r outputMutation/ ' + os.path.dirname(path) + ';'
		cmd += 'echo "\n\nNode: `hostname`\n";'
		cmd += 'echo "\nDate: `date`\n";'
		cmd += 'rm -rf ' + workdir +  ';'

		logPath = os.path.join(project.logPath, str(id), self.name, "stdout.log.full")
		logFile = file(logPath, 'w')
		print cmd
		subprocess.call(cmd, shell=True, stdout=logFile)
		with open(logPath) as data_file:
			log = data_file.read()
			slittedLog = log.split('----SUMMARY_EXECUTION---')
			if(len(slittedLog) > 1):
				print slittedLog[1]
				self.parseLog(slittedLog[1], project, id)
			else:
				slittedLog = log.split('End Repair Loops:')
				if(len(slittedLog) > 1):
					print slittedLog[1]
					self.parseLog(slittedLog[1], project, id)
		

	def run(self, 
		project, 
		id):
		self.runAstor(project, id)

	def parseLog(self, log, project, id):
		programVariant = None
		timeEvaluation = None
		timeTotal = None
		date = datetime.datetime.now().isoformat()
		node = self.getHostname()

		m = re.search('ProgramVariant ([0-9]+)', log)
		if m:
			programVariant = m.group(1)
		m = re.search('Time Evolution\(ms\): ([0-9]+)', log)
		if m:
			timeEvaluation = m.group(1)
		m = re.search('Time Total\(ms\): ([0-9]+)', log)
		if m:
			timeTotal = m.group(1)
		else:
			return
		m = re.search('Node: ([a-zA-Z0-9\-\.]+)', log)
		if m:
			node = m.group(1)
		m = re.search('Date: ([^`]+)$', log)
		if m:
			date = m.group(1)

		operations = []

		operationsSplit = log.split('ProgramVariant ')
		if(len(operationsSplit) > 1):
			for op in operationsSplit:
				generation = None
				className = None
				line = None
				patch = None
				buggyStatement = None
				type = None
				variant = 0
				m = re.search('^([0-9]+)$', op, flags=re.MULTILINE+re.DOTALL)
				if m:
					variant = m.group(1)
				m = re.search('(REPLACE|DELETE|INSERT_BEFORE)', op)
				if m:
					type = m.group(1)
				m = re.search('location= (.*)', op)
				if m:
					className = m.group(1)
				else:
					continue
				m = re.search('line= ([0-9]+)', op)
				if m:
					line = m.group(1)
				m = re.search('^original statement= "?(.*)"?\nfixed statement', op, flags=re.MULTILINE+re.DOTALL)
				if m:
					buggyStatement = m.group(1)
				m = re.search('^fixed statement= "?(.*)"?\ngeneration', op, flags=re.MULTILINE+re.DOTALL)
				if m:
					patch = m.group(1)
				if type == "DELETE":
					patch = 'remove'
				m = re.search('generation= ([0-9]+)', op)
				if m:
					generation = m.group(1)
				if(patch == None):
					continue
				operations.append({
					'type': type,
					'generation': int(generation),
					'variant': int(variant),
					'patchLocation': {
						'className': className,
						'line': int(line)
					},
					'patch': patch,
					'buggyStatement': buggyStatement
				})

		results = {
			'programVariant': programVariant,
			'operations': operations,
			'timeEvaluation': timeEvaluation,
			'timeEvaluation': timeEvaluation,
			'timeTotal': timeTotal,
			'node': node,
			'date': date
		}
		reg = re.compile('#([a-zA-Z]+) *: *([0-9]+)')
		m = reg.findall(log)
		for i in m:
			results[i[0]] = i[1]
		reg = re.compile("time val([0-9]+) \[[0-9]+\]: \[([0-9, ]+)\]")
		m = reg.findall(log)
		for i in m:
			results["timeVal" + i[0]] = []
			t = re.compile('([0-9]+)')
			v = t.findall(i[1])
			for j in v:
				results["timeVal" + i[0]].append(int(j))
			

		path = os.path.join(project.logPath, str(id), self.name, "results.json")
		if not os.path.exists(os.path.dirname(path)):
			os.makedirs(os.path.dirname(path))
		file = open(path, "w")
		file.write(json.dumps(results, indent=4, sort_keys=True))
		file.close()
