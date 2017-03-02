import os
from os.path import expanduser

class Config(object):
	"""Runner configurations"""
	def __init__(self):
		defects4jRepairRoot = os.path.join(os.path.dirname(__file__),'../../../' )

		self.defects4jRepairRoot = defects4jRepairRoot
		self.projectsRoot = expanduser("/mnt/secondary/projects")
		self.defects4jRoot = expanduser("~/git/defects4j")
		self.resultsRoot = os.path.join(defects4jRepairRoot, "results/2016-november")
		self.z3Root = os.path.join(defects4jRepairRoot, "libs", "z3")
		self.javaHome = expanduser("/usr/lib/jvm/java-7-openjdk-amd64/bin/")
		self.javaHome8 = expanduser("/usr/lib/jvm/jdk1.8.0_73/bin/")
		self.javaArgs = "-Xmx4096m"

conf = Config()
