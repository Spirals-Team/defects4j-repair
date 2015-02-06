# Defects4j-Nopol

## Reset depots

```
export HTTP_PROXY="http://proxy:3128/"
export HTTPS_PROXY="https://proxy:3128/"

rm -rf defects4j/ defects4j-nopol/ nopol/

git clone https://github.com/rsommerard/nopol.git
git clone https://github.com/rsommerard/defects4j.git
git clone https://github.com/rsommerard/defects4j-nopol.git
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
