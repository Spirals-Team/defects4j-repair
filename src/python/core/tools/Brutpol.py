from core.tools.Nopol import Nopol

class Brutpol(Nopol):
	"""docstring for BrutpolC"""
	def __init__(self):
		super(Brutpol, self).__init__("Brutpol")

	def run(self, project, id):
		log = self.runNopol(project, id, mode="repair", type="pre_then_cond", oracle="angelic", synthesis="dynamoth")
		slittedLog = log.split('----INFORMATION----')
		if(len(slittedLog) > 1):
			print slittedLog[1]
			self.parseLog(slittedLog[1], project, id)