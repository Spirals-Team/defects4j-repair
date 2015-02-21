# Lang - Nopol ranking

## Bug 1

- Nb. modified sources: 2

- Nb. nopol ranking entries: 38065

###  org.apache.commons.math3.fraction.BigFraction

```
303a304,308
>                 // in maxDenominator mode, if the last fraction was very close to the actual value
>                 // q2 may overflow in the next iteration; in this case return the last one.
>                 if (epsilon == 0.0 && FastMath.abs(q1) < maxDenominator) {
>                     break;
>                 }
```

- Deleted lines: 1<br />
- Added lines: 5<br />
- Diff added/deleted: 4


- Nb. undetected lines: 1/1 ( 303 )

###  org.apache.commons.math3.fraction.Fraction

```
85a86,88
>     /** The default epsilon used for convergence. */
>     private static final double DEFAULT_EPSILON = 1e-5;
> 
99c102
<         this(value, 1.0e-5, 100);
---
>         this(value, DEFAULT_EPSILON, 100);
207a211
> 
208a213,217
>                 // in maxDenominator mode, if the last fraction was very close to the actual value
>                 // q2 may overflow in the next iteration; in this case return the last one.
>                 if (epsilon == 0.0 && FastMath.abs(q1) < maxDenominator) {
>                     break;
>                 }
```

- Deleted lines: 2<br />
- Added lines: 10<br />
- Diff added/deleted: 8


- Nb. undetected lines: 4/4 ( 85 99 207 208 )

## Bug 2

- Nb. modified sources: 1

- Nb. nopol ranking entries: 37209

###  org.apache.commons.math3.distribution.HypergeometricDistribution

```
268c268
<         return (double) (getSampleSize() * getNumberOfSuccesses()) / (double) getPopulationSize();
---
>         return getSampleSize() * (getNumberOfSuccesses() / (double) getPopulationSize());
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0


- Nb. undetected lines: 1/1 ( 268 )

## Bug 3

- Nb. modified sources: 1

- Nb. nopol ranking entries: 31510

###  org.apache.commons.math3.util.MathArrays

```
820a821,825
>         if (len == 1) {
>             // Revert to scalar multiplication.
>             return a[0] * b[0];
>         }
> 
```

- Deleted lines: 0<br />
- Added lines: 5<br />
- Diff added/deleted: 5


- Nb. undetected lines: 1/1 ( 820 )

## Bug 4

- Nb. modified sources: 2

- Nb. nopol ranking entries: 39550

###  org.apache.commons.math3.geometry.euclidean.twod.SubLine

```
113a114,116
>         if (v1D == null) {
>             return null;
>         }
```

- Deleted lines: 0<br />
- Added lines: 3<br />
- Diff added/deleted: 3


- Nb. undetected lines: 1/1 ( 117 )

###  org.apache.commons.math3.geometry.euclidean.threed.SubLine

```
113a114,116
>         if (v1D == null) {
>             return null;
>         }
```

- Deleted lines: 0<br />
- Added lines: 3<br />
- Diff added/deleted: 3


- Nb. undetected lines: 1/1 ( 113 )

## Bug 5

- Nb. modified sources: 1

- Nb. nopol ranking entries: 20368

###  org.apache.commons.math3.complex.Complex

```
305c305
<             return NaN;
---
>             return INF;
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0


- Nb. undetected lines: 1/1 ( 305 )

## Bug 6

- Nb. modified sources: 7

- Nb. nopol ranking entries: 20698

###  org.apache.commons.math3.optim.nonlinear.vector.jacobian.LevenbergMarquardtOptimizer

```
322d321
<         int iter = 0;
325c324,325
<             ++iter;
---
>             incrementIterationCount();
> 
489c489
<                         if (checker.converged(iter, previous, current)) {
---
>                         if (checker.converged(getIterations(), previous, current)) {
```

- Deleted lines: 3<br />
- Added lines: 3<br />
- Diff added/deleted: 0


- Nb. undetected lines: 3/3 ( 322 325 489 )

###  org.apache.commons.math3.optim.BaseOptimizer

```
51c51
<         iterations = new Incrementor(0, new MaxIterCallback());
---
>         iterations = new Incrementor(Integer.MAX_VALUE, new MaxIterCallback());
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0


- Nb. undetected lines: 1/1 ( 51 )

###  org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizer

```
387a388,389
>             incrementIterationCount();
> 
```

- Deleted lines: 0<br />
- Added lines: 2<br />
- Diff added/deleted: 2


- Nb. undetected lines: 1/1 ( 387 )

###  org.apache.commons.math3.optim.nonlinear.vector.jacobian.GaussNewtonOptimizer

```
106d105
<         int iter = 0;
108c107
<             ++iter;
---
>             incrementIterationCount();
160c159
<                 converged = checker.converged(iter, previous, current);
---
>                 converged = checker.converged(getIterations(), previous, current);
```

- Deleted lines: 3<br />
- Added lines: 2<br />
- Diff added/deleted: -1


- Nb. undetected lines: 3/3 ( 106 108 160 )

###  org.apache.commons.math3.optim.nonlinear.scalar.noderiv.SimplexOptimizer

```
158c158
<             if (iteration > 0) {
---
>             if (getIterations() > 0) {
174c174,175
<             ++iteration;
---
> 
>             incrementIterationCount();
```

- Deleted lines: 2<br />
- Added lines: 4<br />
- Diff added/deleted: 2


- Nb. undetected lines: 2/2 ( 158 174 )

###  org.apache.commons.math3.optim.nonlinear.scalar.gradient.NonLinearConjugateGradientOptimizer

```
214d213
<         int iter = 0;
217c216
<             ++iter;
---
>             incrementIterationCount();
223c222
<                 if (checker.converged(iter, previous, current)) {
---
>                 if (checker.converged(getIterations(), previous, current)) {
277c276
<             if (iter % n == 0 ||
---
>             if (getIterations() % n == 0 ||
```

- Deleted lines: 4<br />
- Added lines: 3<br />
- Diff added/deleted: -1


- Nb. undetected lines: 4/4 ( 214 217 223 277 )

###  org.apache.commons.math3.optim.nonlinear.scalar.noderiv.PowellOptimizer

```
191d190
<         int iter = 0;
193c192
<             ++iter;
---
>             incrementIterationCount();
227c226
<                     stop = checker.converged(iter, previous, current);
---
>                     stop = checker.converged(getIterations(), previous, current);
```

- Deleted lines: 3<br />
- Added lines: 2<br />
- Diff added/deleted: -1


- Nb. undetected lines: 3/3 ( 191 193 227 )

## Bug 7

- Nb. modified sources: 1

- Nb. nopol ranking entries: 20309

###  org.apache.commons.math3.ode.AbstractIntegrator

```
341c341
<                 // trigger the event
---
>                 // get state at event time
344,345c344,349
<                 currentEvent.stepAccepted(eventT, eventY);
<                 isLastStep = currentEvent.stop();
---
> 
>                 // advance all event states to current time
>                 for (final EventState state : eventsStates) {
>                     state.stepAccepted(eventT, eventY);
>                     isLastStep = isLastStep || state.stop();
>                 }
355,357d358
<                     for (final EventState remaining : occuringEvents) {
<                         remaining.stepAccepted(eventT, eventY);
<                     }
361c362,366
<                 if (currentEvent.reset(eventT, eventY)) {
---
>                 boolean needReset = false;
>                 for (final EventState state : eventsStates) {
>                     needReset =  needReset || state.reset(eventT, eventY);
>                 }
>                 if (needReset) {
367,369d371
<                     for (final EventState remaining : occuringEvents) {
<                         remaining.stepAccepted(eventT, eventY);
<                     }
```

- Deleted lines: 10<br />
- Added lines: 12<br />
- Diff added/deleted: 2


- Nb. undetected lines: 10/10 ( 341 344 345 355 356 357 361 367 368 369 )

## Bug 8

- Nb. modified sources: 1

- Nb. nopol ranking entries: 12235

###  org.apache.commons.math3.distribution.DiscreteDistribution

```
19d18
< import java.lang.reflect.Array;
21a21
> 
181c181
<     public T[] sample(int sampleSize) throws NotStrictlyPositiveException {
---
>     public Object[] sample(int sampleSize) throws NotStrictlyPositiveException {
186,187c186,187
<         @SuppressWarnings("unchecked")
<         final T[]out = (T[]) Array.newInstance(singletons.get(0).getClass(), sampleSize);
---
> 
>         final Object[] out = new Object[sampleSize];
```

- Deleted lines: 4<br />
- Added lines: 4<br />
- Diff added/deleted: 0


- Nb. undetected lines: 5/5 ( 19 21 181 186 187 )

## Bug 9

- Nb. modified sources: 1

- Nb. nopol ranking entries: 12185

###  org.apache.commons.math3.geometry.euclidean.threed.Line

```
87c87,89
<         return new Line(zero, zero.subtract(direction));
---
>         final Line reverted = new Line(this);
>         reverted.direction = reverted.direction.negate();
>         return reverted;
```

- Deleted lines: 1<br />
- Added lines: 3<br />
- Diff added/deleted: 2


- Nb. undetected lines: 1/1 ( 87 )

## Bug 10

- Nb. modified sources: 1

- Nb. nopol ranking entries: 15051

###  org.apache.commons.math3.analysis.differentiation.DSCompiler

```
1417a1418,1420
>         // fix value to take special cases (+0/+0, +0/-0, -0/+0, -0/-0, +/-infinity) correctly
>         result[resultOffset] = FastMath.atan2(y[yOffset], x[xOffset]);
> 
```

- Deleted lines: 0<br />
- Added lines: 3<br />
- Diff added/deleted: 3


- Nb. undetected lines: 1/1 ( 1417 )

## Bug 11

- Nb. modified sources: 1

- Nb. nopol ranking entries: 13866

###  org.apache.commons.math3.distribution.MultivariateNormalDistribution

```
183c183
<         return FastMath.pow(2 * FastMath.PI, -dim / 2) *
---
>         return FastMath.pow(2 * FastMath.PI, -0.5 * dim) *
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0


- Nb. undetected lines: 1/1 ( 183 )

## Bug 12

- Nb. modified sources: 1

- Nb. nopol ranking entries: 25043

###  org.apache.commons.math3.random.BitsStreamGenerator

```
18a19,20
> import java.io.Serializable;
> 
23c25
< 
---
>  *
26d27
< 
28,29c29,33
< public abstract class BitsStreamGenerator implements RandomGenerator {
< 
---
> public abstract class BitsStreamGenerator
>     implements RandomGenerator,
>                Serializable {
>     /** Serializable version identifier */
>     private static final long serialVersionUID = 20130104L;
33c37,38
<     /** Creates a new random number generator.
---
>     /**
>      * Creates a new random number generator.
```

- Deleted lines: 5<br />
- Added lines: 10<br />
- Diff added/deleted: 5


- Nb. undetected lines: 6/6 ( 18 23 26 28 29 33 )

## Bug 13

- Nb. modified sources: 2

- Nb. nopol ranking entries: 24718

###  org.apache.commons.math3.optimization.Weight

```
21c21
< import org.apache.commons.math3.linear.Array2DRowRealMatrix;
---
> import org.apache.commons.math3.linear.DiagonalMatrix;
44,48c44
<         final int dim = weight.length;
<         weightMatrix = new Array2DRowRealMatrix(dim, dim);
<         for (int i = 0; i < dim; i++) {
<             weightMatrix.setEntry(i, i, weight[i]);
<         }
---
>         weightMatrix = new DiagonalMatrix(weight);
```

- Deleted lines: 6<br />
- Added lines: 2<br />
- Diff added/deleted: -4


- Nb. undetected lines: 6/6 ( 21 44 45 46 47 48 )

###  org.apache.commons.math3.optimization.general.AbstractLeastSquaresOptimizer

```
561a562,569
>         if (m instanceof DiagonalMatrix) {
>             final int dim = m.getRowDimension();
>             final RealMatrix sqrtM = new DiagonalMatrix(dim);
>             for (int i = 0; i < dim; i++) {
>                sqrtM.setEntry(i, i, FastMath.sqrt(m.getEntry(i, i)));
>             }
>             return sqrtM;
>         } else {
564a573
>     }
```

- Deleted lines: 1<br />
- Added lines: 9<br />
- Diff added/deleted: 8


- Nb. undetected lines: 2/2 ( 561 564 )

## Bug 14

- Nb. modified sources: 2

- Nb. nopol ranking entries: 19675

###  org.apache.commons.math3.optim.nonlinear.vector.Weight

```
21c21
< import org.apache.commons.math3.linear.MatrixUtils;
---
> import org.apache.commons.math3.linear.DiagonalMatrix;
43,46c43
<         weightMatrix = MatrixUtils.createRealMatrix(dim, dim);
<         for (int i = 0; i < dim; i++) {
<             weightMatrix.setEntry(i, i, weight[i]);
<         }
---
>         weightMatrix = new DiagonalMatrix(weight);
```

- Deleted lines: 5<br />
- Added lines: 2<br />
- Diff added/deleted: -3


- Nb. undetected lines: 5/5 ( 21 43 44 45 46 )

###  org.apache.commons.math3.optim.nonlinear.vector.jacobian.AbstractLeastSquaresOptimizer

```
266a267,274
>         if (m instanceof DiagonalMatrix) {
>             final int dim = m.getRowDimension();
>             final RealMatrix sqrtM = new DiagonalMatrix(dim);
>             for (int i = 0; i < dim; i++) {
>                 sqrtM.setEntry(i, i, FastMath.sqrt(m.getEntry(i, i)));
>             }
>             return sqrtM;
>         } else {
269a278
>     }
```

- Deleted lines: 1<br />
- Added lines: 9<br />
- Diff added/deleted: 8


- Nb. undetected lines: 2/2 ( 266 269 )

## Bug 15

- Nb. modified sources: 1

- Nb. nopol ranking entries: 31217

###  org.apache.commons.math3.util.FastMath

```
311a312,313
>     /** 2^53 - double numbers this large must be even. */
>     private static final double TWO_POWER_53 = 2 * TWO_POWER_52;
1540c1542
<             if (y >= TWO_POWER_52 || y <= -TWO_POWER_52) {
---
>             if (y >= TWO_POWER_53 || y <= -TWO_POWER_53) {
```

- Deleted lines: 2<br />
- Added lines: 4<br />
- Diff added/deleted: 2


- Nb. undetected lines: 2/2 ( 311 1540 )

## Bug 16

- Nb. modified sources: 1

- Nb. nopol ranking entries: 31686

###  org.apache.commons.math3.util.FastMath

```
80a81,82
>     /** StrictMath.log(Double.MAX_VALUE): {@value} */
>     private static final double LOG_MAX_VALUE = StrictMath.log(Double.MAX_VALUE);
392,393c394,408
<       if (x > 20.0) {
<           return exp(x)/2.0;
---
>       if (x > 20) {
>           if (x >= LOG_MAX_VALUE) {
>               // Avoid overflow (MATH-905).
>               final double t = exp(0.5 * x);
>               return (0.5 * t) * t;
>           } else {
>               return 0.5 * exp(x);
>           }
>       } else if (x < -20) {
>           if (x <= -LOG_MAX_VALUE) {
>               // Avoid overflow (MATH-905).
>               final double t = exp(-0.5 * x);
>               return (0.5 * t) * t;
>           } else {
>               return 0.5 * exp(-x);
395,397d409
< 
<       if (x < -20) {
<           return exp(-x)/2.0;
400c412
<       double hiPrec[] = new double[2];
---
>       final double hiPrec[] = new double[2];
452,453c464,478
<       if (x > 20.0) {
<           return exp(x)/2.0;
---
>       if (x > 20) {
>           if (x >= LOG_MAX_VALUE) {
>               // Avoid overflow (MATH-905).
>               final double t = exp(0.5 * x);
>               return (0.5 * t) * t;
>           } else {
>               return 0.5 * exp(x);
>           }
>       } else if (x < -20) {
>           if (x <= -LOG_MAX_VALUE) {
>               // Avoid overflow (MATH-905).
>               final double t = exp(-0.5 * x);
>               return (-0.5 * t) * t;
>           } else {
>               return -0.5 * exp(-x);
455,457d479
< 
<       if (x < -20) {
<           return -exp(-x)/2.0;
```

- Deleted lines: 15<br />
- Added lines: 35<br />
- Diff added/deleted: 20


- Nb. undetected lines: 12/12 ( 80 392 393 395 396 397 400 452 453 455 456 457 )

## Bug 17

- Nb. modified sources: 1

- Nb. nopol ranking entries: 30415

###  org.apache.commons.math3.dfp.Dfp

```
1598,1599c1598
<     /** Multiply this by a single digit 0&lt;=x&lt;radix.
<      * There are speed advantages in this special case
---
>     /** Multiply this by a single digit x.
1603a1603,1615
>         if (x >= 0 && x < RADIX) {
>             return multiplyFast(x);
>         } else {
>             return multiply(newInstance(x));
>         }
>     }
> 
>     /** Multiply this by a single digit 0&lt;=x&lt;radix.
>      * There are speed advantages in this special case.
>      * @param x multiplicand
>      * @return product of this and x
>      */
>     private Dfp multiplyFast(final int x) {
```

- Deleted lines: 3<br />
- Added lines: 14<br />
- Diff added/deleted: 11


- Nb. undetected lines: 3/3 ( 1598 1599 1603 )

## Bug 18

- Nb. modified sources: 1

- Nb. nopol ranking entries: 30888

###  org.apache.commons.math3.optimization.direct.CMAESOptimizer

```
932c932
<                 res[i] = (x[i] - boundaries[0][i]) / diff;
---
>                 res[i] = x[i] / diff;
958c958
<                 res[i] = diff * x[i] + boundaries[0][i];
---
>                 res[i] = diff * x[i];
988a989,992
> 
>             final double[] bLoEnc = encode(boundaries[0]);
>             final double[] bHiEnc = encode(boundaries[1]);
> 
990c994
<                 if (x[i] < 0) {
---
>                 if (x[i] < bLoEnc[i]) {
993c997
<                 if (x[i] > 1.0) {
---
>                 if (x[i] > bHiEnc[i]) {
```

- Deleted lines: 5<br />
- Added lines: 9<br />
- Diff added/deleted: 4


- Nb. undetected lines: 5/5 ( 932 958 988 990 993 )

## Bug 19

- Nb. modified sources: 1

- Nb. nopol ranking entries: 30237

###  org.apache.commons.math3.optimization.direct.CMAESOptimizer

```
27d26
< import org.apache.commons.math3.exception.MathIllegalStateException;
28a28
> import org.apache.commons.math3.exception.NumberIsTooLargeException;
537a538,552
> 
>                 // Abort early if the normalization will overflow (cf. "encode" method).
>                 for (int i = 0; i < lB.length; i++) {
>                     if (Double.isInfinite(boundaries[1][i] - boundaries[0][i])) {
>                         final double max = Double.MAX_VALUE + boundaries[0][i];
>                         final NumberIsTooLargeException e
>                             = new NumberIsTooLargeException(boundaries[1][i],
>                                                             max,
>                                                             true);
>                         e.getContext().addMessage(LocalizedFormats.OVERFLOW);
>                         e.getContext().addMessage(LocalizedFormats.INDEX, i);
> 
>                         throw e;
>                     }
>                 }
```

- Deleted lines: 2<br />
- Added lines: 16<br />
- Diff added/deleted: 14


- Nb. undetected lines: 3/3 ( 27 28 537 )

## Bug 20

- Nb. modified sources: 1

- Nb. nopol ranking entries: 30560

###  org.apache.commons.math3.optimization.direct.CMAESOptimizer

```
419c419
<                             fitfun.decode(bestArx.getColumn(0)),
---
>                             fitfun.repairAndDecode(bestArx.getColumn(0)),
917a918,927
>          * @return the original objective variables, possibly repaired.
>          */
>         public double[] repairAndDecode(final double[] x) {
>             return boundaries != null && isRepairMode ?
>                 decode(repair(x)) :
>                 decode(x);
>         }
> 
>         /**
>          * @param x Normalized objective variables.
```

- Deleted lines: 1<br />
- Added lines: 11<br />
- Diff added/deleted: 10


- Nb. undetected lines: 2/2 ( 419 917 )

## Bug 21

- Nb. modified sources: 1

- Nb. nopol ranking entries: 32190

###  org.apache.commons.math3.linear.RectangularCholeskyDecomposition

```
65,67c65,67
<         int order = matrix.getRowDimension();
<         double[][] c = matrix.getData();
<         double[][] b = new double[order][order];
---
>         final int order = matrix.getRowDimension();
>         final double[][] c = matrix.getData();
>         final double[][] b = new double[order][order];
69d68
<         int[] swap  = new int[order];
79c78
<             swap[r] = r;
---
>             int swapR = r;
82,84c81,83
<                 int isi = index[swap[i]];
<                 if (c[ii][ii] > c[isi][isi]) {
<                     swap[r] = i;
---
>                 int isr = index[swapR];
>                 if (c[ii][ii] > c[isr][isr]) {
>                     swapR = i;
90,93c89,95
<             if (swap[r] != r) {
<                 int tmp = index[r];
<                 index[r] = index[swap[r]];
<                 index[swap[r]] = tmp;
---
>             if (swapR != r) {
>                 final int tmpIndex    = index[r];
>                 index[r]              = index[swapR];
>                 index[swapR]          = tmpIndex;
>                 final double[] tmpRow = b[r];
>                 b[r]                  = b[swapR];
>                 b[swapR]              = tmpRow;
121c123
<                 double sqrt = FastMath.sqrt(c[ir][ir]);
---
>                 final double sqrt = FastMath.sqrt(c[ir][ir]);
123c125,126
<                 double inverse = 1 / sqrt;
---
>                 final double inverse  = 1 / sqrt;
>                 final double inverse2 = 1 / c[ir][ir];
125,126c128,129
<                     int ii = index[i];
<                     double e = inverse * c[ii][ir];
---
>                     final int ii = index[i];
>                     final double e = inverse * c[ii][ir];
128c131
<                     c[ii][ii] -= e * e;
---
>                     c[ii][ii] -= c[ii][ir] * c[ii][ir] * inverse2;
130,131c133,134
<                         int ij = index[j];
<                         double f = c[ii][ij] - e * b[j][r];
---
>                         final int ij = index[j];
>                         final double f = c[ii][ij] - e * b[j][r];
```

- Deleted lines: 19<br />
- Added lines: 23<br />
- Diff added/deleted: 4


- Nb. undetected lines: 19/19 ( 65 66 67 69 79 82 83 84 90 91 92 93 121 123 125 126 128 130 131 )

## Bug 22

- Nb. modified sources: 2

- Nb. nopol ranking entries: 30743

###  org.apache.commons.math3.distribution.FDistribution

```
275c275
<         return true;
---
>         return false;
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0


- Nb. undetected lines: 1/1 ( 275 )

###  org.apache.commons.math3.distribution.UniformRealDistribution

```
184c184
<         return false;
---
>         return true;
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0


- Nb. undetected lines: 1/1 ( 184 )

## Bug 23

- Nb. modified sources: 1

- Nb. nopol ranking entries: 30231

###  org.apache.commons.math3.optimization.univariate.BrentOptimizer

```
149a150,151
>         // Best point encountered so far (which is the initial guess).
>         UnivariatePointValuePair best = current;
232a235,239
>                 best = best(best,
>                             best(current,
>                                  previous,
>                                  isMinim),
>                             isMinim);
236c243
<                         return best(current, previous, isMinim);
---
>                         return best;
273c280,284
<                 return best(current, previous, isMinim);
---
>                 return best(best,
>                             best(current,
>                                  previous,
>                                  isMinim),
>                             isMinim);
301c312
<             return a.getValue() < b.getValue() ? a : b;
---
>             return a.getValue() <= b.getValue() ? a : b;
303c314
<             return a.getValue() > b.getValue() ? a : b;
---
>             return a.getValue() >= b.getValue() ? a : b;
```

- Deleted lines: 5<br />
- Added lines: 16<br />
- Diff added/deleted: 11


- Nb. undetected lines: 6/6 ( 149 232 236 273 301 303 )

## Bug 24

- Nb. modified sources: 1

- Nb. nopol ranking entries: 30807

###  org.apache.commons.math3.optimization.univariate.BrentOptimizer

```
230c230
<                         return current;
---
>                         return best(current, previous, isMinim);
267c267
<                 return current;
---
>                 return best(current, previous, isMinim);
271a272,298
> 
>     /**
>      * Selects the best of two points.
>      *
>      * @param a Point and value.
>      * @param b Point and value.
>      * @param isMinim {@code true} if the selected point must be the one with
>      * the lowest value.
>      * @return the best point, or {@code null} if {@code a} and {@code b} are
>      * both {@code null}.
>      */
>     private UnivariatePointValuePair best(UnivariatePointValuePair a,
>                                           UnivariatePointValuePair b,
>                                           boolean isMinim) {
>         if (a == null) {
>             return b;
>         }
>         if (b == null) {
>             return a;
>         }
> 
>         if (isMinim) {
>             return a.getValue() < b.getValue() ? a : b;
>         } else {
>             return a.getValue() > b.getValue() ? a : b;
>         }
>     }
```

- Deleted lines: 3<br />
- Added lines: 29<br />
- Diff added/deleted: 26


- Nb. undetected lines: 3/3 ( 230 267 271 )

## Bug 25

- Nb. modified sources: 2

- Nb. nopol ranking entries: 30703

###  org.apache.commons.math3.exception.util.LocalizedFormats

```
347c347
<     ZERO_DENOMINATOR("denominator must be different from 0"),
---
>     ZERO_DENOMINATOR("denominator must be different from 0"), /* keep */
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0


- Nb. undetected lines: 1/1 ( 347 )

###  org.apache.commons.math3.optimization.fitting.HarmonicFitter

```
322a323,328
>                 if (c2 == 0) {
>                     // In some ill-conditioned cases (cf. MATH-844), the guesser
>                     // procedure cannot produce sensible results.
>                     throw new MathIllegalStateException(LocalizedFormats.ZERO_DENOMINATOR);
>                 }
> 
```

- Deleted lines: 0<br />
- Added lines: 6<br />
- Diff added/deleted: 6


- Nb. undetected lines: 1/1 ( 322 )

## Bug 26

- Nb. modified sources: 1

- Nb. nopol ranking entries: 29563

###  org.apache.commons.math3.fraction.Fraction

```
181c181
<         if (a0 > overflow) {
---
>         if (FastMath.abs(a0) > overflow) {
209c209
<             if ((p2 > overflow) || (q2 > overflow)) {
---
>             if ((FastMath.abs(p2) > overflow) || (FastMath.abs(q2) > overflow)) {
```

- Deleted lines: 2<br />
- Added lines: 4<br />
- Diff added/deleted: 2


- Nb. undetected lines: 2/2 ( 181 209 )

## Bug 27

- Nb. modified sources: 1

- Nb. nopol ranking entries: 30271

###  org.apache.commons.math3.fraction.Fraction

```
597c597
<         return multiply(100).doubleValue();
---
>         return 100 * doubleValue();
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0


- Nb. undetected lines: 1/1 ( 597 )

## Bug 28

- Nb. modified sources: 1

- Nb. nopol ranking entries: 30362

###  org.apache.commons.math3.optimization.linear.SimplexSolver

```
118a119
>             if (tableau.getNumArtificialVariables() > 0) {
127a129
>             }
133a136,140
>             //
>             // Additional heuristic: if we did not get a solution after half of maxIterations
>             //                       revert to the simple case of just returning the top-most row
>             // This heuristic is based on empirical data gathered while investigating MATH-828.
>             if (getIterations() < getMaxIterations() / 2) {
137c144,145
<                 for (int i = tableau.getNumObjectiveFunctions(); i < tableau.getWidth() - 1 && minRow != row; i++) {
---
>                     int i = tableau.getNumObjectiveFunctions();
>                     for (; i < tableau.getWidth() - 1 && minRow != row; i++) {
146d153
< 
148a156
>         }
```

- Deleted lines: 4<br />
- Added lines: 10<br />
- Diff added/deleted: 6


- Nb. undetected lines: 6/6 ( 118 127 133 137 146 148 )

## Bug 29

- Nb. modified sources: 1

- Nb. nopol ranking entries: 28543

###  org.apache.commons.math3.linear.OpenMapRealVector

```
344,347c344,351
<         Iterator iter = entries.iterator();
<         while (iter.hasNext()) {
<             iter.advance();
<             res.setEntry(iter.key(), iter.value() / v.getEntry(iter.key()));
---
>         /*
>          * MATH-803: it is not sufficient to loop through non zero entries of
>          * this only. Indeed, if this[i] = 0d and v[i] = 0d, then
>          * this[i] / v[i] = NaN, and not 0d.
>          */
>         final int n = getDimension();
>         for (int i = 0; i < n; i++) {
>             res.setEntry(i, this.getEntry(i) / v.getEntry(i));
361a366,384
>         /*
>          * MATH-803: the above loop assumes that 0d * x  = 0d for any double x,
>          * which allows to consider only the non-zero entries of this. However,
>          * this fails if this[i] == 0d and (v[i] = NaN or v[i] = Infinity).
>          *
>          * These special cases are handled below.
>          */
>         if (v.isNaN() || v.isInfinite()) {
>             final int n = getDimension();
>             for (int i = 0; i < n; i++) {
>                 final double y = v.getEntry(i);
>                 if (Double.isNaN(y)) {
>                     res.setEntry(i, Double.NaN);
>                 } else if (Double.isInfinite(y)) {
>                     final double x = this.getEntry(i);
>                     res.setEntry(i, x * y);
>                 }
>             }
>         }
```

- Deleted lines: 6<br />
- Added lines: 27<br />
- Diff added/deleted: 21


- Nb. undetected lines: 5/5 ( 344 345 346 347 361 )

## Bug 30

- Nb. modified sources: 1

- Nb. nopol ranking entries: 29760

###  org.apache.commons.math3.stat.inference.MannWhitneyUTest

```
173c173
<         final int n1n2prod = n1 * n2;
---
>         final double n1n2prod = n1 * n2;
176,177c176,177
<         final double EU = (double) n1n2prod / 2.0;
<         final double VarU = (double) (n1n2prod * (n1 + n2 + 1)) / 12.0;
---
>         final double EU = n1n2prod / 2.0;
>         final double VarU = n1n2prod * (n1 + n2 + 1) / 12.0;
```

- Deleted lines: 3<br />
- Added lines: 3<br />
- Diff added/deleted: 0


- Nb. undetected lines: 3/3 ( 173 176 177 )

## Bug 31

- Nb. modified sources: 1

- Nb. nopol ranking entries: 27744

###  org.apache.commons.math3.util.ContinuedFraction

```
124,165c124,129
<         double p0 = 1.0;
<         double p1 = getA(0, x);
<         double q0 = 0.0;
<         double q1 = 1.0;
<         double c = p1 / q1;
<         int n = 0;
<         double relativeError = Double.MAX_VALUE;
<         while (n < maxIterations && relativeError > epsilon) {
<             ++n;
<             double a = getA(n, x);
<             double b = getB(n, x);
<             double p2 = a * p1 + b * p0;
<             double q2 = a * q1 + b * q0;
<             boolean infinite = false;
<             if (Double.isInfinite(p2) || Double.isInfinite(q2)) {
<                 /*
<                  * Need to scale. Try successive powers of the larger of a or b
<                  * up to 5th power. Throw ConvergenceException if one or both
<                  * of p2, q2 still overflow.
<                  */
<                 double scaleFactor = 1d;
<                 double lastScaleFactor = 1d;
<                 final int maxPower = 5;
<                 final double scale = FastMath.max(a,b);
<                 if (scale <= 0) {  // Can't scale
<                     throw new ConvergenceException(LocalizedFormats.CONTINUED_FRACTION_INFINITY_DIVERGENCE,
<                                                    x);
<                 }
<                 infinite = true;
<                 for (int i = 0; i < maxPower; i++) {
<                     lastScaleFactor = scaleFactor;
<                     scaleFactor *= scale;
<                     if (a != 0.0 && a > b) {
<                         p2 = p1 / lastScaleFactor + (b / scaleFactor * p0);
<                         q2 = q1 / lastScaleFactor + (b / scaleFactor * q0);
<                     } else if (b != 0) {
<                         p2 = (a / scaleFactor * p1) + p0 / lastScaleFactor;
<                         q2 = (a / scaleFactor * q1) + q0 / lastScaleFactor;
<                     }
<                     infinite = Double.isInfinite(p2) || Double.isInfinite(q2);
<                     if (!infinite) {
<                         break;
---
>         final double small = 1e-50;
>         double hPrev = getA(0, x);
> 
>         // use the value of small as epsilon criteria for zero checks
>         if (Precision.equals(hPrev, 0.0, small)) {
>             hPrev = small;
166a131,143
> 
>         int n = 1;
>         double dPrev = 0.0;
>         double cPrev = hPrev;
>         double hN = hPrev;
> 
>         while (n < maxIterations) {
>             final double a = getA(n, x);
>             final double b = getB(n, x);
> 
>             double dN = a + b * dPrev;
>             if (Precision.equals(dN, 0.0, small)) {
>                 dN = small;
167a145,147
>             double cN = a + b / cPrev;
>             if (Precision.equals(cN, 0.0, small)) {
>                 cN = small;
170,171c150,154
<             if (infinite) {
<                // Scaling failed
---
>             dN = 1 / dN;
>             final double deltaN = cN * dN;
>             hN = hPrev * deltaN;
> 
>             if (Double.isInfinite(hN)) {
175,178c158
< 
<             double r = p2 / q2;
< 
<             if (Double.isNaN(r)) {
---
>             if (Double.isNaN(hN)) {
182d161
<             relativeError = FastMath.abs(r / c - 1.0);
184,189c163,170
<             // prepare for next iteration
<             c = p2 / q2;
<             p0 = p1;
<             p1 = p2;
<             q0 = q1;
<             q1 = q2;
---
>             if (FastMath.abs(deltaN - 1.0) < epsilon) {
>                 break;
>             }
> 
>             dPrev = dN;
>             cPrev = cN;
>             hPrev = hN;
>             n++;
197c178
<         return c;
---
>         return hN;
198a180
> 
```

- Deleted lines: 58<br />
- Added lines: 40<br />
- Diff added/deleted: -18


- Nb. undetected lines: 59/59 ( 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 170 171 175 176 177 178 182 184 185 186 187 188 189 197 198 )

## Bug 32

- Nb. modified sources: 1

- Nb. nopol ranking entries: 27579

###  org.apache.commons.math3.geometry.euclidean.twod.PolygonsSet

```
135c135,137
<             if ((Boolean) getTree(false).getAttribute()) {
---
>             final BSPTree<Euclidean2D> tree = getTree(false);
>             if (tree.getCut() == null && (Boolean) tree.getAttribute()) {
>                 // the instance covers the whole space
```

- Deleted lines: 2<br />
- Added lines: 3<br />
- Diff added/deleted: 1


- Nb. undetected lines: 1/1 ( 135 )

## Bug 33

- Nb. modified sources: 1

- Nb. nopol ranking entries: 27388

###  org.apache.commons.math3.optimization.linear.SimplexTableau

```
338c338
<             if (Precision.compareTo(entry, 0d, maxUlps) > 0) {
---
>             if (Precision.compareTo(entry, 0d, epsilon) > 0) {
```

- Deleted lines: 1<br />
- Added lines: 2<br />
- Diff added/deleted: 1


- Nb. undetected lines: 1/1 ( 338 )

## Bug 34

- Nb. modified sources: 1

- Nb. nopol ranking entries: 27405

###  org.apache.commons.math3.genetics.ListPopulation

```
203c203,204
<      * Chromosome list iterator
---
>      * Returns an iterator over the unmodifiable list of chromosomes.
>      * <p>Any call to {@link Iterator#remove()} will result in a {@link UnsupportedOperationException}.</p>
208c209
<         return chromosomes.iterator();
---
>         return getChromosomes().iterator();
```

- Deleted lines: 3<br />
- Added lines: 3<br />
- Diff added/deleted: 0


- Nb. undetected lines: 2/2 ( 203 208 )

## Bug 35

- Nb. modified sources: 1

- Nb. nopol ranking entries: 27242

###  org.apache.commons.math3.genetics.ElitisticListPopulation

```
44a45
>      * @throws OutOfRangeException if the elitism rate is outside the [0, 1] range
50c51
<         this.elitismRate = elitismRate;
---
>         setElitismRate(elitismRate);
59a61
>      * @throws OutOfRangeException if the elitism rate is outside the [0, 1] range
63c65
<         this.elitismRate = elitismRate;
---
>         setElitismRate(elitismRate);
```

- Deleted lines: 2<br />
- Added lines: 4<br />
- Diff added/deleted: 2


- Nb. undetected lines: 4/4 ( 44 50 59 63 )

## Bug 36

- Nb. modified sources: 1

- Nb. nopol ranking entries: 10329

###  org.apache.commons.math.fraction.BigFraction

```
685c685,694
<         return numerator.doubleValue() / denominator.doubleValue();
---
>         double result = numerator.doubleValue() / denominator.doubleValue();
>         if (Double.isNaN(result)) {
>             // Numerator and/or denominator must be out of range:
>             // Calculate how far to shift them to put them in range.
>             int shift = Math.max(numerator.bitLength(),
>                                  denominator.bitLength()) - Double.MAX_EXPONENT;
>             result = numerator.shiftRight(shift).doubleValue() /
>                 denominator.shiftRight(shift).doubleValue();
>         }
>         return result;
729c738,747
<         return numerator.floatValue() / denominator.floatValue();
---
>         float result = numerator.floatValue() / denominator.floatValue();
>         if (Double.isNaN(result)) {
>             // Numerator and/or denominator must be out of range:
>             // Calculate how far to shift them to put them in range.
>             int shift = Math.max(numerator.bitLength(),
>                                  denominator.bitLength()) - Float.MAX_EXPONENT;
>             result = numerator.shiftRight(shift).floatValue() /
>                 denominator.shiftRight(shift).floatValue();
>         }
>         return result;
```

- Deleted lines: 2<br />
- Added lines: 20<br />
- Diff added/deleted: 18


- Nb. undetected lines: 2/2 ( 685 729 )

## Bug 37

- Nb. modified sources: 1

- Nb. nopol ranking entries: 12272

###  org.apache.commons.math.complex.Complex

```
1018c1018
<         if (isNaN) {
---
>         if (isNaN || Double.isInfinite(real)) {
1020a1021,1026
>         if (imaginary > 20.0) {
>             return createComplex(0.0, 1.0);
>         }
>         if (imaginary < -20.0) {
>             return createComplex(0.0, -1.0);
>         }
1063c1069
<         if (isNaN) {
---
>         if (isNaN || Double.isInfinite(imaginary)) {
1066c1072,1077
< 
---
>         if (real > 20.0) {
>             return createComplex(1.0, 0.0);
>         }
>         if (real < -20.0) {
>             return createComplex(-1.0, 0.0);
>         }
```

- Deleted lines: 5<br />
- Added lines: 14<br />
- Diff added/deleted: 9


- Nb. undetected lines: 4/4 ( 1018 1020 1063 1066 )

## Bug 38

- Nb. modified sources: 1

- Nb. nopol ranking entries: 25140

###  org.apache.commons.math.optimization.direct.BOBYQAOptimizer

```
1660c1660
<                     throw new PathIsExploredException(); // XXX
---
> //                     throw new PathIsExploredException(); // XXX
1662,1663c1662,1665
<                 interpolationPoints.setEntry(nfm, ipt, interpolationPoints.getEntry(ipt, ipt));
<                 interpolationPoints.setEntry(nfm, jpt, interpolationPoints.getEntry(jpt, jpt));
---
>                 final int iptMinus1 = ipt - 1;
>                 final int jptMinus1 = jpt - 1;
>                 interpolationPoints.setEntry(nfm, iptMinus1, interpolationPoints.getEntry(ipt, iptMinus1));
>                 interpolationPoints.setEntry(nfm, jptMinus1, interpolationPoints.getEntry(jpt, jptMinus1));
1750c1752
<                 throw new PathIsExploredException(); // XXX
---
> //                 throw new PathIsExploredException(); // XXX
2465d2466
< }
2467c2468
< /**
---
>     /**
2471c2472
< class PathIsExploredException extends RuntimeException {
---
>     private static class PathIsExploredException extends RuntimeException {
2478c2479,2480
<         super(PATH_IS_EXPLORED);
---
>             super(PATH_IS_EXPLORED + " " + BOBYQAOptimizer.caller(3));
>         }
```

- Deleted lines: 8<br />
- Added lines: 10<br />
- Diff added/deleted: 2


- Nb. undetected lines: 8/8 ( 1660 1662 1663 1750 2465 2467 2471 2478 )

## Bug 39

- Nb. modified sources: 1

- Nb. nopol ranking entries: 28850

###  org.apache.commons.math.ode.nonstiff.EmbeddedRungeKuttaIntegrator

```
249a250,258
>         if (forward) {
>             if (stepStart + stepSize >= t) {
>                 stepSize = t - stepStart;
>             }
>         } else {
>             if (stepStart + stepSize <= t) {
>                 stepSize = t - stepStart;
>             }
>         }
```

- Deleted lines: 1<br />
- Added lines: 9<br />
- Diff added/deleted: 8


- Nb. undetected lines: 1/1 ( 249 )

## Bug 40

- Nb. modified sources: 1

- Nb. nopol ranking entries: 24794

###  org.apache.commons.math.analysis.solvers.BracketingNthOrderBrentSolver

```
235c235,238
<                 targetY = -REDUCTION_FACTOR * yB;
---
>                 final int p = agingA - MAXIMAL_AGING;
>                 final double weightA = (1 << p) - 1;
>                 final double weightB = p + 1;
>                 targetY = (weightA * yA - weightB * REDUCTION_FACTOR * yB) / (weightA + weightB);
238c241,244
<                 targetY = -REDUCTION_FACTOR * yA;
---
>                 final int p = agingB - MAXIMAL_AGING;
>                 final double weightA = p + 1;
>                 final double weightB = (1 << p) - 1;
>                 targetY = (weightB * yB - weightA * REDUCTION_FACTOR * yA) / (weightA + weightB);
```

- Deleted lines: 4<br />
- Added lines: 8<br />
- Diff added/deleted: 4


- Nb. undetected lines: 2/2 ( 235 238 )

## Bug 41

- Nb. modified sources: 1

- Nb. nopol ranking entries: 148

###  org.apache.commons.math.stat.descriptive.moment.Variance

```
520c520
<                 for (int i = 0; i < weights.length; i++) {
---
>                 for (int i = begin; i < begin + length; i++) {
```

- Deleted lines: 2<br />
- Added lines: 1<br />
- Diff added/deleted: -1

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 520 | org.apache.commons.math.stat.descriptive.moment.Variance:520 -> 0.0890870806374748 (ep: 4, ef: 2, np: 3189, nf: -1) | 30 |

- Nb. undetected lines: 0/1

## Bug 42

- Nb. modified sources: 1

- Nb. nopol ranking entries: 28490

###  org.apache.commons.math.optimization.linear.SimplexTableau

```
410c410,415
<           if (basicRows.contains(basicRow)) {
---
>           if (basicRow != null && basicRow == 0) {
>               // if the basic row is found to be the objective function row
>               // set the coefficient to 0 -> this case handles unconstrained 
>               // variables that are still part of the objective function
>               coefficients[i] = 0;
>           } else if (basicRows.contains(basicRow)) {
```

- Deleted lines: 1<br />
- Added lines: 6<br />
- Diff added/deleted: 5


- Nb. undetected lines: 1/1 ( 410 )

## Bug 43

- Nb. modified sources: 1

- Nb. nopol ranking entries: 307

###  org.apache.commons.math.stat.descriptive.SummaryStatistics

```
158c158
<         if (!(meanImpl instanceof Mean)) {
---
>         if (meanImpl != mean) {
161c161
<         if (!(varianceImpl instanceof Variance)) {
---
>         if (varianceImpl != variance) {
164c164
<         if (!(geoMeanImpl instanceof GeometricMean)) {
---
>         if (geoMeanImpl != geoMean) {
```

- Deleted lines: 3<br />
- Added lines: 3<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 158 | org.apache.commons.math.stat.descriptive.SummaryStatistics:158 -> 0.09174483527748864 (ep: 85, ef: 6, np: 3062, nf: 0) | 19 |
| 161 | org.apache.commons.math.stat.descriptive.SummaryStatistics:161 -> 0.09174483527748864 (ep: 85, ef: 6, np: 3062, nf: 0) | 20 |
| 164 | org.apache.commons.math.stat.descriptive.SummaryStatistics:164 -> 0.09174483527748864 (ep: 85, ef: 6, np: 3062, nf: 0) | 21 |

- Nb. undetected lines: 0/3

## Bug 44

- Nb. modified sources: 1

- Nb. nopol ranking entries: 789

###  org.apache.commons.math.ode.AbstractIntegrator

```
43d42
< import org.apache.commons.math.util.MathUtils;
281d279
<             resetOccurred = false;
334a333,335
>                     for (final EventState remaining : occuringEvents) {
>                         remaining.stepAccepted(eventT, eventY);
>                     }
343a345,347
>                     for (final EventState remaining : occuringEvents) {
>                         remaining.stepAccepted(eventT, eventY);
>                     }
```

- Deleted lines: 2<br />
- Added lines: 6<br />
- Diff added/deleted: 4

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 281 | org.apache.commons.math.ode.AbstractIntegrator:281 -> 0.013135173437318345 (ep: 137, ef: 1, np: 2981, nf: 0) | 462 |
| 343 | org.apache.commons.math.ode.AbstractIntegrator:343 -> 0.04279604925109129 (ep: 12, ef: 1, np: 3106, nf: 0) | 8 |

- Nb. undetected lines: 2/4 ( 43 334 )

## Bug 45

- Nb. modified sources: 1

- Nb. nopol ranking entries: 26

###  org.apache.commons.math.linear.OpenMapRealMatrix

```
49a50,54
>         long lRow = (long) rowDimension;
>         long lCol = (long) columnDimension;
>         if (lRow * lCol >= (long) Integer.MAX_VALUE) {
>             throw new NumberIsTooLargeException(lRow * lCol, Integer.MAX_VALUE, false);
>         }
```

- Deleted lines: 0<br />
- Added lines: 5<br />
- Diff added/deleted: 5


- Nb. undetected lines: 1/1 ( 49 )

## Bug 46

- Nb. modified sources: 1

- Nb. nopol ranking entries: 62

###  org.apache.commons.math.complex.Complex

```
259c259,260
<             return isZero ? NaN : INF;
---
>             // return isZero ? NaN : INF; // See MATH-657
>             return NaN;
295c296,297
<             return isZero ? NaN : INF;
---
>             // return isZero ? NaN : INF; // See MATH-657
>             return NaN;
```

- Deleted lines: 2<br />
- Added lines: 4<br />
- Diff added/deleted: 2

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 259 | org.apache.commons.math.complex.Complex:259 -> 0.15249857033260467 (ep: 2, ef: 2, np: 2993, nf: 0) | 1 |

- Nb. undetected lines: 1/2 ( 295 )

## Bug 47

- Nb. modified sources: 1

- Nb. nopol ranking entries: 112

###  org.apache.commons.math.complex.Complex

```
80a81,82
>     /** Record whether this complex number is zero. */
>     private final transient boolean isZero;
103a106
>         isZero = real == 0 && imaginary == 0;
255,258c258,259
<         final double c = divisor.getReal();
<         final double d = divisor.getImaginary();
<         if (c == 0.0 && d == 0.0) {
<             return NaN;
---
>         if (divisor.isZero) {
>             return isZero ? NaN : INF;
264a266,268
>         final double c = divisor.getReal();
>         final double d = divisor.getImaginary();
> 
291c295
<             return NaN;
---
>             return isZero ? NaN : INF;
```

- Deleted lines: 5<br />
- Added lines: 9<br />
- Diff added/deleted: 4

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 255 | org.apache.commons.math.complex.Complex:255 -> 0.07874992309581577 (ep: 13, ef: 2, np: 2982, nf: 0) | 4 |
| 256 | org.apache.commons.math.complex.Complex:256 -> 0.07874992309581577 (ep: 13, ef: 2, np: 2982, nf: 0) | 5 |
| 257 | org.apache.commons.math.complex.Complex:257 -> 0.07874992309581577 (ep: 13, ef: 2, np: 2982, nf: 0) | 6 |
| 258 | org.apache.commons.math.complex.Complex:258 -> 0.15249857033260467 (ep: 2, ef: 2, np: 2993, nf: 0) | 2 |

- Nb. undetected lines: 4/8 ( 80 103 264 291 )

## Bug 48

- Nb. modified sources: 1

- Nb. nopol ranking entries: 145

###  org.apache.commons.math.analysis.solvers.BaseSecantSolver

```
187c187,191
<                     // Nothing.
---
>                     // Detect early that algorithm is stuck, instead of waiting
>                     // for the maximum number of iterations to be exceeded.
>                     if (x == x1) {
>                         throw new ConvergenceException();
>                     }
```

- Deleted lines: 1<br />
- Added lines: 5<br />
- Diff added/deleted: 4


- Nb. undetected lines: 1/1 ( 187 )

## Bug 49

- Nb. modified sources: 1

- Nb. nopol ranking entries: 145

###  org.apache.commons.math.linear.OpenMapRealVector

```
345c345
<         Iterator iter = res.entries.iterator();
---
>         Iterator iter = entries.iterator();
358c358
<         Iterator iter = res.entries.iterator();
---
>         Iterator iter = entries.iterator();
370c370
<         Iterator iter = res.entries.iterator();
---
>         Iterator iter = entries.iterator();
383c383
<         Iterator iter = res.entries.iterator();
---
>         Iterator iter = entries.iterator();
```

- Deleted lines: 4<br />
- Added lines: 4<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 370 | org.apache.commons.math.linear.OpenMapRealVector:370 -> 0.1091089451179962 (ep: 1, ef: 1, np: 2952, nf: 0) | 6 |

- Nb. undetected lines: 3/4 ( 345 358 383 )

## Bug 50

- Nb. modified sources: 1

- Nb. nopol ranking entries: 98

###  org.apache.commons.math.analysis.solvers.BaseSecantSolver

```
186,193c186
<                     if (x == x1) {
<                         final double delta = FastMath.max(rtol * FastMath.abs(x1),
<                                                           atol);
<                         // Update formula cannot make any progress: Update the
<                         // search interval.
<                         x0 = 0.5 * (x0 + x1 - delta);
<                         f0 = computeObjectiveValue(x0);
<                     }
---
>                     // Nothing.
```

- Deleted lines: 8<br />
- Added lines: 1<br />
- Diff added/deleted: -7

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 186 | org.apache.commons.math.analysis.solvers.BaseSecantSolver:186 -> 0.05832118435198043 (ep: 6, ef: 1, np: 2945, nf: 0) | 6 |
| 187 | org.apache.commons.math.analysis.solvers.BaseSecantSolver:187 -> 0.1543033499620919 (ep: 0, ef: 1, np: 2951, nf: 0) | 1 |
| 191 | org.apache.commons.math.analysis.solvers.BaseSecantSolver:191 -> 0.1543033499620919 (ep: 0, ef: 1, np: 2951, nf: 0) | 2 |
| 192 | org.apache.commons.math.analysis.solvers.BaseSecantSolver:192 -> 0.1543033499620919 (ep: 0, ef: 1, np: 2951, nf: 0) | 3 |
| 193 | org.apache.commons.math.analysis.solvers.BaseSecantSolver:193 -> 0.1543033499620919 (ep: 0, ef: 1, np: 2951, nf: 0) | 4 |

- Nb. undetected lines: 3/8 ( 188 189 190 )

## Bug 51

- Nb. modified sources: 1

- Nb. nopol ranking entries: 149

###  org.apache.commons.math.analysis.solvers.BaseSecantSolver

```
172,173c172
<                 // We had [x0..x1]. We update it to [x1, x]. Note that the
<                 // value of x1 has switched to the other bound, thus inverting
---
>                 // The value of x1 has switched to the other bound, thus inverting
177,178d175
<                 x1 = x;
<                 f1 = fx;
181,182c178,179
<                 // We had [x0..x1]. We update it to [x0, x].
<                 if (method == Method.ILLINOIS) {
---
>                 switch (method) {
>                 case ILLINOIS:
184,185c181,182
<                 }
<                 if (method == Method.PEGASUS) {
---
>                     break;
>                 case PEGASUS:
186a184,192
>                     break;
>                 case REGULA_FALSI:
>                     if (x == x1) {
>                         final double delta = FastMath.max(rtol * FastMath.abs(x1),
>                                                           atol);
>                         // Update formula cannot make any progress: Update the
>                         // search interval.
>                         x0 = 0.5 * (x0 + x1 - delta);
>                         f0 = computeObjectiveValue(x0);
187a194,200
>                     break;
>                 default:
>                     // Should never happen.
>                     throw new MathInternalError();
>                 }
>             }
>             // Update from [x0, x1] to [x0, x].
190d202
<             }
```

- Deleted lines: 9<br />
- Added lines: 21<br />
- Diff added/deleted: 12

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 177 | org.apache.commons.math.analysis.solvers.BaseSecantSolver:177 -> 0.03329635791060134 (ep: 21, ef: 1, np: 2919, nf: 0) | 42 |
| 178 | org.apache.commons.math.analysis.solvers.BaseSecantSolver:178 -> 0.03329635791060134 (ep: 21, ef: 1, np: 2919, nf: 0) | 43 |
| 182 | org.apache.commons.math.analysis.solvers.BaseSecantSolver:182 -> 0.03329635791060134 (ep: 21, ef: 1, np: 2919, nf: 0) | 45 |
| 185 | org.apache.commons.math.analysis.solvers.BaseSecantSolver:185 -> 0.03329635791060134 (ep: 21, ef: 1, np: 2919, nf: 0) | 46 |

- Nb. undetected lines: 7/11 ( 172 173 181 184 186 187 190 )

## Bug 52

- Nb. modified sources: 1

- Nb. nopol ranking entries: 92

###  org.apache.commons.math.geometry.euclidean.threed.Rotation

```
316,319c316,319
<   double u1u1 = Vector3D.dotProduct(u1, u1);
<   double u2u2 = Vector3D.dotProduct(u2, u2);
<   double v1v1 = Vector3D.dotProduct(v1, v1);
<   double v2v2 = Vector3D.dotProduct(v2, v2);
---
>   double u1u1 = u1.getNormSq();
>   double u2u2 = u2.getNormSq();
>   double v1v1 = v1.getNormSq();
>   double v2v2 = v2.getNormSq();
324,331d323
<   double u1x = u1.getX();
<   double u1y = u1.getY();
<   double u1z = u1.getZ();
< 
<   double u2x = u2.getX();
<   double u2y = u2.getY();
<   double u2z = u2.getZ();
< 
333,341c325,329
<   double coeff = FastMath.sqrt (u1u1 / v1v1);
<   double v1x   = coeff * v1.getX();
<   double v1y   = coeff * v1.getY();
<   double v1z   = coeff * v1.getZ();
<   v1 = new Vector3D(v1x, v1y, v1z);
< 
<   // adjust v2 in order to have (u1|u2) = (v1|v2) and (v2'|v2') = (u2|u2)
<   double u1u2   = Vector3D.dotProduct(u1, u2);
<   double v1v2   = Vector3D.dotProduct(v1, v2);
---
>   v1 = new Vector3D(FastMath.sqrt(u1u1 / v1v1), v1);
> 
>   // adjust v2 in order to have (u1|u2) = (v1'|v2') and (v2'|v2') = (u2|u2)
>   double u1u2   = u1.dotProduct(u2);
>   double v1v2   = v1.dotProduct(v2);
346,353c334,336
<   double v2x    = alpha * v1x + beta * v2.getX();
<   double v2y    = alpha * v1y + beta * v2.getY();
<   double v2z    = alpha * v1z + beta * v2.getZ();
<   v2 = new Vector3D(v2x, v2y, v2z);
< 
<   // preliminary computation (we use explicit formulation instead
<   // of relying on the Vector3D class in order to avoid building lots
<   // of temporary objects)
---
>   v2 = new Vector3D(alpha, v1, beta, v2);
> 
>   // preliminary computation
356,370c339,346
<   double dx1 = v1x - u1.getX();
<   double dy1 = v1y - u1.getY();
<   double dz1 = v1z - u1.getZ();
<   double dx2 = v2x - u2.getX();
<   double dy2 = v2y - u2.getY();
<   double dz2 = v2z - u2.getZ();
<   Vector3D k = new Vector3D(dy1 * dz2 - dz1 * dy2,
<                             dz1 * dx2 - dx1 * dz2,
<                             dx1 * dy2 - dy1 * dx2);
<   double c = k.getX() * (u1y * u2z - u1z * u2y) +
<              k.getY() * (u1z * u2x - u1x * u2z) +
<              k.getZ() * (u1x * u2y - u1y * u2x);
< 
<   if (c == 0) {
<     // the (q1, q2, q3) vector is in the (u1, u2) plane
---
>   Vector3D v1Su1 = v1.subtract(u1);
>   Vector3D v2Su2 = v2.subtract(u2);
>   Vector3D k     = v1Su1.crossProduct(v2Su2);
>   Vector3D u3    = u1.crossProduct(u2);
>   double c       = k.dotProduct(u3);
>   final double inPlaneThreshold = 0.001;
>   if (c <= inPlaneThreshold * k.getNorm() * u3.getNorm()) {
>     // the (q1, q2, q3) vector is close to the (u1, u2) plane
372d347
<     Vector3D u3 = Vector3D.crossProduct(u1, u2);
374,399c349,358
<     double u3x  = u3.getX();
<     double u3y  = u3.getY();
<     double u3z  = u3.getZ();
<     double v3x  = v3.getX();
<     double v3y  = v3.getY();
<     double v3z  = v3.getZ();
< 
<     double dx3 = v3x - u3x;
<     double dy3 = v3y - u3y;
<     double dz3 = v3z - u3z;
<     k = new Vector3D(dy1 * dz3 - dz1 * dy3,
<                      dz1 * dx3 - dx1 * dz3,
<                      dx1 * dy3 - dy1 * dx3);
<     c = k.getX() * (u1y * u3z - u1z * u3y) +
<         k.getY() * (u1z * u3x - u1x * u3z) +
<         k.getZ() * (u1x * u3y - u1y * u3x);
< 
<     if (c == 0) {
<       // the (q1, q2, q3) vector is aligned with u1:
<       // we try (u2, u3) and (v2, v3)
<       k = new Vector3D(dy2 * dz3 - dz2 * dy3,
<                        dz2 * dx3 - dx2 * dz3,
<                        dx2 * dy3 - dy2 * dx3);
<       c = k.getX() * (u2y * u3z - u2z * u3y) +
<           k.getY() * (u2z * u3x - u2x * u3z) +
<           k.getZ() * (u2x * u3y - u2y * u3x);
---
>     Vector3D v3Su3 = v3.subtract(u3);
>     k = v1Su1.crossProduct(v3Su3);
>     Vector3D u2Prime = u1.crossProduct(u3);
>     c = k.dotProduct(u2Prime);
> 
>     if (c <= inPlaneThreshold * k.getNorm() * u2Prime.getNorm()) {
>       // the (q1, q2, q3) vector is also close to the (u1, u3) plane,
>       // it is almost aligned with u1: we try (u2, u3) and (v2, v3)
>       k = v2Su2.crossProduct(v3Su3);;
>       c = k.dotProduct(u2.crossProduct(u3));;
401c360
<       if (c == 0) {
---
>       if (c <= 0) {
430,431c389
<    c = Vector3D.dotProduct(k, k);
<   q0 = Vector3D.dotProduct(vRef, k) / (c + c);
---
>   q0 = vRef.dotProduct(k) / (2 * k.getNormSq());
455c413
<     double dot = Vector3D.dotProduct(u, v);
---
>     double dot = u.dotProduct(v);
470,472c428,431
<       q1 = coeff * (v.getY() * u.getZ() - v.getZ() * u.getY());
<       q2 = coeff * (v.getZ() * u.getX() - v.getX() * u.getZ());
<       q3 = coeff * (v.getX() * u.getY() - v.getY() * u.getX());
---
>       Vector3D q = v.crossProduct(u);
>       q1 = coeff * q.getX();
>       q2 = coeff * q.getY();
>       q3 = coeff * q.getZ();
```

- Deleted lines: 81<br />
- Added lines: 37<br />
- Diff added/deleted: -44

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 316 | org.apache.commons.math.geometry.euclidean.threed.Rotation:316 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 2 |
| 317 | org.apache.commons.math.geometry.euclidean.threed.Rotation:317 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 3 |
| 318 | org.apache.commons.math.geometry.euclidean.threed.Rotation:318 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 4 |
| 319 | org.apache.commons.math.geometry.euclidean.threed.Rotation:319 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 5 |
| 324 | org.apache.commons.math.geometry.euclidean.threed.Rotation:324 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 7 |
| 325 | org.apache.commons.math.geometry.euclidean.threed.Rotation:325 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 8 |
| 326 | org.apache.commons.math.geometry.euclidean.threed.Rotation:326 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 9 |
| 328 | org.apache.commons.math.geometry.euclidean.threed.Rotation:328 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 10 |
| 329 | org.apache.commons.math.geometry.euclidean.threed.Rotation:329 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 11 |
| 330 | org.apache.commons.math.geometry.euclidean.threed.Rotation:330 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 12 |
| 333 | org.apache.commons.math.geometry.euclidean.threed.Rotation:333 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 13 |
| 334 | org.apache.commons.math.geometry.euclidean.threed.Rotation:334 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 14 |
| 335 | org.apache.commons.math.geometry.euclidean.threed.Rotation:335 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 15 |
| 336 | org.apache.commons.math.geometry.euclidean.threed.Rotation:336 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 16 |
| 337 | org.apache.commons.math.geometry.euclidean.threed.Rotation:337 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 17 |
| 340 | org.apache.commons.math.geometry.euclidean.threed.Rotation:340 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 18 |
| 341 | org.apache.commons.math.geometry.euclidean.threed.Rotation:341 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 19 |
| 346 | org.apache.commons.math.geometry.euclidean.threed.Rotation:346 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 24 |
| 347 | org.apache.commons.math.geometry.euclidean.threed.Rotation:347 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 25 |
| 348 | org.apache.commons.math.geometry.euclidean.threed.Rotation:348 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 26 |
| 349 | org.apache.commons.math.geometry.euclidean.threed.Rotation:349 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 27 |
| 356 | org.apache.commons.math.geometry.euclidean.threed.Rotation:356 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 30 |
| 357 | org.apache.commons.math.geometry.euclidean.threed.Rotation:357 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 31 |
| 358 | org.apache.commons.math.geometry.euclidean.threed.Rotation:358 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 32 |
| 359 | org.apache.commons.math.geometry.euclidean.threed.Rotation:359 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 33 |
| 360 | org.apache.commons.math.geometry.euclidean.threed.Rotation:360 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 34 |
| 361 | org.apache.commons.math.geometry.euclidean.threed.Rotation:361 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 35 |
| 362 | org.apache.commons.math.geometry.euclidean.threed.Rotation:362 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 36 |
| 365 | org.apache.commons.math.geometry.euclidean.threed.Rotation:365 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 37 |
| 369 | org.apache.commons.math.geometry.euclidean.threed.Rotation:369 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 38 |
| 430 | org.apache.commons.math.geometry.euclidean.threed.Rotation:430 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 45 |
| 431 | org.apache.commons.math.geometry.euclidean.threed.Rotation:431 -> 0.11043152607484653 (ep: 1, ef: 1, np: 2916, nf: 0) | 46 |

- Nb. undetected lines: 46/78 ( 327 331 338 339 350 351 352 353 363 364 366 367 368 370 372 374 375 376 377 378 379 380 381 382 383 384 385 386 387 388 389 390 391 392 393 394 395 396 397 398 399 401 455 470 471 472 )

## Bug 53

- Nb. modified sources: 1

- Nb. nopol ranking entries: 13

###  org.apache.commons.math.complex.Complex

```
152a153,155
>         if (isNaN || rhs.isNaN) {
>             return NaN;
>         }
```

- Deleted lines: 0<br />
- Added lines: 3<br />
- Diff added/deleted: 3

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 152 | org.apache.commons.math.complex.Complex:152 -> 0.22360679774997896 (ep: 19, ef: 1, np: 2505, nf: 0) | 1 |

- Nb. undetected lines: 0/1

## Bug 54

- Nb. modified sources: 1

- Nb. nopol ranking entries: 1235

###  org.apache.commons.math.dfp.Dfp

```
271a272,275
>                 // make sure 0 has the right sign
>                 if ((bits & 0x8000000000000000L) != 0) {
>                     sign = -1;
>                 }
2318c2322,2325
<         if (lessThan(getZero())) {
---
>         int cmp0 = compare(this, getZero());
>         if (cmp0 == 0) {
>             return sign < 0 ? -0.0 : +0.0;
>         } else if (cmp0 < 0) {
```

- Deleted lines: 3<br />
- Added lines: 8<br />
- Diff added/deleted: 5

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 2318 | org.apache.commons.math.dfp.Dfp:2318 -> 0.15811388300841897 (ep: 19, ef: 1, np: 2400, nf: 0) | 209 |

- Nb. undetected lines: 1/2 ( 271 )

## Bug 55

- Nb. modified sources: 1

- Nb. nopol ranking entries: 8

###  org.apache.commons.math.geometry.Vector3D

```
457,460c457,491
<   public static Vector3D crossProduct(Vector3D v1, Vector3D v2) {
<     return new Vector3D(v1.y * v2.z - v1.z * v2.y,
<                         v1.z * v2.x - v1.x * v2.z,
<                         v1.x * v2.y - v1.y * v2.x);
---
>   public static Vector3D crossProduct(final Vector3D v1, final Vector3D v2) {
> 
>       final double n1 = v1.getNormSq();
>       final double n2 = v2.getNormSq();
>       if ((n1 * n2) < MathUtils.SAFE_MIN) {
>           return ZERO;
>       }
> 
>       // rescale both vectors without losing precision,
>       // to ensure their norm are the same order of magnitude
>       final int deltaExp = (FastMath.getExponent(n1) - FastMath.getExponent(n2)) / 4;
>       final double x1    = FastMath.scalb(v1.x, -deltaExp);
>       final double y1    = FastMath.scalb(v1.y, -deltaExp);
>       final double z1    = FastMath.scalb(v1.z, -deltaExp);
>       final double x2    = FastMath.scalb(v2.x,  deltaExp);
>       final double y2    = FastMath.scalb(v2.y,  deltaExp);
>       final double z2    = FastMath.scalb(v2.z,  deltaExp);
> 
>       // we reduce cancellation errors by preconditioning,
>       // we replace v1 by v3 = v1 - rho v2 with rho chosen in order to compute
>       // v3 without loss of precision. See Kahan lecture
>       // "Computing Cross-Products and Rotations in 2- and 3-Dimensional Euclidean Spaces"
>       // available at http://www.cs.berkeley.edu/~wkahan/MathH110/Cross.pdf
> 
>       // compute rho as an 8 bits approximation of v1.v2 / v2.v2
>       final double ratio = (x1 * x2 + y1 * y2 + z1 * z2) / FastMath.scalb(n2, 2 * deltaExp);
>       final double rho   = FastMath.rint(256 * ratio) / 256;
> 
>       final double x3 = x1 - rho * x2;
>       final double y3 = y1 - rho * y2;
>       final double z3 = z1 - rho * z2;
> 
>       // compute cross product from v3 and v2 instead of v1 and v2
>       return new Vector3D(y3 * z2 - z3 * y2, z3 * x2 - x3 * z2, x3 * y2 - y3 * x2);
> 
```

- Deleted lines: 5<br />
- Added lines: 35<br />
- Diff added/deleted: 30

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 458 | org.apache.commons.math.geometry.Vector3D:458 -> 0.5 (ep: 3, ef: 1, np: 2397, nf: 0) | 1 |

- Nb. undetected lines: 3/4 ( 457 459 460 )

## Bug 56

- Nb. modified sources: 1

- Nb. nopol ranking entries: 67

###  org.apache.commons.math.util.MultidimensionalCounter

```
237,243c237
<         int idx = 1;
<         while (count < index) {
<             count += idx;
<             ++idx;
<         }
<         --idx;
<         indices[last] = idx;
---
>         indices[last] = index - count;
```

- Deleted lines: 7<br />
- Added lines: 1<br />
- Diff added/deleted: -6

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 237 | org.apache.commons.math.util.MultidimensionalCounter:237 -> 1.0 (ep: 0, ef: 1, np: 2399, nf: 0) | 21 |
| 238 | org.apache.commons.math.util.MultidimensionalCounter:238 -> 1.0 (ep: 0, ef: 1, np: 2399, nf: 0) | 22 |
| 239 | org.apache.commons.math.util.MultidimensionalCounter:239 -> 1.0 (ep: 0, ef: 1, np: 2399, nf: 0) | 23 |
| 240 | org.apache.commons.math.util.MultidimensionalCounter:240 -> 1.0 (ep: 0, ef: 1, np: 2399, nf: 0) | 24 |
| 242 | org.apache.commons.math.util.MultidimensionalCounter:242 -> 1.0 (ep: 0, ef: 1, np: 2399, nf: 0) | 25 |
| 243 | org.apache.commons.math.util.MultidimensionalCounter:243 -> 1.0 (ep: 0, ef: 1, np: 2399, nf: 0) | 26 |

- Nb. undetected lines: 1/7 ( 241 )

## Bug 57

- Nb. modified sources: 1

- Nb. nopol ranking entries: 71

###  org.apache.commons.math.stat.clustering.KMeansPlusPlusClusterer

```
175c175
<             int sum = 0;
---
>             double sum = 0;
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 175 | org.apache.commons.math.stat.clustering.KMeansPlusPlusClusterer:175 -> 0.5773502691896258 (ep: 2, ef: 1, np: 2380, nf: 0) | 4 |

- Nb. undetected lines: 0/1

## Bug 58

- Nb. modified sources: 1

- Nb. nopol ranking entries: 665

###  org.apache.commons.math.optimization.fitting.GaussianFitter

```
120,121c120,121
<         return fit(new Gaussian.Parametric(),
<                    (new ParameterGuesser(getObservations())).guess());
---
>         final double[] guess = (new ParameterGuesser(getObservations())).guess();
>         return fit(guess);
```

- Deleted lines: 2<br />
- Added lines: 2<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 120 | org.apache.commons.math.optimization.fitting.GaussianFitter:120 -> 0.35355339059327373 (ep: 7, ef: 1, np: 2346, nf: 0) | 73 |

- Nb. undetected lines: 1/2 ( 121 )

## Bug 59

- Nb. modified sources: 1

- Nb. nopol ranking entries: 221

###  org.apache.commons.math.util.FastMath

```
3482c3482
<         return (a <= b) ? b : (Float.isNaN(a + b) ? Float.NaN : b);
---
>         return (a <= b) ? b : (Float.isNaN(a + b) ? Float.NaN : a);
```

- Deleted lines: 2<br />
- Added lines: 1<br />
- Diff added/deleted: -1

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 3482 | org.apache.commons.math.util.FastMath:3482 -> 1.0 (ep: 0, ef: 1, np: 2234, nf: 0) | 2 |

- Nb. undetected lines: 0/1

## Bug 60

- Nb. modified sources: 1

- Nb. nopol ranking entries: 218

###  org.apache.commons.math.distribution.NormalDistributionImpl

```
116a117,118
>      * If {@code x}is more than 40 standard deviations from the mean, 0 or 1 is returned,
>      * as in these cases the actual value is within {@code Double.MIN_VALUE} of 0 or 1.
120,122c122
<      * @throws MathException if the algorithm fails to converge; unless
<      * {@code x} is more than 20 standard deviations from the mean, in which
<      * case the convergence exception is caught and 0 or 1 is returned.
---
>      * @throws MathException if the algorithm fails to converge
125,135c125,127
<         try {
<             return 0.5 * (1.0 + Erf.erf((x - mean) /
<                     (standardDeviation * FastMath.sqrt(2.0))));
<         } catch (MaxIterationsExceededException ex) {
<             if (x < (mean - 20 * standardDeviation)) { // JDK 1.5 blows at 38
<                 return 0;
<             } else if (x > (mean + 20 * standardDeviation)) {
<                 return 1;
<             } else {
<                 throw ex;
<             }
---
>         final double dev = x - mean;
>         if (FastMath.abs(dev) > 40 * standardDeviation) { 
>             return dev < 0 ? 0.0d : 1.0d;
136a129,130
>         return 0.5 * (1.0 + Erf.erf((dev) /
>                     (standardDeviation * FastMath.sqrt(2.0))));
```

- Deleted lines: 15<br />
- Added lines: 9<br />
- Diff added/deleted: -6

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 126 | org.apache.commons.math.distribution.NormalDistributionImpl:126 -> 0.35355339059327373 (ep: 7, ef: 1, np: 2210, nf: 0) | 25 |

- Nb. undetected lines: 15/16 ( 116 120 121 122 125 127 128 129 130 131 132 133 134 135 136 )

## Bug 61

- Nb. modified sources: 2

- Nb. nopol ranking entries: 73

###  org.apache.commons.math.distribution.PoissonDistributionImpl

```
22c22
< import org.apache.commons.math.MathRuntimeException;
---
> import org.apache.commons.math.exception.NotStrictlyPositiveException;
80c80
<         this(p, new NormalDistributionImpl());
---
>         this(p, DEFAULT_EPSILON, DEFAULT_MAX_ITERATIONS);
93c93,97
<         setMean(p);
---
>         if (p <= 0) {
>             throw new NotStrictlyPositiveException(LocalizedFormats.MEAN, p);
>         }
>         mean = p;
>         normal = new NormalDistributionImpl(p, FastMath.sqrt(p));
106,107c110
<         setMean(p);
<         this.epsilon = epsilon;
---
>         this(p, epsilon, DEFAULT_MAX_ITERATIONS);
118,137c121
<         setMean(p);
<         this.maxIterations = maxIterations;
<     }
< 
< 
<     /**
<      * Create a new Poisson distribution with the given the mean. The mean value
<      * must be positive; otherwise an <code>IllegalArgument</code> is thrown.
<      *
<      * @param p the Poisson mean
<      * @param z a normal distribution used to compute normal approximations.
<      * @throws IllegalArgumentException if p &le; 0
<      * @since 1.2
<      * @deprecated as of 2.1 (to avoid possibly inconsistent state, the
<      * "NormalDistribution" will be instantiated internally)
<      */
<     @Deprecated
<     public PoissonDistributionImpl(double p, NormalDistribution z) {
<         super();
<         setNormalAndMeanInternal(z, p);
---
>         this(p, DEFAULT_EPSILON, maxIterations);
150,181d133
<      * Set the Poisson mean for the distribution. The mean value must be
<      * positive; otherwise an <code>IllegalArgument</code> is thrown.
<      *
<      * @param p the Poisson mean value
<      * @throws IllegalArgumentException if p &le; 0
<      * @deprecated as of 2.1 (class will become immutable in 3.0)
<      */
<     @Deprecated
<     public void setMean(double p) {
<         setNormalAndMeanInternal(normal, p);
<     }
<     /**
<      * Set the Poisson mean for the distribution. The mean value must be
<      * positive; otherwise an <code>IllegalArgument</code> is thrown.
<      *
<      * @param z the new distribution
<      * @param p the Poisson mean value
<      * @throws IllegalArgumentException if p &le; 0
<      */
<     private void setNormalAndMeanInternal(NormalDistribution z,
<                                           double p) {
<         if (p <= 0) {
<             throw MathRuntimeException.createIllegalArgumentException(
<                     LocalizedFormats.NOT_POSITIVE_POISSON_MEAN, p);
<         }
<         mean = p;
<         normal = z;
<         normal.setMean(p);
<         normal.setStandardDeviation(FastMath.sqrt(p));
<     }
< 
<     /**
289,302d240
< 
<     /**
<      * Modify the normal distribution used to compute normal approximations. The
<      * caller is responsible for insuring the normal distribution has the proper
<      * parameter settings.
<      *
<      * @param value the new distribution
<      * @since 1.2
<      * @deprecated as of 2.1 (class will become immutable in 3.0)
<      */
<     @Deprecated
<     public void setNormal(NormalDistribution value) {
<         setNormalAndMeanInternal(value, mean);
<     }
```

- Deleted lines: 72<br />
- Added lines: 12<br />
- Diff added/deleted: -60

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 80 | org.apache.commons.math.distribution.PoissonDistributionImpl:80 -> 0.2581988897471611 (ep: 14, ef: 1, np: 2351, nf: 0) | 7 |
| 136 | org.apache.commons.math.distribution.PoissonDistributionImpl:136 -> 0.2581988897471611 (ep: 14, ef: 1, np: 2351, nf: 0) | 9 |
| 137 | org.apache.commons.math.distribution.PoissonDistributionImpl:137 -> 0.2581988897471611 (ep: 14, ef: 1, np: 2351, nf: 0) | 12 |
| 171 | org.apache.commons.math.distribution.PoissonDistributionImpl:171 -> 0.2581988897471611 (ep: 14, ef: 1, np: 2351, nf: 0) | 14 |
| 172 | org.apache.commons.math.distribution.PoissonDistributionImpl:172 -> 1.0 (ep: 0, ef: 1, np: 2365, nf: 0) | 3 |
| 175 | org.apache.commons.math.distribution.PoissonDistributionImpl:175 -> 0.2581988897471611 (ep: 14, ef: 1, np: 2351, nf: 0) | 15 |
| 176 | org.apache.commons.math.distribution.PoissonDistributionImpl:176 -> 0.2581988897471611 (ep: 14, ef: 1, np: 2351, nf: 0) | 16 |
| 177 | org.apache.commons.math.distribution.PoissonDistributionImpl:177 -> 0.2581988897471611 (ep: 14, ef: 1, np: 2351, nf: 0) | 17 |
| 178 | org.apache.commons.math.distribution.PoissonDistributionImpl:178 -> 0.2581988897471611 (ep: 14, ef: 1, np: 2351, nf: 0) | 18 |
| 179 | org.apache.commons.math.distribution.PoissonDistributionImpl:179 -> 0.2581988897471611 (ep: 14, ef: 1, np: 2351, nf: 0) | 19 |

- Nb. undetected lines: 61/71 ( 22 93 106 107 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 173 174 180 181 289 290 291 292 293 294 295 296 297 298 299 300 301 302 )

###  org.apache.commons.math.distribution.PoissonDistribution

```
43,54d42
<      * Set the mean for the distribution.
<      * The parameter value must be positive; otherwise an
<      * <code>IllegalArgument</code> is thrown.
<      *
<      * @param p the mean
<      * @throws IllegalArgumentException if p &le; 0
<      * @deprecated as of v2.1
<      */
<     @Deprecated
<     void setMean(double p);
< 
<     /**
62d49
< 
```

- Deleted lines: 13<br />
- Added lines: 1<br />
- Diff added/deleted: -12


- Nb. undetected lines: 13/13 ( 43 44 45 46 47 48 49 50 51 52 53 54 62 )

## Bug 62

- Nb. modified sources: 1

- Nb. nopol ranking entries: 177

###  org.apache.commons.math.optimization.univariate.MultiStartUnivariateRealOptimizer

```
145a146,147
>         return optimize(f, goal, min, max, min + 0.5 * (max - min));
>     }
146a149,153
>     /** {@inheritDoc} */
>     public UnivariateRealPointValuePair optimize(final FUNC f, final GoalType goal,
>                                                  final double min, final double max,
>                                                  final double startValue)
>         throws FunctionEvaluationException {
153,157c160,161
<                 final double bound1 = (i == 0) ? min : min + generator.nextDouble() * (max - min);
<                 final double bound2 = (i == 0) ? max : min + generator.nextDouble() * (max - min);
<                 optima[i] = optimizer.optimize(f, goal,
<                                                FastMath.min(bound1, bound2),
<                                                FastMath.max(bound1, bound2));
---
>                 final double s = (i == 0) ? startValue : min + generator.nextDouble() * (max - min);
>                 optima[i] = optimizer.optimize(f, goal, min, max, s);
180,189d183
<     /** {@inheritDoc} */
<     public UnivariateRealPointValuePair optimize(final FUNC f, final GoalType goalType,
<                                                  final double min, final double max,
<                                                  final double startValue)
<             throws FunctionEvaluationException {
<         // XXX Main code should be here, using "startValue" for the first start.
<         // XXX This method should set "startValue" to min + 0.5 * (max - min)
<         return optimize(f, goalType, min, max);
<     }
< 
```

- Deleted lines: 15<br />
- Added lines: 9<br />
- Diff added/deleted: -6

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 153 | org.apache.commons.math.optimization.univariate.MultiStartUnivariateRealOptimizer:153 -> 0.7071067811865475 (ep: 1, ef: 1, np: 2363, nf: 0) | 9 |
| 154 | org.apache.commons.math.optimization.univariate.MultiStartUnivariateRealOptimizer:154 -> 0.7071067811865475 (ep: 1, ef: 1, np: 2363, nf: 0) | 10 |
| 155 | org.apache.commons.math.optimization.univariate.MultiStartUnivariateRealOptimizer:155 -> 0.7071067811865475 (ep: 1, ef: 1, np: 2363, nf: 0) | 11 |

- Nb. undetected lines: 14/17 ( 145 146 156 157 180 181 182 183 184 185 186 187 188 189 )

## Bug 63

- Nb. modified sources: 1

- Nb. nopol ranking entries: 8

###  org.apache.commons.math.util.MathUtils

```
410c410
<      * {@link #equals(double,double,int) this method}.
---
>      * {@link #equals(double,double,int) equals(x, y, 1)}.
415,420d414
<      * @deprecated This method considers that {@code NaN == NaN}. In release
<      * 3.0, the semantics will change in order to comply with IEEE754 where it
<      * is specified that {@code NaN != NaN}.
<      * New methods have been added for those cases wher the old semantics is
<      * useful (see e.g. {@link #equalsIncludingNaN(double,double)
<      * equalsIncludingNaN}.
423c417
<         return (Double.isNaN(x) && Double.isNaN(y)) || x == y;
---
>         return equals(x, y, 1);
1099,1121d1092
<      * Get the next machine representable number after a number, moving
<      * in the direction of another number.
<      * <p>
<      * If <code>direction</code> is greater than or equal to<code>d</code>,
<      * the smallest machine representable number strictly greater than
<      * <code>d</code> is returned; otherwise the largest representable number
<      * strictly less than <code>d</code> is returned.</p>
<      * <p>
<      * If <code>d</code> is NaN or Infinite, it is returned unchanged.</p>
<      *
<      * @param d base number
<      * @param direction (the only important thing is whether
<      * direction is greater or smaller than d)
<      * @return the next machine representable number in the specified direction
<      * @since 1.2
<      * @deprecated as of 2.2, replaced by {@link FastMath#nextAfter(double, double)}
<      */
<     @Deprecated
<     public static double nextAfter(double d, double direction) {
<         return FastMath.nextAfter(d, direction);
<     }
< 
<     /**
1315c1286
<                 unscaled = FastMath.floor(nextAfter(unscaled, Double.NEGATIVE_INFINITY));
---
>                 unscaled = FastMath.floor(FastMath.nextAfter(unscaled, Double.NEGATIVE_INFINITY));
1317c1288
<                 unscaled = FastMath.ceil(nextAfter(unscaled, Double.POSITIVE_INFINITY));
---
>                 unscaled = FastMath.ceil(FastMath.nextAfter(unscaled, Double.POSITIVE_INFINITY));
1321c1292
<             unscaled = FastMath.floor(nextAfter(unscaled, Double.NEGATIVE_INFINITY));
---
>             unscaled = FastMath.floor(FastMath.nextAfter(unscaled, Double.NEGATIVE_INFINITY));
1325c1296
<                 unscaled = FastMath.ceil(nextAfter(unscaled, Double.POSITIVE_INFINITY));
---
>                 unscaled = FastMath.ceil(FastMath.nextAfter(unscaled, Double.POSITIVE_INFINITY));
1327c1298
<                 unscaled = FastMath.floor(nextAfter(unscaled, Double.NEGATIVE_INFINITY));
---
>                 unscaled = FastMath.floor(FastMath.nextAfter(unscaled, Double.NEGATIVE_INFINITY));
1331c1302
<             unscaled = nextAfter(unscaled, Double.NEGATIVE_INFINITY);
---
>             unscaled = FastMath.nextAfter(unscaled, Double.NEGATIVE_INFINITY);
1358c1329
<             unscaled = nextAfter(unscaled, Double.POSITIVE_INFINITY);
---
>             unscaled = FastMath.nextAfter(unscaled, Double.POSITIVE_INFINITY);
1373c1344
<             unscaled = FastMath.ceil(nextAfter(unscaled,  Double.POSITIVE_INFINITY));
---
>             unscaled = FastMath.ceil(FastMath.nextAfter(unscaled,  Double.POSITIVE_INFINITY));
1902,1919d1872
<      * Checks that the given array is sorted.
<      *
<      * @param val Values
<      * @param dir Order direction (-1 for decreasing, 1 for increasing)
<      * @param strict Whether the order should be strict
<      * @throws NonMonotonousSequenceException if the array is not sorted.
<      * @deprecated as of 2.2 (please use the new {@link #checkOrder(double[],OrderDirection,boolean)
<      * checkOrder} method). To be removed in 3.0.
<      */
<     public static void checkOrder(double[] val, int dir, boolean strict) {
<         if (dir > 0) {
<             checkOrder(val, OrderDirection.INCREASING, strict);
<         } else {
<             checkOrder(val, OrderDirection.DECREASING, strict);
<         }
<     }
< 
<     /**
```

- Deleted lines: 57<br />
- Added lines: 17<br />
- Diff added/deleted: -40

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 423 | org.apache.commons.math.util.MathUtils:423 -> 1.0 (ep: 0, ef: 1, np: 2281, nf: 0) | 1 |

- Nb. undetected lines: 56/57 ( 410 415 416 417 418 419 420 1099 1100 1101 1102 1103 1104 1105 1106 1107 1108 1109 1110 1111 1112 1113 1114 1115 1116 1117 1118 1119 1120 1121 1315 1317 1321 1325 1327 1331 1358 1373 1902 1903 1904 1905 1906 1907 1908 1909 1910 1911 1912 1913 1914 1915 1916 1917 1918 1919 )

## Bug 64

- Nb. modified sources: 2

- Nb. nopol ranking entries: 436

###  org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizer

```
257a258,259
>         double[] oldObj  = new double[rows];
>         double[] qtf     = new double[rows];
270c272,274
< 
---
>             for (int i=0;i<rows;i++) {
>                 qtf[i]=residuals[i];
>             }
279,280c283
<             qTy(residuals);
< 
---
>             qTy(qtf);
318c321
<                             sum += jacobian[i][pj] * residuals[i];
---
>                             sum += jacobian[i][pj] * qtf[i];
325a329,330
>             	updateResidualsAndCost();
>             	current = new VectorialPointValuePair(point, objective);
345a351,353
>                 tmpVec    = objective;
>                 objective = oldObj;
>                 oldObj    = tmpVec;
348c356
<                 determineLMParameter(oldRes, delta, diag, work1, work2, work3);
---
>                 determineLMParameter(qtf, delta, diag, work1, work2, work3);
367d374
<                 current = new VectorialPointValuePair(point, objective);
422a430,438
>                     current = new VectorialPointValuePair(point, objective);
> 
>                     // tests for convergence.
>                     if (checker != null) {
>                     // we use the vectorial convergence checker
>                     	if (checker.converged(getIterations(), previous, current)) {
>                     		return current;
>                     	}
>                     }
432a449,451
>                     tmpVec    = objective;
>                     objective = oldObj;
>                     oldObj    = tmpVec;
434,442c453
< 
<                 // tests for convergence.
<                 if (checker != null) {
<                     // we use the vectorial convergence checker
<                     if (checker.converged(getIterations(), previous, current)) {
<                         return current;
<                     }
<                 } else {
<                     // we use the Levenberg-Marquardt specific convergence parameters
---
>                 if (checker==null) {
450d460
< 
```

- Deleted lines: 17<br />
- Added lines: 26<br />
- Diff added/deleted: 9

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 257 | org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizer:257 -> 0.19802950859533489 (ep: 49, ef: 2, np: 2223, nf: 0) | 311 |
| 279 | org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizer:279 -> 0.2 (ep: 48, ef: 2, np: 2224, nf: 0) | 175 |
| 318 | org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizer:318 -> 0.2 (ep: 48, ef: 2, np: 2224, nf: 0) | 199 |
| 345 | org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizer:345 -> 0.2 (ep: 48, ef: 2, np: 2224, nf: 0) | 215 |
| 348 | org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizer:348 -> 0.2 (ep: 48, ef: 2, np: 2224, nf: 0) | 216 |
| 367 | org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizer:367 -> 0.2 (ep: 48, ef: 2, np: 2224, nf: 0) | 229 |
| 422 | org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizer:422 -> 0.2 (ep: 48, ef: 2, np: 2224, nf: 0) | 262 |
| 432 | org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizer:432 -> 0.2886751345948129 (ep: 22, ef: 2, np: 2250, nf: 0) | 52 |
| 436 | org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizer:436 -> 0.2 (ep: 48, ef: 2, np: 2224, nf: 0) | 263 |

- Nb. undetected lines: 12/21 ( 270 280 325 434 435 437 438 439 440 441 442 450 )

###  org.apache.commons.math.optimization.general.AbstractLeastSquaresOptimizer

```
250,255c250
<         double chiSquare = 0;
<         for (int i = 0; i < rows; ++i) {
<             final double residual = residuals[i];
<             chiSquare += residual * residual * residualsWeights[i];
<         }
<         return chiSquare;
---
>         return cost*cost;
```

- Deleted lines: 6<br />
- Added lines: 1<br />
- Diff added/deleted: -5

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 250 | org.apache.commons.math.optimization.general.AbstractLeastSquaresOptimizer:250 -> 0.21320071635561041 (ep: 42, ef: 2, np: 2230, nf: 0) | 152 |
| 251 | org.apache.commons.math.optimization.general.AbstractLeastSquaresOptimizer:251 -> 0.21320071635561041 (ep: 84, ef: 4, np: 2188, nf: -2) | 153 |
| 252 | org.apache.commons.math.optimization.general.AbstractLeastSquaresOptimizer:252 -> 0.21320071635561041 (ep: 42, ef: 2, np: 2230, nf: 0) | 154 |
| 253 | org.apache.commons.math.optimization.general.AbstractLeastSquaresOptimizer:253 -> 0.21320071635561041 (ep: 42, ef: 2, np: 2230, nf: 0) | 155 |
| 255 | org.apache.commons.math.optimization.general.AbstractLeastSquaresOptimizer:255 -> 0.21320071635561041 (ep: 42, ef: 2, np: 2230, nf: 0) | 157 |

- Nb. undetected lines: 1/6 ( 254 )

## Bug 65

- Nb. modified sources: 3

- Nb. nopol ranking entries: 419

###  org.apache.commons.math.linear.SingularValueDecompositionImpl

```
143c143
<         // There still an sign indetermination of each column of, say, U.
---
>         // There still a sign indetermination of each column of, say, U.
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0


- Nb. undetected lines: 1/1 ( 143 )

###  org.apache.commons.math.optimization.general.AbstractLeastSquaresOptimizer

```
240,245c240
<         double criterion = 0;
<         for (int i = 0; i < rows; ++i) {
<             final double residual = residuals[i];
<             criterion += residualsWeights[i] * residual * residual;
<         }
<         return Math.sqrt(criterion / rows);
---
>         return Math.sqrt(getChiSquare() / rows);
249c244,246
<      * Get the Chi-Square value.
---
>      * Get a Chi-Square-like value assuming the N residuals follow N
>      * distinct normal distributions centered on 0 and whose variances are
>      * the reciprocal of the weights.
256c253
<             chiSquare += residual * residual / residualsWeights[i];
---
>             chiSquare += residual * residual * residualsWeights[i];
```

- Deleted lines: 8<br />
- Added lines: 5<br />
- Diff added/deleted: -3

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 240 | org.apache.commons.math.optimization.general.AbstractLeastSquaresOptimizer:240 -> 0.15075567228888181 (ep: 43, ef: 1, np: 2229, nf: 0) | 75 |
| 241 | org.apache.commons.math.optimization.general.AbstractLeastSquaresOptimizer:241 -> 0.15075567228888181 (ep: 86, ef: 2, np: 2186, nf: -1) | 76 |
| 242 | org.apache.commons.math.optimization.general.AbstractLeastSquaresOptimizer:242 -> 0.15075567228888181 (ep: 43, ef: 1, np: 2229, nf: 0) | 77 |
| 243 | org.apache.commons.math.optimization.general.AbstractLeastSquaresOptimizer:243 -> 0.15075567228888181 (ep: 43, ef: 1, np: 2229, nf: 0) | 78 |
| 245 | org.apache.commons.math.optimization.general.AbstractLeastSquaresOptimizer:245 -> 0.15075567228888181 (ep: 43, ef: 1, np: 2229, nf: 0) | 80 |
| 256 | org.apache.commons.math.optimization.general.AbstractLeastSquaresOptimizer:256 -> 1.0 (ep: 0, ef: 1, np: 2272, nf: 0) | 4 |

- Nb. undetected lines: 2/8 ( 244 249 )

###  org.apache.commons.math.linear.EigenDecompositionImpl

```
564c564
<                     if (e[i + 1] == 0.0 && i >= j)
---
>                     if (t == 0.0 && i >= j)
```

- Deleted lines: 1<br />
- Added lines: 2<br />
- Diff added/deleted: 1


- Nb. undetected lines: 1/1 ( 564 )

## Bug 66

- Nb. modified sources: 1

- Nb. nopol ranking entries: 377

###  org.apache.commons.math.optimization.univariate.BrentOptimizer

```
44c44,47
<         super(100, 1E-10);
---
>         setMaxEvaluations(1000);
>         setMaximalIterationCount(100);
>         setAbsoluteAccuracy(1e-11);
>         setRelativeAccuracy(1e-9);
54,62c57,58
<         throw new UnsupportedOperationException();
<     }
< 
<     /** {@inheritDoc} */
<     public double optimize(final UnivariateRealFunction f, final GoalType goalType,
<                            final double min, final double max, final double startValue)
<         throws MaxIterationsExceededException, FunctionEvaluationException {
<         clearResult();
<         return localMin(f, goalType, min, startValue, max,
---
>         return localMin(getGoalType() == GoalType.MINIMIZE,
>                         getMin(), getStartValue(), getMax(),
66,72d61
<     /** {@inheritDoc} */
<     public double optimize(final UnivariateRealFunction f, final GoalType goalType,
<                            final double min, final double max)
<         throws MaxIterationsExceededException, FunctionEvaluationException {
<         return optimize(f, goalType, min, max, min + GOLDEN_SECTION * (max - min));
<     }
< 
97,98c86
<     private double localMin(UnivariateRealFunction f,
<                             GoalType goalType,
---
>     private double localMin(boolean isMinim,
119a108
>         double d = 0;
121,122c110,111
<         double fx = computeObjectiveValue(f, x);
<         if (goalType == GoalType.MAXIMIZE) {
---
>         double fx = computeObjectiveValue(x);
>         if (!isMinim) {
128,129c117
<         int count = 0;
<         while (count < maximalIterationCount) {
---
>         while (true) {
139d126
<                 double d = 0;
203,204c190,191
<                 double fu = computeObjectiveValue(f, u);
<                 if (goalType == GoalType.MAXIMIZE) {
---
>                 double fu = computeObjectiveValue(u);
>                 if (!isMinim) {
241c228
<                 setResult(x, (goalType == GoalType.MAXIMIZE) ? -fx : fx, count);
---
>                 setFunctionValue(isMinim ? fx : -fx);
244c231
<             ++count;
---
>             incrementIterationsCounter();
246d232
<         throw new MaxIterationsExceededException(maximalIterationCount);
```

- Deleted lines: 29<br />
- Added lines: 15<br />
- Diff added/deleted: -14

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 44 | org.apache.commons.math.optimization.univariate.BrentOptimizer:44 -> 0.6324555320336759 (ep: 6, ef: 4, np: 2251, nf: 0) | 60 |
| 61 | org.apache.commons.math.optimization.univariate.BrentOptimizer:61 -> 0.6324555320336759 (ep: 6, ef: 4, np: 2251, nf: 0) | 62 |
| 62 | org.apache.commons.math.optimization.univariate.BrentOptimizer:62 -> 0.6324555320336759 (ep: 6, ef: 4, np: 2251, nf: 0) | 63 |
| 70 | org.apache.commons.math.optimization.univariate.BrentOptimizer:70 -> 0.6123724356957946 (ep: 3, ef: 3, np: 2254, nf: 1) | 144 |
| 119 | org.apache.commons.math.optimization.univariate.BrentOptimizer:119 -> 0.6324555320336759 (ep: 6, ef: 4, np: 2251, nf: 0) | 69 |
| 121 | org.apache.commons.math.optimization.univariate.BrentOptimizer:121 -> 0.6324555320336759 (ep: 6, ef: 4, np: 2251, nf: 0) | 71 |
| 122 | org.apache.commons.math.optimization.univariate.BrentOptimizer:122 -> 0.6324555320336759 (ep: 6, ef: 4, np: 2251, nf: 0) | 72 |
| 128 | org.apache.commons.math.optimization.univariate.BrentOptimizer:128 -> 0.6324555320336759 (ep: 6, ef: 4, np: 2251, nf: 0) | 75 |
| 129 | org.apache.commons.math.optimization.univariate.BrentOptimizer:129 -> 0.6324555320336759 (ep: 6, ef: 4, np: 2251, nf: 0) | 76 |
| 139 | org.apache.commons.math.optimization.univariate.BrentOptimizer:139 -> 0.6324555320336759 (ep: 6, ef: 4, np: 2251, nf: 0) | 84 |
| 203 | org.apache.commons.math.optimization.univariate.BrentOptimizer:203 -> 0.6324555320336759 (ep: 6, ef: 4, np: 2251, nf: 0) | 105 |
| 204 | org.apache.commons.math.optimization.univariate.BrentOptimizer:204 -> 0.6324555320336759 (ep: 6, ef: 4, np: 2251, nf: 0) | 106 |
| 241 | org.apache.commons.math.optimization.univariate.BrentOptimizer:241 -> 0.6324555320336759 (ep: 6, ef: 4, np: 2251, nf: 0) | 125 |
| 244 | org.apache.commons.math.optimization.univariate.BrentOptimizer:244 -> 0.6324555320336759 (ep: 6, ef: 4, np: 2251, nf: 0) | 127 |

- Nb. undetected lines: 16/30 ( 54 55 56 57 58 59 60 66 67 68 69 71 72 97 98 246 )

## Bug 67

- Nb. modified sources: 1

- Nb. nopol ranking entries: 176

###  org.apache.commons.math.optimization.MultiStartUnivariateRealOptimizer

```
92c92
<         return optimizer.getFunctionValue();
---
>         return optimaValues[0];
97c97
<         return optimizer.getResult();
---
>         return optima[0];
```

- Deleted lines: 2<br />
- Added lines: 2<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 97 | org.apache.commons.math.optimization.MultiStartUnivariateRealOptimizer:97 -> 1.0 (ep: 0, ef: 1, np: 2254, nf: 0) | 3 |

- Nb. undetected lines: 1/2 ( 92 )

## Bug 68

- Nb. modified sources: 1

- Nb. nopol ranking entries: 427

###  org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizer

```
165a166
>         setConvergenceChecker(null);
246a248
>         VectorialPointValuePair current = new VectorialPointValuePair(point, objective);
251a254
>             VectorialPointValuePair previous = current;
303c306
<                 return new VectorialPointValuePair(point, objective);
---
>                 return current;
344a348
>                 current = new VectorialPointValuePair(point, objective);
412a417,423
>                 if (checker != null) {
>                     // we use the vectorial convergence checker
>                     if (checker.converged(getIterations(), previous, current)) {
>                         return current;                        
>                     }
>                 } else {
>                     // we use the Levenberg-Marquardt specific convergence parameters
417c428,429
<                     return new VectorialPointValuePair(point, objective);
---
>                         return current;
>                     }
```

- Deleted lines: 2<br />
- Added lines: 14<br />
- Diff added/deleted: 12

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 246 | org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizer:246 -> 0.21566554640687682 (ep: 41, ef: 2, np: 2143, nf: 0) | 323 |
| 344 | org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizer:344 -> 0.2182178902359924 (ep: 40, ef: 2, np: 2144, nf: 0) | 220 |
| 417 | org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizer:417 -> 0.254000254000381 (ep: 29, ef: 2, np: 2155, nf: 0) | 150 |

- Nb. undetected lines: 4/7 ( 165 251 303 412 )

## Bug 69

- Nb. modified sources: 1

- Nb. nopol ranking entries: 267

###  org.apache.commons.math.stat.correlation.PearsonsCorrelation

```
171c171
<                     out[i][j] = 2 * (1 - tDistribution.cumulativeProbability(t));
---
>                     out[i][j] = 2 * tDistribution.cumulativeProbability(-t);
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 171 | org.apache.commons.math.stat.correlation.PearsonsCorrelation:171 -> 0.5345224838248488 (ep: 5, ef: 2, np: 2179, nf: 0) | 12 |

- Nb. undetected lines: 0/1

## Bug 70

- Nb. modified sources: 1

- Nb. nopol ranking entries: 30

###  org.apache.commons.math.analysis.solvers.BisectionSolver

```
72c72
<         return solve(min, max);
---
>         return solve(f, min, max);
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 72 | org.apache.commons.math.analysis.solvers.BisectionSolver:72 -> 1.0 (ep: 0, ef: 1, np: 2182, nf: 1) | 1 |

- Nb. undetected lines: 0/1

## Bug 71

- Nb. modified sources: 4

- Nb. nopol ranking entries: 447

###  org.apache.commons.math.ode.nonstiff.AdamsMoultonIntegrator

```
292c292,300
<                             // rejecting the step would lead to a too small next step, we accept it
---
>                             // we cannot simply truncate the step, reject the current computation
>                             // and let the loop compute another state with the truncated step.
>                             // it is so small (much probably exactly 0 due to limited accuracy)
>                             // that the code above would fail handling it.
>                             // So we set up an artificial 0 size step by copying states
>                             interpolator.storeTime(stepStart);
>                             System.arraycopy(y, 0, yTmp, 0, y0.length);
>                             hNew     = 0;
>                             stepSize = 0;
```

- Deleted lines: 1<br />
- Added lines: 9<br />
- Diff added/deleted: 8


- Nb. undetected lines: 1/1 ( 292 )

###  org.apache.commons.math.ode.nonstiff.EmbeddedRungeKuttaIntegrator

```
295c295,303
<                   // rejecting the step would lead to a too small next step, we accept it
---
>                   // we cannot simply truncate the step, reject the current computation
>                   // and let the loop compute another state with the truncated step.
>                   // it is so small (much probably exactly 0 due to limited accuracy)
>                   // that the code above would fail handling it.
>                   // So we set up an artificial 0 size step by copying states
>                   interpolator.storeTime(stepStart);
>                   System.arraycopy(y, 0, yTmp, 0, y0.length);
>                   hNew     = 0;
>                   stepSize = 0;
```

- Deleted lines: 1<br />
- Added lines: 9<br />
- Diff added/deleted: 8


- Nb. undetected lines: 1/1 ( 295 )

###  org.apache.commons.math.ode.nonstiff.RungeKuttaIntegrator

```
175c175,182
<                 // rejecting the step would lead to a too small next step, we accept it
---
>                 // we cannot simply truncate the step, reject the current computation
>                 // and let the loop compute another state with the truncated step.
>                 // it is so small (much probably exactly 0 due to limited accuracy)
>                 // that the code above would fail handling it.
>                 // So we set up an artificial 0 size step by copying states
>                 interpolator.storeTime(stepStart);
>                 System.arraycopy(y, 0, yTmp, 0, y0.length);
>                 stepSize = 0;
```

- Deleted lines: 1<br />
- Added lines: 8<br />
- Diff added/deleted: 7


- Nb. undetected lines: 1/1 ( 175 )

###  org.apache.commons.math.ode.nonstiff.AdamsBashforthIntegrator

```
274c274,282
<                             // rejecting the step would lead to a too small next step, we accept it
---
>                             // we cannot simply truncate the step, reject the current computation
>                             // and let the loop compute another state with the truncated step.
>                             // it is so small (much probably exactly 0 due to limited accuracy)
>                             // that the code above would fail handling it.
>                             // So we set up an artificial 0 size step by copying states
>                             interpolator.storeTime(stepStart);
>                             System.arraycopy(y, 0, yTmp, 0, y0.length);
>                             hNew     = 0;
>                             stepSize = 0;
```

- Deleted lines: 1<br />
- Added lines: 9<br />
- Diff added/deleted: 8


- Nb. undetected lines: 1/1 ( 274 )

## Bug 72

- Nb. modified sources: 1

- Nb. nopol ranking entries: 110

###  org.apache.commons.math.analysis.solvers.BrentSolver

```
115c115
<             setResult(yMin, 0);
---
>             setResult(min, 0);
127c127
<             setResult(yMax, 0);
---
>             setResult(max, 0);
```

- Deleted lines: 2<br />
- Added lines: 2<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 115 | org.apache.commons.math.analysis.solvers.BrentSolver:115 -> 0.3779644730092272 (ep: 0, ef: 1, np: 2139, nf: 0) | 16 |

- Nb. undetected lines: 1/2 ( 127 )

## Bug 73

- Nb. modified sources: 1

- Nb. nopol ranking entries: 139

###  org.apache.commons.math.analysis.solvers.BrentSolver

```
34a35,39
>     /** Error message for non-bracketing interval. */
>     private static final String NON_BRACKETING_MESSAGE =
>         "function values at endpoints do not have different signs.  " +
>         "Endpoints: [{0}, {1}], Values: [{2}, {3}]";
> 
130a136,140
>         if (yMin * yMax > 0) {
>             throw MathRuntimeException.createIllegalArgumentException(
>                   NON_BRACKETING_MESSAGE, min, max, yMin, yMax);
>         }
> 
179,181c189
<                         "function values at endpoints do not have different signs.  " +
<                         "Endpoints: [{0}, {1}], Values: [{2}, {3}]",
<                         min, max, yMin, yMax);
---
>                         NON_BRACKETING_MESSAGE, min, max, yMin, yMax);
```

- Deleted lines: 3<br />
- Added lines: 11<br />
- Diff added/deleted: 8


- Nb. undetected lines: 5/5 ( 34 130 179 180 181 )

## Bug 74

- Nb. modified sources: 1

- Nb. nopol ranking entries: 1071

###  org.apache.commons.math.ode.nonstiff.EmbeddedRungeKuttaIntegrator

```
20,21d19
< import java.util.Arrays;
< 
247,249c245,249
<           final double[] scale;
<           if (vecAbsoluteTolerance != null) {
<             scale = vecAbsoluteTolerance;
---
>           final double[] scale = new double[y0.length];
>           if (vecAbsoluteTolerance == null) {
>               for (int i = 0; i < scale.length; ++i) {
>                 scale[i] = scalAbsoluteTolerance + scalRelativeTolerance * Math.abs(y[i]);
>               }
251,252c251,253
<             scale = new double[y0.length];
<             Arrays.fill(scale, scalAbsoluteTolerance);
---
>               for (int i = 0; i < scale.length; ++i) {
>                 scale[i] = vecAbsoluteTolerance[i] + vecRelativeTolerance[i] * Math.abs(y[i]);
>               }
```

- Deleted lines: 9<br />
- Added lines: 8<br />
- Diff added/deleted: -1

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 20 | org.apache.commons.math.ode.nonstiff.EmbeddedRungeKuttaIntegrator:200 -> 0.05399492471560388 (ep: 48, ef: 1, np: 2082, nf: 0) | 760 |
| 21 | org.apache.commons.math.ode.nonstiff.EmbeddedRungeKuttaIntegrator:215 -> 0.05698028822981897 (ep: 43, ef: 1, np: 2087, nf: 0) | 707 |
| 248 | org.apache.commons.math.ode.nonstiff.EmbeddedRungeKuttaIntegrator:248 -> 0.0545544725589981 (ep: 47, ef: 1, np: 2083, nf: 0) | 715 |
| 251 | org.apache.commons.math.ode.nonstiff.EmbeddedRungeKuttaIntegrator:251 -> 0.05832118435198043 (ep: 41, ef: 1, np: 2089, nf: 0) | 673 |
| 252 | org.apache.commons.math.ode.nonstiff.EmbeddedRungeKuttaIntegrator:252 -> 0.05832118435198043 (ep: 41, ef: 1, np: 2089, nf: 0) | 674 |

- Nb. undetected lines: 2/7 ( 247 249 )

## Bug 75

- Nb. modified sources: 1

- Nb. nopol ranking entries: 111

###  org.apache.commons.math.stat.Frequency

```
303c303
<         return getCumPct((Comparable<?>) v);
---
>         return getPct((Comparable<?>) v);
```

- Deleted lines: 2<br />
- Added lines: 2<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 303 | org.apache.commons.math.stat.Frequency:303 -> 0.3779644730092272 (ep: 0, ef: 1, np: 2134, nf: 0) | 16 |

- Nb. undetected lines: 0/1

## Bug 76

- Nb. modified sources: 1

- Nb. nopol ranking entries: 516

###  org.apache.commons.math.linear.SingularValueDecompositionImpl

```
162c162
<                     eigenDecomposition.getV().getSubMatrix(0, p - 1, 0, p - 1);
---
>                     eigenDecomposition.getV().getSubMatrix(0, n - 1, 0, p - 1);
166c166
<                 for (int i = 0; i < p - 1; ++i) {
---
>                 for (int i = 0; i < p; ++i) {
169d168
<                     final double si = secondaryBidiagonal[i];
171a171
>                     if (i < n - 1) {
172a173
>                         final double si = secondaryBidiagonal[i];
176,179c177
<                 }
<                 // last row
<                 final double lastMain = mainBidiagonal[p - 1];
<                 final double[] wr1  = wData[p - 1];
---
>                     } else {
181c179,180
<                     wr1[j] = ei1[j] * lastMain / singularValues[j];
---
>                             wi[j] = mi * ei0[j] / singularValues[j];
>                         }
182a182,183
>                 }
> 
250c251
<                     eigenDecomposition.getV().getSubMatrix(0, p - 1, 0, p - 1);
---
>                     eigenDecomposition.getV().getSubMatrix(0, m - 1, 0, p - 1);
254c255
<                 for (int i = 0; i < p - 1; ++i) {
---
>                 for (int i = 0; i < p; ++i) {
256d256
<                     final double si = secondaryBidiagonal[i];
258a259
>                     if (i < m - 1) {
259a261
>                         final double si = secondaryBidiagonal[i];
263,266c265
<                 }
<                 // last row
<                 final double lastMain = mainBidiagonal[p - 1];
<                 final double[] wr1  = wData[p - 1];
---
>                     } else {
268c267,269
<                     wr1[j] = ei1[j] * lastMain / singularValues[j];
---
>                             wi[j] = mi * ei0[j] / singularValues[j];
>                         }
>                     }
```

- Deleted lines: 20<br />
- Added lines: 17<br />
- Diff added/deleted: -3

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 166 | org.apache.commons.math.linear.SingularValueDecompositionImpl:166 -> 0.21320071635561041 (ep: 16, ef: 3, np: 2117, nf: -1) | 60 |
| 169 | org.apache.commons.math.linear.SingularValueDecompositionImpl:169 -> 0.125 (ep: 7, ef: 1, np: 2126, nf: 1) | 350 |
| 171 | org.apache.commons.math.linear.SingularValueDecompositionImpl:171 -> 0.125 (ep: 7, ef: 1, np: 2126, nf: 1) | 352 |
| 172 | org.apache.commons.math.linear.SingularValueDecompositionImpl:172 -> 0.125 (ep: 7, ef: 1, np: 2126, nf: 1) | 353 |
| 178 | org.apache.commons.math.linear.SingularValueDecompositionImpl:178 -> 0.21320071635561041 (ep: 9, ef: 2, np: 2124, nf: 0) | 61 |
| 179 | org.apache.commons.math.linear.SingularValueDecompositionImpl:179 -> 0.21320071635561041 (ep: 9, ef: 2, np: 2124, nf: 0) | 62 |
| 181 | org.apache.commons.math.linear.SingularValueDecompositionImpl:181 -> 0.21320071635561041 (ep: 9, ef: 2, np: 2124, nf: 0) | 64 |

- Nb. undetected lines: 14/21 ( 162 176 177 182 250 254 256 258 259 263 264 265 266 268 )

## Bug 77

- Nb. modified sources: 3

- Nb. nopol ranking entries: 165

###  org.apache.commons.math.linear.AbstractRealVector

```
208a209,242
>     public double getNorm() {
>         double sum = 0;
>         Iterator<Entry> it = sparseIterator();
>         Entry e;
>         while (it.hasNext() && (e = it.next()) != null) {
>             final double value = e.getValue();
>             sum += value * value;
>         }
>         return Math.sqrt(sum);
>     }
> 
>     /** {@inheritDoc} */
>     public double getL1Norm() {
>         double norm = 0;
>         Iterator<Entry> it = sparseIterator();
>         Entry e;
>         while (it.hasNext() && (e = it.next()) != null) {
>             norm += Math.abs(e.getValue());
>         }
>         return norm;
>     }
> 
>     /** {@inheritDoc} */
>     public double getLInfNorm() {
>         double norm = 0;
>         Iterator<Entry> it = sparseIterator();
>         Entry e;
>         while (it.hasNext() && (e = it.next()) != null) {
>             norm = Math.max(norm, Math.abs(e.getValue()));
>         }
>         return norm;
>     }
> 
>     /** {@inheritDoc} */
```

- Deleted lines: 3<br />
- Added lines: 34<br />
- Diff added/deleted: 31


- Nb. undetected lines: 1/1 ( 208 )

###  org.apache.commons.math.linear.OpenMapRealVector

```
498,508d497
<     /** {@inheritDoc} */
<     public double getL1Norm() {
<         double res = 0;
<         Iterator iter = entries.iterator();
<         while (iter.hasNext()) {
<             iter.advance();
<             res += Math.abs(iter.value());
<         }
<         return res;
<     }
< 
560,581d548
<     public double getLInfNorm() {
<         double max = 0;
<         Iterator iter = entries.iterator();
<         while (iter.hasNext()) {
<             iter.advance();
<             max += iter.value();
<         }
<         return max;
<     }
< 
<     /** {@inheritDoc} */
<     public double getNorm() {
<         double res = 0;
<         Iterator iter = entries.iterator();
<         while (iter.hasNext()) {
<             iter.advance();
<             res += iter.value() * iter.value();
<         }
<         return Math.sqrt(res);
<     }
< 
<     /** {@inheritDoc} */
```

- Deleted lines: 33<br />
- Added lines: 0<br />
- Diff added/deleted: -33

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 500 | org.apache.commons.math.linear.OpenMapRealVector:500 -> 0.35355339059327373 (ep: 0, ef: 1, np: 2127, nf: 1) | 26 |
| 501 | org.apache.commons.math.linear.OpenMapRealVector:501 -> 0.35355339059327373 (ep: 0, ef: 1, np: 2127, nf: 1) | 27 |
| 502 | org.apache.commons.math.linear.OpenMapRealVector:502 -> 0.35355339059327373 (ep: 0, ef: 1, np: 2127, nf: 1) | 28 |
| 503 | org.apache.commons.math.linear.OpenMapRealVector:503 -> 0.35355339059327373 (ep: 0, ef: 1, np: 2127, nf: 1) | 29 |
| 504 | org.apache.commons.math.linear.OpenMapRealVector:504 -> 0.35355339059327373 (ep: 0, ef: 1, np: 2127, nf: 1) | 30 |
| 506 | org.apache.commons.math.linear.OpenMapRealVector:506 -> 0.35355339059327373 (ep: 0, ef: 1, np: 2127, nf: 1) | 31 |
| 561 | org.apache.commons.math.linear.OpenMapRealVector:561 -> 0.35355339059327373 (ep: 0, ef: 1, np: 2127, nf: 1) | 32 |
| 562 | org.apache.commons.math.linear.OpenMapRealVector:562 -> 0.35355339059327373 (ep: 0, ef: 1, np: 2127, nf: 1) | 33 |
| 563 | org.apache.commons.math.linear.OpenMapRealVector:563 -> 0.35355339059327373 (ep: 0, ef: 1, np: 2127, nf: 1) | 34 |
| 564 | org.apache.commons.math.linear.OpenMapRealVector:564 -> 0.35355339059327373 (ep: 0, ef: 1, np: 2127, nf: 1) | 35 |
| 565 | org.apache.commons.math.linear.OpenMapRealVector:565 -> 0.35355339059327373 (ep: 0, ef: 1, np: 2127, nf: 1) | 36 |
| 567 | org.apache.commons.math.linear.OpenMapRealVector:567 -> 0.35355339059327373 (ep: 0, ef: 1, np: 2127, nf: 1) | 37 |
| 572 | org.apache.commons.math.linear.OpenMapRealVector:572 -> 0.35355339059327373 (ep: 0, ef: 1, np: 2127, nf: 1) | 38 |
| 573 | org.apache.commons.math.linear.OpenMapRealVector:573 -> 0.35355339059327373 (ep: 0, ef: 1, np: 2127, nf: 1) | 39 |
| 574 | org.apache.commons.math.linear.OpenMapRealVector:574 -> 0.35355339059327373 (ep: 0, ef: 1, np: 2127, nf: 1) | 40 |
| 575 | org.apache.commons.math.linear.OpenMapRealVector:575 -> 0.35355339059327373 (ep: 0, ef: 1, np: 2127, nf: 1) | 41 |
| 576 | org.apache.commons.math.linear.OpenMapRealVector:576 -> 0.35355339059327373 (ep: 0, ef: 1, np: 2127, nf: 1) | 42 |
| 578 | org.apache.commons.math.linear.OpenMapRealVector:578 -> 0.35355339059327373 (ep: 0, ef: 1, np: 2127, nf: 1) | 43 |

- Nb. undetected lines: 15/33 ( 498 499 505 507 508 560 566 568 569 570 571 577 579 580 581 )

###  org.apache.commons.math.linear.ArrayRealVector

```
696a697
>     @Override
705a707
>     @Override
714a717
>     @Override
718c721
<             max += Math.max(max, Math.abs(a));
---
>             max = Math.max(max, Math.abs(a));
```

- Deleted lines: 1<br />
- Added lines: 4<br />
- Diff added/deleted: 3

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 718 | org.apache.commons.math.linear.ArrayRealVector:718 -> 0.35355339059327373 (ep: 0, ef: 1, np: 2127, nf: 1) | 23 |

- Nb. undetected lines: 3/4 ( 696 705 714 )

## Bug 78

- Nb. modified sources: 1

- Nb. nopol ranking entries: 199

###  org.apache.commons.math.ode.events.EventState

```
190a191,210
>                     if (ga * gb > 0) {
>                         // this is a corner case:
>                         // - there was an event near ta,
>                         // - there is another event between ta and tb
>                         // - when ta was computed, convergence was reached on the "wrong side" of the interval
>                         // this implies that the real sign of ga is the same as gb, so we need to slightly
>                         // shift ta to make sure ga and gb get opposite signs and the solver won't complain
>                         // about bracketing
>                         final double epsilon = (forward ? 0.25 : -0.25) * convergence;
>                         for (int k = 0; (k < 4) && (ga * gb > 0); ++k) {
>                             ta += epsilon;
>                             interpolator.setInterpolatedTime(ta);
>                             ga = handler.g(ta, interpolator.getInterpolatedState());
>                         }
>                         if (ga * gb > 0) {
>                             // this should never happen
>                             throw MathRuntimeException.createInternalError(null);
>                         }
>                     }
>                          
209,218c229,231
<                     double root;
<                     try {
<                         root = (ta <= tb) ? solver.solve(f, ta, tb) : solver.solve(f, tb, ta);
<                     } catch (IllegalArgumentException iae) {
<                         // the interval did not really bracket a root
<                         root = Double.NaN;
<                     }
<                     if (Double.isNaN(root) ||
<                         ((Math.abs(root - ta) <= convergence) &&
<                          (Math.abs(root - previousEventTime) <= convergence))) {
---
>                     final double root = (ta <= tb) ? solver.solve(f, ta, tb) : solver.solve(f, tb, ta);
>                     if ((Math.abs(root - ta) <= convergence) &&
>                          (Math.abs(root - previousEventTime) <= convergence)) {
```

- Deleted lines: 14<br />
- Added lines: 23<br />
- Diff added/deleted: 9

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 211 | org.apache.commons.math.ode.events.EventState:211 -> 0.040996003084539386 (ep: 84, ef: 1, np: 2021, nf: 0) | 93 |
| 212 | org.apache.commons.math.ode.events.EventState:212 -> 0.3779644730092272 (ep: 0, ef: 1, np: 2105, nf: 0) | 16 |
| 214 | org.apache.commons.math.ode.events.EventState:214 -> 0.3779644730092272 (ep: 0, ef: 1, np: 2105, nf: 0) | 17 |
| 215 | org.apache.commons.math.ode.events.EventState:215 -> 0.041239304942116126 (ep: 83, ef: 1, np: 2022, nf: 0) | 77 |
| 216 | org.apache.commons.math.ode.events.EventState:216 -> 0.041239304942116126 (ep: 83, ef: 1, np: 2022, nf: 0) | 78 |

- Nb. undetected lines: 6/11 ( 190 209 210 213 217 218 )

## Bug 79

- Nb. modified sources: 1

- Nb. nopol ranking entries: 98

###  org.apache.commons.math.util.MathUtils

```
1624c1624
<       int sum = 0;
---
>       double sum = 0;
1626c1626
<           final int dp = p1[i] - p2[i];
---
>           final double dp = p1[i] - p2[i];
```

- Deleted lines: 2<br />
- Added lines: 2<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 1624 | org.apache.commons.math.util.MathUtils:1624 -> 0.1889822365046136 (ep: 3, ef: 1, np: 2100, nf: 0) | 67 |
| 1626 | org.apache.commons.math.util.MathUtils:1626 -> 0.1889822365046136 (ep: 3, ef: 1, np: 2100, nf: 0) | 69 |

- Nb. undetected lines: 0/2

## Bug 80

- Nb. modified sources: 1

- Nb. nopol ranking entries: 617

###  org.apache.commons.math.linear.EigenDecompositionImpl

```
1135c1135
<             int j = 4 * n - 1;
---
>             int j = 4 * (n - 1);
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 1135 | org.apache.commons.math.linear.EigenDecompositionImpl:1135 -> 0.3779644730092272 (ep: 0, ef: 1, np: 2100, nf: 1) | 29 |

- Nb. undetected lines: 0/1

## Bug 81

- Nb. modified sources: 1

- Nb. nopol ranking entries: 441

###  org.apache.commons.math.linear.EigenDecompositionImpl

```
598,599c598,603
<         work[lowerStart + m - 1] = dCurrent - eCurrent;
<         work[upperStart + m - 1] = dCurrent + eCurrent;
---
>         final double lower = dCurrent - eCurrent;
>         work[lowerStart + m - 1] = lower;
>         lowerSpectra = Math.min(lowerSpectra, lower);
>         final double upper = dCurrent + eCurrent;
>         work[upperStart + m - 1] = upper;
>         upperSpectra = Math.max(upperSpectra, upper);
902,903c906,907
<                     for (int i = 4 * i0; i < 4 * n0 - 11; i += 4) {
<                         if ((work[i + 3] <= TOLERANCE_2 * work[i]) &&
---
>                     for (int i = 4 * i0; i < 4 * n0 - 16; i += 4) {
>                         if ((work[i + 3] <= TOLERANCE_2 * work[i]) ||
1540c1544
<                 if (end - start > 2) {
---
>                 if (end - start > 3) {
```

- Deleted lines: 7<br />
- Added lines: 10<br />
- Diff added/deleted: 3

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 598 | org.apache.commons.math.linear.EigenDecompositionImpl:598 -> 0.06388765649999399 (ep: 34, ef: 1, np: 2066, nf: 0) | 415 |
| 599 | org.apache.commons.math.linear.EigenDecompositionImpl:599 -> 0.06388765649999399 (ep: 34, ef: 1, np: 2066, nf: 0) | 416 |
| 1540 | org.apache.commons.math.linear.EigenDecompositionImpl:1540 -> 0.2182178902359924 (ep: 2, ef: 1, np: 2098, nf: 0) | 48 |

- Nb. undetected lines: 2/5 ( 902 903 )

## Bug 82

- Nb. modified sources: 1

- Nb. nopol ranking entries: 265

###  org.apache.commons.math.optimization.linear.SimplexSolver

```
80,82c80,83
<             double rhs = tableau.getEntry(i, tableau.getWidth() - 1);
<             if (MathUtils.compareTo(tableau.getEntry(i, col), 0, epsilon) >= 0) {
<                 double ratio = rhs / tableau.getEntry(i, col);
---
>             final double rhs = tableau.getEntry(i, tableau.getWidth() - 1);
>             final double entry = tableau.getEntry(i, col);
>             if (MathUtils.compareTo(entry, 0, epsilon) > 0) {
>                 final double ratio = rhs / entry;
```

- Deleted lines: 3<br />
- Added lines: 5<br />
- Diff added/deleted: 2

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 80 | org.apache.commons.math.optimization.linear.SimplexSolver:80 -> 0.10101525445522107 (ep: 13, ef: 1, np: 2042, nf: 0) | 126 |
| 81 | org.apache.commons.math.optimization.linear.SimplexSolver:81 -> 0.10101525445522107 (ep: 13, ef: 1, np: 2042, nf: 0) | 127 |
| 82 | org.apache.commons.math.optimization.linear.SimplexSolver:82 -> 0.10101525445522107 (ep: 13, ef: 1, np: 2042, nf: 0) | 128 |

- Nb. undetected lines: 0/3

## Bug 83

- Nb. modified sources: 1

- Nb. nopol ranking entries: 290

###  org.apache.commons.math.optimization.linear.SimplexTableau

```
292c292,293
<         for (int i = getNumObjectiveFunctions(); i < getHeight(); i++) {
---
>         int start = ignoreObjectiveRows ? getNumObjectiveFunctions() : 0;
>         for (int i = start; i < getHeight(); i++) {
340,341c341,342
<       Integer basicRow = getBasicRow(getNumObjectiveFunctions() + getOriginalNumDecisionVariables());
<       double mostNegative = basicRow == null ? 0 : getEntry(basicRow, getRhsOffset());
---
>       Integer negativeVarBasicRow = getBasicRowForSolution(getNegativeDecisionVariableOffset());
>       double mostNegative = negativeVarBasicRow == null ? 0 : getEntry(negativeVarBasicRow, getRhsOffset());
344c345
<            basicRow = getBasicRow(getNumObjectiveFunctions() + i);
---
>           Integer basicRow = getBasicRowForSolution(getNumObjectiveFunctions() + i);
```

- Deleted lines: 5<br />
- Added lines: 5<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 292 | org.apache.commons.math.optimization.linear.SimplexTableau:292 -> 0.0944911182523068 (ep: 30, ef: 2, np: 2024, nf: -1) | 195 |
| 340 | org.apache.commons.math.optimization.linear.SimplexTableau:340 -> 0.11396057645963795 (ep: 10, ef: 1, np: 2044, nf: 0) | 80 |
| 341 | org.apache.commons.math.optimization.linear.SimplexTableau:341 -> 0.11396057645963795 (ep: 10, ef: 1, np: 2044, nf: 0) | 81 |
| 344 | org.apache.commons.math.optimization.linear.SimplexTableau:344 -> 0.11396057645963795 (ep: 10, ef: 1, np: 2044, nf: 0) | 84 |

- Nb. undetected lines: 0/4

## Bug 84

- Nb. modified sources: 1

- Nb. nopol ranking entries: 211

###  org.apache.commons.math.optimization.direct.MultiDirectional

```
63a64
>         final RealConvergenceChecker checker = getConvergenceChecker();
94a96,105
>             // check convergence
>             final int iter = getIterations();
>             boolean converged = true;
>             for (int i = 0; i < simplex.length; ++i) {
>                 converged &= checker.converged(iter, original[i], simplex[i]);
>             }
>             if (converged) {
>                 return;
>             }
> 
```

- Deleted lines: 1<br />
- Added lines: 11<br />
- Diff added/deleted: 10


- Nb. undetected lines: 2/2 ( 63 94 )

## Bug 85

- Nb. modified sources: 1

- Nb. nopol ranking entries: 187

###  org.apache.commons.math.analysis.solvers.UnivariateRealSolverUtils

```
198c198
<         if (fa * fb >= 0.0 ) {
---
>         if (fa * fb > 0.0 ) {
```

- Deleted lines: 1<br />
- Added lines: 2<br />
- Diff added/deleted: 1

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 198 | org.apache.commons.math.analysis.solvers.UnivariateRealSolverUtils:198 -> 0.09166984970282113 (ep: 16, ef: 1, np: 1966, nf: 0) | 112 |

- Nb. undetected lines: 0/1

## Bug 86

- Nb. modified sources: 1

- Nb. nopol ranking entries: 279

###  org.apache.commons.math.linear.CholeskyDecompositionImpl

```
114,118d113
<             // check diagonal element
<             if (lTData[i][i] < absolutePositivityThreshold) {
<                 throw new NotPositiveDefiniteMatrixException();
<             }
< 
136a132,137
> 
>             // check diagonal element
>             if (ltI[i] < absolutePositivityThreshold) {
>                 throw new NotPositiveDefiniteMatrixException();
>             }
> 
```

- Deleted lines: 6<br />
- Added lines: 6<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 115 | org.apache.commons.math.linear.CholeskyDecompositionImpl:115 -> 0.21320071635561041 (ep: 9, ef: 2, np: 1883, nf: 0) | 60 |
| 136 | org.apache.commons.math.linear.CholeskyDecompositionImpl:136 -> 0.22360679774997896 (ep: 8, ef: 2, np: 1884, nf: 0) | 42 |

- Nb. undetected lines: 4/6 ( 114 116 117 118 )

## Bug 87

- Nb. modified sources: 1

- Nb. nopol ranking entries: 296

###  org.apache.commons.math.optimization.linear.SimplexTableau

```
275,276c275
<             if (!MathUtils.equals(getEntry(i, col), 0.0, epsilon)) {
<                 if (row == null) {
---
>             if (MathUtils.equals(getEntry(i, col), 1.0, epsilon) && (row == null)) {
278c277
<                 } else {
---
>             } else if (!MathUtils.equals(getEntry(i, col), 0.0, epsilon)) {
282d280
<         }
```

- Deleted lines: 4<br />
- Added lines: 2<br />
- Diff added/deleted: -2

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 275 | org.apache.commons.math.optimization.linear.SimplexTableau:275 -> 0.09759000729485333 (ep: 14, ef: 1, np: 1878, nf: 0) | 172 |
| 276 | org.apache.commons.math.optimization.linear.SimplexTableau:276 -> 0.09759000729485333 (ep: 14, ef: 1, np: 1878, nf: 0) | 173 |

- Nb. undetected lines: 2/4 ( 278 282 )

## Bug 88

- Nb. modified sources: 1

- Nb. nopol ranking entries: 315

###  org.apache.commons.math.optimization.linear.SimplexTableau

```
326c326,329
<         double mostNegative = getDecisionVariableValue(getOriginalNumDecisionVariables());
---
>         Integer basicRow =
>             getBasicRow(getNumObjectiveFunctions() + getOriginalNumDecisionVariables());
>         double mostNegative = basicRow == null ? 0 : getEntry(basicRow, getRhsOffset());
>         Set<Integer> basicRows = new HashSet<Integer>();
327a331,337
>             basicRow = getBasicRow(getNumObjectiveFunctions() + i);
>             if (basicRows.contains(basicRow)) {
>                 // if multiple variables can take a given value 
>                 // then we choose the first and set the rest equal to 0
>                 coefficients[i] = 0;
>             } else {
>                 basicRows.add(basicRow);
329,352c339,340
<                 getDecisionVariableValue(i) - (restrictToNonNegative ? 0 : mostNegative); 
<         }
<         return new RealPointValuePair(coefficients, f.getValue(coefficients));
<     }
< 
<     /**
<      * Get the value of the given decision variable.  This is not the actual
<      * value as it is guaranteed to be >= 0 and thus must be corrected before
<      * being returned to the user.
<      * 
<      * @param decisionVariable The index of the decision variable
<      * @return The value of the given decision variable.
<      */
<     protected double getDecisionVariableValue(final int decisionVariable) {
<       int col = getNumObjectiveFunctions() + decisionVariable;  
<       Integer basicRow = getBasicRow(col);
<       if (basicRow == null) {
<           return 0;
<       }
<       // if there are multiple variables that can take the value on the RHS
<       // then we'll give the first variable that value
<       for (int i = getNumObjectiveFunctions(); i < col; i++) {
<           if (tableau.getEntry(basicRow, i) == 1) {
<               return 0;
---
>                     (basicRow == null ? 0 : getEntry(basicRow, getRhsOffset())) -
>                     (restrictToNonNegative ? 0 : mostNegative);
355c343
<       return getEntry(basicRow, getRhsOffset()); 
---
>         return new RealPointValuePair(coefficients, f.getValue(coefficients));
```

- Deleted lines: 27<br />
- Added lines: 15<br />
- Diff added/deleted: -12

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 326 | org.apache.commons.math.optimization.linear.SimplexTableau:326 -> 0.1259881576697424 (ep: 8, ef: 1, np: 1871, nf: 0) | 62 |
| 327 | org.apache.commons.math.optimization.linear.SimplexTableau:327 -> 0.1259881576697424 (ep: 16, ef: 2, np: 1863, nf: -1) | 63 |
| 331 | org.apache.commons.math.optimization.linear.SimplexTableau:331 -> 0.1259881576697424 (ep: 8, ef: 1, np: 1871, nf: 0) | 66 |
| 343 | org.apache.commons.math.optimization.linear.SimplexTableau:343 -> 0.1259881576697424 (ep: 8, ef: 1, np: 1871, nf: 0) | 67 |
| 344 | org.apache.commons.math.optimization.linear.SimplexTableau:344 -> 0.1259881576697424 (ep: 8, ef: 1, np: 1871, nf: 0) | 68 |
| 345 | org.apache.commons.math.optimization.linear.SimplexTableau:345 -> 0.1259881576697424 (ep: 8, ef: 1, np: 1871, nf: 0) | 69 |
| 346 | org.apache.commons.math.optimization.linear.SimplexTableau:346 -> 0.1259881576697424 (ep: 8, ef: 1, np: 1871, nf: 0) | 70 |
| 350 | org.apache.commons.math.optimization.linear.SimplexTableau:350 -> 0.1336306209562122 (ep: 15, ef: 2, np: 1864, nf: -1) | 58 |
| 351 | org.apache.commons.math.optimization.linear.SimplexTableau:351 -> 0.1259881576697424 (ep: 8, ef: 1, np: 1871, nf: 0) | 72 |
| 352 | org.apache.commons.math.optimization.linear.SimplexTableau:352 -> 0.2182178902359924 (ep: 2, ef: 1, np: 1877, nf: 0) | 39 |
| 355 | org.apache.commons.math.optimization.linear.SimplexTableau:355 -> 0.1259881576697424 (ep: 8, ef: 1, np: 1871, nf: 0) | 73 |

- Nb. undetected lines: 16/27 ( 329 330 332 333 334 335 336 337 338 339 340 341 342 347 348 349 )

## Bug 89

- Nb. modified sources: 1

- Nb. nopol ranking entries: 64

###  org.apache.commons.math.stat.Frequency

```
104,105c104,105
<      * @throws IllegalArgumentException if <code>v</code> is not comparable with previous entries
<      * @throws ClassCastException if <code>v</code> is not Comparable
---
>      * @throws IllegalArgumentException if <code>v</code> is not Comparable, 
>      *         or is not comparable with previous entries
109a110
>         if (v instanceof Comparable<?>){
110a112,114
>         } else {
>             throw new IllegalArgumentException("Object must implement Comparable");
>         }
```

- Deleted lines: 4<br />
- Added lines: 8<br />
- Diff added/deleted: 4

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 110 | org.apache.commons.math.stat.Frequency:110 -> 0.25 (ep: 1, ef: 1, np: 1689, nf: 1) | 38 |

- Nb. undetected lines: 3/4 ( 104 105 109 )

## Bug 90

- Nb. modified sources: 1

- Nb. nopol ranking entries: 68

###  org.apache.commons.math.stat.Frequency

```
104c104,106
<      * @throws IllegalArgumentException if <code>v</code> is not comparable.
---
>      * @throws IllegalArgumentException if <code>v</code> is not comparable with previous entries
>      * @throws ClassCastException if <code>v</code> is not Comparable
>      * @deprecated use {@link #addValue(Comparable)} instead
105a108
>     @Deprecated
106a110,123
>         addValue((Comparable<?>) v);
>     }
>     
>     /**
>      * Adds 1 to the frequency count for v.
>      * <p>
>      * If other objects have already been added to this Frequency, v must
>      * be comparable to those that have already been added.
>      * </p>
>      * 
>      * @param v the value to add.
>      * @throws IllegalArgumentException if <code>v</code> is not comparable with previous entries
>      */
>     public void addValue(Comparable<?>v){
```

- Deleted lines: 8<br />
- Added lines: 19<br />
- Diff added/deleted: 11


- Nb. undetected lines: 3/3 ( 104 105 106 )

## Bug 91

- Nb. modified sources: 1

- Nb. nopol ranking entries: 60

###  org.apache.commons.math.fraction.Fraction

```
259,272c259,261
<         int ret = 0;
<         
<         if (this != object) { 
<             double first = doubleValue();
<             double second = object.doubleValue();
<             
<             if (first < second) {
<                 ret = -1;
<             } else if (first > second) {
<                 ret = 1;
<             }
<         }
<         
<         return ret;
---
>         long nOd = ((long) numerator) * object.denominator;
>         long dOn = ((long) denominator) * object.numerator;
>         return (nOd < dOn) ? -1 : ((nOd > dOn) ? +1 : 0);
```

- Deleted lines: 15<br />
- Added lines: 4<br />
- Diff added/deleted: -11


- Nb. undetected lines: 14/14 ( 259 260 261 262 263 264 265 266 267 268 269 270 271 272 )

## Bug 92

- Nb. modified sources: 1

- Nb. nopol ranking entries: 89

###  org.apache.commons.math.util.MathUtils

```
184,188c184,219
< 
<         long result = Math.round(binomialCoefficientDouble(n, k));
<         if (result == Long.MAX_VALUE) {
<             throw new ArithmeticException(
<                 "result too large to represent in a long integer");
---
>         // Use symmetry for large k
>         if (k > n / 2)
>             return binomialCoefficient(n, n - k);
>         
>         // We use the formula
>         // (n choose k) = n! / (n-k)! / k!
>         // (n choose k) == ((n-k+1)*...*n) / (1*...*k)
>         // which could be written
>         // (n choose k) == (n-1 choose k-1) * n / k
>         long result = 1;
>         if (n <= 61) {
>             // For n <= 61, the naive implementation cannot overflow.
>             for (int j = 1, i = n - k + 1; j <= k; i++, j++) {
>                 result = result * i / j;
>             }
>         } else if (n <= 66) {
>             // For n > 61 but n <= 66, the result cannot overflow,
>             // but we must take care not to overflow intermediate values.
>             for (int j = 1, i = n - k + 1; j <= k; i++, j++) {
>                 // We know that (result * i) is divisible by j,
>                 // but (result * i) may overflow, so we split j:
>                 // Filter out the gcd, d, so j/d and i/d are integer.
>                 // result is divisible by (j/d) because (j/d)
>                 // is relative prime to (i/d) and is a divisor of
>                 // result * (i/d).
>                 long d = gcd(i, j);
>                 result = (result / (j / d)) * (i / d);
>             }
>         } else {
>             // For n > 66, a result overflow might occur, so we check
>             // the multiplication, taking care to not overflow
>             // unnecessary.
>             for (int j = 1, i = n - k + 1; j <= k; i++, j++) {
>                 long d = gcd(i, j);
>                 result = mulAndCheck((result / (j / d)), (i / d));
>             }
216c247,273
<         return Math.floor(Math.exp(binomialCoefficientLog(n, k)) + 0.5);
---
>         if (n < k) {
>             throw new IllegalArgumentException(
>                 "must have n >= k for binomial coefficient (n,k)");
>         }
>         if (n < 0) {
>             throw new IllegalArgumentException(
>                 "must have n >= 0 for binomial coefficient (n,k)");
>         }
>         if ((n == k) || (k == 0)) {
>             return 1d;
>         }
>         if ((k == 1) || (k == n - 1)) {
>             return n;
>         }
>         if (k > n/2) {
>             return binomialCoefficientDouble(n, n - k);
>         }
>         if (n < 67) {
>             return binomialCoefficient(n,k);
>         }
>         
>         double result = 1d;
>         for (int i = 1; i <= k; i++) {
>              result *= (double)(n - k + i) / (double)i;
>         }
>   
>         return Math.floor(result + 0.5);
250c307,315
<             return Math.log((double)n);
---
>             return Math.log((double) n);
>         }
>         
>         /*
>          * For values small enough to do exact integer computation,
>          * return the log of the exact value 
>          */
>         if (n < 67) {  
>             return Math.log(binomialCoefficient(n,k));
251a317,328
>         
>         /*
>          * Return the log of binomialCoefficientDouble for values that will not
>          * overflow binomialCoefficientDouble
>          */
>         if (n < 1030) { 
>             return Math.log(binomialCoefficientDouble(n, k));
>         } 
>         
>         /*
>          * Sum logs for values that could overflow
>          */
```

- Deleted lines: 20<br />
- Added lines: 84<br />
- Diff added/deleted: 64

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 185 | org.apache.commons.math.util.MathUtils:185 -> 0.20412414523193154 (ep: 2, ef: 1, np: 1504, nf: 1) | 44 |
| 186 | org.apache.commons.math.util.MathUtils:186 -> 0.20412414523193154 (ep: 2, ef: 1, np: 1504, nf: 1) | 45 |
| 216 | org.apache.commons.math.util.MathUtils:216 -> 0.11180339887498948 (ep: 9, ef: 1, np: 1497, nf: 1) | 78 |

- Nb. undetected lines: 5/8 ( 184 187 188 250 251 )

## Bug 93

- Nb. modified sources: 1

- Nb. nopol ranking entries: 71

###  org.apache.commons.math.util.MathUtils

```
314a315,321
>     /** All long-representable factorials */
>     private static final long[] factorials = new long[] 
>        {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800,
>         479001600, 6227020800l, 87178291200l, 1307674368000l, 20922789888000l,
>         355687428096000l, 6402373705728000l, 121645100408832000l,
>         2432902008176640000l};
> 
338,339c345,348
<         long result = Math.round(factorialDouble(n));
<         if (result == Long.MAX_VALUE) {
---
>         if (n < 0) {
>             throw new IllegalArgumentException("must have n >= 0 for n!");
>         }
>         if (n > 20) {
341c350
<                 "result too large to represent in a long integer");
---
>                     "factorial value is too large to fit in a long");
343c352
<         return result;
---
>         return factorials[n];
369a379,381
>         if (n < 21) {
>             return factorial(n);
>         }
389a402,404
>         if (n < 21) {
>             return Math.log(factorial(n));
>         }
```

- Deleted lines: 7<br />
- Added lines: 19<br />
- Diff added/deleted: 12

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 338 | org.apache.commons.math.util.MathUtils:338 -> 0.25 (ep: 1, ef: 1, np: 1501, nf: 1) | 39 |
| 339 | org.apache.commons.math.util.MathUtils:339 -> 0.25 (ep: 1, ef: 1, np: 1501, nf: 1) | 40 |
| 343 | org.apache.commons.math.util.MathUtils:343 -> 0.35355339059327373 (ep: 0, ef: 1, np: 1502, nf: 1) | 32 |

- Nb. undetected lines: 4/7 ( 314 341 369 389 )

## Bug 94

- Nb. modified sources: 1

- Nb. nopol ranking entries: 80

###  org.apache.commons.math.util.MathUtils

```
412c412
<         if (u * v == 0) {
---
>         if ((u == 0) || (v == 0)) {
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 412 | org.apache.commons.math.util.MathUtils:412 -> 0.060302268915552716 (ep: 24, ef: 1, np: 1475, nf: 1) | 81 |

- Nb. undetected lines: 0/1

## Bug 95

- Nb. modified sources: 1

- Nb. nopol ranking entries: 172

###  org.apache.commons.math.distribution.FDistributionImpl

```
144,145c144,150
<         return getDenominatorDegreesOfFreedom() /
<             (getDenominatorDegreesOfFreedom() - 2.0);
---
>         double ret = 1.0;
>         double d = getDenominatorDegreesOfFreedom();
>         if (d > 2.0) {
>             // use mean
>             ret = d / (d - 2.0);
>         }
>         return ret;
```

- Deleted lines: 2<br />
- Added lines: 7<br />
- Diff added/deleted: 5

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 144 | org.apache.commons.math.distribution.FDistributionImpl:144 -> 0.18257418583505536 (ep: 2, ef: 1, np: 1297, nf: 1) | 63 |

- Nb. undetected lines: 1/2 ( 145 )

## Bug 96

- Nb. modified sources: 1

- Nb. nopol ranking entries: 61

###  org.apache.commons.math.complex.Complex

```
258,261c258
<                 ret = (Double.doubleToRawLongBits(real) ==
<                         Double.doubleToRawLongBits(rhs.getReal())) &&
<                     (Double.doubleToRawLongBits(imaginary) ==
<                         Double.doubleToRawLongBits(rhs.getImaginary())); 
---
>                     ret = (real == rhs.real) && (imaginary == rhs.imaginary); 
```

- Deleted lines: 4<br />
- Added lines: 1<br />
- Diff added/deleted: -3


- Nb. undetected lines: 4/4 ( 258 259 260 261 )

## Bug 97

- Nb. modified sources: 1

- Nb. nopol ranking entries: 104

###  org.apache.commons.math.analysis.BrentSolver

```
130a131,132
>         double ret = Double.NaN;
>         
135c137,147
<         if (yMin * yMax >= 0) {
---
>         double sign = yMin * yMax;
>         if (sign > 0) {
>             // check if either value is close to a zero
>             if (Math.abs(yMin) <= functionValueAccuracy) {
>                 setResult(min, 0);
>                 ret = min;
>             } else if (Math.abs(yMax) <= functionValueAccuracy) {
>                 setResult(max, 0);
>                 ret = max;
>             } else {
>                 // neither value is close to zero and min and max do not bracket root.
141c153
< 
---
>         } else if (sign < 0){
143c155,163
<         return solve(min, yMin, max, yMax, min, yMin);
---
>             ret = solve(min, yMin, max, yMax, min, yMin);
>         } else {
>             // either min or max is a root
>             if (yMin == 0.0) {
>                 ret = min;
>             } else {
>                 ret = max;
>             }
>         }
144a165
>         return ret;
```

- Deleted lines: 6<br />
- Added lines: 25<br />
- Diff added/deleted: 19

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 135 | org.apache.commons.math.analysis.BrentSolver:135 -> 0.05892556509887897 (ep: 31, ef: 1, np: 1063, nf: 0) | 82 |
| 143 | org.apache.commons.math.analysis.BrentSolver:143 -> 0.061898446059017294 (ep: 28, ef: 1, np: 1066, nf: 0) | 71 |

- Nb. undetected lines: 3/5 ( 130 141 144 )

## Bug 98

- Nb. modified sources: 2

- Nb. nopol ranking entries: 122

###  org.apache.commons.math.linear.RealMatrixImpl

```
779c779
<         final double[] out = new double[v.length];
---
>         final double[] out = new double[nRows];
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 779 | org.apache.commons.math.linear.RealMatrixImpl:779 -> 0.18257418583505536 (ep: 2, ef: 1, np: 1090, nf: 1) | 74 |

- Nb. undetected lines: 0/1

###  org.apache.commons.math.linear.BigMatrixImpl

```
991c991
<         final BigDecimal[] out = new BigDecimal[v.length];
---
>         final BigDecimal[] out = new BigDecimal[nRows];
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 991 | org.apache.commons.math.linear.BigMatrixImpl:991 -> 0.18257418583505536 (ep: 2, ef: 1, np: 1090, nf: 1) | 63 |

- Nb. undetected lines: 0/1

## Bug 99

- Nb. modified sources: 1

- Nb. nopol ranking entries: 104

###  org.apache.commons.math.analysis.BrentSolver

```
130a131,132
>         double ret = Double.NaN;
>         
135c137,147
<         if (yMin * yMax >= 0) {
---
>         double sign = yMin * yMax;
>         if (sign > 0) {
>             // check if either value is close to a zero
>             if (Math.abs(yMin) <= functionValueAccuracy) {
>                 setResult(min, 0);
>                 ret = min;
>             } else if (Math.abs(yMax) <= functionValueAccuracy) {
>                 setResult(max, 0);
>                 ret = max;
>             } else {
>                 // neither value is close to zero and min and max do not bracket root.
141c153
< 
---
>         } else if (sign < 0){
143c155,163
<         return solve(min, yMin, max, yMax, min, yMin);
---
>             ret = solve(min, yMin, max, yMax, min, yMin);
>         } else {
>             // either min or max is a root
>             if (yMin == 0.0) {
>                 ret = min;
>             } else {
>                 ret = max;
>             }
>         }
144a165
>         return ret;
```

- Deleted lines: 6<br />
- Added lines: 25<br />
- Diff added/deleted: 19

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 135 | org.apache.commons.math.analysis.BrentSolver:135 -> 0.05892556509887897 (ep: 31, ef: 1, np: 1148, nf: 0) | 82 |
| 143 | org.apache.commons.math.analysis.BrentSolver:143 -> 0.061898446059017294 (ep: 28, ef: 1, np: 1151, nf: 0) | 71 |

- Nb. undetected lines: 3/5 ( 130 141 144 )

## Bug 100

- Nb. modified sources: 1

- Nb. nopol ranking entries: 112925

###  org.apache.commons.math.estimation.AbstractEstimator

```
166c166
<         final int cols = problem.getAllParameters().length;
---
>         final int cols = problem.getUnboundParameters().length;
202c202
<         int p = problem.getAllParameters().length;
---
>         int p = problem.getUnboundParameters().length;
207c207
<         double[] errors = new double[problem.getAllParameters().length];
---
>         double[] errors = new double[problem.getUnboundParameters().length];
```

- Deleted lines: 3<br />
- Added lines: 3<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 166 | org.apache.commons.math.estimation.AbstractEstimator:166 -> 0.19245008972987526 (ep: 2, ef: 1, np: 1176, nf: 0) | 68 |

- Nb. undetected lines: 2/3 ( 202 207 )

## Bug 101

- Nb. modified sources: 1

- Nb. nopol ranking entries: 65

###  org.apache.commons.math.complex.ComplexFormat

```
377c377,379
<         if (source.substring(startIndex, endIndex).compareTo(
---
>         if ((startIndex >= source.length()) ||
>             (endIndex > source.length()) ||
>             source.substring(startIndex, endIndex).compareTo(
```

- Deleted lines: 1<br />
- Added lines: 3<br />
- Diff added/deleted: 2


- Nb. undetected lines: 1/1 ( 377 )

## Bug 102

- Nb. modified sources: 1

- Nb. nopol ranking entries: 180

###  org.apache.commons.math.stat.inference.ChiSquareTestImpl

```
66,67d65
<         double sumSq = 0.0d;
<         double dev = 0.0d;
75a74,87
>         double sumExpected = 0d;
>         double sumObserved = 0d;
>         for (int i = 0; i < observed.length; i++) {
>             sumExpected += expected[i];
>             sumObserved += observed[i];
>         }
>         double ratio = 1.0d;
>         boolean rescale = false;
>         if (Math.abs(sumExpected - sumObserved) > 10E-6) {
>             ratio = sumObserved / sumExpected;
>             rescale = true;
>         }
>         double sumSq = 0.0d;
>         double dev = 0.0d;
76a89,92
>             if (rescale) {
>                 dev = ((double) observed[i] - ratio * expected[i]);
>                 sumSq += dev * dev / (ratio * expected[i]);
>             } else {
79a96
>         }
83a101,105
>      * {@inheritDoc}
>      * <p><strong>Note: </strong>This implementation rescales the 
>      * <code>expected</code> array if necessary to ensure that the sum of the
>      * expected and observed counts are equal.</p>
>      * 
```

- Deleted lines: 6<br />
- Added lines: 24<br />
- Diff added/deleted: 18

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 66 | org.apache.commons.math.stat.inference.ChiSquareTestImpl:66 -> 0.2710523708715754 (ep: 29, ef: 6, np: 1111, nf: 0) | 55 |
| 67 | org.apache.commons.math.stat.inference.ChiSquareTestImpl:67 -> 0.2710523708715754 (ep: 29, ef: 6, np: 1111, nf: 0) | 56 |
| 76 | org.apache.commons.math.stat.inference.ChiSquareTestImpl:76 -> 0.2710523708715754 (ep: 58, ef: 12, np: 1082, nf: -6) | 59 |

- Nb. undetected lines: 3/6 ( 75 79 83 )

## Bug 103

- Nb. modified sources: 1

- Nb. nopol ranking entries: 147

###  org.apache.commons.math.distribution.NormalDistributionImpl

```
104c104,106
<      * @throws MathException if the algorithm fails to converge.
---
>      * @throws MathException if the algorithm fails to converge; unless
>      * x is more than 20 standard deviations from the mean, in which case the
>      * convergence exception is caught and 0 or 1 is returned.
106a109
>         try {
108a112,120
>         } catch (MaxIterationsExceededException ex) {
>             if (x < (mean - 20 * standardDeviation)) { // JDK 1.5 blows at 38
>                 return 0.0d;
>             } else if (x > (mean + 20 * standardDeviation)) {
>                 return 1.0d;
>             } else {
>                 throw ex;
>             }
>         }
```

- Deleted lines: 2<br />
- Added lines: 13<br />
- Diff added/deleted: 11


- Nb. undetected lines: 3/3 ( 104 106 108 )

## Bug 104

- Nb. modified sources: 2

- Nb. nopol ranking entries: 123

###  org.apache.commons.math.special.Gamma

```
37c37
<     private static final double DEFAULT_EPSILON = 10e-9;
---
>     private static final double DEFAULT_EPSILON = 10e-15;
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0


- Nb. undetected lines: 1/1 ( 37 )

###  org.apache.commons.math.special.Beta

```
36c36
<     private static final double DEFAULT_EPSILON = 10e-9;
---
>     private static final double DEFAULT_EPSILON = 10e-15;
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0


- Nb. undetected lines: 1/1 ( 36 )

## Bug 105

- Nb. modified sources: 1

- Nb. nopol ranking entries: 84

###  org.apache.commons.math.stat.regression.SimpleRegression

```
264c264
<         return sumYY - sumXY * sumXY / sumXX;
---
>         return Math.max(0d, sumYY - sumXY * sumXY / sumXX);
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 264 | org.apache.commons.math.stat.regression.SimpleRegression:264 -> 0.1111111111111111 (ep: 8, ef: 1, np: 878, nf: 0) | 85 |

- Nb. undetected lines: 0/1

## Bug 106

- Nb. modified sources: 1

- Nb. nopol ranking entries: 89

###  org.apache.commons.math.fraction.ProperFractionFormat

```
164a165,170
>         if (num.intValue() < 0) {
>             // minus signs should be leading, invalid expression
>             pos.setIndex(initialIndex);
>             return null;
>         }
> 
197a204,209
>         if (den.intValue() < 0) {
>             // minus signs must be leading, invalid
>             pos.setIndex(initialIndex);
>             return null;
>         }
> 
```

- Deleted lines: 2<br />
- Added lines: 12<br />
- Diff added/deleted: 10


- Nb. undetected lines: 2/2 ( 164 197 )

