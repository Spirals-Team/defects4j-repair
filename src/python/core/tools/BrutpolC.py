from core.tools.Nopol import Nopol

class BrutpolC(Nopol):
	"""docstring for BrutpolC"""
	def __init__(self):
		super(BrutpolC, self).__init__("BrutpolC")

	def run(self, project, id):
		log = self.runNopol(project, id, mode="repair", type="condition", oracle="angelic", synthesis="dynamoth")
		slittedLog = log.split('----INFORMATION----')
		if(len(slittedLog) > 1):
			print slittedLog[1]
			self.parseLog(slittedLog[1], project, id)