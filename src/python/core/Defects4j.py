import json
import os
import subprocess
from pprint import pprint
from core.Config import conf
from os.path import expanduser

class Defects4j(object):
	def __init__(self):
		pass

	def getBinPath(self):
		return conf.defects4jRoot + '/framework/bin'