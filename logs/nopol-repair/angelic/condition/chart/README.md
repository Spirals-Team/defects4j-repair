# Chart - Nopol angelic condition repair

## Bug 1

```
----INFORMATION----
Nb Statements Analyzed : 464
Nb Statements with Angelic Value Found : 0
Nopol Execution time : 288896ms
```

## Bug 2

```
----INFORMATION----
Nb Statements Analyzed : 166
Nb Statements with Angelic Value Found : 0
Nopol Execution time : 98484ms
```

## Bug 3

Time out after 6 hours.

## Bug 4

Time out after 6 hours.

## Bug 5

```
----INFORMATION----
Nb Statements Analyzed : 3
Nb Statements with Angelic Value Found : 1
Nopol Execution time : 101534ms
----PATCH FOUND----
org.jfree.data.xy.XYSeries:561: CONDITIONAL !(org.jfree.data.xy.XYSeries.this.allowDuplicateXValues)
```

## Bug 6

Time out after 6 hours.

## Bug 7

```
----INFORMATION----
Nb Statements Analyzed : 122
Nb Statements with Angelic Value Found : 0
Nopol Execution time : 82130ms
```

## Bug 8

Ignored because of grid5000 bug.

## Bug 9

```
----INFORMATION----
Nb Statements Analyzed : 8
Nb Statements with Angelic Value Found : 1
Nopol Execution time : 102417ms
----PATCH FOUND----
org.jfree.data.time.TimeSeries:935: CONDITIONAL ((org.jfree.data.time.TimeSeries.DEFAULT_RANGE_DESCRIPTION.length())==(startIndex))||((!((startIndex)!=(1)))&&(start!=null))
```

## Bug 10

```
----INFORMATION----
Nb Statements Analyzed : 2
Nb Statements with Angelic Value Found : 0
Nopol Execution time : 68609ms
```

## Bug 11

```
----INFORMATION----
Nb Statements Analyzed : 19
Nb Statements with Angelic Value Found : 0
Nopol Execution time : 74732ms
```

## Bug 12

```
----INFORMATION----
Nb Statements Analyzed : 339
Nb Statements with Angelic Value Found : 0
Nopol Execution time : 156112ms
```

## Bug 13

```
----INFORMATION----
Nb Statements Analyzed : 38
Nb Statements with Angelic Value Found : 1
Nopol Execution time : 112855ms
----PATCH FOUND----
org.jfree.chart.block.BorderArrangement:482: CONDITIONAL null!=null
```

## Bug 14

```
----INFORMATION----
Nb Statements Analyzed : 361
Nb Statements with Angelic Value Found : 0
Nopol Execution time : 226535ms
```

## Bug 15

```
----INFORMATION----
Nb Statements Analyzed : 878
Nb Statements with Angelic Value Found : 1
Nopol Execution time : 278129ms
```

## Bug 16

```
----INFORMATION----
Nb Statements Analyzed : 45
Nb Statements with Angelic Value Found : 0
Nopol Execution time : 74080ms
```

## Bug 17

```
----INFORMATION----
Nb Statements Analyzed : 1
Nb Statements with Angelic Value Found : 1
Nopol Execution time : 100162ms
----PATCH FOUND----
org.jfree.data.time.TimeSeries:880: PRECONDITION (1)==(start)
```

## Bug 18

```
----INFORMATION----
Nb Statements Analyzed : 95
Nb Statements with Angelic Value Found : 0
Nopol Execution time : 79762ms
```

## Bug 19

```
----INFORMATION----
Nb Statements Analyzed : 512
Nb Statements with Angelic Value Found : 0
Nopol Execution time : 220260ms
```

## Bug 20

```
----INFORMATION----
Nb Statements Analyzed : 35
Nb Statements with Angelic Value Found : 0
Nopol Execution time : 70404ms
```

## Bug 21

```
----INFORMATION----
Nb Statements Analyzed : 11
Nb Statements with Angelic Value Found : 1
Nopol Execution time : 101755ms
----PATCH FOUND----
org.jfree.data.Range:335: PRECONDITION (((1)+(1))<((org.jfree.data.Range.this.upper)-(org.jfree.data.Range.this.lower)))||(!(((1)+(1))<=(org.jfree.data.Range.this.lower)))
```

## Bug 22

```
----INFORMATION----
Nb Statements Analyzed : 97
Nb Statements with Angelic Value Found : 0
Nopol Execution time : 77493ms
```

## Bug 23

```
----INFORMATION----
Nb Statements Analyzed : 218
Nb Statements with Angelic Value Found : 0
Nopol Execution time : 114512ms
```

## Bug 24

```
----INFORMATION----
Nb Statements Analyzed : 11
Nb Statements with Angelic Value Found : 0
Nopol Execution time : 65026ms
```

## Bug 25

```
----INFORMATION----
Nb Statements Analyzed : 8
Nb Statements with Angelic Value Found : 1
Nopol Execution time : 98569ms
----PATCH FOUND----
org.jfree.data.statistics.DefaultStatisticalCategoryDataset:110: CONDITIONAL ((org.jfree.data.statistics.DefaultStatisticalCategoryDataset.this.maximumRangeValue)<(org.jfree.data.statistics.DefaultStatisticalCategoryDataset.this.maximumRangeValueIncStdDev))&&(!((org.jfree.data.statistics.DefaultStatisticalCategoryDataset.this.maximumRangeValue)<=(1)))
```

## Bug 26

Time out after 6 hours.

