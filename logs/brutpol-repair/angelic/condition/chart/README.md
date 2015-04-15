# Chart - Brutpol angelic condition repair


- Nb patch found: 3/25

| #Bug | Nb Statements Analyzed | Nb Angelic Value Found | Exec. time | Patch Found |
|------|---------------|--------------|------------|------------|
| 1 | NONE | NONE | > 6h | NO |
| 2 |  166 |  0 |  93494ms | NO |
| 3 |  130 |  1 |  95245ms | NO |
| 4 |  1883 |  0 |  651606ms | NO |
| 5 |  51 |  2 |  74786ms | NO |
| 6 | NONE | NONE | > 6h | NO |
| 7 |  122 |  0 |  78315ms | NO |
| 8 | IGNORED | IGNORED | IGNORED | IGNORED |
| 9 | NONE | NONE | > 6h | NO |
| 10 |  2 |  0 |  56377ms | NO |
| 11 |  19 |  0 |  63405ms | NO |
| 12 |  339 |  0 |  126656ms | NO |
| 13 |  229 |  3 |  107497ms | NO |
| 14 |  5 |  1 |  69144ms | YES |
| 15 |  878 |  0 |  219884ms | NO |
| 16 |  24 |  1 |  69962ms | YES |
| 17 |  93 |  1 |  81248ms | NO |
| 18 |  95 |  0 |  75791ms | NO |
| 19 |  512 |  0 |  188643ms | NO |
| 20 |  35 |  0 |  61684ms | NO |
| 21 | NONE | NONE | > 6h | NO |
| 22 |  97 |  0 |  75974ms | NO |
| 23 |  218 |  0 |  114416ms | NO |
| 24 |  11 |  0 |  57365ms | NO |
| 25 |  8 |  1 |  67157ms | YES |
| 26 | NONE | NONE | > 6h | NO |
## Patches

### Bug 14

- Ranking nopol: 5

- Brutpol patch:

```
----INFORMATION----
Nb Statements Analyzed : 5
Nb Statements with Angelic Value Found : 1
Nb inputs in SMT : 0
Nb variables in SMT : 0
Nopol Execution time : 69144ms
----PATCH FOUND----
org.jfree.chart.plot.CategoryPlot:2440: CONDITIONAL this.rangeCrosshairVisible
```

- IRL patch:

```
org.jfree.chart.plot.CategoryPlot

2165a2166,2168
>         if (markers == null) {
>             return false;
>         }
2448c2451,2453
< 
---
>         if (markers == null) {
>             return false;
>         }
2502d2506
< 
2507d2510
< 


org.jfree.chart.plot.XYPlot

2292a2293,2295
>         if (markers == null) {
>             return false;
>         }
2529c2532,2534
< 
---
>         if (markers == null) {
>             return false;
>         }


```

### Bug 16

- Ranking nopol: 24

- Brutpol patch:

```
----INFORMATION----
Nb Statements Analyzed : 24
Nb Statements with Angelic Value Found : 1
Nb inputs in SMT : 0
Nb variables in SMT : 0
Nopol Execution time : 69962ms
----PATCH FOUND----
org.jfree.data.category.DefaultIntervalCategoryDataset:338: CONDITIONAL 0 != this.getSeriesCount()
```

- IRL patch:

```
org.jfree.data.category.DefaultIntervalCategoryDataset

207,208c207,208
<                 this.seriesKeys = null;
<                 this.categoryKeys = null;
---
>                 this.seriesKeys = new Comparable[0];
>                 this.categoryKeys = new Comparable[0];
338c338
<         if (categoryKeys.length != this.startData[0].length) {
---
>         if (categoryKeys.length != getCategoryCount()) {


```

### Bug 25

- Ranking nopol: 8

- Brutpol patch:

```
----INFORMATION----
Nb Statements Analyzed : 8
Nb Statements with Angelic Value Found : 1
Nb inputs in SMT : 0
Nb variables in SMT : 0
Nopol Execution time : 67157ms
----PATCH FOUND----
org.jfree.data.statistics.DefaultStatisticalCategoryDataset:110: CONDITIONAL 1 == (this.maximumRangeValue - this.getColumnCount())
```

- IRL patch:

```
org.jfree.chart.renderer.category.StatisticalBarRenderer

258a259,261
>         if (meanValue == null) {
>             return;
>         }
315c318,320
<         double valueDelta = dataset.getStdDevValue(row, column).doubleValue();
---
>         Number n = dataset.getStdDevValue(row, column);
>         if (n != null) {
>             double valueDelta = n.doubleValue();
343a349
>         }
402a409,411
>         if (meanValue == null) {
>             return;
>         }
459c468,470
<         double valueDelta = dataset.getStdDevValue(row, column).doubleValue();
---
>         Number n = dataset.getStdDevValue(row, column);
>         if (n != null) {
>             double valueDelta = n.doubleValue();
486a498
>         }


```

