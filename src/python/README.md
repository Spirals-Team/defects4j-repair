# Defects4J OAR runner

## Getting started
This runner is designed to run on a [OAR](http://oar.imag.fr/dokuwiki/doku.php) system.

The program ```defects4j-g5k.py``` is used to start the execution on the cluster.
### ```defects4j-g5k.py``` Usage
```bash
usage: defects4j-g5k.py [-h] -projects PROJECTS [PROJECTS ...] -tools TOOLS
                        [TOOLS ...] [-id ID [ID ...]] [--timeout TIMEOUT]
                        [--with-angelic]

Run tools on defect4j with grid5000

optional arguments:
  -h, --help            show this help message and exit
  -projects PROJECTS [PROJECTS ...]
                        Which project (all, math, lang, time, chart)
  -tools TOOLS [TOOLS ...]
                        Which tool (all, genprog, kali, nopol, ranking, ...)
  -id ID [ID ...]       Bug id
  --timeout TIMEOUT     Node timeout
  --with-angelic        Run only bugs that have an angelic value
```
The program ```defects4j-g5k-node.py``` is used to start run a repair tool on the local machine.
### ```defects4j-g5k-node.py``` Usagegenprog, kali,
```bash
usage: defects4j-g5k-node.py [-h] -project PROJECT -tool TOOL [-id ID]

Run tools on defect4j with grid5000

optional arguments:
  -h, --help        show this help message and exit
  -project PROJECT  Which project (all, math, lang, time, chart)
  -tool TOOL        Which tool (genprog, kali, nopol, ranking, ...)
  -id ID            Bug id
```

The program ```processResult.py``` is used to generate the readme file.


## Screenshot
![screenshot](https://cloud.githubusercontent.com/assets/5577568/9560647/07b3b7ec-4e20-11e5-8734-cb56bffefdf9.png)
