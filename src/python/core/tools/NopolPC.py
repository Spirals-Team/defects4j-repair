from core.tools.Nopol import Nopol

class NopolPC(Nopol):
	"""docstring for NopolPC"""
	def __init__(self):
		super(NopolPC, self).__init__("NopolPC")

	def run(self, project, id):
		log = self.runNopol(project, id, mode="repair", type="precondition", oracle="angelic")
		slittedLog = log.split('----INFORMATION----')
		if(len(slittedLog) > 1):
			print slittedLog[1]
			self.parseLog(slittedLog[1], project, id)