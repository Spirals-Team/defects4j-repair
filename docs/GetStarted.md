# Get started

1. First download Defects4J: https://github.com/rjust/defects4j
2. Follows the Defects4J [Get started](https://github.com/rjust/defects4j#getting-started)
3. Export Defects4J-repair into your PATH: ```PATH=$PATH:~/<defects4j_pach>/framework/bin```
4. Checkout all bugs
```bash
for bug in $(seq 1 26); do defects4j checkout -p Chart -v ${bug}b -w ~/projects/chart/chart_${bug}; done
for bug in $(seq 1 65); do defects4j checkout -p Lang -v ${bug}b -w ~/projects/lang/lang_${bug}; done
for bug in $(seq 1 106); do defects4j checkout -p Math -v ${bug}b -w ~/projects/math/math_${bug}; done
for bug in $(seq 1 27); do defects4j checkout -p Time -v ${bug}b -w ~/projects/time/time_${bug}; done
```
5. Edit the Defects4J-repair config: ```src/python/core/Config.py```
6. Export Defects4J-repair into your PATH: ```PATH=$PATH:~/<defects4j-repair_pach>/src/python/bin```
7. Run Defects4J-repair
```bash
defects4j-g5k.py --project all --tools all  
```
8. Generate readme.md
```bash
processResult.py
```