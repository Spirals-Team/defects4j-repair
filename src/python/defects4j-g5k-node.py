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
    parser.add_argument('-project', required=True, help='Which project (all, math, lang, time)')
    parser.add_argument('-tool', required=True, help='Which tool (nopol, ranking, ...)')
    parser.add_argument('-id',  help='Bug id')
    return parser.parse_args()

args = initParser()
project = None
tool = None
id = int(args.id)
if args.project == "Lang":
    project = LangProject()
elif args.project == "Math":
    project = MathProject()
elif args.project == "Chart":
    project = ChartProject()
elif args.project == "Time":
    project = TimeProject()  

if args.tool == "NopolPC":
    tool = NopolPC()
elif args.tool == "NopolC":
    tool = NopolC() 
elif args.tool == "BrutpolPC":
    tool = BrutpolPC()
elif args.tool == "BrutpolC":
    tool = BrutpolC() 
elif args.tool == "Ranking":
    tool = Ranking()     
elif args.tool == "Genprog":
    tool = Astor()
elif args.tool == "Kali":
    tool = Kali()

tool.run(project, id)
