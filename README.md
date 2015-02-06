# Defects4j-Nopol

## Init projects

Chart:

```
for bug in $(seq 1 26); do defects4j checkout -p Chart -v ${bug}b -w /home/rsommerard/projects/chart/chart_${bug}; done
```

Closure:

```
for bug in $(seq 1 133); do defects4j checkout -p Closure -v ${bug}b -w /home/rsommerard/projects/closure/closure_${bug}; done
```

Lang:

```
for bug in $(seq 1 65); do defects4j checkout -p Lang -v ${bug}b -w /home/rsommerard/projects/lang/lang_${bug}; done
```

Math:

```
for bug in $(seq 1 106); do defects4j checkout -p Math -v ${bug}b -w /home/rsommerard/projects/math/math_${bug}; done
```

Time:

```
for bug in $(seq 1 27); do defects4j checkout -p Time -v ${bug}b -w /home/rsommerard/projects/time/time_${bug}; done
```
