# Chart - Nopol angelic precondition repair


- Nb patch found: 6/25

| #Bug | Nb Statements Analyzed | Nb Angelic Value Found | Exec. time | Patch Found |
|------|---------------|--------------|------------|------------|
| 1 |  464 |  0 |  180169ms | NO |
| 2 |  166 |  0 |  63340ms | NO |
| 3 | NONE | NONE | > 6h | NO |
| 4 | NONE | NONE | > 6h | NO |
| 5 |  3 |  1 |  65540ms | YES |
| 6 | NONE | NONE | > 6h | NO |
| 7 |  122 |  0 |  52386ms | NO |
| 8 | IGNORED | IGNORED | IGNORED | IGNORED |
| 9 |  8 |  1 |  63199ms | YES |
| 10 |  2 |  0 |  39664ms | NO |
| 11 |  19 |  0 |  43512ms | NO |
| 12 |  339 |  0 |  88295ms | NO |
| 13 |  38 |  1 |  66737ms | YES |
| 14 | NONE | NONE | > 6h | NO |
| 15 |  878 |  1 |  173455ms | NO |
| 16 |  45 |  0 |  45031ms | NO |
| 17 |  1 |  1 |  60629ms | YES |
| 18 |  95 |  0 |  50702ms | NO |
| 19 |  512 |  0 |  142700ms | NO |
| 20 |  35 |  0 |  43419ms | NO |
| 21 |  11 |  1 |  67467ms | YES |
| 22 |  97 |  0 |  47035ms | NO |
| 23 |  218 |  0 |  74036ms | NO |
| 24 |  11 |  0 |  40628ms | NO |
| 25 |  8 |  1 |  60716ms | YES |
| 26 | NONE | NONE | > 6h | NO |
## Patches

### Bug 5

```
----INFORMATION----
Nb Statements Analyzed : 3
Nb Statements with Angelic Value Found : 1
Nopol Execution time : 65540ms
----PATCH FOUND----
org.jfree.data.xy.XYSeries:561: CONDITIONAL !(org.jfree.data.xy.XYSeries.this.allowDuplicateXValues)
```
### Bug 9

```
----INFORMATION----
Nb Statements Analyzed : 8
Nb Statements with Angelic Value Found : 1
Nopol Execution time : 63199ms
----PATCH FOUND----
org.jfree.data.time.TimeSeries:935: CONDITIONAL ((org.jfree.data.time.TimeSeries.DEFAULT_RANGE_DESCRIPTION.length())==(startIndex))||((!((startIndex)!=(1)))&&(start!=null))
```
### Bug 13

```
----INFORMATION----
Nb Statements Analyzed : 38
Nb Statements with Angelic Value Found : 1
Nopol Execution time : 66737ms
----PATCH FOUND----
org.jfree.chart.block.BorderArrangement:482: CONDITIONAL null!=null
```
### Bug 17

```
----INFORMATION----
Nb Statements Analyzed : 1
Nb Statements with Angelic Value Found : 1
Nopol Execution time : 60629ms
----PATCH FOUND----
org.jfree.data.time.TimeSeries:880: PRECONDITION (1)==(start)
```
### Bug 21

```
----INFORMATION----
Nb Statements Analyzed : 11
Nb Statements with Angelic Value Found : 1
Nopol Execution time : 67467ms
----PATCH FOUND----
org.jfree.data.Range:335: PRECONDITION (((1)+(1))<((org.jfree.data.Range.this.upper)-(org.jfree.data.Range.this.lower)))||(!(((1)+(1))<=(org.jfree.data.Range.this.lower)))
```
### Bug 25

```
----INFORMATION----
Nb Statements Analyzed : 8
Nb Statements with Angelic Value Found : 1
Nopol Execution time : 60716ms
----PATCH FOUND----
org.jfree.data.statistics.DefaultStatisticalCategoryDataset:110: CONDITIONAL ((org.jfree.data.statistics.DefaultStatisticalCategoryDataset.this.maximumRangeValue)<(org.jfree.data.statistics.DefaultStatisticalCategoryDataset.this.maximumRangeValueIncStdDev))&&(!((org.jfree.data.statistics.DefaultStatisticalCategoryDataset.this.maximumRangeValue)<=(1)))
```
