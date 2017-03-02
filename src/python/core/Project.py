import os
import json
import collections
import subprocess
from core.Defects4j import Defects4j
from core.Config import conf
from os.path import expanduser

class Project(object):
	"""Defects4j Project"""
	def __init__(self, name):
		self.logPath = os.path.join(conf.resultsRoot, name)
		self.name = name
		self.parseData()

	def parseData(self):
		path = os.path.join(os.path.dirname(__file__),'../data/projects', self.name.lower() + '.json' )
		with open(path) as data_file:
			self.data = json.load(data_file)
			self.src = collections.OrderedDict(sorted(self.data["src"].items(), key=lambda t: int(t[0])))
			self.libs = self.data["libs"]
			self.package = self.data["package"]
			self.nbBugs = self.data["nbBugs"]
			self.complianceLevel = self.data["complianceLevel"]
			self.classpath = collections.OrderedDict(sorted(self.data["classpath"].items(), key=lambda t: int(t[0])))
			self.angelicValue = self.data["angelicValue"]
		pass

	def compile(self, workingDirecotory):
		cmd = 'export PATH="' + Defects4j().getBinPath() + ':$PATH";'
		cmd += 'export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8;'
		cmd += 'export PATH="' + conf.javaHome + ':$PATH";'
		cmd += 'cd ' + workingDirecotory +';'
		cmd += 'defects4j compile;'
		return subprocess.check_call(cmd, shell=True)

	def getSource(self, id):
		for index, src in self.src.iteritems():
			if id <= int(index):
				return src['srcjava']
		return ""

	def __str__(self):
		return self.name
