# Chart - Nopol angelic condition repair


- Nb patch found: 6/25

| #Bug | Nb Statements Analyzed | Nb Angelic Value Found | Exec. time | Patch Found |
|------|---------------|--------------|------------|------------|
| 1 |  464 |  0 |  288896ms | NO |
| 2 |  166 |  0 |  98484ms | NO |
| 3 | NONE | NONE | > 6h | NO |
| 4 | NONE | NONE | > 6h | NO |
| 5 |  3 |  1 |  101534ms | YES |
| 6 | NONE | NONE | > 6h | NO |
| 7 |  122 |  0 |  82130ms | NO |
| 8 | IGNORED | IGNORED | IGNORED | IGNORED |
| 9 |  8 |  1 |  102417ms | YES |
| 10 |  2 |  0 |  68609ms | NO |
| 11 |  19 |  0 |  74732ms | NO |
| 12 |  339 |  0 |  156112ms | NO |
| 13 |  38 |  1 |  112855ms | YES |
| 14 |  361 |  0 |  226535ms | NO |
| 15 |  878 |  1 |  278129ms | NO |
| 16 |  45 |  0 |  74080ms | NO |
| 17 |  1 |  1 |  100162ms | YES |
| 18 |  95 |  0 |  79762ms | NO |
| 19 |  512 |  0 |  220260ms | NO |
| 20 |  35 |  0 |  70404ms | NO |
| 21 |  11 |  1 |  101755ms | YES |
| 22 |  97 |  0 |  77493ms | NO |
| 23 |  218 |  0 |  114512ms | NO |
| 24 |  11 |  0 |  65026ms | NO |
| 25 |  8 |  1 |  98569ms | YES |
| 26 | NONE | NONE | > 6h | NO |
## Patches

### Bug 5

- Ranking nopol: 3

- Nopol patch:

```
----INFORMATION----
Nb Statements Analyzed : 3
Nb Statements with Angelic Value Found : 1
Nopol Execution time : 101534ms
----PATCH FOUND----
org.jfree.data.xy.XYSeries:561: CONDITIONAL !(org.jfree.data.xy.XYSeries.this.allowDuplicateXValues)
```

- IRL patch:

```
org.jfree.data.xy.XYSeries

543a544,549
>         if (this.allowDuplicateXValues) {
>             add(x, y);
>             return null;
>         }
> 
>         // if we get to here, we know that duplicate X values are not permitted
546c552
<         if (index >= 0 && !this.allowDuplicateXValues) {
---
>         if (index >= 0) {


```

### Bug 9

- Ranking nopol: 8

- Nopol patch:

```
----INFORMATION----
Nb Statements Analyzed : 8
Nb Statements with Angelic Value Found : 1
Nopol Execution time : 102417ms
----PATCH FOUND----
org.jfree.data.time.TimeSeries:935: CONDITIONAL ((org.jfree.data.time.TimeSeries.DEFAULT_RANGE_DESCRIPTION.length())==(startIndex))||((!((startIndex)!=(1)))&&(start!=null))
```

- IRL patch:

```
org.jfree.data.time.TimeSeries

677c677
<         return this.addOrUpdate(period, new Double(value));
---
>         return addOrUpdate(period, new Double(value));
944c944
<         if (endIndex < 0) {
---
>         if ((endIndex < 0)  || (endIndex < startIndex)) {
973,975c973,974
<         if (!ObjectUtilities.equal(
<             getDomainDescription(), s.getDomainDescription()
<         )) {
---
>         if (!ObjectUtilities.equal(getDomainDescription(),
>                 s.getDomainDescription())) {
979,981c978,979
<         if (!ObjectUtilities.equal(
<             getRangeDescription(), s.getRangeDescription()
<         )) {
---
>         if (!ObjectUtilities.equal(getRangeDescription(),
>                 s.getRangeDescription())) {


```

### Bug 13

- Ranking nopol: 38

- Nopol patch:

```
----INFORMATION----
Nb Statements Analyzed : 38
Nb Statements with Angelic Value Found : 1
Nopol Execution time : 112855ms
----PATCH FOUND----
org.jfree.chart.block.BorderArrangement:482: CONDITIONAL null!=null
```

- IRL patch:

```
org.jfree.chart.block.BorderArrangement

166,169c166,167
<                 contentSize = arrangeRR(
<                     container, constraint.getWidthRange(),
<                     constraint.getHeightRange(), g2
<                 );  
---
>                 contentSize = arrangeRR(container, constraint.getWidthRange(),
>                         constraint.getHeightRange(), g2);
172,175c170,171
<         return new Size2D(
<             container.calculateTotalWidth(contentSize.getWidth()),
<             container.calculateTotalHeight(contentSize.getHeight())
<         );
---
>         return new Size2D(container.calculateTotalWidth(contentSize.getWidth()),
>                 container.calculateTotalHeight(contentSize.getHeight()));
190,192c186
<             Size2D size = this.topBlock.arrange(
<                 g2, RectangleConstraint.NONE
<             );
---
>             Size2D size = this.topBlock.arrange(g2, RectangleConstraint.NONE);
197,199c191,192
<             Size2D size = this.bottomBlock.arrange(
<                 g2, RectangleConstraint.NONE
<             );
---
>             Size2D size = this.bottomBlock.arrange(g2,
>                     RectangleConstraint.NONE);
204,206c197
<             Size2D size = this.leftBlock.arrange(
<                 g2, RectangleConstraint.NONE
<             );
---
>             Size2D size = this.leftBlock.arrange(g2, RectangleConstraint.NONE);
211,213c202
<             Size2D size = this.rightBlock.arrange(
<                 g2, RectangleConstraint.NONE
<             );
---
>             Size2D size = this.rightBlock.arrange(g2, RectangleConstraint.NONE);
222,224c211,212
<             Size2D size = this.centerBlock.arrange(
<                 g2, RectangleConstraint.NONE
<             );
---
>             Size2D size = this.centerBlock.arrange(g2,
>                     RectangleConstraint.NONE);
232,234c220,221
<             this.topBlock.setBounds(
<                 new Rectangle2D.Double(0.0, 0.0, width, h[0])
<             );
---
>             this.topBlock.setBounds(new Rectangle2D.Double(0.0, 0.0, width,
>                     h[0]));
237,239c224,225
<             this.bottomBlock.setBounds(
<                 new Rectangle2D.Double(0.0, height - h[1], width, h[1])
<             );
---
>             this.bottomBlock.setBounds(new Rectangle2D.Double(0.0,
>                     height - h[1], width, h[1]));
242,244c228,229
<             this.leftBlock.setBounds(
<                 new Rectangle2D.Double(0.0, h[0], w[2], centerHeight)
<             );
---
>             this.leftBlock.setBounds(new Rectangle2D.Double(0.0, h[0], w[2],
>                     centerHeight));
247,249c232,233
<             this.rightBlock.setBounds(
<                 new Rectangle2D.Double(width - w[3], h[0], w[3], centerHeight)
<             );
---
>             this.rightBlock.setBounds(new Rectangle2D.Double(width - w[3],
>                     h[0], w[3], centerHeight));
253,257c237,238
<             this.centerBlock.setBounds(
<                 new Rectangle2D.Double(
<                     w[2], h[0], width - w[2] - w[3], centerHeight
<                 )
<             );
---
>             this.centerBlock.setBounds(new Rectangle2D.Double(w[2], h[0],
>                     width - w[2] - w[3], centerHeight));
298,301c279,281
<         RectangleConstraint c1 = new RectangleConstraint(
<             width, null, LengthConstraintType.FIXED,
<             0.0, null, LengthConstraintType.NONE
<         );
---
>         RectangleConstraint c1 = new RectangleConstraint(width, null,
>                 LengthConstraintType.FIXED, 0.0, null,
>                 LengthConstraintType.NONE);
312,315c292,294
<         RectangleConstraint c2 = new RectangleConstraint(
<             0.0, new Range(0.0, width), LengthConstraintType.RANGE,
<             0.0, null, LengthConstraintType.NONE
<         );
---
>         RectangleConstraint c2 = new RectangleConstraint(0.0,
>                 new Range(0.0, width), LengthConstraintType.RANGE,
>                 0.0, null, LengthConstraintType.NONE);
323,327c302,305
<             RectangleConstraint c3 = new RectangleConstraint(
<                 0.0, new Range(Math.min(w[2], maxW), maxW), 
<                 LengthConstraintType.RANGE,
<                 0.0, null, LengthConstraintType.NONE
<             );    
---
>             RectangleConstraint c3 = new RectangleConstraint(0.0,
>                     new Range(Math.min(w[2], maxW), maxW),
>                     LengthConstraintType.RANGE, 0.0, null,
>                     LengthConstraintType.NONE);
337,340c315,317
<             RectangleConstraint c4 = new RectangleConstraint(
<                 width - w[2] - w[3], null, LengthConstraintType.FIXED,
<                 0.0, null, LengthConstraintType.NONE
<             );    
---
>             RectangleConstraint c4 = new RectangleConstraint(width - w[2]
>                     - w[3], null, LengthConstraintType.FIXED, 0.0, null,
>                     LengthConstraintType.NONE);
366,368c343,344
<             RectangleConstraint c1 = new RectangleConstraint(
<                 widthRange, heightRange
<             );
---
>             RectangleConstraint c1 = new RectangleConstraint(widthRange,
>                     heightRange);
375,377c351,352
<             RectangleConstraint c2 = new RectangleConstraint(
<                 widthRange, heightRange2
<             );  
---
>             RectangleConstraint c2 = new RectangleConstraint(widthRange,
>                     heightRange2);
384,386c359,360
<             RectangleConstraint c3 = new RectangleConstraint(
<                 widthRange, heightRange3
<             );
---
>             RectangleConstraint c3 = new RectangleConstraint(widthRange,
>                     heightRange3);
393,395c367,368
<             RectangleConstraint c4 = new RectangleConstraint(
<                 widthRange2, heightRange3
<             );
---
>             RectangleConstraint c4 = new RectangleConstraint(widthRange2,
>                     heightRange3);
405,407c378,379
<             RectangleConstraint c5 = new RectangleConstraint(
<                 widthRange3, heightRange3
<             );
---
>             RectangleConstraint c5 = new RectangleConstraint(widthRange3,
>                     heightRange3);
418,420c390,391
<             this.topBlock.setBounds(
<                 new Rectangle2D.Double(0.0, 0.0, width, h[0])
<             );
---
>             this.topBlock.setBounds(new Rectangle2D.Double(0.0, 0.0, width,
>                     h[0]));
423,425c394,395
<             this.bottomBlock.setBounds(
<                 new Rectangle2D.Double(0.0, height - h[1], width, h[1])
<             );
---
>             this.bottomBlock.setBounds(new Rectangle2D.Double(0.0,
>                     height - h[1], width, h[1]));
428,430c398,399
<             this.leftBlock.setBounds(
<                 new Rectangle2D.Double(0.0, h[0], w[2], h[2])
<             );
---
>             this.leftBlock.setBounds(new Rectangle2D.Double(0.0, h[0], w[2],
>                     h[2]));
433,435c402,403
<             this.rightBlock.setBounds(
<                 new Rectangle2D.Double(width - w[3], h[0], w[3], h[3])
<             );
---
>             this.rightBlock.setBounds(new Rectangle2D.Double(width - w[3],
>                     h[0], w[3], h[3]));
439,443c407,408
<             this.centerBlock.setBounds(
<                 new Rectangle2D.Double(
<                     w[2], h[0], width - w[2] - w[3], height - h[0] - h[1]
<                 )
<             );
---
>             this.centerBlock.setBounds(new Rectangle2D.Double(w[2], h[0],
>                     width - w[2] - w[3], height - h[0] - h[1]));
463,467c428,431
<             RectangleConstraint c1 = new RectangleConstraint(
<                 w[0], null, LengthConstraintType.FIXED,
<                 0.0, new Range(0.0, constraint.getHeight()), 
<                 LengthConstraintType.RANGE
<             );
---
>             RectangleConstraint c1 = new RectangleConstraint(w[0], null,
>                     LengthConstraintType.FIXED, 0.0,
>                     new Range(0.0, constraint.getHeight()),
>                     LengthConstraintType.RANGE);
473,477c437,439
<             RectangleConstraint c2 = new RectangleConstraint(
<                 w[0], null, LengthConstraintType.FIXED,
<                 0.0, new Range(0.0, constraint.getHeight() - h[0]), 
<                 LengthConstraintType.RANGE
<             );
---
>             RectangleConstraint c2 = new RectangleConstraint(w[0], null,
>                     LengthConstraintType.FIXED, 0.0, new Range(0.0,
>                     constraint.getHeight() - h[0]), LengthConstraintType.RANGE);
483,487c445,448
<             RectangleConstraint c3 = new RectangleConstraint(
<                 0.0, new Range(0.0, constraint.getWidth()), 
<                 LengthConstraintType.RANGE,
<                 h[2], null, LengthConstraintType.FIXED
<             );
---
>             RectangleConstraint c3 = new RectangleConstraint(0.0,
>                     new Range(0.0, constraint.getWidth()),
>                     LengthConstraintType.RANGE, h[2], null,
>                     LengthConstraintType.FIXED);
493,497c454,457
<             RectangleConstraint c4 = new RectangleConstraint(
<                 0.0, new Range(0.0, constraint.getWidth() - w[2]), 
<                 LengthConstraintType.RANGE,
<                 h[2], null, LengthConstraintType.FIXED
<             );
---
>             RectangleConstraint c4 = new RectangleConstraint(0.0,
>                     new Range(0.0, Math.max(constraint.getWidth() - w[2], 0.0)),
>                     LengthConstraintType.RANGE, h[2], null,
>                     LengthConstraintType.FIXED);
509,511c469,470
<             this.topBlock.setBounds(
<                 new Rectangle2D.Double(0.0, 0.0, w[0], h[0])
<             );
---
>             this.topBlock.setBounds(new Rectangle2D.Double(0.0, 0.0, w[0],
>                     h[0]));
514,516c473,474
<             this.bottomBlock.setBounds(
<                 new Rectangle2D.Double(0.0, h[0] + h[2], w[1], h[1])
<             );
---
>             this.bottomBlock.setBounds(new Rectangle2D.Double(0.0, h[0] + h[2],
>                     w[1], h[1]));
519,521c477,478
<             this.leftBlock.setBounds(
<                 new Rectangle2D.Double(0.0, h[0], w[2], h[2])
<             );
---
>             this.leftBlock.setBounds(new Rectangle2D.Double(0.0, h[0], w[2],
>                     h[2]));
524,526c481,482
<             this.rightBlock.setBounds(
<                 new Rectangle2D.Double(w[2] + w[4], h[0], w[3], h[3])
<             );
---
>             this.rightBlock.setBounds(new Rectangle2D.Double(w[2] + w[4], h[0],
>                     w[3], h[3]));
529,531c485,486
<             this.centerBlock.setBounds(
<                 new Rectangle2D.Double(w[2], h[0], w[4], h[4])
<             );
---
>             this.centerBlock.setBounds(new Rectangle2D.Double(w[2], h[0], w[4],
>                     h[4]));


```

### Bug 17

- Ranking nopol: 1

- Nopol patch:

```
----INFORMATION----
Nb Statements Analyzed : 1
Nb Statements with Angelic Value Found : 1
Nopol Execution time : 100162ms
----PATCH FOUND----
org.jfree.data.time.TimeSeries:880: PRECONDITION (1)==(start)
```

- IRL patch:

```
org.jfree.data.time.TimeSeries

857c857,858
<         Object clone = createCopy(0, getItemCount() - 1);
---
>         TimeSeries clone = (TimeSeries) super.clone();
>         clone.data = (List) ObjectUtilities.deepClone(this.data);


```

### Bug 21

- Ranking nopol: 11

- Nopol patch:

```
----INFORMATION----
Nb Statements Analyzed : 11
Nb Statements with Angelic Value Found : 1
Nopol Execution time : 101755ms
----PATCH FOUND----
org.jfree.data.Range:335: PRECONDITION (((1)+(1))<((org.jfree.data.Range.this.upper)-(org.jfree.data.Range.this.lower)))||(!(((1)+(1))<=(org.jfree.data.Range.this.lower)))
```

- IRL patch:

```
org.jfree.data.statistics.DefaultBoxAndWhiskerCategoryDataset

123,124c123,126
<      * @param rowKey  the row key.
<      * @param columnKey  the column key.
---
>      * @param rowKey  the row key (<code>null</code> not permitted).
>      * @param columnKey  the column key (<code>null</code> not permitted).
>      * 
>      * @see #add(BoxAndWhiskerItem, Comparable, Comparable)
127,128c129,130
<         BoxAndWhiskerItem item 
<             = BoxAndWhiskerCalculator.calculateBoxAndWhiskerStatistics(list);
---
>         BoxAndWhiskerItem item = BoxAndWhiskerCalculator
>                 .calculateBoxAndWhiskerStatistics(list);
137,138c139,142
<      * @param rowKey  the row key.
<      * @param columnKey  the column key.
---
>      * @param rowKey  the row key (<code>null</code> not permitted).
>      * @param columnKey  the column key (<code>null</code> not permitted).
>      * 
>      * @see #add(List, Comparable, Comparable)
140,141c144
<     public void add(BoxAndWhiskerItem item, 
<                     Comparable rowKey, 
---
>     public void add(BoxAndWhiskerItem item, Comparable rowKey, 
149,155c152,155
<         if (this.maximumRangeValueRow == r 
<                 && this.maximumRangeValueColumn == c) {
<             this.maximumRangeValue = Double.NaN;
<         }
<         if (this.minimumRangeValueRow == r 
<                 && this.minimumRangeValueColumn == c) {
<             this.minimumRangeValue = Double.NaN;
---
>         if ((this.maximumRangeValueRow == r && this.maximumRangeValueColumn 
>                 == c) || (this.minimumRangeValueRow == r 
>                 && this.minimumRangeValueColumn == c))  {
>             updateBounds();
157c157
<         
---
>         else {
188a189
>         }
192d192
< 
737a738,783
>      * Resets the cached bounds, by iterating over the entire dataset to find
>      * the current bounds.
>      */
>     private void updateBounds() {
>         this.minimumRangeValue = Double.NaN;
>         this.minimumRangeValueRow = -1;
>         this.minimumRangeValueColumn = -1;
>         this.maximumRangeValue = Double.NaN;
>         this.maximumRangeValueRow = -1;
>         this.maximumRangeValueColumn = -1;
>         int rowCount = getRowCount();
>         int columnCount = getColumnCount();
>         for (int r = 0; r < rowCount; r++) {
>             for (int c = 0; c < columnCount; c++) {
>                 BoxAndWhiskerItem item = getItem(r, c);
>                 if (item != null) {
>                     Number min = item.getMinOutlier();
>                     if (min != null) {
>                         double minv = min.doubleValue();
>                         if (!Double.isNaN(minv)) {
>                             if (minv < this.minimumRangeValue || Double.isNaN(
>                                     this.minimumRangeValue)) {
>                                 this.minimumRangeValue = minv;
>                                 this.minimumRangeValueRow = r;
>                                 this.minimumRangeValueColumn = c;
>                             }
>                         }
>                     }
>                     Number max = item.getMaxOutlier();
>                     if (max != null) {
>                         double maxv = max.doubleValue();
>                         if (!Double.isNaN(maxv)) {
>                             if (maxv > this.maximumRangeValue || Double.isNaN(
>                                     this.maximumRangeValue)) {
>                                 this.maximumRangeValue = maxv;
>                                 this.maximumRangeValueRow = r;
>                                 this.maximumRangeValueColumn = c;
>                             }
>                         }
>                     }
>                 }
>             }
>         }
>     }
>     
>     /**


```

### Bug 25

- Ranking nopol: 8

- Nopol patch:

```
----INFORMATION----
Nb Statements Analyzed : 8
Nb Statements with Angelic Value Found : 1
Nopol Execution time : 98569ms
----PATCH FOUND----
org.jfree.data.statistics.DefaultStatisticalCategoryDataset:110: CONDITIONAL ((org.jfree.data.statistics.DefaultStatisticalCategoryDataset.this.maximumRangeValue)<(org.jfree.data.statistics.DefaultStatisticalCategoryDataset.this.maximumRangeValueIncStdDev))&&(!((org.jfree.data.statistics.DefaultStatisticalCategoryDataset.this.maximumRangeValue)<=(1)))
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

