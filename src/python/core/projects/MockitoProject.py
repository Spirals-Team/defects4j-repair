import subprocess
from core.Project import Project
from core.Defects4j import Defects4j
from core.Config import conf


class MockitoProject(Project):
    """Representation of the Mockito project"""

    def __init__(self):
        super(MockitoProject, self).__init__("Mockito")

    def compile(self, workingDirecotory):
		cmd = 'export PATH="' + Defects4j().getBinPath() + ':$PATH";'
		cmd += 'export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8;'
		cmd += 'export PATH="' + conf.javaHome8 + ':$PATH";'
		cmd += 'cd ' + workingDirecotory +';'
		cmd += 'defects4j compile;'
		return subprocess.check_call(cmd, shell=True)