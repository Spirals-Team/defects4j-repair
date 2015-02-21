# Time - Nopol ranking

## Bug 1

- Nb. modified sources: 2

- Nb. nopol ranking entries: 139

###  org.joda.time.field.UnsupportedDurationField

```
227,229d226
<         if (durationField.isSupported()) {
<             return 1;
<         }
```

- Deleted lines: 3<br />
- Added lines: 0<br />
- Diff added/deleted: -3

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 227 | org.joda.time.field.UnsupportedDurationField:227 -> 0.29277002188455997 (ep: 18, ef: 3, np: 12106, nf: 1) | 4 |
| 228 | org.joda.time.field.UnsupportedDurationField:228 -> 0.29277002188455997 (ep: 18, ef: 3, np: 12106, nf: 1) | 5 |

- Nb. undetected lines: 1/3 ( 229 )

###  org.joda.time.Partial

```
216a217,225
>                 if (loopUnitField.isSupported() == false) {
>                     if (lastUnitField.isSupported()) {
>                         throw new IllegalArgumentException("Types array must be in order largest-smallest: " +
>                                         types[i - 1].getName() + " < " + loopType.getName());
>                     } else {
>                         throw new IllegalArgumentException("Types array must not contain duplicate unsupported: " +
>                                         types[i - 1].getName() + " and " + loopType.getName());
>                     }
>                 }
221c230
<                 } else if (compare == 0) {
---
>                 } else if (compare == 0 && lastUnitField.equals(loopUnitField)) {
```

- Deleted lines: 2<br />
- Added lines: 10<br />
- Diff added/deleted: 8

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 216 | org.joda.time.Partial:216 -> 0.06262242910851494 (ep: 456, ef: 3, np: 11668, nf: 1) | 29 |
| 221 | org.joda.time.Partial:221 -> 0.06523280730534423 (ep: 420, ef: 3, np: 11704, nf: 1) | 20 |

- Nb. undetected lines: 0/2

## Bug 2

- Nb. modified sources: 2

- Nb. nopol ranking entries: 148

###  org.joda.time.field.UnsupportedDurationField

```
226a227,229
>         if (durationField.isSupported()) {
>             return 1;
>         }
```

- Deleted lines: 0<br />
- Added lines: 3<br />
- Diff added/deleted: 3


- Nb. undetected lines: 1/1 ( 226 )

###  org.joda.time.Partial

```
218c218
<                 if (compare < 0 || (compare != 0 && loopUnitField.isSupported() == false)) {
---
>                 if (compare < 0) {
224c224,225
<                             throw new IllegalArgumentException("Types array must not contain duplicate: " + loopType.getName());
---
>                             throw new IllegalArgumentException("Types array must not contain duplicate: " +
>                                             types[i - 1].getName() + " and " + loopType.getName());
238c239,240
<                             throw new IllegalArgumentException("Types array must not contain duplicate: " + loopType.getName());
---
>                             throw new IllegalArgumentException("Types array must not contain duplicate: " +
>                                             types[i - 1].getName() + " and " + loopType.getName());
446a449,451
>                             if (fieldType.getRangeDurationType() == null) {
>                                 break;
>                             }
```

- Deleted lines: 4<br />
- Added lines: 8<br />
- Diff added/deleted: 4

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 218 | org.joda.time.Partial:218 -> 0.05976143046671969 (ep: 417, ef: 3, np: 11707, nf: 1) | 44 |
| 224 | org.joda.time.Partial:224 -> 0.5 (ep: 3, ef: 3, np: 12121, nf: 1) | 1 |

- Nb. undetected lines: 2/4 ( 238 446 )

## Bug 3

- Nb. modified sources: 1

- Nb. nopol ranking entries: 896

###  org.joda.time.MutableDateTime

```
638a639
>         if (amount != 0) {
640a642
>     }
659a662
>         if (years != 0) {
661a665
>     }
680a685
>         if (weekyears != 0) {
682a688
>     }
701a708
>         if (months != 0) {
703a711
>     }
722a731
>         if (weeks != 0) {
724a734
>     }
763a774
>         if (days != 0) {
765a777
>     }
784a797
>         if (hours != 0) {
786a800
>     }
815a830
>         if (minutes != 0) {
817a833
>     }
846a863
>         if (seconds != 0) {
848a866
>     }
879a898
>         if (millis != 0) {
881a901
>     }
```

- Deleted lines: 0<br />
- Added lines: 20<br />
- Diff added/deleted: 20

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 640 | org.joda.time.MutableDateTime:640 -> 0.242535625036333 (ep: 6, ef: 3, np: 12097, nf: 13) | 13 |
| 661 | org.joda.time.MutableDateTime:661 -> 0.242535625036333 (ep: 6, ef: 3, np: 12097, nf: 13) | 7 |
| 703 | org.joda.time.MutableDateTime:703 -> 0.242535625036333 (ep: 6, ef: 3, np: 12097, nf: 13) | 15 |
| 724 | org.joda.time.MutableDateTime:724 -> 0.242535625036333 (ep: 6, ef: 3, np: 12097, nf: 13) | 11 |
| 765 | org.joda.time.MutableDateTime:765 -> 0.242535625036333 (ep: 6, ef: 3, np: 12097, nf: 13) | 9 |
| 786 | org.joda.time.MutableDateTime:786 -> 0.5613608914238398 (ep: 27, ef: 15, np: 12076, nf: 1) | 2 |

- Nb. undetected lines: 14/20 ( 638 659 680 682 701 722 763 784 815 817 846 848 879 881 )

## Bug 4

- Nb. modified sources: 1

- Nb. nopol ranking entries: 156

###  org.joda.time.Partial

```
462,463c462,464
<             
<             Partial newPartial = new Partial(iChronology, newTypes, newValues);
---
>             // use public constructor to ensure full validation
>             // this isn't overly efficient, but is safe
>             Partial newPartial = new Partial(newTypes, newValues, iChronology);
```

- Deleted lines: 2<br />
- Added lines: 3<br />
- Diff added/deleted: 1

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 463 | org.joda.time.Partial:463 -> 0.15491933384829668 (ep: 72, ef: 3, np: 11971, nf: 1) | 30 |

- Nb. undetected lines: 1/2 ( 462 )

## Bug 5

- Nb. modified sources: 1

- Nb. nopol ranking entries: 241

###  org.joda.time.Period

```
1616a1617
>         type = DateTimeUtils.getPeriodType(type);
1623c1624
<         Period result = new Period(millis, DateTimeUtils.getPeriodType(type), ISOChronology.getInstanceUTC());
---
>         Period result = new Period(millis, type, ISOChronology.getInstanceUTC());
1627,1630c1628,1632
<             years = FieldUtils.safeAdd(years, months / 12);
<             months = months % 12;
<             if (years != 0) {
<                 result = result.withYears(years);
---
>             long totalMonths = years * 12L + months;
>             if (type.isSupported(DurationFieldType.YEARS_TYPE)) {
>                 int normalizedYears = FieldUtils.safeToInt(totalMonths / 12);
>                 result = result.withYears(normalizedYears);
>                 totalMonths = totalMonths - (normalizedYears * 12);
1632,1633c1634,1640
<             if (months != 0) {
<                 result = result.withMonths(months);
---
>             if (type.isSupported(DurationFieldType.MONTHS_TYPE)) {
>                 int normalizedMonths = FieldUtils.safeToInt(totalMonths);
>                 result = result.withMonths(normalizedMonths);
>                 totalMonths = totalMonths - normalizedMonths;
>             }
>             if (totalMonths != 0) {
>                 throw new UnsupportedOperationException("Unable to normalize as PeriodType is missing either years or months but period has a month/year amount: " + toString());
```

- Deleted lines: 7<br />
- Added lines: 14<br />
- Diff added/deleted: 7

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 1623 | org.joda.time.Period:1623 -> 0.34188172937891387 (ep: 54, ef: 9, np: 11980, nf: 1) | 20 |
| 1627 | org.joda.time.Period:1627 -> 0.41871789467931186 (ep: 33, ef: 9, np: 12001, nf: 1) | 7 |
| 1628 | org.joda.time.Period:1628 -> 0.45226701686664544 (ep: 27, ef: 9, np: 12007, nf: 1) | 5 |
| 1629 | org.joda.time.Period:1629 -> 0.45226701686664544 (ep: 27, ef: 9, np: 12007, nf: 1) | 6 |
| 1630 | org.joda.time.Period:1630 -> 0.4723774929733302 (ep: 24, ef: 9, np: 12010, nf: 1) | 2 |

- Nb. undetected lines: 3/8 ( 1616 1632 1633 )

## Bug 6

- Nb. modified sources: 1

- Nb. nopol ranking entries: 721

###  org.joda.time.chrono.GJChronology

```
195a196,199
>             LocalDate cutoverDate = new LocalDate(cutoverInstant.getMillis(), GregorianChronology.getInstance(zone));
>             if (cutoverDate.getYear() <= 0) {
>                 throw new IllegalArgumentException("Cutover too early. Must be on or after 0001-01-01.");
>             }
978a983,993
>                         if (iConvertByWeekyear) {
>                             int wyear = iGregorianChronology.weekyear().get(instant);
>                             if (wyear <= 0) {
>                                 instant = iGregorianChronology.weekyear().add(instant, -1);
>                             }
>                         } else {
>                             int year = iGregorianChronology.year().get(instant);
>                             if (year <= 0) {
>                                 instant = iGregorianChronology.year().add(instant, -1);
>                             }
>                         }
1000a1016,1026
>                         if (iConvertByWeekyear) {
>                             int wyear = iGregorianChronology.weekyear().get(instant);
>                             if (wyear <= 0) {
>                                 instant = iGregorianChronology.weekyear().add(instant, -1);
>                             }
>                         } else {
>                             int year = iGregorianChronology.year().get(instant);
>                             if (year <= 0) {
>                                 instant = iGregorianChronology.year().add(instant, -1);
>                             }
>                         }
```

- Deleted lines: 5<br />
- Added lines: 26<br />
- Diff added/deleted: 21

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 195 | org.joda.time.chrono.GJChronology:195 -> 0.05163212931161357 (ep: 208, ef: 3, np: 11775, nf: 13) | 336 |

- Nb. undetected lines: 2/3 ( 978 1000 )

## Bug 7

- Nb. modified sources: 1

- Nb. nopol ranking entries: 474

###  org.joda.time.format.DateTimeFormatter

```
707a708
>         int defaultYear = DateTimeUtils.getChronology(chrono).year().get(instantMillis);
712c713
<             instantLocal, chrono, iLocale, iPivotYear, chrono.year().get(instantLocal));
---
>             instantLocal, chrono, iLocale, iPivotYear, defaultYear);
```

- Deleted lines: 1<br />
- Added lines: 2<br />
- Diff added/deleted: 1

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 707 | org.joda.time.format.DateTimeFormatter:707 -> 0.2618614682831909 (ep: 69, ef: 6, np: 11869, nf: 1) | 13 |

- Nb. undetected lines: 1/2 ( 712 )

## Bug 8

- Nb. modified sources: 1

- Nb. nopol ranking entries: 197

###  org.joda.time.DateTimeZone

```
279c279
<         if (minutesOffset < 0 || minutesOffset > 59) {
---
>         if (minutesOffset < -59 || minutesOffset > 59) {
281a282,284
>         if (hoursOffset > 0 && minutesOffset < 0) {
>             throw new IllegalArgumentException("Positive hours must not have negative minutes: " + minutesOffset);
>         }
286c289
<                 minutesOffset = hoursInMinutes - minutesOffset;
---
>                 minutesOffset = hoursInMinutes - Math.abs(minutesOffset);
```

- Deleted lines: 4<br />
- Added lines: 6<br />
- Diff added/deleted: 2

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 279 | org.joda.time.DateTimeZone:279 -> 0.19205531989934396 (ep: 58, ef: 3, np: 11853, nf: 1) | 21 |

- Nb. undetected lines: 2/3 ( 281 286 )

## Bug 9

- Nb. modified sources: 1

- Nb. nopol ranking entries: 198

###  org.joda.time.DateTimeZone

```
35d34
< import org.joda.time.format.DateTimeFormat;
95a95,96
>     /** Maximum offset. */
>     private static final int MAX_MILLIS = (86400 * 1000) - 1;
256a258,260
>         if (hoursOffset < -23 || hoursOffset > 23) {
>             throw new IllegalArgumentException("Hours out of range: " + hoursOffset);
>         }
262c266
<             int hoursInMinutes = FieldUtils.safeMultiply(hoursOffset, 60);
---
>             int hoursInMinutes = hoursOffset * 60;
264c268
<                 minutesOffset = FieldUtils.safeAdd(hoursInMinutes, -minutesOffset);
---
>                 minutesOffset = hoursInMinutes - minutesOffset;
266c270
<                 minutesOffset = FieldUtils.safeAdd(hoursInMinutes, minutesOffset);
---
>                 minutesOffset = hoursInMinutes + minutesOffset;
278c282
<      * @param millisOffset  the offset in millis from UTC
---
>      * @param millisOffset  the offset in millis from UTC, from -23:59:59.999 to +23:59:59.999
281a286,288
>         if (millisOffset < -MAX_MILLIS || millisOffset > MAX_MILLIS) {
>             throw new IllegalArgumentException("Millis out of range: " + millisOffset);
>         }
```

- Deleted lines: 7<br />
- Added lines: 12<br />
- Diff added/deleted: 5

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 35 | org.joda.time.DateTimeZone:358 -> 0.14301938838683884 (ep: 107, ef: 3, np: 11804, nf: 1) | 34 |
| 262 | org.joda.time.DateTimeZone:262 -> 0.19205531989934396 (ep: 58, ef: 3, np: 11853, nf: 1) | 22 |
| 264 | org.joda.time.DateTimeZone:264 -> 0.3535533905932738 (ep: 15, ef: 3, np: 11896, nf: 1) | 3 |
| 266 | org.joda.time.DateTimeZone:266 -> 0.21428571428571427 (ep: 46, ef: 3, np: 11865, nf: 1) | 18 |

- Nb. undetected lines: 4/8 ( 95 256 278 281 )

## Bug 10

- Nb. modified sources: 1

- Nb. nopol ranking entries: 456

###  org.joda.time.base.BaseSingleFieldPeriod

```
50a51,52
>     /** The start of 1972. */
>     private static final long START_1972 = 2L * 365L * 86400L * 1000L;
103c105
<         int[] values = chrono.get(zeroInstance, chrono.set(start, 0L), chrono.set(end, 0L));
---
>         int[] values = chrono.get(zeroInstance, chrono.set(start, START_1972), chrono.set(end, START_1972));
```

- Deleted lines: 1<br />
- Added lines: 3<br />
- Diff added/deleted: 2

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 103 | org.joda.time.base.BaseSingleFieldPeriod:103 -> 0.3779644730092272 (ep: 30, ef: 6, np: 11830, nf: 1) | 12 |

- Nb. undetected lines: 1/2 ( 50 )

## Bug 11

- Nb. modified sources: 1

- Nb. nopol ranking entries: 495

###  org.joda.time.tz.ZoneInfoCompiler

```
68,70c68,70
<     static ThreadLocal<Boolean> cVerbose = new ThreadLocal<Boolean>();
<     static {
<         cVerbose.set(Boolean.FALSE);
---
>     static ThreadLocal<Boolean> cVerbose = new ThreadLocal<Boolean>() {
>         protected Boolean initialValue() {
>             return Boolean.FALSE;
71a72
>     };
```

- Deleted lines: 4<br />
- Added lines: 5<br />
- Diff added/deleted: 1


- Nb. undetected lines: 4/4 ( 68 69 70 71 )

## Bug 12

- Nb. modified sources: 2

- Nb. nopol ranking entries: 318

###  org.joda.time.LocalDateTime

```
198a199,200
>         int era = calendar.get(Calendar.ERA);
>         int yearOfEra = calendar.get(Calendar.YEAR);
200c202
<             calendar.get(Calendar.YEAR),
---
>             (era == GregorianCalendar.AD ? yearOfEra : 1 - yearOfEra),
234a237,242
>         if (date.getTime() < 0) {
>             // handle years in era BC
>             GregorianCalendar cal = new GregorianCalendar();
>             cal.setTime(date);
>             return fromCalendarFields(cal);
>         }
```

- Deleted lines: 2<br />
- Added lines: 9<br />
- Diff added/deleted: 7


- Nb. undetected lines: 3/3 ( 198 200 234 )

###  org.joda.time.LocalDate

```
209a210,211
>         int era = calendar.get(Calendar.ERA);
>         int yearOfEra = calendar.get(Calendar.YEAR);
211c213
<             calendar.get(Calendar.YEAR),
---
>             (era == GregorianCalendar.AD ? yearOfEra : 1 - yearOfEra),
241a244,249
>         if (date.getTime() < 0) {
>             // handle years in era BC
>             GregorianCalendar cal = new GregorianCalendar();
>             cal.setTime(date);
>             return fromCalendarFields(cal);
>         }
```

- Deleted lines: 2<br />
- Added lines: 9<br />
- Diff added/deleted: 7


- Nb. undetected lines: 3/3 ( 209 211 241 )

## Bug 13

- Nb. modified sources: 1

- Nb. nopol ranking entries: 243

###  org.joda.time.format.PeriodFormatterBuilder

```
1097,1098c1097,1098
<                 // the minimum output is 0.000, which is 4 digits
<                 sum = Math.max(sum, 4);
---
>                 // the minimum output is 0.000, which is 4 or 5 digits with a negative
>                 sum = (valueLong < 0 ? Math.max(sum, 5) : Math.max(sum, 4));
1132a1133
>             int bufLen = buf.length();
1141a1143,1145
>                     if (valueLong < 0 && valueLong > -DateTimeConstants.MILLIS_PER_SECOND) {
>                         buf.insert(bufLen, '-');
>                     }
```

- Deleted lines: 4<br />
- Added lines: 6<br />
- Diff added/deleted: 2


- Nb. undetected lines: 4/4 ( 1097 1098 1132 1141 )

## Bug 14

- Nb. modified sources: 1

- Nb. nopol ranking entries: 491

###  org.joda.time.chrono.BasicMonthOfYearDateTimeField

```
208a209,214
>         if (partial.size() > 0 && partial.getFieldType(0).equals(DateTimeFieldType.monthOfYear()) && fieldIndex == 0) {
>             // month is largest field and being added to, such as month-day
>             int curMonth0 = partial.getValue(0) - 1;
>             int newMonth = ((curMonth0 + (valueToAdd % 12) + 12) % 12) + 1;
>             return set(partial, 0, values, newMonth);
>         }
```

- Deleted lines: 0<br />
- Added lines: 6<br />
- Diff added/deleted: 6


- Nb. undetected lines: 1/1 ( 208 )

## Bug 15

- Nb. modified sources: 1

- Nb. nopol ranking entries: 143

###  org.joda.time.field.FieldUtils

```
121,122c121
<             throw new ArithmeticException
<                 ("The calculation caused an overflow: " + val1 + " * " + val2);
---
>           throw new ArithmeticException("Multiplication overflows an int: " + val1 + " * " + val2);
131c130
<      * @param scalar  the second value
---
>      * @param val2  the second value
136,137c135,136
<     public static long safeMultiply(long val1, int scalar) {
<         switch (scalar) {
---
>     public static long safeMultiply(long val1, int val2) {
>         switch (val2) {
138a138,140
>                 if (val1 == Long.MIN_VALUE) {
>                     throw new ArithmeticException("Multiplication overflows a long: " + val1 + " * " + val2);
>                 }
145,148c147,149
<         long total = val1 * scalar;
<         if (total / scalar != val1) {
<             throw new ArithmeticException
<                 ("The calculation caused an overflow: " + val1 + " * " + scalar);
---
>         long total = val1 * val2;
>         if (total / val2 != val1) {
>           throw new ArithmeticException("Multiplication overflows a long: " + val1 + " * " + val2);
```

- Deleted lines: 9<br />
- Added lines: 10<br />
- Diff added/deleted: 1

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 137 | org.joda.time.field.FieldUtils:137 -> 0.09078412990032037 (ep: 153, ef: 3, np: 11527, nf: 4) | 25 |
| 145 | org.joda.time.field.FieldUtils:145 -> 0.12598815766974242 (ep: 78, ef: 3, np: 11602, nf: 4) | 22 |
| 146 | org.joda.time.field.FieldUtils:146 -> 0.12598815766974242 (ep: 78, ef: 3, np: 11602, nf: 4) | 23 |

- Nb. undetected lines: 7/10 ( 121 122 131 136 138 147 148 )

## Bug 16

- Nb. modified sources: 1

- Nb. nopol ranking entries: 879

###  org.joda.time.format.DateTimeFormatter

```
709c709
<             instantLocal, chrono, iLocale, iPivotYear, iDefaultYear);
---
>             instantLocal, chrono, iLocale, iPivotYear, chrono.year().get(instantLocal));
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0


- Nb. undetected lines: 1/1 ( 709 )

## Bug 17

- Nb. modified sources: 1

- Nb. nopol ranking entries: 442

###  org.joda.time.DateTimeZone

```
1164,1167c1164,1191
<         long before = convertUTCToLocal(instant - 3 * DateTimeConstants.MILLIS_PER_HOUR);
<         long after = convertUTCToLocal(instant + 3 * DateTimeConstants.MILLIS_PER_HOUR);
<         if (before == after) {
<             return instant;
---
>         // a bit messy, but will work in all non-pathological cases
>         
>         // evaluate 3 hours before and after to work out if anything is happening
>         long instantBefore = instant - 3 * DateTimeConstants.MILLIS_PER_HOUR;
>         long instantAfter = instant + 3 * DateTimeConstants.MILLIS_PER_HOUR;
>         long offsetBefore = getOffset(instantBefore);
>         long offsetAfter = getOffset(instantAfter);
>         if (offsetBefore <= offsetAfter) {
>             return instant;  // not an overlap (less than is a gap, equal is normal case)
>         }
>         
>         // work out range of instants that have duplicate local times
>         long diff = offsetBefore - offsetAfter;
>         long transition = nextTransition(instantBefore);
>         long overlapStart = transition - diff;
>         long overlapEnd = transition + diff;
>         if (instant < overlapStart || instant >= overlapEnd) {
>           return instant;  // not an overlap
>         }
>         
>         // calculate result
>         long afterStart = instant - overlapStart;
>         if (afterStart >= diff) {
>           // currently in later offset
>           return earlierOrLater ? instant : instant - diff;
>         } else {
>           // currently in earlier offset
>           return earlierOrLater ? instant + diff : instant;
1169,1170d1192
<         long local = convertUTCToLocal(instant);
<         return convertLocalToUTC(local, false, earlierOrLater ? after : before);
1171a1194
> //    System.out.println(new DateTime(transitionStart, DateTimeZone.UTC) + " " + new DateTime(transitionStart, this));
```

- Deleted lines: 8<br />
- Added lines: 29<br />
- Diff added/deleted: 21

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 1164 | org.joda.time.DateTimeZone:1164 -> 0.3779644730092272 (ep: 6, ef: 3, np: 11641, nf: 4) | 5 |
| 1165 | org.joda.time.DateTimeZone:1165 -> 0.3779644730092272 (ep: 6, ef: 3, np: 11641, nf: 4) | 6 |
| 1166 | org.joda.time.DateTimeZone:1166 -> 0.3779644730092272 (ep: 6, ef: 3, np: 11641, nf: 4) | 7 |
| 1169 | org.joda.time.DateTimeZone:1169 -> 0.3779644730092272 (ep: 6, ef: 3, np: 11641, nf: 4) | 8 |
| 1170 | org.joda.time.DateTimeZone:1170 -> 0.3779644730092272 (ep: 6, ef: 3, np: 11641, nf: 4) | 9 |

- Nb. undetected lines: 2/7 ( 1167 1171 )

## Bug 18

- Nb. modified sources: 1

- Nb. nopol ranking entries: 233

###  org.joda.time.chrono.GJChronology

```
363c363,365
<         long instant = iGregorianChronology.getDateTimeMillis
---
>         long instant;
>         try {
>             instant = iGregorianChronology.getDateTimeMillis
365a368,378
>         } catch (IllegalFieldValueException ex) {
>             if (monthOfYear != 2 || dayOfMonth != 29) {
>                 throw ex;
>             }
>             instant = iGregorianChronology.getDateTimeMillis
>                 (year, monthOfYear, 28,
>                  hourOfDay, minuteOfHour, secondOfMinute, millisOfSecond);
>             if (instant >= iCutoverMillis) {
>                 throw ex;
>             }
>         }
```

- Deleted lines: 1<br />
- Added lines: 14<br />
- Diff added/deleted: 13

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 363 | org.joda.time.chrono.GJChronology:363 -> 0.15018785229652767 (ep: 54, ef: 3, np: 11563, nf: 4) | 16 |

- Nb. undetected lines: 1/2 ( 365 )

## Bug 19

- Nb. modified sources: 1

- Nb. nopol ranking entries: 517

###  org.joda.time.DateTimeZone

```
900c900
<         } else if (offsetLocal > 0) {
---
>         } else if (offsetLocal >= 0) {
```

- Deleted lines: 1<br />
- Added lines: 2<br />
- Diff added/deleted: 1

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 900 | org.joda.time.DateTimeZone:900 -> 0.02451697264152958 (ep: 2136, ef: 3, np: 9475, nf: 4) | 297 |

- Nb. undetected lines: 0/1

## Bug 20

- Nb. modified sources: 1

- Nb. nopol ranking entries: 946

###  org.joda.time.format.DateTimeFormatterBuilder

```
2541a2542
>             String best = null;
2544,2545c2545,2546
<                     bucket.setZone(DateTimeZone.forID(id));
<                     return position + id.length();
---
>                 	if (best == null || id.length() > best.length()) {
>                 		best = id;
2547a2549,2553
>             }
>             if (best != null) {
>                 bucket.setZone(DateTimeZone.forID(best));
>                 return position + best.length();
>             }
```

- Deleted lines: 2<br />
- Added lines: 8<br />
- Diff added/deleted: 6


- Nb. undetected lines: 4/4 ( 2541 2544 2545 2547 )

## Bug 21

- Nb. modified sources: 1

- Nb. nopol ranking entries: 479

###  org.joda.time.tz.DefaultNameProvider

```
65,69c65,84
<             String[][] zoneStrings = DateTimeUtils.getDateFormatSymbols(locale).getZoneStrings();
<             for (int i=0; i<zoneStrings.length; i++) {
<                 String[] set = zoneStrings[i];
<                 if (set != null && set.length == 5 && id.equals(set[0])) {
<                     byNameKeyCache.put(set[2], new String[] {set[2], set[1]});
---
>             
>             String[][] zoneStringsEn = DateTimeUtils.getDateFormatSymbols(Locale.ENGLISH).getZoneStrings();
>             String[] setEn = null;
>             for (String[] strings : zoneStringsEn) {
>               if (strings != null && strings.length == 5 && id.equals(strings[0])) {
>                 setEn = strings;
>                 break;
>               }
>             }
>             String[][] zoneStringsLoc = DateTimeUtils.getDateFormatSymbols(locale).getZoneStrings();
>             String[] setLoc = null;
>             for (String[] strings : zoneStringsLoc) {
>               if (strings != null && strings.length == 5 && id.equals(strings[0])) {
>                 setLoc = strings;
>                 break;
>               }
>             }
>             
>             if (setEn != null && setLoc != null) {
>               byNameKeyCache.put(setEn[2], new String[] {setLoc[2], setLoc[1]});
73,74c88,89
<                     if (set[2].equals(set[4])) {
<                         byNameKeyCache.put(set[4] + "-Summer", new String[] {set[4], set[3]});
---
>               if (setEn[2].equals(setEn[4])) {
>                   byNameKeyCache.put(setEn[4] + "-Summer", new String[] {setLoc[4], setLoc[3]});
76c91
<                         byNameKeyCache.put(set[4], new String[] {set[4], set[3]});
---
>                   byNameKeyCache.put(setEn[4], new String[] {setLoc[4], setLoc[3]});
78d92
<                     break;
81,83c95
<         }
< 
<         return (String[])byNameKeyCache.get(nameKey);
---
>         return (String[]) byNameKeyCache.get(nameKey);
```

- Deleted lines: 12<br />
- Added lines: 24<br />
- Diff added/deleted: 12


- Nb. undetected lines: 12/12 ( 65 66 67 68 69 73 74 76 78 81 82 83 )

## Bug 22

- Nb. modified sources: 3

- Nb. nopol ranking entries: 784

###  org.joda.time.Period

```
382c382
<         super(duration, null, null);
---
>         super(duration);
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 382 | org.joda.time.Period:382 -> 0.10830607221477646 (ep: 93, ef: 6, np: 11411, nf: 25) | 208 |

- Nb. undetected lines: 0/1

###  org.joda.time.MutablePeriod

```
180c180
<         super(duration, null, null);
---
>         super(duration);
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0


- Nb. undetected lines: 1/1 ( 180 )

###  org.joda.time.base.BasePeriod

```
213a214,231
>      * Creates a period from the given millisecond duration with the standard period type
>      * and ISO rules, ensuring that the calculation is performed with the time-only period type.
>      * <p>
>      * The calculation uses the hour, minute, second and millisecond fields.
>      *
>      * @param duration  the duration, in milliseconds
>      */
>     protected BasePeriod(long duration) {
>         super();
>         // bug [3264409]
>         iType = PeriodType.time();
>         int[] values = ISOChronology.getInstanceUTC().get(this, duration);
>         iType = PeriodType.standard();
>         iValues = new int[8];
>         System.arraycopy(values, 0, iValues, 4, 4);
>     }
> 
>     /**
```

- Deleted lines: 1<br />
- Added lines: 18<br />
- Diff added/deleted: 17


- Nb. undetected lines: 1/1 ( 213 )

## Bug 23

- Nb. modified sources: 1

- Nb. nopol ranking entries: 735

###  org.joda.time.DateTimeZone

```
563a564,568
>             map.put("WET", "WET");
>             map.put("CET", "CET");
>             map.put("MET", "CET");
>             map.put("ECT", "CET");
>             map.put("EET", "EET");
565c570
<             map.put("HST", "Pacific/Honolulu");
---
>             map.put("HST", "Pacific/Honolulu");  // JDK 1.1 compatible
568c573
<             map.put("MST", "America/Denver");
---
>             map.put("MST", "America/Denver");  // JDK 1.1 compatible
571,572c576,577
<             map.put("EST", "America/New_York");
<             map.put("IET", "America/Indianapolis");
---
>             map.put("EST", "America/New_York");  // JDK 1.1 compatible
>             map.put("IET", "America/Indiana/Indianapolis");
575c580
<             map.put("AGT", "America/Buenos_Aires");
---
>             map.put("AGT", "America/Argentina/Buenos_Aires");
577,578d581
<             map.put("WET", "Europe/London");
<             map.put("ECT", "Europe/Paris");
581d583
<             map.put("EET", "Europe/Bucharest");
583d584
<             map.put("MET", "Asia/Tehran");
586c587
<             map.put("IST", "Asia/Calcutta");
---
>             map.put("IST", "Asia/Kolkata");
588c589
<             map.put("VST", "Asia/Saigon");
---
>             map.put("VST", "Asia/Ho_Chi_Minh");
```

- Deleted lines: 11<br />
- Added lines: 12<br />
- Diff added/deleted: 1


- Nb. undetected lines: 12/12 ( 563 565 568 571 572 575 577 578 581 583 586 588 )

## Bug 24

- Nb. modified sources: 1

- Nb. nopol ranking entries: 1087

###  org.joda.time.format.DateTimeParserBucket

```
354a355,359
>             if (resetFields) {
>                 for (int i = 0; i < count; i++) {
>                     millis = savedFields[i].set(millis, i == (count - 1));
>                 }
>             }
```

- Deleted lines: 1<br />
- Added lines: 5<br />
- Diff added/deleted: 4


- Nb. undetected lines: 1/1 ( 354 )

## Bug 25

- Nb. modified sources: 1

- Nb. nopol ranking entries: 848

###  org.joda.time.DateTimeZone

```
869,870c869,874
<      * NOTE: The behaviour of this method changed in v1.5, with the emphasis
<      * on returning a consistent result later along the time-line (shown above).
---
>      * During a DST overlap (where the local time is ambiguous) this method will return
>      * the earlier instant. The combination of these two rules is to always favour
>      * daylight (summer) time over standard (winter) time.
>      * <p>
>      * NOTE: Prior to v2.0, the DST overlap behaviour was not defined and varied by hemisphere.
>      * Prior to v1.5, the DST gap behaviour was also not defined.
872,873c876
<      * @param instantLocal  the millisecond instant, relative to this time zone, to
<      * get the offset for
---
>      * @param instantLocal  the millisecond instant, relative to this time zone, to get the offset for
878c881
<         int offsetLocal = getOffset(instantLocal);
---
>         final int offsetLocal = getOffset(instantLocal);
880c883,884
<         int offsetAdjusted = getOffset(instantLocal - offsetLocal);
---
>         final long instantAdjusted = instantLocal - offsetLocal;
>         final int offsetAdjusted = getOffset(instantAdjusted);
889c893
<                 long nextLocal = nextTransition(instantLocal - offsetLocal);
---
>                 long nextLocal = nextTransition(instantAdjusted);
894a899,907
>         } else if (offsetLocal > 0) {
>             long prev = previousTransition(instantAdjusted);
>             if (prev < instantAdjusted) {
>                 int offsetPrev = getOffset(prev);
>                 int diff = offsetPrev - offsetLocal;
>                 if (instantAdjusted - prev <= diff) {
>                     return offsetPrev;
>                 }
>             }
```

- Deleted lines: 10<br />
- Added lines: 20<br />
- Diff added/deleted: 10

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 878 | org.joda.time.DateTimeZone:878 -> 0.0332567803013923 (ep: 2145, ef: 9, np: 9296, nf: 25) | 606 |
| 880 | org.joda.time.DateTimeZone:880 -> 0.0332567803013923 (ep: 2145, ef: 9, np: 9296, nf: 25) | 607 |
| 889 | org.joda.time.DateTimeZone:889 -> 0.06193801042615005 (ep: 66, ef: 3, np: 11375, nf: 31) | 389 |

- Nb. undetected lines: 5/8 ( 869 870 872 873 894 )

## Bug 26

- Nb. modified sources: 2

- Nb. nopol ranking entries: 1529

###  org.joda.time.field.LenientDateTimeField

```
75c75
<         return iBase.getZone().convertLocalToUTC(localInstant, false);
---
>         return iBase.getZone().convertLocalToUTC(localInstant, false, instant);
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0


- Nb. undetected lines: 1/1 ( 75 )

###  org.joda.time.chrono.ZonedChronology

```
436c436
<                return iZone.convertLocalToUTC(localInstant, false);
---
>                return iZone.convertLocalToUTC(localInstant, false, instant);
448c448
<                return iZone.convertLocalToUTC(localInstant, false);
---
>                return iZone.convertLocalToUTC(localInstant, false, instant);
460c460
<                 return iZone.convertLocalToUTC(localInstant, false);
---
>                 return iZone.convertLocalToUTC(localInstant, false, instant);
467c467
<             long result = iZone.convertLocalToUTC(localInstant, false);
---
>             long result = iZone.convertLocalToUTC(localInstant, false, instant);
481c481
<             return iZone.convertLocalToUTC(localInstant, false);
---
>             return iZone.convertLocalToUTC(localInstant, false, instant);
528c528
<                 return iZone.convertLocalToUTC(localInstant, false);
---
>                 return iZone.convertLocalToUTC(localInstant, false, instant);
540c540
<                 return iZone.convertLocalToUTC(localInstant, false);
---
>                 return iZone.convertLocalToUTC(localInstant, false, instant);
```

- Deleted lines: 7<br />
- Added lines: 7<br />
- Diff added/deleted: 0


- Nb. undetected lines: 7/7 ( 436 448 460 467 481 528 540 )

## Bug 27

- Nb. modified sources: 1

- Nb. nopol ranking entries: 1430

###  org.joda.time.format.PeriodFormatterBuilder

```
800a801
>             if (sep.iAfterParser == null && sep.iAfterPrinter == null) {
804a806
>         }
```

- Deleted lines: 0<br />
- Added lines: 2<br />
- Diff added/deleted: 2

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 800 | org.joda.time.format.PeriodFormatterBuilder:800 -> 0.0657793514480272 (ep: 23, ef: 3, np: 11185, nf: 81) | 624 |

- Nb. undetected lines: 1/2 ( 804 )

