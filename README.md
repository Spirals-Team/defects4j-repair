# Defects4j-Repair

## Infos

Nb. of tested bugs: 223 (25 + 65 + 106 + 27)

## Reset script

```
export HTTP_PROXY="http://proxy:3128/"
export HTTPS_PROXY="https://proxy:3128/"

rm -rf defects4j/ defects4j-repair/ nopol/ astor/

git clone https://github.com/rsommerard/nopol.git
git clone https://github.com/rsommerard/astor.git
git clone https://github.com/rsommerard/defects4j.git
git clone https://github.com/Spirals-Team/defects4j-repair.git
```

## Check available ressources

```
disco grenoble lille luxembourg lyon nancy nantes reims rennes sophia toulouse
```

## Delete reservations

```
for i in $(oarstat -u | grep <name> | cut -f 1 -d ' '); do echo $i; oardel $i; done
```

## Init projects

Chart:

```
for bug in $(seq 1 26); do defects4j checkout -p Chart -v ${bug}b -w ~/projects/chart/chart_${bug}; done
```

Closure:

```
for bug in $(seq 1 133); do defects4j checkout -p Closure -v ${bug}b -w ~/projects/closure/closure_${bug}; done
```

Lang:

```
for bug in $(seq 1 65); do defects4j checkout -p Lang -v ${bug}b -w ~/projects/lang/lang_${bug}; done
```

Math:

```
for bug in $(seq 1 106); do defects4j checkout -p Math -v ${bug}b -w ~/projects/math/math_${bug}; done
```

Time:

```
for bug in $(seq 1 27); do defects4j checkout -p Time -v ${bug}b -w ~/projects/time/time_${bug}; done
```
