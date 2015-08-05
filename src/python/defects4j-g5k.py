#!/usr/bin/env python

import argparse
from core.projects.LangProject import LangProject
from core.projects.MathProject import MathProject
from core.projects.ChartProject import ChartProject
from core.projects.TimeProject import TimeProject

from core.tools.Ranking import Ranking
from core.tools.NopolPC import NopolPC
from core.tools.NopolC import NopolC
from core.tools.BrutpolPC import BrutpolPC
from core.tools.BrutpolC import BrutpolC
from core.tools.Astor import Astor
from core.tools.Kali import Kali

from core.NodeHandler import NodeHandler
from core.RunnerTask import RunnerTask



def initParser():
    parser = argparse.ArgumentParser(description='Run tools on defect4j with grid5000')
    parser.add_argument('-projects', nargs='+', required=True, help='Which project (all, math, lang, time)')
    parser.add_argument('-tools', nargs='+', required=True, help='Which tool (all, nopol, ranking, ...)')
    parser.add_argument('-id', nargs='+', help='Bug id')
    parser.add_argument('--timeout', required=False, help='Node timeout')
    parser.add_argument('--with-angelic', action='store_true', default=False, help='Run only bug with angelic')
    return parser.parse_args()

args = initParser()

projects = []
for project in args.projects:
    if project.lower() == "all":
        projects.append(ChartProject())
        projects.append(LangProject())
        projects.append(MathProject())
        projects.append(TimeProject())
    elif project.lower() == "chart":
        projects.append(ChartProject())
    elif project.lower() == "lang":
        projects.append(LangProject())
    elif project.lower() == "math":
        projects.append(MathProject())
    elif project.lower() == "time":
        projects.append(TimeProject())

tools = []
for tool in args.tools:
    if tool.lower() == "all":
        tools.append(NopolPC())
        tools.append(NopolC())
        tools.append(Astor())
        tools.append(Kali())
        tools.append(BrutpolPC())
        tools.append(BrutpolC())
    elif tool.lower() == "nopol":
        tools.append(NopolPC())
        tools.append(NopolC())
    elif tool.lower() == "nopolpc":
        tools.append(NopolPC())
    elif tool.lower() == "ranking":
        tools.append(Ranking())    
    elif tool.lower() == "nopolc":
        tools.append(NopolC())
    elif tool.lower() == "brutpol":
        tools.append(BrutpolPC())
        tools.append(BrutpolC())
    elif tool.lower() == "brutpolpc":
        tools.append(BrutpolPC())
    elif tool.lower() == "brutpolc":
        tools.append(BrutpolC())
    elif tool.lower() == "genprog":
        tools.append(Astor())
    elif tool.lower() == "kali":
        tools.append(Kali())

tasks = []

for project in projects:
    for tool in tools:
        if args.id:
            for id in args.id:
                task = RunnerTask(tool, project, int(id))
                tasks.append(task)
        elif args.with_angelic:
            for i in project.angelicValue:
                task = RunnerTask(tool, project, int(i))
                tasks.append(task)
        else:
            for i in range(1, project.nbBugs + 1):
                task = RunnerTask(tool, project, int(i))
                tasks.append(task)
                
nodeHandler = NodeHandler(tasks)
nodeHandler.run(args.timeout)
