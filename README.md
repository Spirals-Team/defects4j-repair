# Defects4j-Repair

This repository contains the raw experimental results of an experiment done at INRIA Lille on the automatic repair of the bugs of the Defects4J dataset.

## Infos

Nb. of tested bugs: 224 (226 + 65 + 106 + 27)

## Check available ressources

```Bash
disco grenoble lille luxembourg lyon nancy nantes reims rennes sophia toulouse
```

## Delete reservations

```Bash
for i in $(oarstat -u | grep `whoami` | cut -f 1 -d ' '); do echo $i; oardel $i; done
```

## Init projects

Chart:

```Bash
for bug in $(seq 1 26); do defects4j checkout -p Chart -v ${bug}b -w ~/projects/chart/chart_${bug}; done
```

Closure:

```Bash
for bug in $(seq 1 133); do defects4j checkout -p Closure -v ${bug}b -w ~/projects/closure/closure_${bug}; done
```

Lang:

```Bash
for bug in $(seq 1 65); do defects4j checkout -p Lang -v ${bug}b -w ~/projects/lang/lang_${bug}; done
```

Math:

```Bash
for bug in $(seq 1 106); do defects4j checkout -p Math -v ${bug}b -w ~/projects/math/math_${bug}; done
```

Time:

```Bash
for bug in $(seq 1 27); do defects4j checkout -p Time -v ${bug}b -w ~/projects/time/time_${bug}; done
```
