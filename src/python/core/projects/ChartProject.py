from core.Project import Project

class ChartProject(Project):
	"""docstring for ChartProject"""
	def __init__(self):
		super(ChartProject, self).__init__("Chart")
		self.maxExecution = "01:00:00"
