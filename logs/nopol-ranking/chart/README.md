# Chart - Nopol ranking

## Bug 1

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.chart.renderer.category.AbstractCategoryItemRenderer

```
1797c1797
<         if (dataset != null) {
---
>         if (dataset == null) {
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0


- Nb. undetected lines: 1/1 ( 1797 )

## Bug 2

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.data.general.DatasetUtilities

```
754a755
>                     double value = intervalXYData.getXValue(series, item);
756a758,761
>                     if (!Double.isNaN(value)) {
>                         minimum = Math.min(minimum, value);
>                         maximum = Math.max(maximum, value);
>                     }
758a764
>                         maximum = Math.max(maximum, lvalue);
760a767
>                         minimum = Math.min(minimum, uvalue);
1241a1249
>                     double value = ixyd.getYValue(series, item);
1243a1252,1255
>                     if (!Double.isNaN(value)) {
>                         minimum = Math.min(minimum, value);
>                         maximum = Math.max(maximum, value);
>                     }
1245a1258
>                         maximum = Math.max(maximum, lvalue);
1247a1261
>                         minimum = Math.min(minimum, uvalue);
```

- Deleted lines: 0<br />
- Added lines: 14<br />
- Diff added/deleted: 14


- Nb. undetected lines: 8/8 ( 754 756 758 760 1241 1243 1245 1247 )

## Bug 3

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.data.time.TimeSeries

```
1057c1057,1058
< 
---
>         copy.minY = Double.NaN;
>         copy.maxY = Double.NaN;
```

- Deleted lines: 1<br />
- Added lines: 2<br />
- Diff added/deleted: 1


- Nb. undetected lines: 1/1 ( 1057 )

## Bug 4

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.chart.plot.XYPlot

```
4492a4493
>                 if (r != null) {
4502a4504
>         }
```

- Deleted lines: 0<br />
- Added lines: 2<br />
- Diff added/deleted: 2


- Nb. undetected lines: 2/2 ( 4492 4502 )

## Bug 5

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.data.xy.XYSeries

```
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

- Deleted lines: 1<br />
- Added lines: 8<br />
- Diff added/deleted: 7


- Nb. undetected lines: 2/2 ( 543 546 )

## Bug 6

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.chart.util.ShapeList

```
99c99
<      * @param obj  the other object.
---
>      * @param obj  the other object (<code>null</code> permitted).
105,108d104
<         if (obj == null) {
<             return false;
<         }
< 
112,114c108,109
< 
<         if (obj instanceof ShapeList) {
<             return super.equals(obj);
---
>         if (!(obj instanceof ShapeList)) {
>             return false;
116c111,114
< 
---
>         ShapeList that = (ShapeList) obj;
>         int listSize = size();
>         for (int i = 0; i < listSize; i++) {
>            if (!ShapeUtilities.equal((Shape) get(i), (Shape) that.get(i))) {
117a116,118
>            }
>         }
>         return true;
```

- Deleted lines: 11<br />
- Added lines: 10<br />
- Diff added/deleted: -1


- Nb. undetected lines: 10/10 ( 99 105 106 107 108 112 113 114 116 117 )

## Bug 7

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.data.time.TimePeriodValues

```
300c300
<             long s = getDataItem(this.minMiddleIndex).getPeriod().getStart()
---
>             long s = getDataItem(this.maxMiddleIndex).getPeriod().getStart()
302c302
<             long e = getDataItem(this.minMiddleIndex).getPeriod().getEnd()
---
>             long e = getDataItem(this.maxMiddleIndex).getPeriod().getEnd()
```

- Deleted lines: 2<br />
- Added lines: 2<br />
- Diff added/deleted: 0


- Nb. undetected lines: 2/2 ( 300 302 )

## Bug 8

Ignored because of grid5000 bug.

## Bug 9

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.data.time.TimeSeries

```
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

- Deleted lines: 9<br />
- Added lines: 6<br />
- Diff added/deleted: -3


- Nb. undetected lines: 8/8 ( 677 944 973 974 975 979 980 981 )

## Bug 10

- Nb. modified sources: 3

- Nb. nopol ranking entries: -2

###  org.jfree.chart.imagemap.StandardToolTipTagFragmentGenerator

```
50a51,57
>      * Creates a new instance.
>      */
>     public StandardToolTipTagFragmentGenerator() {
>         super();
>     }
> 	
>     /**
58c65,66
<         return " title=\"" + toolTipText + "\" alt=\"\"";
---
>         return " title=\"" + ImageMapUtilities.htmlEscape(toolTipText) 
>             + "\" alt=\"\"";
```

- Deleted lines: 1<br />
- Added lines: 9<br />
- Diff added/deleted: 8


- Nb. undetected lines: 2/2 ( 50 58 )

###  org.jfree.chart.imagemap.OverLIBToolTipTagFragmentGenerator

```
51a52,58
>      * Creates a new instance.
>      */
>     public OverLIBToolTipTagFragmentGenerator() {
>         super();
>     }
> 	
>     /**
54c61
<      * @param toolTipText  the tooltip.
---
>      * @param toolTipText  the tooltip text.
59c66,67
<         return " onMouseOver=\"return overlib('" + toolTipText 
---
>         return " onMouseOver=\"return overlib('" 
>                 + ImageMapUtilities.htmlEscape(toolTipText) 
```

- Deleted lines: 2<br />
- Added lines: 10<br />
- Diff added/deleted: 8


- Nb. undetected lines: 3/3 ( 51 54 59 )

###  org.jfree.chart.imagemap.DynamicDriveToolTipTagFragmentGenerator

```
5c5
<  * (C) Copyright 2000-2007, by Object Refinery Limited and Contributors.
---
>  * (C) Copyright 2000-2008, by Object Refinery Limited and Contributors.
30c30
<  * (C) Copyright 2003-2007, by Richard Atkinson and Contributors.
---
>  * (C) Copyright 2003-2008, by Richard Atkinson and Contributors.
32a33
>  * Contributors:     David Gilbert (for Object Refinery Limited);
36a38
>  * 04-Dec-2007 : Escape tool tip text to fix bug 1400917 (DG);
83,85c85,88
<         return " onMouseOver=\"return stm(['" + this.title + "','" 
<             + toolTipText + "'],Style[" + this.style + "]);\"" 
<             + " onMouseOut=\"return htm();\"";
---
>         return " onMouseOver=\"return stm(['"
>             + ImageMapUtilities.htmlEscape(this.title) + "','"
>             + ImageMapUtilities.htmlEscape(toolTipText) + "'],Style["
>             + this.style + "]);\"" + " onMouseOut=\"return htm();\"";
```

- Deleted lines: 5<br />
- Added lines: 8<br />
- Diff added/deleted: 3


- Nb. undetected lines: 7/7 ( 5 30 32 36 83 84 85 )

## Bug 11

- Nb. modified sources: 2

- Nb. nopol ranking entries: -2

###  org.jfree.chart.util.SerialUtilities

```
318,321c318,319
<                             gp.curveTo(
<                                 args[0], args[1], args[2],
<                                 args[3], args[4], args[5]
<                             );
---
>                             gp.curveTo(args[0], args[1], args[2],
>                                     args[3], args[4], args[5]);
327c325
<                             //result = gp;
---
>                             gp.closePath();
331,332c329
<                                 "JFreeChart - No path exists"
<                             );
---
>                                     "JFreeChart - No path exists");
```

- Deleted lines: 7<br />
- Added lines: 4<br />
- Diff added/deleted: -3


- Nb. undetected lines: 7/7 ( 318 319 320 321 327 331 332 )

###  org.jfree.chart.util.ShapeUtilities

```
275c275
<         PathIterator iterator2 = p1.getPathIterator(null);
---
>         PathIterator iterator2 = p2.getPathIterator(null);
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0


- Nb. undetected lines: 1/1 ( 275 )

## Bug 12

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.chart.plot.MultiplePiePlot

```
145c145
<         this.dataset = dataset;
---
>         setDataset(dataset);
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0


- Nb. undetected lines: 1/1 ( 145 )

## Bug 13

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.chart.block.BorderArrangement

```
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

- Deleted lines: 124<br />
- Added lines: 79<br />
- Diff added/deleted: -45


- Nb. undetected lines: 124/124 ( 166 167 168 169 172 173 174 175 190 191 192 197 198 199 204 205 206 211 212 213 222 223 224 232 233 234 237 238 239 242 243 244 247 248 249 253 254 255 256 257 298 299 300 301 312 313 314 315 323 324 325 326 327 337 338 339 340 366 367 368 375 376 377 384 385 386 393 394 395 405 406 407 418 419 420 423 424 425 428 429 430 433 434 435 439 440 441 442 443 463 464 465 466 467 473 474 475 476 477 483 484 485 486 487 493 494 495 496 497 509 510 511 514 515 516 519 520 521 524 525 526 529 530 531 )

## Bug 14

- Nb. modified sources: 2

- Nb. nopol ranking entries: -2

###  org.jfree.chart.plot.CategoryPlot

```
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
```

- Deleted lines: 3<br />
- Added lines: 6<br />
- Diff added/deleted: 3


- Nb. undetected lines: 4/4 ( 2165 2448 2502 2507 )

###  org.jfree.chart.plot.XYPlot

```
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

- Deleted lines: 1<br />
- Added lines: 6<br />
- Diff added/deleted: 5


- Nb. undetected lines: 2/2 ( 2292 2529 )

## Bug 15

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.chart.plot.PiePlot

```
1377a1378,1380
>         if (this.dataset == null) {
>             return 0.0;
>         }
2050a2054
>         if (this.dataset != null) {
2052a2057
>         }
```

- Deleted lines: 0<br />
- Added lines: 5<br />
- Diff added/deleted: 5


- Nb. undetected lines: 3/3 ( 1377 2050 2052 )

## Bug 16

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.data.category.DefaultIntervalCategoryDataset

```
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

- Deleted lines: 3<br />
- Added lines: 3<br />
- Diff added/deleted: 0


- Nb. undetected lines: 3/3 ( 207 208 338 )

## Bug 17

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.data.time.TimeSeries

```
857c857,858
<         Object clone = createCopy(0, getItemCount() - 1);
---
>         TimeSeries clone = (TimeSeries) super.clone();
>         clone.data = (List) ObjectUtilities.deepClone(this.data);
```

- Deleted lines: 1<br />
- Added lines: 2<br />
- Diff added/deleted: 1


- Nb. undetected lines: 1/1 ( 857 )

## Bug 18

- Nb. modified sources: 2

- Nb. nopol ranking entries: -2

###  org.jfree.data.DefaultKeyedValues2D

```
442c442
<      * Removes a column.
---
>      * Removes a column from the table.
445a446,450
>      * @throws UnknownKeyException if the table does not contain a column with
>      *     the specified key.
>      * @throws IllegalArgumentException if <code>columnKey</code> is 
>      *     <code>null</code>.
>      * 
449a455,460
>     	if (columnKey == null) {
>     		throw new IllegalArgumentException("Null 'columnKey' argument.");
>     	}
>     	if (!this.columnKeys.contains(columnKey)) {
>     		throw new UnknownKeyException("Unknown key: " + columnKey);
>     	}
452a464,465
>             int index = rowData.getIndex(columnKey);
>             if (index >= 0) {
454a468
>         }
```

- Deleted lines: 3<br />
- Added lines: 15<br />
- Diff added/deleted: 12


- Nb. undetected lines: 5/5 ( 442 445 449 452 454 )

###  org.jfree.data.DefaultKeyedValues

```
318,320d317
< 
<         // did we remove the last item? If not, then rebuild the index ..
<         if (index < this.keys.size()) {
323d319
<     }
326,327c322
<      * Removes a value from the collection.  If there is no item with the 
<      * specified key, this method does nothing.
---
>      * Removes a value from the collection.
332a328
>      * @throws UnknownKeyException if <code>key</code> is not recognised.
336,337c332,334
<         if (index >= 0) {
<             removeValue(index);
---
>         if (index < 0) {
>             throw new UnknownKeyException("The key (" + key 
>                     + ") is not recognised.");
338a336
>         removeValue(index);
```

- Deleted lines: 10<br />
- Added lines: 7<br />
- Diff added/deleted: -3


- Nb. undetected lines: 10/10 ( 318 319 320 323 326 327 332 336 337 338 )

## Bug 19

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.chart.plot.CategoryPlot

```
688c688
<      * @param axis  the axis.
---
>      * @param axis  the axis (<code>null</code> not permitted).
691a692,694
>      * @see #getDomainAxis(int)
>      * @see #getRangeAxisIndex(ValueAxis)
>      * 
694a698,700
>         if (axis == null) {
>             throw new IllegalArgumentException("Null 'axis' argument.");
>         }
954a961
> 
959c966
<      * @param axis  the axis.
---
>      * @param axis  the axis (<code>null</code> not permitted).
962a970
>      * @see #getRangeAxis(int)
967a976,978
>         if (axis == null) {
>             throw new IllegalArgumentException("Null 'axis' argument.");
>         }
```

- Deleted lines: 4<br />
- Added lines: 13<br />
- Diff added/deleted: 9


- Nb. undetected lines: 7/7 ( 688 691 694 954 959 962 967 )

## Bug 20

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.chart.plot.ValueMarker

```
91c91
<      * @param alpha  the alpha transparency.
---
>      * @param alpha  the alpha transparency (in the range 0.0f to 1.0f).
95c95
<         super(paint, stroke, paint, stroke, alpha);
---
>         super(paint, stroke, outlinePaint, outlineStroke, alpha);
```

- Deleted lines: 2<br />
- Added lines: 2<br />
- Diff added/deleted: 0


- Nb. undetected lines: 2/2 ( 91 95 )

## Bug 21

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.data.statistics.DefaultBoxAndWhiskerCategoryDataset

```
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

- Deleted lines: 24<br />
- Added lines: 63<br />
- Diff added/deleted: 39


- Nb. undetected lines: 19/19 ( 123 124 127 128 137 138 140 141 149 150 151 152 153 154 155 157 188 192 737 )

## Bug 22

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.data.KeyedObjects2D

```
204,205c204,205
<      * @param rowKey  the row key.
<      * @param columnKey  the column key.
---
>      * @param rowKey  the row key (<code>null</code> not permitted).
>      * @param columnKey  the column key (<code>null</code> not permitted).
207c207,212
<      * @return The object.
---
>      * @return The object (possibly <code>null</code>).
>      * 
>      * @throws IllegalArgumentException if <code>rowKey<code> or 
>      *         <code>columnKey</code> is <code>null</code>.
>      * @throws UnknownKeyException if <code>rowKey</code> or 
>      *         <code>columnKey</code> is not recognised.
210,211c215,220
< 
<         Object result = null;
---
>         if (rowKey == null) {
>             throw new IllegalArgumentException("Null 'rowKey' argument.");
>         }
>         if (columnKey == null) {
>             throw new IllegalArgumentException("Null 'columnKey' argument.");
>         }
213c222,230
<         if (row >= 0) {
---
>         if (row < 0) {
>             throw new UnknownKeyException("Row key (" + rowKey 
>                     + ") not recognised.");
>         }
>         int column = this.columnKeys.indexOf(columnKey);
>         if (column < 0) {
>             throw new UnknownKeyException("Column key (" + columnKey 
>                     + ") not recognised.");
>         }
215c232,237
<             result = rowData.getObject(columnKey);
---
>         int index = rowData.getIndex(columnKey);
>         if (index >= 0) {
>             return rowData.getObject(index);
>         }
>         else {
>             return null;
217,218d238
<         return result;
< 
225,226c245,246
<      * @param rowKey  the row key.
<      * @param columnKey  the column key.
---
>      * @param rowKey  the row key (<code>null</code> not permitted).
>      * @param columnKey  the column key (<code>null</code> not permitted).
228,229c248
<     public void addObject(Object object, 
<                           Comparable rowKey, 
---
>     public void addObject(Object object, Comparable rowKey, 
238,239c257,258
<      * @param rowKey  the row key.
<      * @param columnKey  the column key.
---
>      * @param rowKey  the row key (<code>null</code> not permitted).
>      * @param columnKey  the column key (<code>null</code> not permitted).
241,242c260
<     public void setObject(Object object, 
<                           Comparable rowKey, 
---
>     public void setObject(Object object, Comparable rowKey, 
244a263,268
>         if (rowKey == null) {
>             throw new IllegalArgumentException("Null 'rowKey' argument.");
>         }
>         if (columnKey == null) {
>             throw new IllegalArgumentException("Null 'columnKey' argument.");
>         }
264c288,293
<      * Removes an object.
---
>      * Removes an object from the table by setting it to <code>null</code>.  If
>      * all the objects in the specified row and/or column are now 
>      * <code>null</code>, the row and/or column is removed from the table.
>      *
>      * @param rowKey  the row key (<code>null</code> not permitted).
>      * @param columnKey  the column key (<code>null</code> not permitted).
266,267c295
<      * @param rowKey  the row key.
<      * @param columnKey  the column key.
---
>      * @see #addObject(Object, Comparable, Comparable)
271,272c299,341
<         // actually, a null value is different to a value that doesn't exist 
<         // at all, need to fix this code.
---
>         
>         // 1. check whether the row is now empty.
>         boolean allNull = true;
>         int rowIndex = getRowIndex(rowKey);
>         KeyedObjects row = (KeyedObjects) this.rows.get(rowIndex);
> 
>         for (int item = 0, itemCount = row.getItemCount(); item < itemCount; 
>              item++) {
>             if (row.getObject(item) != null) {
>                 allNull = false;
>                 break;
>             }
>         }
>         
>         if (allNull) {
>             this.rowKeys.remove(rowIndex);
>             this.rows.remove(rowIndex);
>         }
>         
>         // 2. check whether the column is now empty.
>         allNull = true;
>         
>         for (int item = 0, itemCount = this.rows.size(); item < itemCount; 
>              item++) {
>             row = (KeyedObjects) this.rows.get(item);
>             int columnIndex = row.getIndex(columnKey);
>             if (columnIndex >= 0 && row.getObject(columnIndex) != null) {
>                 allNull = false;
>                 break;
>             }
>         }
>         
>         if (allNull) {
>             for (int item = 0, itemCount = this.rows.size(); item < itemCount; 
>                  item++) {
>                 row = (KeyedObjects) this.rows.get(item);
>                 int columnIndex = row.getIndex(columnKey);
>                 if (columnIndex >= 0) {
>                     row.removeValue(columnIndex);
>                 }
>             }
>             this.columnKeys.remove(columnKey);
>         }
276c345
<      * Removes a row.
---
>      * Removes an entire row from the table.
278a348,349
>      * 
>      * @see #removeColumn(int)
286c357,361
<      * Removes a row.
---
>      * Removes an entire row from the table.
>      *
>      * @param rowKey  the row key (<code>null</code> not permitted).
>      * 
>      * @throws UnknownKeyException if <code>rowKey</code> is not recognised.
288c363
<      * @param rowKey  the row key.
---
>      * @see #removeColumn(Comparable)
291c366,371
<         removeRow(getRowIndex(rowKey));
---
>         int index = getRowIndex(rowKey);
>         if (index < 0) {
>             throw new UnknownKeyException("Row key (" + rowKey 
>                     + ") not recognised.");
>         }
>         removeRow(index);
295c375
<      * Removes a column.
---
>      * Removes an entire column from the table.
297a378,379
>      * 
>      * @see #removeRow(int)
305c387
<      * Removes a column.
---
>      * Removes an entire column from the table.
307c389,393
<      * @param columnKey  the column key.
---
>      * @param columnKey  the column key (<code>null</code> not permitted).
>      * 
>      * @throws UnknownKeyException if <code>rowKey</code> is not recognised.
>      * 
>      * @see #removeRow(Comparable)
309a396,400
>         int index = getColumnIndex(columnKey);
>         if (index < 0) {
>             throw new UnknownKeyException("Column key (" + columnKey 
>                     + ") not recognised.");
>         }
313c404,407
<             rowData.removeValue(columnKey);
---
>             int i = rowData.getIndex(columnKey);
>             if (i >= 0) {
>                 rowData.removeValue(i);
>             }
```

- Deleted lines: 56<br />
- Added lines: 125<br />
- Diff added/deleted: 69


- Nb. undetected lines: 34/34 ( 204 205 207 210 211 213 215 217 218 225 226 228 229 238 239 241 242 244 264 266 267 271 272 276 278 286 288 291 295 297 305 307 309 313 )

## Bug 23

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.chart.renderer.category.MinMaxCategoryRenderer

```
86d85
< import org.jfree.chart.entity.CategoryItemEntity;
89d87
< import org.jfree.chart.labels.CategoryToolTipGenerator;
91a90
> import org.jfree.chart.util.PaintUtilities;
220c219,220
<      * value.
---
>      * value and sends a {@link RendererChangeEvent} to all registered 
>      * listeners.
222c222
<      * @param groupStroke The new stroke
---
>      * @param stroke the new stroke (<code>null</code> not permitted).
224,225c224,229
<     public void setGroupStroke(Stroke groupStroke) {
<         this.groupStroke = groupStroke;
---
>     public void setGroupStroke(Stroke stroke) {
>         if (stroke == null) {
>             throw new IllegalArgumentException("Null 'stroke' argument.");
>         }
>         this.groupStroke = stroke;
>         notifyListeners(new RendererChangeEvent(this));        
413,414c417
<             // collect entity and tool tip information...
<             if (state.getInfo() != null) {
---
>             // add an item entity, if this information is being collected
417,426c420,444
<                     String tip = null;
<                     CategoryToolTipGenerator tipster = getToolTipGenerator(row,
<                             column);
<                     if (tipster != null) {
<                         tip = tipster.generateToolTip(dataset, row, column);
<                     }
<                     CategoryItemEntity entity = new CategoryItemEntity(
<                             shape, tip, null, dataset, dataset.getRowKey(row), 
<                             dataset.getColumnKey(column));
<                     entities.add(entity);
---
>                 addItemEntity(entities, dataset, row, column, shape);
>             }
>         }
>     }
>     
>     /**
>      * Tests this instance for equality with an arbitrary object.  The icon fields
>      * are NOT included in the test, so this implementation is a little weak.
>      * 
>      * @param obj  the object (<code>null</code> permitted).
>      * 
>      * @return A boolean.
>      *
>      * @since 1.0.7
>      */
>     public boolean equals(Object obj) {
>         if (obj == this) {
>             return true;
>         }
>         if (!(obj instanceof MinMaxCategoryRenderer)) {
>             return false;
>         }
>         MinMaxCategoryRenderer that = (MinMaxCategoryRenderer) obj;
>         if (this.plotLines != that.plotLines) {
>             return false;
427a446,447
>         if (!PaintUtilities.equal(this.groupPaint, that.groupPaint)) {
>             return false;
428a449,450
>         if (!this.groupStroke.equals(that.groupStroke)) {
>             return false;
429a452
>         return super.equals(obj);
```

- Deleted lines: 20<br />
- Added lines: 41<br />
- Diff added/deleted: 21


- Nb. undetected lines: 22/22 ( 86 89 91 220 222 224 225 413 414 417 418 419 420 421 422 423 424 425 426 427 428 429 )

## Bug 24

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.chart.renderer.GrayPaintScale

```
118c118,119
<      * @param value  the value.
---
>      * @param value  the value (must be within the range specified by the
>      *         lower and upper bounds for the scale).
125c126
<         int g = (int) ((value - this.lowerBound) / (this.upperBound 
---
>         int g = (int) ((v - this.lowerBound) / (this.upperBound 
```

- Deleted lines: 2<br />
- Added lines: 3<br />
- Diff added/deleted: 1


- Nb. undetected lines: 2/2 ( 118 125 )

## Bug 25

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.chart.renderer.category.StatisticalBarRenderer

```
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

- Deleted lines: 2<br />
- Added lines: 14<br />
- Diff added/deleted: 12


- Nb. undetected lines: 6/6 ( 258 315 343 402 459 486 )

## Bug 26

- Nb. modified sources: 1

- Nb. nopol ranking entries: -2

###  org.jfree.chart.axis.Axis

```
1191,1192c1191,1193
<             EntityCollection entities = plotState.getOwner()
<                     .getEntityCollection();
---
>             ChartRenderingInfo owner = plotState.getOwner();
>             if (owner != null) {
>                 EntityCollection entities = owner.getEntityCollection();
1197a1199
>         }
```

- Deleted lines: 2<br />
- Added lines: 4<br />
- Diff added/deleted: 2


- Nb. undetected lines: 3/3 ( 1191 1192 1197 )

