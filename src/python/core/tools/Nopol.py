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
    def __init__(self, name):
        super(Nopol, self).__init__(name, "nopol")
        self.solverPath = self.data["solverPath"].replace("<defects4j-repair>", conf.defects4jRepairRoot)
        self.solver = self.data["solver"]

    def runNopol(self, project, id, mode="repair", type="condition", synthesis="smt", oracle="angelic"):
        classpath = ""
        for index, cp in project.classpath.iteritems():
            if id <= int(index):
                classpath = cp
                break
        source = ""
        for index, src in project.src.iteritems():
            if id <= int(index):
                source = src['srcjava']
                # source += " " + src['srctest']
                break
        for lib in project.libs:
            classpath += ":lib/" + lib
        classpath += ":" + self.jar
        workdir = self.initTask(project, id)
        cmd = 'cd ' + workdir +  ';'
        cmd += 'export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8;'
        cmd += 'export PATH="' + conf.javaHome + ':$PATH";'
        cmd += 'cp -r ' + conf.z3Root + ' lib/z3;'
        cmd += 'time java %s -cp %s:%s/../lib/tools.jar %s' % (conf.javaArgs, self.jar, conf.javaHome, self.main)
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
        cmd += 'rm -rf ' + workdir +  ';'
        logPath = os.path.join(project.logPath, str(id), self.name, "stdout.log.full")
        if not os.path.exists(os.path.dirname(logPath)):
            os.makedirs(os.path.dirname(logPath))
        log = file(logPath, 'w')
        print cmd
        subprocess.call(cmd, shell=True, stdout=log)
        with open(logPath) as data_file:
            return data_file.read()


    def parseLog(self, log, project, id):
        nbStatement = None
        nbAngelic = None
        nbInput = None
        nbVariable = None
        executionTime = None
        className = None
        line = None
        patchType = None
        patch = None
        date = datetime.datetime.now().isoformat()
        node = self.getHostname()

        m = re.search('Nb Statements Analyzed : ([0-9]+)', log)
        if m:
            nbStatement = int(m.group(1))
        else:
            return
        m = re.search('Nb Statements with Angelic Value Found : ([0-9]+)', log)
        if m:
            nbAngelic = int(m.group(1))
        m = re.search('Nb inputs in SMT : ([0-9]+)', log)
        if m:
            nbInput = int(m.group(1))
        m = re.search('Nb variables in SMT : ([0-9]+)', log)
        if m:
            nbVariable = int(m.group(1))
        m = re.search('NoPol Execution time : ([0-9]+)ms', log)
        if m:
            executionTime = int(m.group(1))
        m = re.search('----PATCH FOUND----\n([^:]+):([0-9]+): ([^ ]+) (.+)', log)
        if m:
            className = m.group(1)
            line = int(m.group(2))
            patchType = m.group(3)
            patch = m.group(4)
        m = re.search('Node: ([a-zA-Z0-9\-\.]+)', log)
        if m:
            node = m.group(1)
        m = re.search('Date: ([^`]+)$', log)
        if m:
            date = m.group(1)
        
        results = {
            'nbStatement': nbStatement,
            'nbAngelicValue': nbAngelic,
            'nbSMTInput': nbInput,
            'nbSMTVariable': nbVariable,
            'executionTime': executionTime,
            'patchLocation': {
                'className': className,
                'line': line
            },
            'patchType': patchType,
            'patch': patch,
            'node': node,
            'date': date
        }
        path = os.path.join(project.logPath, str(id), self.name, "results.json")
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        file = open(path, "w")
        file.write(json.dumps(results, indent=4, sort_keys=True))
        file.close()
