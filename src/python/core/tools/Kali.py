import json
import re
import os
import subprocess
from core.tools.Astor import Astor
from pprint import pprint

class Kali(Astor):
	"""docstring for Kali"""
	def __init__(self):
		super(Kali, self).__init__(name="Kali")

	def run(self, 
		project, 
		id):
		self.runAstor(project, id, mode="statement-remove")