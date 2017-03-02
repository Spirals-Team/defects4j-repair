#!/usr/bin/env python

import os
import re
import json
import subprocess
from core.Config import conf

reps = {
    "Math": "/home/thomas/git/commons-math",
    "Lang": "/home/thomas/git/commons-lang",
    "Time": "/home/thomas/git/joda-time",
    "Chart": "/home/spirals/git/jfreechart-fse",
    "Closure": "https://github.com/google/closure-compiler",
}
devnull = open('/dev/null', 'w')
commitsId = {
    "Math": {},
    "Lang": {},
    "Time": {},
    "Chart": {},
    "Closure": {}
}
for project in reps:
    pathProject = os.path.join(conf.projectsRoot, project.lower())
    for bugDir in sorted(os.listdir(pathProject)):
        try:
            bugId = int(bugDir.replace(project.lower() + "_", ""))
        except Exception, e:
            continue
        pathBug = os.path.join(pathProject, bugDir)
        cmd = """cd %s;git log -n 1 --skip 2""" % (pathBug)
        output = subprocess.check_output(cmd, shell=True, stdin=None, stderr=devnull)
        if len(output) == 0:
            continue
        m = re.search('commit ([a-f0-9]+)', output)
        if m:
            commitId = m.group(1)
        if project == "Math":
            m = re.search(re.compile('Date:   (.+)$', re.M), output)
            if m:
                date = m.group(1)
                cmd1 = """cd %s;
git log | grep -B 2 "%s"
""" % (reps[project], date)

                try:
                    output = subprocess.check_output(cmd1, shell=True, stdin=None, stderr=devnull)
                    if len(output) == 0:
                        continue
                    m = re.search('commit ([a-f0-9]+)', output)
                    if m:
                        commitId = m.group(1)
                except e:
                    print e
            else:
                continue
        commitsId[project][bugId] = commitId
print json.dumps(commitsId, sort_keys=True, indent=4, separators=(',', ': '))
