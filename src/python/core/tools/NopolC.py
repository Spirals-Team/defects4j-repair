from core.tools.Nopol import Nopol

class NopolC(Nopol):
	"""docstring for NopolC"""
	def __init__(self):
		super(NopolC, self).__init__("NopolC")

	def run(self, project, id):
		log = self.runNopol(project, id, mode="repair", type="condition", oracle="angelic")
		slittedLog = log.split('----INFORMATION----')
		if(len(slittedLog) > 1):
			print slittedLog[1]
			self.parseLog(slittedLog[1], project, id)