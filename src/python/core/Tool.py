import json
import os
import subprocess
from pprint import pprint
from core.Config import conf
from os.path import expanduser

class Tool(object):
	"""Repair tool"""
	def __init__(self, name, configName):
		self.name = name
		self.configName = configName
		self.maxExecution = "01:00:00"
		self.parseData();

	def parseData(self):
		path = os.path.join(os.path.dirname(__file__),'../data/tools', self.configName + '.json' )
		with open(path) as data_file:
			self.data = json.load(data_file)
			self.main = self.data["main"]
			self.jar = expanduser(self.data["jar"].replace("<defects4j-repair>", conf.defects4jRepairRoot))
		pass

	def initTask(self, project, id):
		workdir = os.path.join("/tmp/", "%s_%d_%s"% (project.name.lower(), id, self.name))
		cmd = 'cp -r ' + conf.projectsRoot + '/' + project.name.lower() + '/' + project.name.lower() + '_' + str(id) + ' ' + workdir +  ';'
		cmd += 'cd ' + workdir +';'
		cmd += 'mkdir lib/;'
		cmd += 'cp -r ' + conf.defects4jRoot + '/framework/projects/lib/* lib/;'
		cmd += 'cp -r ' + conf.defects4jRoot + '/framework/projects/' + project.name + '/lib/* lib/;'
		cmd += 'find . -type f -name "package-info.java" -delete;'

		subprocess.check_output(cmd, shell=True)
		project.compile(workdir)
		return workdir

	def getHostname(self):
		cmd = 'hostname;'
		return subprocess.check_output(cmd, shell=True)
	
	def __str__(self):
		return self.name