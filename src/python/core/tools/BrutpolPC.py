from core.tools.Nopol import Nopol

class BrutpolPC(Nopol):
	"""docstring for BrutpolPC"""
	def __init__(self):
		super(BrutpolPC, self).__init__("BrutpolPC")

	def run(self, project, id):
		log = self.runNopol(project, id, mode="repair", type="precondition", oracle="angelic", synthesis="dynamoth")
		slittedLog = log.split('----INFORMATION----')
		if(len(slittedLog) > 1):
			print slittedLog[1]
			self.parseLog(slittedLog[1], project, id)