import re
import os
import json
import datetime
import collections
from core.tools.Nopol import Nopol
from core.Config import conf
from math import sqrt

class Ranking(Nopol):
    """docstring for Ranking"""
    def __init__(self):
        super(Ranking, self).__init__("Ranking")

    def run(self, project, id):
        log = self.runNopol(project, id, mode="ranking")
        slittedLog = log.split('/******** Tests *********/')
        if(len(slittedLog) > 1):
            print slittedLog[1]
            self.parseLog(slittedLog[1], project, id)

    def parseLog(self, log, project, id):
        suspiciousStatements = {}
        smooth = 0.000001
        rank = 0
        reg = re.compile('([0-9a-zA-Z\-_\.\$]+):([0-9]+) -> ([0-9\.]+) \(ep: ([0-9]+), ef: ([0-9]+), np: ([0-9]+), nf: ([0-9]+)\)')
        m = reg.findall(log)
        for i in m:
            rank += 1
            ep = int(i[3])
            ef = int(i[4])
            np = int(i[5])
            nf = int(i[6])
            suspiciousStatements[i[0]+":"+i[1]] = {
                "class": i[0],
                "line": int(i[1]),
                "ep": ep,
                "ef": ef,
                "np": np,
                "nf": nf,
                "rank": {
                    "ochiai": rank
                },
                "metrics": {
                    "gzoltar": float(i[2]),
                    "ochiai": (ef)/sqrt((ef+ep)*(ef+nf)),
                    "tarantula": (ef/float(ef+nf + smooth))/float((ef/float(ef+nf + smooth))+(ep/float(ep+np + smooth)) + smooth),
                    "ample": abs((ef/float(ef+nf)) - (ep/float(ep+np))),
                    "jaccard": ef / float(ef + ep + nf),
                    "naish1": np if ef == 0 else -1,
                    "naish2": ef - (ep / float(ep + np + 1)),
                    "gp13": ef * (1 + 1 / float(2* ep + ef))
                }
            }
        rank = 0
        suspiciousStatementsAmple = collections.OrderedDict(sorted(suspiciousStatements.items(), key=lambda t: t[1]['metrics']['ample'], reverse=True))
        for i in suspiciousStatementsAmple:
            rank += 1
            suspiciousStatements[i]['rank']['ample'] = rank
        rank = 0
        suspiciousStatementsJaccard = collections.OrderedDict(sorted(suspiciousStatements.items(), key=lambda t: t[1]['metrics']['jaccard'], reverse=True))
        for i in suspiciousStatementsJaccard:
            rank += 1
            suspiciousStatementsJaccard[i]['rank']['jaccard'] = rank

        rank = 0
        suspiciousStatementsNaish1 = collections.OrderedDict(sorted(suspiciousStatements.items(), key=lambda t: t[1]['metrics']['naish1'], reverse=True))
        for i in suspiciousStatementsNaish1:
            rank += 1
            suspiciousStatementsNaish1[i]['rank']['naish1'] = rank

        rank = 0
        suspiciousStatementsNaish2 = collections.OrderedDict(sorted(suspiciousStatements.items(), key=lambda t: t[1]['metrics']['naish2'], reverse=True))
        for i in suspiciousStatementsNaish2:
            rank += 1
            suspiciousStatementsNaish2[i]['rank']['naish2'] = rank

        rank = 0
        suspiciousStatementsGP13 = collections.OrderedDict(sorted(suspiciousStatements.items(), key=lambda t: t[1]['metrics']['gp13'], reverse=True))
        for i in suspiciousStatementsGP13:
            rank += 1
            suspiciousStatementsGP13[i]['rank']['gp13'] = rank

        rank = 0
        suspiciousStatementsTarantula = collections.OrderedDict(sorted(suspiciousStatements.items(), key=lambda t: t[1]['metrics']['tarantula'], reverse=True))
        for i in suspiciousStatementsTarantula:
            rank += 1
            suspiciousStatementsTarantula[i]['rank']['tarantula'] = rank

        executedTest = None
        successfulTest = None
        failedTest = None
        date = datetime.datetime.now().isoformat()
        node = self.getHostname()
        failedTestDetails = []
        m = re.search('Executed tests:   ([0-9]+)', log)
        if m:
            executedTest = int(m.group(1))
        m = re.search('Successful tests: ([0-9]+)', log)
        if m:
            successfulTest = int(m.group(1))
        m = re.search('Failed tests:     ([0-9]+)', log)
        if m:
            failedTest = int(m.group(1))
        m = re.search('Executed tests:   ([0-9]+)', log)
        if m:
            executedTest = int(m.group(1))

        m = re.search('Node: ([a-zA-Z0-9\-\.]+)', log)
        if m:
            node = m.group(1)
        m = re.search('Date: ([^`]+)$', log)
        if m:
            date = m.group(1)

        patches = []
        humanPatchpath = os.path.join(conf.defects4jRoot, "framework/projects", project.name, "patches",  "%d.src.patch" % id)
        regexSource = re.compile(r'^--- (?P<filename>[^\t\n]+)(?:\t(?P<timestamp>[^\n]+))?')
        regexDest = re.compile(r'^\+\+\+ (?P<filename>[^\t\n]+)(?:\t(?P<timestamp>[^\n]+))?')
        regexAdd = re.compile("^-.*")
        regexChange = re.compile("^\+.*")
        regexHunk = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))?\ @@[ ]?(.*)")
        regexHunkLine = re.compile(r'^(?P<line_type>[- \+\\])(?P<value>.*)')
        with open(humanPatchpath) as data_patch:
            current_file = None
            source_file = None
            source_timestamp = None
            target_file = None
            target_timestamp = None
            for line in data_patch:
                is_source_filename = regexSource.match(line)
                if is_source_filename:
                    source_file = re.sub(r"(\$[0-9]+)?\.java$", "", re.sub(r"^a\/", "", is_source_filename.group('filename')))
                    source_timestamp = is_source_filename.group('timestamp')
                    # reset current file
                    current_file = None
                    continue
                # check for target file header
                is_target_filename = regexDest.match(line)
                if is_target_filename:
                    if current_file is not None:
                        continue
                    target_file = re.sub(r"(\$[0-9]+)?\.java$", "", re.sub(r"^b\/", "", is_target_filename.group('filename')))
                    target_timestamp = is_target_filename.group('timestamp')
                    # add current file to PatchSet
                    current_file = {
                        'source_file': source_file.replace("/", "."),
                        'target_file': target_file.replace("/", "."),
                        'source_timestamp': source_timestamp,
                        'target_timestamp': target_timestamp,
                        'hunks': []
                    }
                    patches.append(current_file)
                    continue

                # check for hunk header
                is_hunk_header = regexHunk.match(line)
                if is_hunk_header:
                    if current_file is None:
                        continue
                    hunk = {
                        'src_start': int(is_hunk_header.group(1)),
                        'src_len': int(is_hunk_header.group(2)),
                        'tgt_start': int(is_hunk_header.group(3)),
                        'tgt_len': int(is_hunk_header.group(4)),
                        'section_header': is_hunk_header.group(5),
                        'changes': []
                    }
                    source_line_no = hunk['src_start']
                    target_line_no = hunk['tgt_start']
                    diffLineSourceTarget = hunk['src_start'] - hunk['tgt_start']
                    current_file['hunks'].append(hunk)
                    current_line = None
                    for line in data_patch:
                        is_hunk_line = regexHunkLine.match(line)
                        if is_hunk_line is None:
                            break
                        line_type = is_hunk_line.group('line_type')
                        value = is_hunk_line.group('value').strip()
                        if line_type[0] == '+':
                            if current_line is None or target_line_no + diffLineSourceTarget != current_line['line']:
                                current_line = {
                                    'target': value,
                                    'original': '',
                                    'line': target_line_no
                                }
                                hunk['changes'].append(current_line);
                                target_line_no += 1
                                continue
                            if value != current_line['original']:
                                current_line['target'] = value
                                current_line['targetLine '] = target_line_no
                            else:
                                hunk['changes'].remove(current_line)
                            target_line_no += 1
                        elif line_type[0] == '-':
                            current_line = {
                                'original': value,
                                'target': '',
                                'line': source_line_no
                            }
                            hunk['changes'].append(current_line)
                            source_line_no += 1
                        else:
                            target_line_no += 1
                            source_line_no += 1
                            current_line = None
                        if (source_line_no == (hunk['src_start'] + hunk['src_len']) and 
                            target_line_no == (hunk['tgt_start'] + hunk['tgt_len'])):
                            break
        modifiedLines = []
        for patchedFile in patches:
            for hunk in patchedFile['hunks']:
                for change in hunk['changes']:
                    if change['target'] is not None and change['target'] != '':
                        if (change['target'][0] == '*' or 
                            change['target'] == '/**' or 
                            change['target'] == '**/'):
                            continue
                        line = change['line']
                        modifiedLines.append({
                            'class': patchedFile['source_file'],
                            'line': line
                            })

        reg = re.compile('([0-9a-zA-Z\.\-_\$]+)#([^\n]+)')
        m = reg.findall(log)
        for i in m:
            cl = i[0]
            md = i[1]
            failedTestDetails.append({
                'class': cl,
                'method': md
            })
        results = {
            'executedTest': executedTest,
            'successfulTest': successfulTest,
            'failedTest': failedTest,
            'failedTestDetails': failedTestDetails,
            'nbsuspicious': len(suspiciousStatements),
            'suspicious': suspiciousStatements,
            'modifiedLines': modifiedLines,
            'node': node,
            'date': date
        }
        path = os.path.join(project.logPath, str(id), self.name, "results.json")
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        file = open(path, "w")
        file.write(json.dumps(results, indent=4, sort_keys=True))
        file.close()