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

reload(sys)  
sys.setdefaultencoding('Cp1252')

tools = ["NopolPC", "NopolC", "Genprog", "Kali"]

ignored = {
	"Math": [99],
	"Chart": [8]
}
root = conf.resultsRoot
resultsAll = {}
resultsAllPath = os.path.join(root, "results.json")
resultsMdPath = os.path.join(root, "readme.md")
detailedResultsMdPath = os.path.join(root, "detailed-results.md")
resultsTexPath = os.path.join(root, "results.tex")
rankingAll = {}

nbError = 0
nbEmpty = 0
nbTimeout = 0
fixedBugs = 0
totalBugs = 0
totalExecutionTime = 0

count = {}
result = "# All fixed bugs\n\n"
body = ""
line = " #   | BugId             | "
texTable = """\\begin{table}[!t]
\label{tab:bugs_summary}
\centering
\\resizebox{0.5\\textwidth}{!}{
\setlength\\tabcolsep{0.3 ex}
\\begin{tabular}{|c|c|c|c|c|c|}
\hline 
Bug id            & """

def projectToObj(project):
	if project == "Math":
		return MathProject()
	if project == "Lang":
		return LangProject()
	if project == "Time":
		return TimeProject()
	if project == "Chart":
		return ChartProject()
def getToolName(tool):
	if tool == "Ranking":
		return None
	elif tool == "BrutpolC" and "BrutpolPC" in tools:
		return None
	elif tool == "NopolC" and "NopolPC" in tools:
		return None
	elif tool == "BrutpolPC" and "BrutpolC" in tools:
		tool = "Brutpol"
	elif tool == "NopolPC" and "NopolC" in tools:
		tool = "Nopol"
	elif tool == "Genprog":
		tool = "jGenProg"
	elif tool == "Kali":
		tool = "jKali"
	return tool
def getToolsHeader(tools, separator = "|"):
	results = ""
	for tool in sorted(tools):
		tool = getToolName(tool)
		if tool == None:
			continue
		results += "{0:9} {1:1} ".format(tool, separator)
	return results

line += getToolsHeader(tools, "|")
texTable += getToolsHeader(tools, "&")

tableHeader = "%sTotal\n---- | ----------------- | " % line
texTable += "Total \\\\\n\\hline\n"
for tool in tools:
	tool = getToolName(tool)
	if tool == None:
		continue
	tableHeader += "--------- | "
tableHeader += "------\n"
result += tableHeader
resultSimple = result

fullTable = tableHeader
simpleTable = tableHeader
body = ""
print("Start the output proccess")
bugCount = 0
patchCount = 0
commits = {}

pathCommitId = os.path.join(os.path.dirname(__file__),'data/commitID.json')
with open(pathCommitId) as data_file:
	commits = json.load(data_file)

for project in sorted(os.listdir(root)):
	projectPath = os.path.join(root, project) 
	if os.path.isfile(projectPath):
		continue
	projectobj = projectToObj(project)
	smallName = project[0]
	resultsProject = {}
	rankingBug = {}
	for bugId in sorted(os.listdir(projectPath), key = lambda k: int(k) if k.isdigit() else k):
		bugPath = os.path.join(projectPath, bugId) 
		if not bugId.isdigit() or os.path.isfile(bugPath):
			continue
		bugId = int(bugId)
		bugCount += 1

		sys.stdout.write("\033[F")
		sys.stdout.write("\033[K")
		print "Process: %s %d" %(project, bugId)
		
		ranking = None

		totalBugs += 1
		line = " {0:3} | {1:17} |"
		lineArgs = []
		texLineArgs = []
		texLineTable = "{0:17} &"
		lineArgs += [bugCount, "[%s%d](#%s-%s)" % (smallName, bugId, project.lower(), bugId)]
		texLineArgs += ["%s%d"  % (smallName, bugId)]
		lineCount = 0

		resultsBugPath = os.path.join(bugPath, "results.json")
		resultsBug = {}

		if project in ignored and bugId in ignored[project]:
			for (index, tool) in enumerate(tools):
				tool = getToolName(tool)
				if tool == None:
					continue
				resultsBug[tool] = {
					"error": "IGNORED"
				}
		else:
			for (index, tool) in enumerate(tools):
				if tool == "Ranking":
					continue
				toolPath = os.path.join(bugPath, tool)
				if os.path.isfile(toolPath):
					continue
				resultsToolPath = os.path.join(toolPath, "results.json")
				stderrToolPath = os.path.join(toolPath, "stderr.log")
				stdoutToolPath = os.path.join(toolPath, "stdout.log")
				if os.path.exists(resultsToolPath):
					with open(resultsToolPath) as data_file:
						if (tool == "NopolC" and 
							"Nopol" in resultsBug and 
							"patch" in resultsBug["Nopol"] and 
							resultsBug["Nopol"]["patch"] is not None):
							continue
						if (tool == "BrutpolC" and 
							"Brutpol" in resultsBug and 
							"patch" in resultsBug["Brutpol"] and 
							resultsBug["Brutpol"]["patch"] is not None):
							continue
						
						values = json.load(data_file)
						if tool == "BrutpolC":
							tool = "Brutpol"
						elif tool == "NopolC":
							tool = "Nopol"
						tool = getToolName(tool)
						# ignore the results Math 44 and Math 56
						if (bugId == 44 or bugId == 56) and project == "Math":
							values["operations"] = []
						resultsBug[tool] = values
				elif os.path.exists(stderrToolPath):
					if ("Nopol" in tool and 
						"Nopol" in resultsBug):
						continue
					if ( "Brutpol" in tool and 
						"Brutpol" in resultsBug):
						continue
					if tool == "BrutpolC":
						tool = "Brutpol"
					elif tool == "NopolC":
						tool = "Nopol"
					tool = getToolName(tool)
					with open(stderrToolPath) as data_file:
						data = data_file.read()
						m = re.search("Job [0-9]+ KILLED", data)
						if m:
							resultsBug[tool] = {
								"error": "TIMEOUT"
							}
						elif len(data) == 0:
							resultsBug[tool] = {
								"error": "EMPTY"
							}
						else:
							resultsBug[tool] = {
								"error": "ERROR"
							}
							
				else:
					lineArgs += [""]
					texLineArgs += [""]
					continue
		index = 0
		for tool in sorted(tools):
			tool = getToolName(tool)
			if tool == None:
				continue
			if "error" in resultsBug[tool]:
				if "EMPTY" in resultsBug[tool]["error"]:
					nbEmpty += 1
				elif "TIMEOUT" in resultsBug[tool]["error"]:
					nbTimeout += 1
				elif "ERROR" in resultsBug[tool]["error"]:
					nbError += 1
			index += 1
			line += " {%d:9} |" % (index + 1)
			texLineTable +=  " {%d:9} &" % (index)
			if 'executionTime' in resultsBug[tool] and resultsBug[tool]['executionTime']:
				totalExecutionTime += resultsBug[tool]['executionTime']
			elif 'timeTotal' in resultsBug[tool]:
				if resultsBug[tool]['timeTotal']:
					totalExecutionTime += int(resultsBug[tool]['timeTotal'])
			if (("patch" in resultsBug[tool] and resultsBug[tool]["patch"]) or 
				("operations" in resultsBug[tool] and len(resultsBug[tool]["operations"]) > 0)):
				if ranking is None:
					rankingPath = os.path.join(os.path.join(bugPath, "Ranking"), "results.json")
					if os.path.exists(rankingPath):
						with open(rankingPath) as data_file:
							ranking = json.load(data_file)
					# create the body of the file
					body += "# %s %s\n\n" % (project, bugId)
					if 'executedTest' in ranking:
						body += "Nb Executed tests: %s\n\n" % ranking['executedTest']
					if 'failedTest' in ranking:
						body += "Nb Failing tests: %s\n\n" % ranking['failedTest']
					if 'failedTestDetails' in ranking:
						for test in ranking['failedTestDetails']:
							body += ">\t%s#%s\n" % (test['class'], test['method'])
					body += "\n## Human Patch \n\n"
					path = os.path.join(conf.defects4jRoot, "framework/projects", project, "patches",  "%d.src.patch" % bugId)
					with open(path) as patchFile:
						content = patchFile.read()
						content = re.sub(re.compile(r"^& ", re.IGNORECASE + re.M), "- ", re.sub(re.compile(r"^- ", re.IGNORECASE + re.M), "+ ", re.sub(re.compile(r"^\+ ", re.IGNORECASE + re.M), "& ", content)))
						body += "```Java\n%s\n```\n\n" % (content)
				patchCount += 1
				lineArgs += ["Yes"]
				texLineArgs += ["Fixed"]
				lineCount += 1
				if(not tool in count):
					count[tool] = 1
				else:
					count[tool] += 1

				def getPatchLocation(className, line):
					if project in commits and str(bugId) in commits[project]:
						source = projectobj.getSource(bugId)
						repo = projectobj.data["url"]
						commitID = commits[project][str(bugId)]
						classPath = className.replace(".", "/")
						return "[%s:%s](%s/blob/%s/%s/%s.java#L%s)" % (className, line,repo, commitID, source, classPath, line)
					return "%s:%s" % (className, line)
				body += "## Patch #%d %s \n\n" % (patchCount, tool)
				if "operations" in resultsBug[tool]:
					for operation in resultsBug[tool]["operations"][0:1]:
						lineKey = "%s:%d" % (operation['patchLocation']["className"], operation['patchLocation']["line"])
						pathLocation = getPatchLocation(operation['patchLocation']["className"],operation['patchLocation']["line"])
						if 'suspicious' in ranking and lineKey in ranking['suspicious']:
							ranks = ranking['suspicious'][lineKey]['rank']
							body += "%s (Suspicious rank: " % (pathLocation)
							for rank in ranks:
								body += "%s %d, " % (rank, ranks[rank])
							body += ")\n"
						else:
							body += "%s\n" % (pathLocation)
						if 'type' in operation:
							body+= "\nPatch type: %s \n " % operation["type"]
						body += "\n```Java\n%s\n```\n\n" % (operation["patch"])
				else:
					lineKey = "%s:%d" % (resultsBug[tool]['patchLocation']["className"], resultsBug[tool]['patchLocation']["line"])
					pathLocation = getPatchLocation(resultsBug[tool]['patchLocation']["className"],resultsBug[tool]['patchLocation']["line"])
					if 'suspicious' in ranking and lineKey in ranking['suspicious']:
						ranks = ranking['suspicious'][lineKey]['rank']
						body += "%s (Suspicious rank: " % (pathLocation)
						for rank in ranks:
							body += "%s %d, " % (rank, ranks[rank])
						body += ")\n"
					else:
						body += "%s\n" % (pathLocation)
					body+= "\nPatch type: %s" % resultsBug[tool]["patchType"]
					patch = resultsBug[tool]["patch"]
					if(resultsBug[tool]["patchType"] == "PRECONDITION"):
						patch = "if(%s)" % patch
					body += "\n```Java\n%s\n```\n\n" % (patch)
					body += "Nb Angelic value: %s\n\n" % resultsBug[tool]['nbAngelicValue']
					body += "Nb analyzed Statement: %d\n\n" % resultsBug[tool]['nbStatement']
				if 'executionTime' in resultsBug[tool]:
					body += "Execution time: %s\n\n" % datetime.timedelta(milliseconds=resultsBug[tool]['executionTime'])
				if 'timeTotal' in resultsBug[tool]:
					body += "Execution time: %s\n\n" % datetime.timedelta(milliseconds=int(resultsBug[tool]['timeTotal']))
				if 'node' in resultsBug[tool]:
					body += "Grid5000 node: %s\n\n" % resultsBug[tool]['node']


			elif ("error" in resultsBug[tool]):
				if resultsBug[tool]["error"] != "TIMEOUT":
					lineArgs += [resultsBug[tool]["error"]]
				else:
					lineArgs += ["No"]
				texLineArgs += ["--"]
			else:
				if "nbAngelicValue" in resultsBug[tool]:
					lineArgs += ["%s AV" % resultsBug[tool]["nbAngelicValue"]]
				elif "RegressionTestCases" in resultsBug[tool]:
					lineArgs += ["%s Reg" % resultsBug[tool]["RegressionTestCases"]]
				else:
					lineArgs += ["No"]
				texLineArgs += ["--"]
		line += "{%d:7}" % (index + 2)
		texLineTable +=  "{%d:7} \\\\" % (index + 1)
		lineArgs += [lineCount]
		if lineCount > 0:
			texLineArgs += ["Fixed"]
			result += line.format(*lineArgs) + "\n"
			resultSimple += re.sub("[0-9]+ Reg", "No  ", re.sub("[0-9]+ AV", "No  ", line.format(*lineArgs))) + "\n"
			texTable += texLineTable.format(*texLineArgs) + "\n"
			fixedBugs += 1
		simpleTable += re.sub("[0-9]+ Reg", "No  ", re.sub("[0-9]+ AV", "No  ", line.format(*lineArgs))) + "\n"
		fullTable += line.format(*lineArgs) + "\n"

	texTable += "\hline\n"

totalLine = "     | {0:17} | ".format("Total")
texLineTable = "{0:17} & ".format("Total")
total = 0
for tool in sorted(tools):
	tool = getToolName(tool)
	if tool == None:
		continue
	value = 0
	percent = 0
	if(tool in count):
		total += count[tool]
		value = count[tool]
		percent = float(count[tool])/float(totalBugs)*100
	totalLine += "{0:9} | ".format("%d (%d%%)" % (value, percent))
	texLineTable += "{0:9} & ".format("%d (%d\\%%)" % (value, percent))
totalLine += "{0:6}\n".format(total)
totalLine += "Fixed bugs: %d/%d (%d%%)\n\n" % (fixedBugs, totalBugs, float(fixedBugs)/float(totalBugs)*100)
totalLine += "Nb bugs ends with an execution error: %d\n\n"  % (nbError)
totalLine += "Nb bugs ends with an empty log: %d\n\n"  % (nbEmpty)
totalLine += "Nb bugs ends with the Grid5000 timeout: %d\n\n"  % (nbTimeout)
totalLine += "Total execution time: %s\n"  % (datetime.timedelta(milliseconds=totalExecutionTime + (nbTimeout * 3600000)))
texLineTable += "%d (%d\\%%)\\\\\n"  % (fixedBugs, float(fixedBugs)/float(totalBugs)*100)
texTable += texLineTable
texTable += """\hline 
\end{tabular}%
}
\caption{Experimental results on repairing the bugs of the Defects4J benchmarks with 4 different repair approaches.}
\end{table}
"""
result += totalLine
resultSimple += totalLine
result += "# All bugs\n\n"
resultSimple += "# All bugs\n\n"
print result + fullTable + totalLine

resultsAllFile = open(detailedResultsMdPath, "w")
resultsAllFile.write("%s%s%s\n\n\n%s" % (result, fullTable,totalLine,body))
resultsAllFile.close()

resultsAllFile = open(resultsMdPath, "w")
resultsAllFile.write("%s%s%s\n\n\n%s" % (resultSimple, simpleTable,totalLine,body))
resultsAllFile.close()

resultsTexFile = open(resultsTexPath, "w")
resultsTexFile.write(texTable)
resultsTexFile.close()
