#!/usr/bin/env python

import os
import json
import re
import sys
import datetime
from core.Config import conf

reload(sys)  
sys.setdefaultencoding('Cp1252')

tools = ["NopolPC", "NopolC", "BrutpolPC", "BrutpolC", "Genprog", "Kali"]

root = conf.resultsRoot
resultsAll = {}
resultsAllPath = os.path.join(root, "results.json")
resultsMdPath = os.path.join(root, "results.md")
resultsTexPath = os.path.join(root, "results.tex")
rankingAll = {}

nbError = 0
nbEmpty = 0
nbTimeout = 0
fixedBugs = 0
totalBugs = 0
totalExecutionTime = 0

count = {}
result = "# Summary\n\n"
body = ""
line = "BugId             | "
texTable = """\\begin{table}[!t]
\label{tab:bugs_summary}
\centering
\\resizebox{0.5\\textwidth}{!}{
\setlength\\tabcolsep{0.3 ex}
\\begin{tabular}{|c|c|c|c|c|c|}
\hline 
Bug id            & """
for tool in tools:
	if tool == "Ranking":
		continue
	line += "{0:9} | ".format(tool)
	texTable += "{0:9} & ".format(tool)

tableHeader = "%sTotal\n----------------- | " % line
texTable += "Total \\\\\n\\hline\n"
for tool in tools:
	if tool == "Ranking":
		continue
	tableHeader += "--------- | "
tableHeader += "------\n"
result += tableHeader

fullTable = tableHeader
body = ""
print("Start the output proccess")
for project in os.listdir(root):
	projectPath = os.path.join(root, project) 
	if os.path.isfile(projectPath):
		continue
	smallName = project[0]
	resultsProject = {}
	rankingBug = {}
	for bugId in sorted(os.listdir(projectPath), key = lambda k: int(k) if k.isdigit() else k):
		bugPath = os.path.join(projectPath, bugId) 
		if not bugId.isdigit() or os.path.isfile(bugPath):
			continue
		bugId = int(bugId)

		sys.stdout.write("\033[F")
		sys.stdout.write("\033[K")
		print "Process: %s %d" %(project, bugId)
		
		ranking = None

		totalBugs += 1
		line = "{0:17} |"
		lineArgs = []
		texLineArgs = []
		texLineTable = "{0:17} &"
		lineArgs += ["[%s%d](#%s-%s)" % (smallName, bugId, project.lower(), bugId)]
		texLineArgs += ["%s%d"  % (smallName, bugId)]
		lineCount = 0

		resultsBugPath = os.path.join(bugPath, "results.json")
		resultsBug = {}
		for (index, tool) in enumerate(tools):
			if tool == "Ranking":
				continue
			toolPath = os.path.join(bugPath, tool)
			if os.path.isfile(toolPath):
				continue
			line += " {%d:9} |" % (index + 1)
			texLineTable +=  " {%d:9} &" % (index + 1)
			resultsToolPath = os.path.join(toolPath, "results.json")
			stderrToolPath = os.path.join(toolPath, "stderr.log")
			stdoutToolPath = os.path.join(toolPath, "stdout.log")
			if os.path.exists(resultsToolPath):
				with open(resultsToolPath) as data_file:
					resultsBug[tool] = json.load(data_file)
			elif os.path.exists(stderrToolPath):
				with open(stderrToolPath) as data_file:
					data = data_file.read()
					m = re.search("Job [0-9]+ KILLED", data)
					if m:
						resultsBug[tool] = {
							"error": "TIMEOUT"
						}
						nbTimeout += 1
					elif len(data) == 0:
						resultsBug[tool] = {
							"error": "EMPTY"
						}
						nbEmpty += 1
					else:
						resultsBug[tool] = {
							"error": "ERROR"
						}
						nbError += 1
			else:
				lineArgs += [""]
				texLineArgs += [""]
				continue

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
						body += "```Java\n%s\n```\n\n" % (content)
				lineArgs += ["Yes"]
				texLineArgs += ["Fixed"]
				lineCount += 1
				if(not tool in count):
					count[tool] = 1
				else:
					count[tool] += 1

				body += "## %s \n\n" % (tool)
				if "operations" in resultsBug[tool]:
					for operation in resultsBug[tool]["operations"]:
						lineKey = "%s:%d" % (operation['patchLocation']["className"], operation['patchLocation']["line"])
						if 'suspicious' in ranking and lineKey in ranking['suspicious']:
							ranks = ranking['suspicious'][lineKey]['rank']
							body += "%s (Suspicious rank: " % (lineKey)
							for rank in ranks:
								body += "%s %d, " % (rank, ranks[rank])
							body += ")\n"
						else:
							body += "%s\n" % (lineKey)
						if 'type' in operation:
							body+= operation["type"] + "\n"
						body += "```Java\n%s\n```\n\n" % (operation["patch"])
				else:
					lineKey = "%s:%d" % (resultsBug[tool]['patchLocation']["className"], resultsBug[tool]['patchLocation']["line"])
					if 'suspicious' in ranking and lineKey in ranking['suspicious']:
						ranks = ranking['suspicious'][lineKey]['rank']
						body += "%s (Suspicious rank: " % (lineKey)
						for rank in ranks:
							body += "%s %d, " % (rank, ranks[rank])
						body += ")\n"
					else:
						body += "%s\n" % (lineKey)
					body += "```Java\n%s\n```\n\n" % (resultsBug[tool]["patch"])
					body += "Nb Angelic value: %d\n\n" % resultsBug[tool]['nbAngelicValue']
					body += "Nb analyzed Statement: %d\n\n" % resultsBug[tool]['nbStatement']
				if 'executionTime' in resultsBug[tool]:
					body += "Execution time: %s\n\n" % datetime.timedelta(milliseconds=resultsBug[tool]['executionTime'])
				if 'node' in resultsBug[tool]:
					body += "Grid5000 node: %s\n\n" % resultsBug[tool]['node']


			elif ("error" in resultsBug[tool]):
				lineArgs += [resultsBug[tool]["error"]]
				texLineArgs += ["--"]
			else:
				lineArgs += ["No"]
				texLineArgs += ["--"]
		line += "{%d:7}" % (len(tools) + 1)
		texLineTable +=  "{%d:7} \\\\" % (len(tools) + 1)
		lineArgs += [lineCount]
		if lineCount > 0:
			texLineArgs += ["Fixed"]
			result += line.format(*lineArgs) + "\n"
			texTable += texLineTable.format(*lineArgs) + "\n"
			fixedBugs += 1
		fullTable += line.format(*lineArgs) + "\n"

	texTable += "\hline\n"

totalLine = "{0:17} | ".format("Total")
texLineTable = "{0:17} & ".format("Total")
total = 0
for tool in tools:
	if tool == "Ranking":
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

result += "# Complete data\n\n"
result += fullTable
result += totalLine
print result

resultsAllFile = open(resultsMdPath, "w")
resultsAllFile.write("%s\n\n\n%s" % (result,body))
resultsAllFile.close()

resultsTexFile = open(resultsTexPath, "w")
resultsTexFile.write(texTable)
resultsTexFile.close()
