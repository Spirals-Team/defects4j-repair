import os
import json
import collections

class RunnerTask(object):
	"""docstring for NodeHandler"""
	def __init__(self, tool, project, id):
		self.tool = tool
		self.project = project
		self.id = id
