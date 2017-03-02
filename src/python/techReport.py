#!/usr/bin/env python

import os
import json
import re
import sys
import datetime
from core.Config import conf

from core.projects.LangProject import LangProject
from core.projects.MathProject import MathProject
from core.projects.ChartProject import ChartProject
from core.projects.TimeProject import TimeProject
from core.projects.ClosureProject import ClosureProject

reload(sys)
sys.setdefaultencoding('Cp1252')

tools = ["Nopol", "Brutpol", "Genprog", "Kali"]

ignored = {
    "Math": [99],
    "Chart": [8]
}
root = conf.resultsRoot
resultsAll = {}
rankingAll = {}

nbError = 0
nbEmpty = 0
nbTimeout = 0
fixedBugs = 0
totalBugs = 0
totalExecutionTime = 0

patchCount = 0
count = {}
body = ""

print ""

def project_to_obj(project):
    if project == "Math":
        return MathProject()
    if project == "Lang":
        return LangProject()
    if project == "Time":
        return TimeProject()
    if project == "Chart":
        return ChartProject()
    if project == "Closure":
        return ClosureProject()

def get_tool_name(tool):
    if tool == "Ranking":
        return None
    elif tool == "BrutpolC" and "BrutpolPC" in tools:
        return None
    elif tool == "NopolC" and "NopolPC" in tools:
        return None
    elif tool == "Brutpol":
        tool = "DynaMoth"
    elif tool == "NopolPC" and "NopolC" in tools:
        tool = "Nopol"
    elif tool == "Genprog":
        tool = "jGenProg"
    elif tool == "Kali":
        tool = "jKali"
    return tool

def getResultsByTool():
    output = {}
    for project in sorted(os.listdir(root)):
        projectPath = os.path.join(root, project)
        if os.path.isfile(projectPath):
            continue
        for bugId in sorted(os.listdir(projectPath), key=lambda k: int(k) if k.isdigit() else k):
            bugPath = os.path.join(projectPath, bugId)
            if not bugId.isdigit() or os.path.isfile(bugPath):
                continue
            bugId = int(bugId) 
            resultsBugPath = os.path.join(bugPath, "results.json")
            for (index, tool) in enumerate(tools):
                if tool == "Ranking":
                    continue
                toolPath = os.path.join(bugPath, tool)
                if os.path.isfile(toolPath):
                    continue
                resultsToolPath = os.path.join(toolPath, "results.json")
                stderrToolPath = os.path.join(toolPath, "stderr.log")
                stdoutToolPath = os.path.join(toolPath, "stdout.log")
                tool = get_tool_name(tool)
                if os.path.exists(resultsToolPath):
                    with open(resultsToolPath) as data_file:
                        values = json.load(data_file)
                        if 'nbAngelicValue' in values and values['nbAngelicValue'] is None:
                            values['nbAngelicValue'] = 0

                        if tool in output and project in output[tool] and bugId in output[tool][project] and'nbAngelicValue' in output[tool][project][bugId] and 'nbAngelicValue' in values:
                            output[tool][project][bugId]['nbAngelicValue'] += values['nbAngelicValue']
                            values['nbAngelicValue'] = output[tool][project][bugId]['nbAngelicValue']
                        if (tool == "Nopol" and
                                tool in output and 
                                project in output[tool] and 
                                bugId in output[tool][project] and
                                "patches" in output[tool][project][bugId] and
                                len(output[tool][project][bugId]["patches"]) > 0):
                            continue
                        if (tool == "DynaMoth" and
                                tool in output and 
                                project in output[tool] and 
                                bugId in output[tool][project] and
                                "patches" in output[tool][project][bugId] and
                                len(output[tool][project][bugId]["patches"]) > 0):
                            continue
                        if "patch" in values:
                            if values["patch"] is not None:
                                values["patches"] = values["patch"]
                            else:
                                values["patches"] = []
                            values.pop("path", None)
                            values.pop("patchLocation", None)
                        else:
                            values["patches"] = []
                        if "operations" in values:
                            values["patches"] = values["operations"]
                            values.pop("operations", None)
                        if "timeTotal" in values:
                            values["executionTime"] = values["timeTotal"]
                            values.pop("timeTotal", None)
                        if tool not in output:
                            output[tool] = {}
                        if project not in output[tool]:
                            output[tool][project] = {}
                        output[tool][project][bugId] = values
                elif (tool in output and project in output[tool] and bugId not in output[tool][project]):
                    if tool not in output:
                        output[tool] = {}
                    if project not in output[tool]:
                        output[tool][project] = {}
                    output[tool][project][bugId] = None
    return output

def formatDuration(duration):
    output = ""
    duration = duration / 1000
    days = duration // 86400
    hours = duration // 3600 % 24
    minutes = duration // 60 % 60
    seconds = duration % 60
    if days > 1:
        output += "%d days, " % days
    elif days == 1:
        output += "1 day, "
    if hours > 1:
        output += "%d hours, " % hours
    elif hours == 1:
        output += "1 hour, "
    if minutes > 1:
        output += "%d minutes, " % minutes
    elif minutes == 1:
        output += "1 minute, "
    if seconds > 1:
        output += "%d seconds  " % seconds
    elif seconds == 1:
        output += "1 second  "
    return output[0:-2]

results = getResultsByTool()
for tool in results:
    count = 0
    countFixed = 0
    projectCount = {}
    for project in results[tool]:
        if project not in projectCount:
            projectCount[project] = 0
        for bugId in results[tool][project]:
            count += 1
            if results[tool][project][bugId] is not None and len(results[tool][project][bugId]["patches"]) > 0:
                countFixed += 1
                projectCount[project] += 1

    body += "{0:} generates {1:} patches for the {2:} bugs of Defects4J.\n\n".format(tool, countFixed, count)

    body += """
\\begin{table}[!t] 
\caption{The number of generated patches for each project.}
\label{tab:defects4j}
\centering
%\\resizebox{0.5\\textwidth}{!}{
%\setlength\\tabcolsep{0.4 ex}
\\begin{tabular}{|c|r|r|r|}

\hline
Project & \# Patches & \# Bugs & Repair Rate \\\\ \hline\hline
"""
    for project in sorted(results[tool]):
        body += "{0:} & {1:} & {2:} & {3:}\%\\\\\n".format(project, projectCount[project], len(results[tool][project]), projectCount[project]*100/len(results[tool][project]))
    body += "\hline\n"
    body += "{0:} & {1:} & {2:} & {3:}\%\\\\\n".format("Total", countFixed, count, countFixed*100/count)
    body += """
\hline

\end{tabular}
%}
\end{table}
"""

    for project in sorted(results[tool]):
        body += "\section{{{0:}}}\label{{{0:}}}\n\n".format(project)
        body += "{0:} repairs {1:} bugs in the project {2:}.\n\n".format(tool, projectCount[project], project)
        for bugId in sorted(results[tool][project].iterkeys()):
            if results[tool][project][bugId] is not None and len(results[tool][project][bugId]["patches"]) > 0:
                body += "\subsection{{{0:} {1:}}}\label{{{0:}_{1:}}}\n".format(project, bugId)
                for patch in results[tool][project][bugId]["patches"]:
                    body += "\n\\begin{lstlisting}[language=diff,caption=\"%s\", label=\"%s\"]\n%s\n\\end{lstlisting}\n\n" % (
                                "The generated patch for the bug %s %s" % (project, bugId),
                                "fig:%s_%s" % (project, bugId),
                                patch['patch'])
                    body += "Number of tests that execute the patch: %d\n\n" % patch['nb_test_that_execute_statement']
                if 'executionTime' in results[tool][project][bugId]:
                    body += "Execution time: %s\n\n" % formatDuration(results[tool][project][bugId]['executionTime'])
print body