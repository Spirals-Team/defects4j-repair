import json
import re
import os
import subprocess
import datetime
from core.Tool import Tool
from core.Config import conf
from pprint import pprint

class Nopol(Tool):
    """docstring for Nopol"""
    def __init__(self, name="Nopol"):
        super(Nopol, self).__init__(name, "nopol")
        self.solverPath = self.data["solverPath"].replace("<defects4j-repair>", conf.defects4jRepairRoot)
        self.solver = self.data["solver"]

    def run(self, project, id):
        log = self.runNopol(project, id, mode="repair", type="pre_then_cond", oracle="angelic")
        slittedLog = log.split('----INFORMATION----')
        if(len(slittedLog) > 1):
            print slittedLog[1]
            self.parseLog(slittedLog[1], project, id)

    def runNopol(self, project, id, mode="repair", type="pre_then_cond", synthesis="smt", oracle="angelic"):
        workdir = self.initTask(project, id)
        classpath = ""
        for index, cp in project.classpath.iteritems():
            if id <= int(index):
                for c in cp.split(":"):
                    if classpath != "":
                        classpath += ":"    
                    classpath += os.path.join(workdir, c) 
                break
        source = ""
        for index, src in project.src.iteritems():
            if id <= int(index):
                source = os.path.join(workdir, src['srcjava'])
                # source += " " + src['srctest']
                break
        for lib in project.libs:
            if os.path.exists(os.path.join(workdir, "lib", lib)):
                classpath += ":" + os.path.join(workdir, "lib", lib)
        classpath += ":" + self.jar
        
        cmd = 'cd ' + workdir +  ';'
        cmd += 'export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8;'
        cmd += 'TZ="America/New_York"; export TZ;'
        cmd += 'export PATH="' + conf.javaHome + ':$PATH";'
        cmd += 'cp -r ' + conf.z3Root + ' lib/z3;'
        cmd += 'time java %s -cp %s:%s/../lib/tools.jar %s' % (conf.javaArgs, self.jar, conf.javaHome, self.main)
        cmd += ' --flocal gzoltar '
        cmd += ' --maxTime 300 '
        cmd += ' --json '
        cmd += ' --mode ' + mode
        cmd += ' --type ' + type
        cmd += ' --oracle ' + oracle
        cmd += ' --synthesis ' + synthesis
        cmd += ' --solver ' + self.solver 
        cmd += ' --solver-path ' + self.solverPath 
        cmd += ' --complianceLevel ' + str(project.complianceLevel[str(id)]['source'])
        cmd += ' --source ' + source 
        cmd += ' --classpath ' + classpath + ';'
        cmd += 'echo "\n\nNode: `hostname`\n";'
        cmd += 'echo "\nDate: `date`\n";'
        logPath = os.path.join(project.logPath, str(id), self.name, "stdout.log.full")
        if not os.path.exists(os.path.dirname(logPath)):
            os.makedirs(os.path.dirname(logPath))
        log = file(logPath, 'w')
        print cmd
        subprocess.call(cmd, shell=True, stdout=log)
        with open(logPath) as data_file:
            return data_file.read()


    def parseLog(self, log, project, id):
        workdir = os.path.join("/tmp/", "%s_%d_%s"% (project.name.lower(), id, self.name))
        results = {}
        with open(os.path.join(workdir, "output.json")) as data_file:
            results = json.load(data_file)
        results['node'] = self.getHostname()
        subprocess.call('rm -rf ' + workdir +  ';', shell=True)
        
        path = os.path.join(project.logPath, str(id), self.name, "results.json")
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        file = open(path, "w")
        file.write(json.dumps(results, indent=4, sort_keys=True))
        file.close()
