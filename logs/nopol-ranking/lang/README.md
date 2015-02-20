# Lang - Nopol ranking

## Bug 1

- Nb. modified sources: 1

- Nb. nopol ranking entries: 89

###  org.apache.commons.lang3.math.NumberUtils

```
466a467,475
>             char firstSigDigit = 0; // strip leading zeroes
>             for(int i = pfxLen; i < str.length(); i++) {
>                 firstSigDigit = str.charAt(i);
>                 if (firstSigDigit == '0') { // count leading zeroes
>                     pfxLen++;
>                 } else {
>                     break;
>                 }
>             }
468c477
<             if (hexDigits > 16) { // too many for Long
---
>             if (hexDigits > 16 || (hexDigits == 16 && firstSigDigit > '7')) { // too many for Long
471c480
<             if (hexDigits > 8) { // too many for an int
---
>             if (hexDigits > 8 || (hexDigits == 8 && firstSigDigit > '7')) { // too many for an int
```

- Deleted lines: 3<br />
- Added lines: 13<br />
- Diff added/deleted: 10

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 466 | org.apache.commons.lang3.math.NumberUtils:466 -> 0.055048188256318034 (ep: 9, ef: 1, np: 2251, nf: 30) | 65 |
| 468 | org.apache.commons.lang3.math.NumberUtils:468 -> 0.08703882797784893 (ep: 3, ef: 1, np: 2257, nf: 30) | 40 |
| 471 | org.apache.commons.lang3.math.NumberUtils:471 -> 0.08703882797784893 (ep: 3, ef: 1, np: 2257, nf: 30) | 41 |

- Nb. undetected lines: 0/3

## Bug 2

- Nb. modified sources: 1

- Nb. nopol ranking entries: 92

###  org.apache.commons.lang3.LocaleUtils

```
91a92,94
>         if (str.contains("#")) { // LANG-879 - Cannot handle Java 7 script & extensions
>             throw new IllegalArgumentException("Invalid locale format: " + str);
>         }
```

- Deleted lines: 0<br />
- Added lines: 3<br />
- Diff added/deleted: 3


- Nb. undetected lines: 1/1 ( 91 )

## Bug 3

- Nb. modified sources: 1

- Nb. nopol ranking entries: 106

###  org.apache.commons.lang3.math.NumberUtils

```
484a485
>         int numDecimals = 0; // Check required precision (LANG-693)
495a497
>             numDecimals = dec.length(); // gets number of digits past the decimal to ensure no loss of precision for floating point numbers.
590a593
>             if(numDecimals <= 7){// If number has 7 or fewer digits past the decimal point then make it a float
594a598
>             }
598a603
>             if(numDecimals <= 16){// If number has between 8 and 16 digits past the decimal point then make it a double
602a608
>             }
```

- Deleted lines: 2<br />
- Added lines: 6<br />
- Diff added/deleted: 4

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 495 | org.apache.commons.lang3.math.NumberUtils:495 -> 0.0778498944161523 (ep: 4, ef: 1, np: 2251, nf: 30) | 43 |

- Nb. undetected lines: 5/6 ( 484 590 594 598 602 )

## Bug 4

- Nb. modified sources: 1

- Nb. nopol ranking entries: 95

###  org.apache.commons.lang3.text.translate.LookupTranslator

```
26,29d25
<  * NOTE: This class is broken for any CharSequence implementation that does not define 
<  *       equals(Object) and hashCode() methods as the class uses the CharSequence as 
<  *       the key to a HashMap. See http://issues.apache.org/jira/browse/LANG-882.
<  * 
35c31
<     private final HashMap<CharSequence, CharSequence> lookupMap;
---
>     private final HashMap<String, CharSequence> lookupMap;
41a38,42
>      * Note that, as of Lang 3.1, the key to the lookup table is converted to a 
>      * java.lang.String, while the value remains as a java.lang.CharSequence. 
>      * This is because we need the key to support hashCode and equals(Object), 
>      * allowing it to be the key for a HashMap. See LANG-882.
>      *
45c46
<         lookupMap = new HashMap<CharSequence, CharSequence>();
---
>         lookupMap = new HashMap<String, CharSequence>();
50c51
<                 this.lookupMap.put(seq[0], seq[1]);
---
>                 this.lookupMap.put(seq[0].toString(), seq[1]);
76c77
<             final CharSequence result = lookupMap.get(subSeq);
---
>             final CharSequence result = lookupMap.get(subSeq.toString());
```

- Deleted lines: 10<br />
- Added lines: 11<br />
- Diff added/deleted: 1

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 45 | org.apache.commons.lang3.text.translate.LookupTranslator:45 -> 0.10050378152592121 (ep: 2, ef: 1, np: 2252, nf: 30) | 35 |
| 50 | org.apache.commons.lang3.text.translate.LookupTranslator:50 -> 0.10050378152592121 (ep: 2, ef: 1, np: 2252, nf: 30) | 40 |
| 76 | org.apache.commons.lang3.text.translate.LookupTranslator:76 -> 0.034815531191139566 (ep: 24, ef: 1, np: 2230, nf: 30) | 91 |

- Nb. undetected lines: 6/9 ( 26 27 28 29 35 41 )

## Bug 5

- Nb. modified sources: 1

- Nb. nopol ranking entries: 34

###  org.apache.commons.lang3.LocaleUtils

```
88c88
<     public static Locale toLocale(String str) {
---
>     public static Locale toLocale(final String str) {
92,93c92,93
<         int len = str.length();
<         if (len != 2 && len != 5 && len < 7) {
---
>         final int len = str.length();
>         if (len < 2) {
96,98c96,98
<         char ch0 = str.charAt(0);
<         char ch1 = str.charAt(1);
<         if (ch0 < 'a' || ch0 > 'z' || ch1 < 'a' || ch1 > 'z') {
---
>         final char ch0 = str.charAt(0);
>         if (ch0 == '_') {
>             if (len < 3) {
101,102c101,115
<         if (len == 2) {
<             return new Locale(str, "");
---
>             final char ch1 = str.charAt(1);
>             final char ch2 = str.charAt(2);
>             if (!Character.isUpperCase(ch1) || !Character.isUpperCase(ch2)) {
>                 throw new IllegalArgumentException("Invalid locale format: " + str);
>             }
>             if (len == 3) {
>                 return new Locale("", str.substring(1, 3));
>             }
>             if (len < 5) {
>                 throw new IllegalArgumentException("Invalid locale format: " + str);
>             }
>             if (str.charAt(3) != '_') {
>                 throw new IllegalArgumentException("Invalid locale format: " + str);
>             }
>             return new Locale("", str.substring(1, 3), str.substring(4));
103a117,126
>             final char ch1 = str.charAt(1);
>             if (!Character.isLowerCase(ch0) || !Character.isLowerCase(ch1)) {
>                 throw new IllegalArgumentException("Invalid locale format: " + str);
>             }
>             if (len == 2) {
>                 return new Locale(str);
>             }
>             if (len < 5) {
>                 throw new IllegalArgumentException("Invalid locale format: " + str);
>             }
107c130
<             char ch3 = str.charAt(3);
---
>             final char ch3 = str.charAt(3);
111,112c134,135
<             char ch4 = str.charAt(4);
<             if (ch3 < 'A' || ch3 > 'Z' || ch4 < 'A' || ch4 > 'Z') {
---
>             final char ch4 = str.charAt(4);
>             if (!Character.isUpperCase(ch3) || !Character.isUpperCase(ch4)) {
117c140,143
<             } else {
---
>             }
>             if (len < 7) {
>                 throw new IllegalArgumentException("Invalid locale format: " + str);
>             }
124d149
<     }
```

- Deleted lines: 18<br />
- Added lines: 40<br />
- Diff added/deleted: 22

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 92 | org.apache.commons.lang3.LocaleUtils:92 -> 0.08032193289024989 (ep: 4, ef: 1, np: 2236, nf: 30) | 27 |
| 93 | org.apache.commons.lang3.LocaleUtils:93 -> 0.08032193289024989 (ep: 4, ef: 1, np: 2236, nf: 30) | 28 |

- Nb. undetected lines: 12/14 ( 88 96 97 98 101 102 103 107 111 112 117 124 )

## Bug 6

- Nb. modified sources: 1

- Nb. nopol ranking entries: 117

###  org.apache.commons.lang3.text.translate.CharSequenceTranslator

```
95c95
<                 pos += Character.charCount(Character.codePointAt(input, pos));
---
>                 pos += Character.charCount(Character.codePointAt(input, pt));
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 95 | org.apache.commons.lang3.text.translate.CharSequenceTranslator:95 -> 0.03225806451612903 (ep: 30, ef: 1, np: 2202, nf: 30) | 107 |

- Nb. undetected lines: 0/1

## Bug 7

- Nb. modified sources: 1

- Nb. nopol ranking entries: 119

###  org.apache.commons.lang3.math.NumberUtils

```
452,458d451
<         if (str.startsWith("--")) {
<             // this is protection for poorness in java.lang.BigDecimal.
<             // it accepts this as a legal value, but it does not appear 
<             // to be in specification of class. OS X Java parses it to 
<             // a wrong value.
<             return null;
<         }
724a718,724
>         if (str.trim().startsWith("--")) {
>             // this is protection for poorness in java.lang.BigDecimal.
>             // it accepts this as a legal value, but it does not appear 
>             // to be in specification of class. OS X Java parses it to 
>             // a wrong value.
>             throw new NumberFormatException(str + " is not a valid number.");
>         }
```

- Deleted lines: 7<br />
- Added lines: 7<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 452 | org.apache.commons.lang3.math.NumberUtils:452 -> 0.10369516947304253 (ep: 2, ef: 1, np: 2228, nf: 30) | 67 |
| 457 | org.apache.commons.lang3.math.NumberUtils:457 -> 0.1270001270001905 (ep: 1, ef: 1, np: 2229, nf: 30) | 31 |

- Nb. undetected lines: 6/8 ( 453 454 455 456 458 724 )

## Bug 8

- Nb. modified sources: 1

- Nb. nopol ranking entries: 240

###  org.apache.commons.lang3.time.FastDatePrinter

```
1096c1096,1097
<         private final TimeZone mTimeZone;
---
>         private final Locale mLocale;
>         private final int mStyle;
1108c1109,1110
<             mTimeZone = timeZone;
---
>             mLocale = locale;
>             mStyle = style;
1130,1131c1132,1135
<             if (mTimeZone.useDaylightTime() && calendar.get(Calendar.DST_OFFSET) != 0) {
<                 buffer.append(mDaylight);
---
>             TimeZone zone = calendar.getTimeZone();
>             if (zone.useDaylightTime()
>                     && calendar.get(Calendar.DST_OFFSET) != 0) {
>                 buffer.append(getTimeZoneDisplay(zone, true, mStyle, mLocale));
1133c1137
<                 buffer.append(mStandard);
---
>                 buffer.append(getTimeZoneDisplay(zone, false, mStyle, mLocale));
```

- Deleted lines: 5<br />
- Added lines: 9<br />
- Diff added/deleted: 4


- Nb. undetected lines: 5/5 ( 1096 1108 1130 1131 1133 )

## Bug 9

- Nb. modified sources: 1

- Nb. nopol ranking entries: 194

###  org.apache.commons.lang3.time.FastDateParser

```
143a144,146
>         if (patternMatcher.regionStart() != patternMatcher.regionEnd()) {
>             throw new IllegalArgumentException("Failed to parse \""+pattern+"\" ; gave up at index "+patternMatcher.regionStart());
>         }
```

- Deleted lines: 0<br />
- Added lines: 3<br />
- Diff added/deleted: 3

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 143 | org.apache.commons.lang3.time.FastDateParser:143 -> 0.041959067914834454 (ep: 69, ef: 2, np: 2099, nf: 30) | 96 |

- Nb. undetected lines: 0/1

## Bug 10

- Nb. modified sources: 1

- Nb. nopol ranking entries: 242

###  org.apache.commons.lang3.time.FastDateParser

```
304d303
<         boolean wasWhite= false;
307,314d305
<             if(Character.isWhitespace(c)) {
<                 if(!wasWhite) {
<                     wasWhite= true;
<                     regex.append("\\s*+");
<                 }
<                 continue;
<             }
<             wasWhite= false;
```

- Deleted lines: 9<br />
- Added lines: 0<br />
- Diff added/deleted: -9

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 304 | org.apache.commons.lang3.time.FastDateParser:304 -> 0.04351941398892446 (ep: 64, ef: 2, np: 2102, nf: 30) | 108 |
| 307 | org.apache.commons.lang3.time.FastDateParser:307 -> 0.04351941398892446 (ep: 64, ef: 2, np: 2102, nf: 30) | 111 |
| 308 | org.apache.commons.lang3.time.FastDateParser:308 -> 0.05590169943749474 (ep: 38, ef: 2, np: 2128, nf: 30) | 77 |
| 309 | org.apache.commons.lang3.time.FastDateParser:309 -> 0.05590169943749474 (ep: 38, ef: 2, np: 2128, nf: 30) | 78 |
| 310 | org.apache.commons.lang3.time.FastDateParser:310 -> 0.05590169943749474 (ep: 38, ef: 2, np: 2128, nf: 30) | 79 |
| 314 | org.apache.commons.lang3.time.FastDateParser:314 -> 0.044194173824159216 (ep: 62, ef: 2, np: 2104, nf: 30) | 101 |

- Nb. undetected lines: 3/9 ( 311 312 313 )

## Bug 11

- Nb. modified sources: 1

- Nb. nopol ranking entries: 38

###  org.apache.commons.lang3.RandomStringUtils

```
244a245,248
>         } else {
>             if (end <= start) {
>                 throw new IllegalArgumentException("Parameter end (" + end + ") must be greater than start (" + start + ")");
>             }
```

- Deleted lines: 1<br />
- Added lines: 4<br />
- Diff added/deleted: 3


- Nb. undetected lines: 1/1 ( 244 )

## Bug 12

- Nb. modified sources: 1

- Nb. nopol ranking entries: 47

###  org.apache.commons.lang3.RandomStringUtils

```
229a230,232
>         if (chars != null && chars.length == 0) {
>             throw new IllegalArgumentException("The chars array must not be empty");
>         }
232,233c235,237
<             end = 'z' + 1;
<             start = ' ';
---
>             if (chars != null) {
>                 end = chars.length;
>             } else {
235d238
<                 start = 0;
236a240,243
>                 } else {
>                     end = 'z' + 1;
>                     start = ' ';                
>                 }
```

- Deleted lines: 3<br />
- Added lines: 10<br />
- Diff added/deleted: 7

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 232 | org.apache.commons.lang3.RandomStringUtils:232 -> 0.1336306209562122 (ep: 5, ef: 2, np: 2100, nf: 30) | 25 |
| 233 | org.apache.commons.lang3.RandomStringUtils:233 -> 0.1336306209562122 (ep: 5, ef: 2, np: 2100, nf: 30) | 26 |
| 235 | org.apache.commons.lang3.RandomStringUtils:235 -> 0.17677669529663687 (ep: 2, ef: 2, np: 2103, nf: 30) | 3 |
| 236 | org.apache.commons.lang3.RandomStringUtils:236 -> 0.17677669529663687 (ep: 2, ef: 2, np: 2103, nf: 30) | 4 |

- Nb. undetected lines: 1/5 ( 229 )

## Bug 13

- Nb. modified sources: 1

- Nb. nopol ranking entries: 60

###  org.apache.commons.lang3.SerializationUtils

```
238a239,240
>         private static final Map<String, Class<?>> primitiveTypes = 
>                 new HashMap<String, Class<?>>();
251a254,262
>             primitiveTypes.put("byte", byte.class);
>             primitiveTypes.put("short", short.class);
>             primitiveTypes.put("int", int.class);
>             primitiveTypes.put("long", long.class);
>             primitiveTypes.put("float", float.class);
>             primitiveTypes.put("double", double.class);
>             primitiveTypes.put("boolean", boolean.class);
>             primitiveTypes.put("char", char.class);
>             primitiveTypes.put("void", void.class);
267a279
>                 try {
268a281,287
>                 } catch (ClassNotFoundException cnfe) {
>                     Class<?> cls = primitiveTypes.get(name);
>                     if (cls != null)
>                         return cls;
>                     else
>                         throw cnfe;
>                 }
```

- Deleted lines: 3<br />
- Added lines: 19<br />
- Diff added/deleted: 16


- Nb. undetected lines: 4/4 ( 238 251 267 268 )

## Bug 14

- Nb. modified sources: 1

- Nb. nopol ranking entries: 29

###  org.apache.commons.lang3.StringUtils

```
782c782,791
<         return cs1 == null ? cs2 == null : cs1.equals(cs2);
---
>         if (cs1 == cs2) {
>             return true;
>         }
>         if (cs1 == null || cs2 == null) {
>             return false;
>         }
>         if (cs1 instanceof String && cs2 instanceof String) {
>             return cs1.equals(cs2);
>         }
>         return CharSequenceUtils.regionMatches(cs1, false, 0, cs2, 0, Math.max(cs1.length(), cs2.length()));
```

- Deleted lines: 1<br />
- Added lines: 10<br />
- Diff added/deleted: 9

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 782 | org.apache.commons.lang3.StringUtils:782 -> 0.04356068418690321 (ep: 16, ef: 1, np: 2026, nf: 30) | 30 |

- Nb. undetected lines: 0/1

## Bug 15

- Nb. modified sources: 1

- Nb. nopol ranking entries: 269

###  org.apache.commons.lang3.reflect.TypeUtils

```
219,221c219,221
<         for (Map.Entry<TypeVariable<?>, Type> entry : toTypeVarAssigns.entrySet()) {
<             Type toTypeArg = entry.getValue();
<             Type fromTypeArg = fromTypeVarAssigns.get(entry.getKey());
---
>         for (TypeVariable<?> var : toTypeVarAssigns.keySet()) {
>             Type toTypeArg = unrollVariableAssignments(var, toTypeVarAssigns);
>             Type fromTypeArg = unrollVariableAssignments(var, fromTypeVarAssigns);
236a237,248
>     private static Type unrollVariableAssignments(TypeVariable<?> var, Map<TypeVariable<?>, Type> typeVarAssigns) {
>         Type result;
>         do {
>             result = typeVarAssigns.get(var);
>             if (result instanceof TypeVariable<?> && !result.equals(var)) {
>                 var = (TypeVariable<?>) result;
>                 continue;
>             }
>             break;
>         } while (true);
>         return result;
>     }
663c675
<         if (cls.getTypeParameters().length > 0 || toClass.equals(cls)) {
---
>         if (toClass.equals(cls)) {
```

- Deleted lines: 8<br />
- Added lines: 18<br />
- Diff added/deleted: 10

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 219 | org.apache.commons.lang3.reflect.TypeUtils:219 -> 0.10206207261596577 (ep: 2, ef: 1, np: 2013, nf: 31) | 189 |
| 220 | org.apache.commons.lang3.reflect.TypeUtils:220 -> 0.10206207261596577 (ep: 2, ef: 1, np: 2013, nf: 31) | 190 |
| 221 | org.apache.commons.lang3.reflect.TypeUtils:221 -> 0.10206207261596577 (ep: 2, ef: 1, np: 2013, nf: 31) | 191 |
| 663 | org.apache.commons.lang3.reflect.TypeUtils:663 -> 0.15811388300841897 (ep: 3, ef: 2, np: 2012, nf: 30) | 65 |

- Nb. undetected lines: 1/5 ( 236 )

## Bug 16

- Nb. modified sources: 1

- Nb. nopol ranking entries: 92

###  org.apache.commons.lang3.math.NumberUtils

```
458c458
<         if (str.startsWith("0x") || str.startsWith("-0x")) {
---
>         if (str.startsWith("0x") || str.startsWith("-0x") || str.startsWith("0X") || str.startsWith("-0X")) {
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 458 | org.apache.commons.lang3.math.NumberUtils:458 -> 0.10369516947304253 (ep: 2, ef: 1, np: 2013, nf: 30) | 49 |

- Nb. undetected lines: 0/1

## Bug 17

- Nb. modified sources: 1

- Nb. nopol ranking entries: 55

###  org.apache.commons.lang3.text.translate.CharSequenceTranslator

```
82,87c82,85
<         int sz = Character.codePointCount(input, 0, input.length());
<         for (int i = 0; i < sz; i++) {
< 
<             // consumed is the number of codepoints consumed
<             int consumed = translate(input, i, out);
< 
---
>         int pos = 0;
>         int len = input.length();
>         while (pos < len) {
>             int consumed = translate(input, pos, out);
89,90c87,91
<                 out.write(Character.toChars(Character.codePointAt(input, i)));
<             } else {
---
>                 char[] c = Character.toChars(Character.codePointAt(input, pos));
>                 out.write(c);
>                 pos+= c.length;
>                 continue;
>             }
93,102c94,95
<                 for (int j = 0; j < consumed; j++) {
<                     if (i < sz - 2) {
<                         i += Character.charCount(Character.codePointAt(input, i));
<                     } else {
<                         // If the String ends with a high surrogate, just add the 1 and don't worry about such things
<                         i++;
<                     }
<                 }
<                 // for loop will increment 1 anyway, so remove 1 to account for that
<                 i--;
---
>             for (int pt = 0; pt < consumed; pt++) {
>                 pos += Character.charCount(Character.codePointAt(input, pos));
```

- Deleted lines: 20<br />
- Added lines: 11<br />
- Diff added/deleted: -9

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 82 | org.apache.commons.lang3.text.translate.CharSequenceTranslator:82 -> 0.030802055181684874 (ep: 33, ef: 1, np: 1839, nf: 30) | 52 |
| 83 | org.apache.commons.lang3.text.translate.CharSequenceTranslator:83 -> 0.030802055181684874 (ep: 66, ef: 2, np: 1806, nf: 29) | 53 |
| 86 | org.apache.commons.lang3.text.translate.CharSequenceTranslator:86 -> 0.030802055181684874 (ep: 33, ef: 1, np: 1839, nf: 30) | 54 |
| 89 | org.apache.commons.lang3.text.translate.CharSequenceTranslator:89 -> 0.036661778755338326 (ep: 23, ef: 1, np: 1849, nf: 30) | 44 |

- Nb. undetected lines: 14/18 ( 84 85 87 90 93 94 95 96 97 98 99 100 101 102 )

## Bug 18

- Nb. modified sources: 1

- Nb. nopol ranking entries: 227

###  org.apache.commons.lang3.time.FastDateFormat

```
495,497c495
<                 if (tokenLen >= 4) {
<                     rule = selectNumberRule(Calendar.YEAR, tokenLen);
<                 } else {
---
>                 if (tokenLen == 2) {
498a497,498
>                 } else {
>                     rule = selectNumberRule(Calendar.YEAR, tokenLen < 4 ? 4 : tokenLen);
```

- Deleted lines: 4<br />
- Added lines: 4<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 495 | org.apache.commons.lang3.time.FastDateFormat:495 -> 0.04016096644512494 (ep: 19, ef: 1, np: 1852, nf: 30) | 112 |
| 496 | org.apache.commons.lang3.time.FastDateFormat:496 -> 0.04120428217151646 (ep: 18, ef: 1, np: 1853, nf: 30) | 104 |
| 498 | org.apache.commons.lang3.time.FastDateFormat:498 -> 0.10369516947304253 (ep: 2, ef: 1, np: 1869, nf: 30) | 51 |

- Nb. undetected lines: 1/4 ( 497 )

## Bug 19

- Nb. modified sources: 1

- Nb. nopol ranking entries: 54

###  org.apache.commons.lang3.text.translate.NumericEntityUnescaper

```
38c38,40
<         if(input.charAt(index) == '&' && index < (input.length() - 1) && input.charAt(index + 1) == '#') {
---
>         int seqEnd = input.length();
>         // Uses -2 to ensure there is something after the &#
>         if(input.charAt(index) == '&' && index < seqEnd - 2 && input.charAt(index + 1) == '#') {
45a48,52
> 
>                 // Check there's more than just an x after the &#
>                 if(start == seqEnd) {
>                     return 0;
>                 }
49c56,60
<             while(input.charAt(end) != ';') {
---
>             // Note that this supports character codes without a ; on the end
>             while(end < seqEnd && ( (input.charAt(end) >= '0' && input.charAt(end) <= '9') ||
>                                     (input.charAt(end) >= 'a' && input.charAt(end) <= 'f') ||
>                                     (input.charAt(end) >= 'A' && input.charAt(end) <= 'F') ) )
>             {
60a72
>             System.err.println("FAIL: " + input.subSequence(start, end) + "[" + start +"]["+ end +"]");
71c83,86
<             return 2 + (end - start) + (isHex ? 1 : 0) + 1;
---
> 
>             boolean semiNext = (end != seqEnd) && (input.charAt(end) == ';');
> 
>             return 2 + (end - start) + (isHex ? 1 : 0) + (semiNext ? 1 : 0);
```

- Deleted lines: 7<br />
- Added lines: 18<br />
- Diff added/deleted: 11

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 38 | org.apache.commons.lang3.text.translate.NumericEntityUnescaper:38 -> 0.10660035817780521 (ep: 9, ef: 2, np: 1836, nf: 30) | 30 |
| 45 | org.apache.commons.lang3.text.translate.NumericEntityUnescaper:45 -> 0.125 (ep: 1, ef: 1, np: 1844, nf: 31) | 27 |
| 49 | org.apache.commons.lang3.text.translate.NumericEntityUnescaper:49 -> 0.07905694150420949 (ep: 4, ef: 1, np: 1841, nf: 31) | 38 |

- Nb. undetected lines: 2/5 ( 60 71 )

## Bug 20

- Nb. modified sources: 1

- Nb. nopol ranking entries: 61

###  org.apache.commons.lang3.StringUtils

```
3293,3294c3293,3294
<         int bufSize = (endIndex - startIndex);
<         if (bufSize <= 0) {
---
>         int noOfItems = (endIndex - startIndex);
>         if (noOfItems <= 0) {
3298,3299c3298
<         bufSize *= ((array[startIndex] == null ? 16 : array[startIndex].toString().length()) + 1);
<         StringBuilder buf = new StringBuilder(bufSize);
---
>         StringBuilder buf = new StringBuilder(noOfItems * 16);
3379,3380c3378,3379
<         int bufSize = (endIndex - startIndex);
<         if (bufSize <= 0) {
---
>         int noOfItems = (endIndex - startIndex);
>         if (noOfItems <= 0) {
3384,3387c3383
<         bufSize *= ((array[startIndex] == null ? 16 : array[startIndex].toString().length())
<                         + separator.length());
< 
<         StringBuilder buf = new StringBuilder(bufSize);
---
>         StringBuilder buf = new StringBuilder(noOfItems * 16);
```

- Deleted lines: 12<br />
- Added lines: 6<br />
- Diff added/deleted: -6

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 3293 | org.apache.commons.lang3.StringUtils:3293 -> 0.125 (ep: 1, ef: 1, np: 1843, nf: 31) | 26 |
| 3294 | org.apache.commons.lang3.StringUtils:3294 -> 0.125 (ep: 1, ef: 1, np: 1843, nf: 31) | 27 |
| 3298 | org.apache.commons.lang3.StringUtils:3298 -> 0.125 (ep: 1, ef: 1, np: 1843, nf: 31) | 29 |
| 3299 | org.apache.commons.lang3.StringUtils:3299 -> 0.125 (ep: 1, ef: 1, np: 1843, nf: 31) | 30 |
| 3379 | org.apache.commons.lang3.StringUtils:3379 -> 0.08838834764831843 (ep: 3, ef: 1, np: 1841, nf: 31) | 51 |
| 3380 | org.apache.commons.lang3.StringUtils:3380 -> 0.08838834764831843 (ep: 3, ef: 1, np: 1841, nf: 31) | 52 |
| 3384 | org.apache.commons.lang3.StringUtils:3384 -> 0.08838834764831843 (ep: 3, ef: 1, np: 1841, nf: 31) | 53 |
| 3387 | org.apache.commons.lang3.StringUtils:3387 -> 0.08838834764831843 (ep: 3, ef: 1, np: 1841, nf: 31) | 54 |

- Nb. undetected lines: 2/10 ( 3385 3386 )

## Bug 21

- Nb. modified sources: 1

- Nb. nopol ranking entries: 30

###  org.apache.commons.lang3.time.DateUtils

```
265c265
<                 cal1.get(Calendar.HOUR) == cal2.get(Calendar.HOUR) &&
---
>                 cal1.get(Calendar.HOUR_OF_DAY) == cal2.get(Calendar.HOUR_OF_DAY) &&
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0


- Nb. undetected lines: 1/1 ( 265 )

## Bug 22

- Nb. modified sources: 1

- Nb. nopol ranking entries: 85

###  org.apache.commons.lang3.math.Fraction

```
582,583c582,590
<         //if either op. is abs 0 or 1, return 1:
<         if (Math.abs(u) <= 1 || Math.abs(v) <= 1) {
---
>         // From Commons Math:
>         if ((u == 0) || (v == 0)) {
>             if ((u == Integer.MIN_VALUE) || (v == Integer.MIN_VALUE)) {
>                 throw new ArithmeticException("overflow: gcd is 2^31");
>             }
>             return Math.abs(u) + Math.abs(v);
>         }
>         //if either operand is abs 1, return 1:
>         if (Math.abs(u) == 1 || Math.abs(v) == 1) {
```

- Deleted lines: 2<br />
- Added lines: 9<br />
- Diff added/deleted: 7

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 583 | org.apache.commons.lang3.math.Fraction:583 -> 0.11952286093343936 (ep: 8, ef: 2, np: 1789, nf: 26) | 48 |

- Nb. undetected lines: 1/2 ( 582 )

## Bug 23

- Nb. modified sources: 1

- Nb. nopol ranking entries: 144

###  org.apache.commons.lang3.text.ExtendedMessageFormat

```
72a73
>     private static final int HASH_SEED = 31;
257a259,301
>      * Check if this extended message format is equal to another object.
>      *
>      * @param obj the object to compare to
>      * @return true if this object equals the other, otherwise false
>      */
>     @Override
>     public boolean equals(Object obj) {
>         if (obj == this) {
>             return true;
>         }
>         if (obj == null) {
>             return false;
>         }
>         if (!super.equals(obj)) {
>             return false;
>         }
>         if (ObjectUtils.notEqual(getClass(), obj.getClass())) {
>           return false;
>         }
>         ExtendedMessageFormat rhs = (ExtendedMessageFormat)obj;
>         if (ObjectUtils.notEqual(toPattern, rhs.toPattern)) {
>             return false;
>         }
>         if (ObjectUtils.notEqual(registry, rhs.registry)) {
>             return false;
>         }
>         return true;
>     }
> 
>     /**
>      * Return the hashcode.
>      *
>      * @return the hashcode
>      */
>     @Override
>     public int hashCode() {
>         int result = super.hashCode();
>         result = HASH_SEED * result + ObjectUtils.hashCode(registry);
>         result = HASH_SEED * result + ObjectUtils.hashCode(toPattern);
>         return result;
>     }
> 
>     /**
```

- Deleted lines: 0<br />
- Added lines: 44<br />
- Diff added/deleted: 44


- Nb. undetected lines: 2/2 ( 72 257 )

## Bug 24

- Nb. modified sources: 1

- Nb. nopol ranking entries: 172

###  org.apache.commons.lang3.math.NumberUtils

```
1412,1413c1412,1413
<                 // not allowing L with an exponent
<                 return foundDigit && !hasExp;
---
>                 // not allowing L with an exponent or decimal point
>                 return foundDigit && !hasExp && !hasDecPoint;
```

- Deleted lines: 2<br />
- Added lines: 2<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 1413 | org.apache.commons.lang3.math.NumberUtils:1413 -> 0.19245008972987526 (ep: 0, ef: 1, np: 1795, nf: 26) | 67 |

- Nb. undetected lines: 1/2 ( 1412 )

## Bug 25

- Nb. modified sources: 1

- Nb. nopol ranking entries: 29

###  org.apache.commons.lang3.text.translate.EntityArrays

```
74,100c74,100
<         {"\u00CB", "&Ecirc;"}, // Ê - uppercase E, circumflex accent
<         {"\u00CC", "&Euml;"}, // Ë - uppercase E, umlaut
<         {"\u00CD", "&Igrave;"}, // Ì - uppercase I, grave accent
<         {"\u00CE", "&Iacute;"}, // Í - uppercase I, acute accent
<         {"\u00CF", "&Icirc;"}, // Î - uppercase I, circumflex accent
<         {"\u00D0", "&Iuml;"}, // Ï - uppercase I, umlaut
<         {"\u00D1", "&ETH;"}, // Ð - uppercase Eth, Icelandic
<         {"\u00D2", "&Ntilde;"}, // Ñ - uppercase N, tilde
<         {"\u00D3", "&Ograve;"}, // Ò - uppercase O, grave accent
<         {"\u00D4", "&Oacute;"}, // Ó - uppercase O, acute accent
<         {"\u00D5", "&Ocirc;"}, // Ô - uppercase O, circumflex accent
<         {"\u00D6", "&Otilde;"}, // Õ - uppercase O, tilde
<         {"\u00D7", "&Ouml;"}, // Ö - uppercase O, umlaut
<         {"\u00D8", "&times;"}, // multiplication sign
<         {"\u00D9", "&Oslash;"}, // Ø - uppercase O, slash
<         {"\u00DA", "&Ugrave;"}, // Ù - uppercase U, grave accent
<         {"\u00DB", "&Uacute;"}, // Ú - uppercase U, acute accent
<         {"\u00DC", "&Ucirc;"}, // Û - uppercase U, circumflex accent
<         {"\u00DD", "&Uuml;"}, // Ü - uppercase U, umlaut
<         {"\u00DE", "&Yacute;"}, // Ý - uppercase Y, acute accent
<         {"\u00DF", "&THORN;"}, // Þ - uppercase THORN, Icelandic
<         {"\u00E0", "&szlig;"}, // ß - lowercase sharps, German
<         {"\u00E1", "&agrave;"}, // à - lowercase a, grave accent
<         {"\u00E2", "&aacute;"}, // á - lowercase a, acute accent
<         {"\u00E3", "&acirc;"}, // â - lowercase a, circumflex accent
<         {"\u00E4", "&atilde;"}, // ã - lowercase a, tilde
<         {"\u00E5", "&auml;"}, // ä - lowercase a, umlaut
---
>         {"\u00CA", "&Ecirc;"}, // Ê - uppercase E, circumflex accent
>         {"\u00CB", "&Euml;"}, // Ë - uppercase E, umlaut
>         {"\u00CC", "&Igrave;"}, // Ì - uppercase I, grave accent
>         {"\u00CD", "&Iacute;"}, // Í - uppercase I, acute accent
>         {"\u00CE", "&Icirc;"}, // Î - uppercase I, circumflex accent
>         {"\u00CF", "&Iuml;"}, // Ï - uppercase I, umlaut
>         {"\u00D0", "&ETH;"}, // Ð - uppercase Eth, Icelandic
>         {"\u00D1", "&Ntilde;"}, // Ñ - uppercase N, tilde
>         {"\u00D2", "&Ograve;"}, // Ò - uppercase O, grave accent
>         {"\u00D3", "&Oacute;"}, // Ó - uppercase O, acute accent
>         {"\u00D4", "&Ocirc;"}, // Ô - uppercase O, circumflex accent
>         {"\u00D5", "&Otilde;"}, // Õ - uppercase O, tilde
>         {"\u00D6", "&Ouml;"}, // Ö - uppercase O, umlaut
>         {"\u00D7", "&times;"}, // multiplication sign
>         {"\u00D8", "&Oslash;"}, // Ø - uppercase O, slash
>         {"\u00D9", "&Ugrave;"}, // Ù - uppercase U, grave accent
>         {"\u00DA", "&Uacute;"}, // Ú - uppercase U, acute accent
>         {"\u00DB", "&Ucirc;"}, // Û - uppercase U, circumflex accent
>         {"\u00DC", "&Uuml;"}, // Ü - uppercase U, umlaut
>         {"\u00DD", "&Yacute;"}, // Ý - uppercase Y, acute accent
>         {"\u00DE", "&THORN;"}, // Þ - uppercase THORN, Icelandic
>         {"\u00DF", "&szlig;"}, // ß - lowercase sharps, German
>         {"\u00E0", "&agrave;"}, // à - lowercase a, grave accent
>         {"\u00E1", "&aacute;"}, // á - lowercase a, acute accent
>         {"\u00E2", "&acirc;"}, // â - lowercase a, circumflex accent
>         {"\u00E3", "&atilde;"}, // ã - lowercase a, tilde
>         {"\u00E4", "&auml;"}, // ä - lowercase a, umlaut
```

- Deleted lines: 27<br />
- Added lines: 27<br />
- Diff added/deleted: 0


- Nb. undetected lines: 27/27 ( 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 )

## Bug 26

- Nb. modified sources: 1

- Nb. nopol ranking entries: 137

###  org.apache.commons.lang3.time.FastDateFormat

```
820c820
<         Calendar c = new GregorianCalendar(mTimeZone);
---
>         Calendar c = new GregorianCalendar(mTimeZone, mLocale);
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 820 | org.apache.commons.lang3.time.FastDateFormat:820 -> 0.03456505649101418 (ep: 30, ef: 1, np: 1733, nf: 26) | 124 |

- Nb. undetected lines: 0/1

## Bug 27

- Nb. modified sources: 1

- Nb. nopol ranking entries: 84

###  org.apache.commons.lang3.math.NumberUtils

```
479c479
<                 if (expPos < decPos) {
---
>                 if (expPos < decPos || expPos > str.length()) {
488a489,491
>                 if (expPos > str.length()) {
>                     throw new NumberFormatException(str + " is not a valid number.");
>                 }
```

- Deleted lines: 2<br />
- Added lines: 4<br />
- Diff added/deleted: 2

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 479 | org.apache.commons.lang3.math.NumberUtils:479 -> 0.14433756729740646 (ep: 1, ef: 1, np: 1760, nf: 23) | 12 |
| 488 | org.apache.commons.lang3.math.NumberUtils:488 -> 0.11785113019775793 (ep: 2, ef: 1, np: 1759, nf: 23) | 47 |

- Nb. undetected lines: 0/2

## Bug 28

- Nb. modified sources: 1

- Nb. nopol ranking entries: 33

###  org.apache.commons.lang3.text.translate.NumericEntityUnescaper

```
63c63,67
<             // TODO: if(entityValue > 0xFFFF) {
---
>             if(entityValue > 0xFFFF) {
>                 char[] chrs = Character.toChars(entityValue);
>                 out.write(chrs[0]);
>                 out.write(chrs[1]);
>             } else {
64a69
>             }
```

- Deleted lines: 1<br />
- Added lines: 7<br />
- Diff added/deleted: 6

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 64 | org.apache.commons.lang3.text.translate.NumericEntityUnescaper:64 -> 0.11785113019775793 (ep: 2, ef: 1, np: 1737, nf: 23) | 5 |

- Nb. undetected lines: 1/2 ( 63 )

## Bug 29

- Nb. modified sources: 1

- Nb. nopol ranking entries: 10

###  org.apache.commons.lang3.SystemUtils

```
1672c1672
<     static float toJavaVersionInt(String version) {
---
>     static int toJavaVersionInt(String version) {
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0


- Nb. undetected lines: 1/1 ( 1672 )

## Bug 30

- Nb. modified sources: 1

- Nb. nopol ranking entries: 54

###  org.apache.commons.lang3.StringUtils

```
1375c1375,1379
<         for (int i = 0; i < cs.length(); i++) {
---
>         int csLen = cs.length();
>         int csLast = csLen - 1;
>         int searchLen = searchChars.length;
>         int searchLast = searchLen - 1;
>         for (int i = 0; i < csLen; i++) {
1377c1381
<             for (int j = 0; j < searchChars.length; j++) {
---
>             for (int j = 0; j < searchLen; j++) {
1378a1383,1388
>                     if (i < csLast && j < searchLast && Character.isHighSurrogate(ch)) {
>                         // ch is a supplementary character
>                         if (searchChars[j + 1] == cs.charAt(i + 1)) {
>                             return i;
>                         }
>                     } else {
1382a1393
>         }
1440c1451
<     public static boolean containsAny(CharSequence cs, char[] searchChars) {
---
>     public static boolean containsAny(String cs, char[] searchChars) {
1446,1447c1457,1458
<         int csLastIndex = csLength - 1;
<         int searchLastIndex = searchLength - 1;
---
>         int csLast = csLength - 1;
>         int searchLast = searchLength - 1;
1452,1454c1463,1468
<                     if (i < csLastIndex && j < searchLastIndex && ch >= Character.MIN_HIGH_SURROGATE && ch <= Character.MAX_HIGH_SURROGATE) {
<                         // ch is a supplementary character
<                         if (searchChars[j + 1] == cs.charAt(i + 1)) {
---
>                     if (Character.isHighSurrogate(ch)) {
>                         if (j == searchLast) {
>                             // missing low surrogate, fine, like String.indexOf(String)
>                             return true;
>                         }
>                         if (i < csLast && searchChars[j + 1] == cs.charAt(i + 1)) {
1494c1508
<     public static boolean containsAny(CharSequence cs, String searchChars) {
---
>     public static boolean containsAny(String cs, String searchChars) {
1529c1543,1548
<         outer : for (int i = 0; i < cs.length(); i++) {
---
>         int csLen = cs.length();
>         int csLast = csLen - 1;
>         int searchLen = searchChars.length;
>         int searchLast = searchLen - 1;
>         outer:
>         for (int i = 0; i < csLen; i++) {
1531c1550
<             for (int j = 0; j < searchChars.length; j++) {
---
>             for (int j = 0; j < searchLen; j++) {
1532a1552,1556
>                     if (i < csLast && j < searchLast && Character.isHighSurrogate(ch)) {
>                         if (searchChars[j + 1] == cs.charAt(i + 1)) {
>                             continue outer;
>                         }
>                     } else {
1535a1560
>             }
1567,1568c1592,1602
<         for (int i = 0; i < str.length(); i++) {
<             if (searchChars.indexOf(str.charAt(i)) < 0) {
---
>         int strLen = str.length();
>         for (int i = 0; i < strLen; i++) {
>             char ch = str.charAt(i);
>             boolean chFound = searchChars.indexOf(ch) >= 0;
>             if (i + 1 < strLen && Character.isHighSurrogate(ch)) {
>                 char ch2 = str.charAt(i + 1);
>                 if (chFound && searchChars.indexOf(ch2) < 0) {
>                     return i;
>                 }
>             } else {
>                 if (!chFound) {
1571a1606
>         }
1661c1696
<      * @param invalidChars  an array of invalid chars, may be null
---
>      * @param searchChars  an array of invalid chars, may be null
1665,1666c1700,1701
<     public static boolean containsNone(CharSequence cs, char[] invalidChars) {
<         if (cs == null || invalidChars == null) {
---
>     public static boolean containsNone(CharSequence cs, char[] searchChars) {
>         if (cs == null || searchChars == null) {
1669,1671c1704,1708
<         int strSize = cs.length();
<         int validSize = invalidChars.length;
<         for (int i = 0; i < strSize; i++) {
---
>         int csLen = cs.length();
>         int csLast = csLen - 1;
>         int searchLen = searchChars.length;
>         int searchLast = searchLen - 1;
>         for (int i = 0; i < csLen; i++) {
1673,1674c1710,1714
<             for (int j = 0; j < validSize; j++) {
<                 if (invalidChars[j] == ch) {
---
>             for (int j = 0; j < searchLen; j++) {
>                 if (searchChars[j] == ch) {
>                     if (Character.isHighSurrogate(ch)) {
>                         if (j == searchLast) {
>                             // missing low surrogate, fine, like String.indexOf(String)
1676a1717,1724
>                         if (i < csLast && searchChars[j + 1] == cs.charAt(i + 1)) {
>                             return false;
>                         }
>                     } else {
>                         // ch is in the Basic Multilingual Plane
>                         return false;
>                     }
>                 }
```

- Deleted lines: 34<br />
- Added lines: 70<br />
- Diff added/deleted: 36

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 1375 | org.apache.commons.lang3.StringUtils:1375 -> 0.18257418583505536 (ep: 4, ef: 2, np: 1699, nf: 28) | 15 |
| 1377 | org.apache.commons.lang3.StringUtils:1377 -> 0.18257418583505536 (ep: 4, ef: 2, np: 1699, nf: 28) | 17 |
| 1378 | org.apache.commons.lang3.StringUtils:1378 -> 0.18257418583505536 (ep: 2, ef: 2, np: 1701, nf: 28) | 18 |
| 1446 | org.apache.commons.lang3.StringUtils:1446 -> 0.12909944487358055 (ep: 6, ef: 2, np: 1697, nf: 28) | 27 |
| 1447 | org.apache.commons.lang3.StringUtils:1447 -> 0.12909944487358055 (ep: 6, ef: 2, np: 1697, nf: 28) | 28 |
| 1452 | org.apache.commons.lang3.StringUtils:1452 -> 0.12909944487358055 (ep: 6, ef: 2, np: 1697, nf: 28) | 33 |
| 1529 | org.apache.commons.lang3.StringUtils:1529 -> 0.06900655593423542 (ep: 12, ef: 2, np: 1691, nf: 28) | 50 |
| 1531 | org.apache.commons.lang3.StringUtils:1531 -> 0.09128709291752768 (ep: 9, ef: 2, np: 1694, nf: 28) | 47 |
| 1532 | org.apache.commons.lang3.StringUtils:1532 -> 0.06900655593423542 (ep: 6, ef: 1, np: 1697, nf: 29) | 53 |
| 1567 | org.apache.commons.lang3.StringUtils:1567 -> 0.12909944487358055 (ep: 2, ef: 2, np: 1701, nf: 28) | 38 |
| 1568 | org.apache.commons.lang3.StringUtils:1568 -> 0.12909944487358055 (ep: 1, ef: 1, np: 1702, nf: 29) | 39 |
| 1666 | org.apache.commons.lang3.StringUtils:1666 -> 0.2581988897471611 (ep: 4, ef: 4, np: 1699, nf: 26) | 2 |
| 1669 | org.apache.commons.lang3.StringUtils:1669 -> 0.2581988897471611 (ep: 4, ef: 4, np: 1699, nf: 26) | 3 |
| 1670 | org.apache.commons.lang3.StringUtils:1670 -> 0.2581988897471611 (ep: 4, ef: 4, np: 1699, nf: 26) | 4 |
| 1671 | org.apache.commons.lang3.StringUtils:1671 -> 0.2581988897471611 (ep: 8, ef: 6, np: 1695, nf: 24) | 5 |
| 1673 | org.apache.commons.lang3.StringUtils:1673 -> 0.2581988897471611 (ep: 8, ef: 6, np: 1695, nf: 24) | 7 |
| 1674 | org.apache.commons.lang3.StringUtils:1674 -> 0.2581988897471611 (ep: 4, ef: 4, np: 1699, nf: 26) | 8 |

- Nb. undetected lines: 10/27 ( 1382 1440 1453 1454 1494 1535 1571 1661 1665 1676 )

## Bug 31

- Nb. modified sources: 1

- Nb. nopol ranking entries: 8

###  org.apache.commons.lang3.StringUtils

```
1441c1441
<         if (cs == null || cs.length() == 0 || searchChars == null || searchChars.length == 0) {
---
> 		if (isEmpty(cs) || ArrayUtils.isEmpty(searchChars)) {
1444c1444,1448
<         for (int i = 0; i < cs.length(); i++) {
---
> 		int csLength = cs.length();
> 		int searchLength = searchChars.length;
> 		int csLastIndex = csLength - 1;
> 		int searchLastIndex = searchLength - 1;
> 		for (int i = 0; i < csLength; i++) {
1446c1450
<             for (int j = 0; j < searchChars.length; j++) {
---
> 			for (int j = 0; j < searchLength; j++) {
1447a1452,1458
> 					if (i < csLastIndex && j < searchLastIndex && ch >= Character.MIN_HIGH_SURROGATE && ch <= Character.MAX_HIGH_SURROGATE) {
> 						// ch is a supplementary character
> 						if (searchChars[j + 1] == cs.charAt(i + 1)) {
> 							return true;
> 						}
> 					} else {
> 						// ch is in the Basic Multilingual Plane
1451a1463
> 		}
```

- Deleted lines: 6<br />
- Added lines: 15<br />
- Diff added/deleted: 9

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 1441 | org.apache.commons.lang3.StringUtils:1441 -> 0.17407765595569785 (ep: 4, ef: 2, np: 1695, nf: 20) | 2 |
| 1444 | org.apache.commons.lang3.StringUtils:1444 -> 0.17407765595569785 (ep: 8, ef: 2, np: 1691, nf: 20) | 3 |
| 1446 | org.apache.commons.lang3.StringUtils:1446 -> 0.17407765595569785 (ep: 8, ef: 2, np: 1691, nf: 20) | 5 |
| 1447 | org.apache.commons.lang3.StringUtils:1447 -> 0.17407765595569785 (ep: 4, ef: 2, np: 1695, nf: 20) | 6 |

- Nb. undetected lines: 1/5 ( 1451 )

## Bug 32

- Nb. modified sources: 1

- Nb. nopol ranking entries: 56

###  org.apache.commons.lang3.builder.HashCodeBuilder

```
104,111c104
<     private static final ThreadLocal<Set<IDKey>> registry = new ThreadLocal<Set<IDKey>>() {
<         @Override
<         protected Set<IDKey> initialValue() {
<             // The HashSet implementation is not synchronized,
<             // which is just what we need here.
<             return new HashSet<IDKey>();
<         }
<     };
---
>     private static final ThreadLocal<Set<IDKey>> REGISTRY = new ThreadLocal<Set<IDKey>>();
139c132
<         return registry.get();
---
>         return REGISTRY.get();
154c147,148
<         return getRegistry().contains(new IDKey(value));
---
>         Set<IDKey> registry = getRegistry();
>         return registry != null && registry.contains(new IDKey(value));
523a518,522
>         synchronized (HashCodeBuilder.class) {
>             if (getRegistry() == null) {
>                 REGISTRY.set(new HashSet<IDKey>());
>             }
>         }
540c539,547
<         getRegistry().remove(new IDKey(value));
---
>         Set<IDKey> s = getRegistry();
>         if (s != null) {
>             s.remove(new IDKey(value));
>             synchronized (HashCodeBuilder.class) {
>                 if (s.isEmpty()) {
>                     REGISTRY.remove();
>                 }
>             }
>         }
```

- Deleted lines: 15<br />
- Added lines: 21<br />
- Diff added/deleted: 6

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 139 | org.apache.commons.lang3.builder.HashCodeBuilder:139 -> 0.11180339887498948 (ep: 7, ef: 1, np: 1653, nf: 9) | 13 |
| 154 | org.apache.commons.lang3.builder.HashCodeBuilder:154 -> 0.11180339887498948 (ep: 7, ef: 1, np: 1653, nf: 9) | 14 |
| 540 | org.apache.commons.lang3.builder.HashCodeBuilder:540 -> 0.11180339887498948 (ep: 7, ef: 1, np: 1653, nf: 9) | 36 |

- Nb. undetected lines: 9/12 ( 104 105 106 107 108 109 110 111 523 )

## Bug 33

- Nb. modified sources: 1

- Nb. nopol ranking entries: 8

###  org.apache.commons.lang3.ClassUtils

```
910c910
<             classes[i] = array[i].getClass();
---
>             classes[i] = array[i] == null ? null : array[i].getClass();
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 910 | org.apache.commons.lang3.ClassUtils:910 -> 0.31622776601683794 (ep: 0, ef: 1, np: 1660, nf: 9) | 7 |

- Nb. undetected lines: 0/1

## Bug 34

- Nb. modified sources: 1

- Nb. nopol ranking entries: 300

###  org.apache.commons.lang3.builder.ToStringStyle

```
147,149c147,148
<     static Set<Object> getRegistry() {
<         WeakHashMap<Object, Object> m = REGISTRY.get();
<         return m == null ? Collections.<Object> emptySet() : m.keySet();
---
>     static Map<Object, Object> getRegistry() {
>         return REGISTRY.get();
164c163,164
<         return getRegistry().contains(value);
---
>         Map<Object, Object> m = getRegistry();
>         return m != null && m.containsKey(value);
```

- Deleted lines: 6<br />
- Added lines: 7<br />
- Diff added/deleted: 1

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 147 | org.apache.commons.lang3.builder.ToStringStyle:1470 -> 0.44339817517393193 (ep: 76, ef: 27, np: 1558, nf: 9) | 61 |
| 148 | org.apache.commons.lang3.builder.ToStringStyle:148 -> 0.4271210980886246 (ep: 84, ef: 27, np: 1550, nf: 9) | 62 |
| 149 | org.apache.commons.lang3.builder.ToStringStyle:149 -> 0.4271210980886246 (ep: 84, ef: 27, np: 1550, nf: 9) | 63 |
| 164 | org.apache.commons.lang3.builder.ToStringStyle:164 -> 0.4271210980886246 (ep: 84, ef: 27, np: 1550, nf: 9) | 64 |

- Nb. undetected lines: 0/4

## Bug 35

- Nb. modified sources: 1

- Nb. nopol ranking entries: 5

###  org.apache.commons.lang3.ArrayUtils

```
3283,3284c3283,3284
<      * in which case it will have the same type as the element (unless that is also null)
<      * in which case the returned type will be Object[].
---
>      * in which case it will have the same type as the element.
>      * If both are null, an IllegalArgumentException is thrown
3285a3286
>      * @throws IllegalArgumentException if both arguments are null
3288,3289c3289,3297
<         Class<?> type = array != null ? array.getClass() : (element != null ? element.getClass() : Object.class);
<         // TODO - this is NOT safe to ignore - see LANG-571
---
>         Class<?> type;
>         if (array != null){
>             type = array.getClass();
>         } else if (element != null) {
>             type = element.getClass();
>         } else {
>             throw new IllegalArgumentException("Arguments cannot both be null");            
>         }
>         @SuppressWarnings("unchecked") // type must be T
3566,3568c3574
<             // TODO this is not type-safe - see LANG-571
<             final T[] emptyArray = (T[]) new Object[] { null };
<             return emptyArray;
---
>             throw new IllegalArgumentException("Array and element cannot both be null");            
```

- Deleted lines: 8<br />
- Added lines: 14<br />
- Diff added/deleted: 6

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 3288 | org.apache.commons.lang3.ArrayUtils:3288 -> 0.18257418583505536 (ep: 2, ef: 1, np: 1632, nf: 9) | 1 |

- Nb. undetected lines: 7/8 ( 3283 3284 3285 3289 3566 3567 3568 )

## Bug 36

- Nb. modified sources: 1

- Nb. nopol ranking entries: 147

###  org.apache.commons.lang3.math.NumberUtils

```
491c491
<         if (!Character.isDigit(lastChar)) {
---
>         if (!Character.isDigit(lastChar) && lastChar != '.') {
1387a1388,1395
>             if (chars[i] == '.') {
>                 if (hasDecPoint || hasExp) {
>                     // two decimal points or dec in exponent
>                     return false;
>                 }
>                 // single trailing decimal point after non-exponent is ok
>                 return foundDigit;
>             }
```

- Deleted lines: 1<br />
- Added lines: 9<br />
- Diff added/deleted: 8

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 491 | org.apache.commons.lang3.math.NumberUtils:491 -> 0.8164965809277261 (ep: 1, ef: 2, np: 1625, nf: 0) | 42 |

- Nb. undetected lines: 1/2 ( 1387 )

## Bug 37

- Nb. modified sources: 1

- Nb. nopol ranking entries: 5

###  org.apache.commons.lang3.ArrayUtils

```
2959,2960c2959,2960
<         T[] joinedArray = (T[]) Array.newInstance(array1.getClass().getComponentType(),
<                                                             array1.length + array2.length);
---
>         final Class<?> type1 = array1.getClass().getComponentType();
>         T[] joinedArray = (T[]) Array.newInstance(type1, array1.length + array2.length);
2961a2962
>         try {
2962a2964,2971
>         } catch (ArrayStoreException ase) {
>             // Check if problem is incompatible types
>             final Class<?> type2 = array2.getClass().getComponentType();
>             if (!type1.isAssignableFrom(type2)){
>                 throw new IllegalArgumentException("Cannot store "+type2.getName()+" in an array of "+type1.getName());
>             }
>             throw ase; // No, so rethrow original
>         }
```

- Deleted lines: 4<br />
- Added lines: 11<br />
- Diff added/deleted: 7

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 2959 | org.apache.commons.lang3.ArrayUtils:2959 -> 0.5 (ep: 3, ef: 1, np: 1623, nf: 0) | 3 |
| 2961 | org.apache.commons.lang3.ArrayUtils:2961 -> 0.5 (ep: 3, ef: 1, np: 1623, nf: 0) | 4 |
| 2962 | org.apache.commons.lang3.ArrayUtils:2962 -> 0.5 (ep: 3, ef: 1, np: 1623, nf: 0) | 5 |

- Nb. undetected lines: 1/4 ( 2960 )

## Bug 38

- Nb. modified sources: 1

- Nb. nopol ranking entries: 143

###  org.apache.commons.lang3.time.FastDateFormat

```
871a872
>             calendar.getTime(); /// LANG-538
```

- Deleted lines: 0<br />
- Added lines: 1<br />
- Diff added/deleted: 1

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 871 | org.apache.commons.lang3.time.FastDateFormat:871 -> 0.17149858514250882 (ep: 33, ef: 1, np: 1590, nf: 0) | 137 |

- Nb. undetected lines: 0/1

## Bug 39

- Nb. modified sources: 1

- Nb. nopol ranking entries: 55

###  org.apache.commons.lang3.StringUtils

```
3675a3676,3678
>             if (searchList[i] == null || replacementList[i] == null) {
>                 continue;
>             }
```

- Deleted lines: 0<br />
- Added lines: 3<br />
- Diff added/deleted: 3

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 3675 | org.apache.commons.lang3.StringUtils:3675 -> 0.7071067811865475 (ep: 2, ef: 2, np: 1615, nf: -1) | 27 |

- Nb. undetected lines: 0/1

## Bug 40

- Nb. modified sources: 1

- Nb. nopol ranking entries: 3

###  org.apache.commons.lang.StringUtils

```
1048c1048,1055
<         return contains(str.toUpperCase(), searchStr.toUpperCase());
---
>         int len = searchStr.length();
>         int max = str.length() - len;
>         for (int i = 0; i <= max; i++) {
>             if (str.regionMatches(true, i, searchStr, 0, len)) {
>                 return true;
>             }
>         }
>         return false;
```

- Deleted lines: 2<br />
- Added lines: 8<br />
- Diff added/deleted: 6

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 1048 | org.apache.commons.lang.StringUtils:1048 -> 0.7071067811865475 (ep: 1, ef: 1, np: 1578, nf: 63) | 2 |

- Nb. undetected lines: 0/1

## Bug 41

- Nb. modified sources: 1

- Nb. nopol ranking entries: 13

###  org.apache.commons.lang.ClassUtils

```
190a191,208
>         StringBuffer arrayPrefix = new StringBuffer();
> 
>         // Handle array encoding
>         if (className.startsWith("[")) {
>             while (className.charAt(0) == '[') {
>                 className = className.substring(1);
>                 arrayPrefix.append("[]");
>             }
>             // Strip Object type encoding
>             if (className.charAt(0) == 'L' && className.charAt(className.length() - 1) == ';') {
>                 className = className.substring(1, className.length() - 1);
>             }
>         }
> 
>         if (reverseAbbreviationMap.containsKey(className)) {
>             className = reverseAbbreviationMap.get(className);
>         }
> 
198c216
<         return out;
---
>         return out + arrayPrefix;
227c245
<         return cls.getPackage().getName();
---
>         return getPackageName(cls.getName());
240c258
<         if (className == null) {
---
>         if (className == null || className.length() == 0) {
242a261,270
> 
>         // Strip array encoding
>         while (className.charAt(0) == '[') {
>             className = className.substring(1);
>         }
>         // Strip Object type encoding
>         if (className.charAt(0) == 'L' && className.charAt(className.length() - 1) == ';') {
>             className = className.substring(1);
>         }
> 
```

- Deleted lines: 3<br />
- Added lines: 31<br />
- Diff added/deleted: 28

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 198 | org.apache.commons.lang.ClassUtils:198 -> 0.12909944487358055 (ep: 29, ef: 1, np: 1530, nf: 64) | 14 |
| 227 | org.apache.commons.lang.ClassUtils:227 -> 0.5 (ep: 1, ef: 1, np: 1558, nf: 64) | 4 |

- Nb. undetected lines: 3/5 ( 190 240 242 )

## Bug 42

- Nb. modified sources: 1

- Nb. nopol ranking entries: 69

###  org.apache.commons.lang.Entities

```
828c828
<             char c = str.charAt(i);
---
>             int c = Character.codePointAt(str, i); 
831c831,836
<                 if (c > 0x7F) {
---
>                 if (c >= 0x010000 && i < len - 1) {
>                     writer.write("&#");
>                     writer.write(Integer.toString(c, 10));
>                     writer.write(';');
>                     i++;
>                 } else if (c > 0x7F) { 
```

- Deleted lines: 3<br />
- Added lines: 8<br />
- Diff added/deleted: 5

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 828 | org.apache.commons.lang.Entities:828 -> 0.3779644730092272 (ep: 6, ef: 1, np: 1833, nf: 63) | 23 |
| 831 | org.apache.commons.lang.Entities:831 -> 0.4472135954999579 (ep: 4, ef: 1, np: 1835, nf: 63) | 13 |

- Nb. undetected lines: 0/2

## Bug 43

- Nb. modified sources: 1

- Nb. nopol ranking entries: 26

###  org.apache.commons.lang.text.ExtendedMessageFormat

```
421a422
>             next(pos);
```

- Deleted lines: 0<br />
- Added lines: 1<br />
- Diff added/deleted: 1

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 421 | org.apache.commons.lang.text.ExtendedMessageFormat:421 -> 1.0 (ep: 0, ef: 1, np: 1838, nf: 63) | 5 |

- Nb. undetected lines: 0/1

## Bug 44

- Nb. modified sources: 1

- Nb. nopol ranking entries: 21

###  org.apache.commons.lang.NumberUtils

```
144a145,147
>         if (val.length() == 1 && !Character.isDigit(val.charAt(0))) {
>             throw new NumberFormatException(val + " is not a valid number.");
>         }
```

- Deleted lines: 0<br />
- Added lines: 3<br />
- Diff added/deleted: 3


- Nb. undetected lines: 1/1 ( 144 )

## Bug 45

- Nb. modified sources: 1

- Nb. nopol ranking entries: 23

###  org.apache.commons.lang.WordUtils

```
613a614,618
>         // if the lower value is greater than the length of the string,
>         // set to the length of the string
>         if (lower > str.length()) {
>             lower = str.length();    
>         }
```

- Deleted lines: 0<br />
- Added lines: 5<br />
- Diff added/deleted: 5


- Nb. undetected lines: 1/1 ( 613 )

## Bug 46

- Nb. modified sources: 1

- Nb. nopol ranking entries: 20

###  org.apache.commons.lang.StringEscapeUtils

```
86c86
<         return escapeJavaStyleString(str, false);
---
>         return escapeJavaStyleString(str, false, false);
102c102
<         escapeJavaStyleString(out, str, false);
---
>         escapeJavaStyleString(out, str, false, false);
127c127
<         return escapeJavaStyleString(str, true);
---
>         return escapeJavaStyleString(str, true, true);
143c143
<         escapeJavaStyleString(out, str, true);
---
>         escapeJavaStyleString(out, str, true, true);
150a151
>      * @param escapeForwardSlash TODO
153c154
<     private static String escapeJavaStyleString(String str, boolean escapeSingleQuotes) {
---
>     private static String escapeJavaStyleString(String str, boolean escapeSingleQuotes, boolean escapeForwardSlash) {
159c160
<             escapeJavaStyleString(writer, str, escapeSingleQuotes);
---
>             escapeJavaStyleString(writer, str, escapeSingleQuotes, escapeForwardSlash);
173a175
>      * @param escapeForwardSlash TODO
176c178,179
<     private static void escapeJavaStyleString(Writer out, String str, boolean escapeSingleQuote) throws IOException {
---
>     private static void escapeJavaStyleString(Writer out, String str, boolean escapeSingleQuote,
>             boolean escapeForwardSlash) throws IOException {
197c200
<                     case '\b':
---
>                     case '\b' :
201c204
<                     case '\n':
---
>                     case '\n' :
205c208
<                     case '\t':
---
>                     case '\t' :
209c212
<                     case '\f':
---
>                     case '\f' :
213c216
<                     case '\r':
---
>                     case '\r' :
227c230
<                     case '\'':
---
>                     case '\'' :
233c236
<                     case '"':
---
>                     case '"' :
237c240
<                     case '\\':
---
>                     case '\\' :
241c244,245
<                     case '/':
---
>                     case '/' :
>                         if (escapeForwardSlash) {
242a247
>                         }
```

- Deleted lines: 16<br />
- Added lines: 21<br />
- Diff added/deleted: 5

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 86 | org.apache.commons.lang.StringEscapeUtils:86 -> 0.5 (ep: 3, ef: 1, np: 1762, nf: 63) | 4 |
| 159 | org.apache.commons.lang.StringEscapeUtils:159 -> 0.4472135954999579 (ep: 4, ef: 1, np: 1761, nf: 63) | 7 |
| 242 | org.apache.commons.lang.StringEscapeUtils:242 -> 0.7071067811865475 (ep: 1, ef: 1, np: 1764, nf: 63) | 1 |

- Nb. undetected lines: 16/19 ( 102 127 143 150 153 173 176 197 201 205 209 213 227 233 237 241 )

## Bug 47

- Nb. modified sources: 1

- Nb. nopol ranking entries: 16

###  org.apache.commons.lang.text.StrBuilder

```
1185a1186,1188
>             if (str == null) {
>                 str = "";
>             }
1229a1233,1235
>             if (str == null) {
>                 str = "";
>             }
```

- Deleted lines: 0<br />
- Added lines: 6<br />
- Diff added/deleted: 6

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 1185 | org.apache.commons.lang.text.StrBuilder:1185 -> 0.4082482904638631 (ep: 2, ef: 1, np: 1762, nf: 64) | 4 |
| 1229 | org.apache.commons.lang.text.StrBuilder:1229 -> 0.35355339059327373 (ep: 3, ef: 1, np: 1761, nf: 64) | 8 |

- Nb. undetected lines: 0/2

## Bug 48

- Nb. modified sources: 1

- Nb. nopol ranking entries: 11

###  org.apache.commons.lang.builder.EqualsBuilder

```
379a380,382
>             if (lhs instanceof java.math.BigDecimal) {
>                 isEquals = (((java.math.BigDecimal)lhs).compareTo(rhs) == 0);
>             } else {
381a385
>             }
```

- Deleted lines: 0<br />
- Added lines: 4<br />
- Diff added/deleted: 4

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 379 | org.apache.commons.lang.builder.EqualsBuilder:379 -> 0.14744195615489714 (ep: 45, ef: 1, np: 1655, nf: 63) | 7 |
| 381 | org.apache.commons.lang.builder.EqualsBuilder:381 -> 0.22360679774997896 (ep: 19, ef: 1, np: 1681, nf: 63) | 2 |

- Nb. undetected lines: 0/2

## Bug 49

- Nb. modified sources: 1

- Nb. nopol ranking entries: 33

###  org.apache.commons.lang.math.Fraction

```
465a466,468
>         if (numerator == 0) {
>             return equals(ZERO) ? this : ZERO;
>         }
```

- Deleted lines: 0<br />
- Added lines: 3<br />
- Diff added/deleted: 3


- Nb. undetected lines: 1/1 ( 465 )

## Bug 50

- Nb. modified sources: 1

- Nb. nopol ranking entries: 155

###  org.apache.commons.lang.time.FastDateFormat

```
284,286d283
<         if (locale != null) {
<             key = new Pair(key, locale);
<         }
288,289d284
<         FastDateFormat format = (FastDateFormat) cDateInstanceCache.get(key);
<         if (format == null) {
293a289,292
>         key = new Pair(key, locale);
> 
>         FastDateFormat format = (FastDateFormat) cDateInstanceCache.get(key);
>         if (format == null) {
464,469d462
<         if (locale != null) {
<             key = new Pair(key, locale);
<         }
< 
<         FastDateFormat format = (FastDateFormat) cDateTimeInstanceCache.get(key);
<         if (format == null) {
472a466
>         key = new Pair(key, locale);
473a468,469
>         FastDateFormat format = (FastDateFormat) cDateTimeInstanceCache.get(key);
>         if (format == null) {
```

- Deleted lines: 11<br />
- Added lines: 7<br />
- Diff added/deleted: -4

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 284 | org.apache.commons.lang.time.FastDateFormat:284 -> 0.5 (ep: 1, ef: 1, np: 1748, nf: 64) | 36 |
| 285 | org.apache.commons.lang.time.FastDateFormat:285 -> 0.5 (ep: 1, ef: 1, np: 1748, nf: 64) | 37 |
| 288 | org.apache.commons.lang.time.FastDateFormat:288 -> 0.5 (ep: 1, ef: 1, np: 1748, nf: 64) | 38 |
| 289 | org.apache.commons.lang.time.FastDateFormat:289 -> 0.5 (ep: 1, ef: 1, np: 1748, nf: 64) | 39 |
| 464 | org.apache.commons.lang.time.FastDateFormat:464 -> 0.7071067811865475 (ep: 0, ef: 1, np: 1749, nf: 64) | 12 |
| 465 | org.apache.commons.lang.time.FastDateFormat:465 -> 0.7071067811865475 (ep: 0, ef: 1, np: 1749, nf: 64) | 13 |
| 468 | org.apache.commons.lang.time.FastDateFormat:468 -> 0.7071067811865475 (ep: 0, ef: 1, np: 1749, nf: 64) | 14 |
| 469 | org.apache.commons.lang.time.FastDateFormat:469 -> 0.7071067811865475 (ep: 0, ef: 1, np: 1749, nf: 64) | 15 |

- Nb. undetected lines: 6/14 ( 286 293 466 467 472 473 )

## Bug 51

- Nb. modified sources: 1

- Nb. nopol ranking entries: 18

###  org.apache.commons.lang.BooleanUtils

```
681a682
>                 return false;
```

- Deleted lines: 0<br />
- Added lines: 1<br />
- Diff added/deleted: 1


- Nb. undetected lines: 1/1 ( 681 )

## Bug 52

- Nb. modified sources: 1

- Nb. nopol ranking entries: 27

###  org.apache.commons.lang.StringEscapeUtils

```
235a236,239
>                     case '/':
>                         out.write('\\');
>                         out.write('/');
>                         break;
```

- Deleted lines: 0<br />
- Added lines: 4<br />
- Diff added/deleted: 4


- Nb. undetected lines: 1/1 ( 235 )

## Bug 53

- Nb. modified sources: 1

- Nb. nopol ranking entries: 41

###  org.apache.commons.lang.time.DateUtils

```
642a643
>         }
646d646
<         }
651a652
>         }
655d655
<         }
```

- Deleted lines: 2<br />
- Added lines: 2<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 642 | org.apache.commons.lang.time.DateUtils:642 -> 0.4082482904638631 (ep: 5, ef: 1, np: 1649, nf: 63) | 15 |

- Nb. undetected lines: 3/4 ( 646 651 655 )

## Bug 54

- Nb. modified sources: 1

- Nb. nopol ranking entries: 13

###  org.apache.commons.lang.LocaleUtils

```
113a114,116
>             if (ch3 == '_') {
>                 return new Locale(str.substring(0, 2), "", str.substring(4));
>             }
```

- Deleted lines: 0<br />
- Added lines: 3<br />
- Diff added/deleted: 3

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 113 | org.apache.commons.lang.LocaleUtils:113 -> 0.5773502691896258 (ep: 2, ef: 1, np: 1644, nf: 63) | 3 |

- Nb. undetected lines: 0/1

## Bug 55

- Nb. modified sources: 1

- Nb. nopol ranking entries: 21

###  org.apache.commons.lang.time.StopWatch

```
117a118
>         if(this.runningState == STATE_RUNNING) {
118a120
>         }
```

- Deleted lines: 0<br />
- Added lines: 2<br />
- Diff added/deleted: 2

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 118 | org.apache.commons.lang.time.StopWatch:118 -> 0.4472135954999579 (ep: 4, ef: 1, np: 1642, nf: 63) | 7 |

- Nb. undetected lines: 1/2 ( 117 )

## Bug 56

- Nb. modified sources: 1

- Nb. nopol ranking entries: 66

###  org.apache.commons.lang.time.FastDateFormat

```
140c140
<     private Rule[] mRules;
---
>     private transient Rule[] mRules;
144c144
<     private int mMaxLengthEstimate;
---
>     private transient int mMaxLengthEstimate;
1019a1020,1026
>     // Serializing
>     //-----------------------------------------------------------------------
>     private void readObject(ObjectInputStream in) throws IOException, ClassNotFoundException {
>         in.defaultReadObject();
>         init();
>     }
>     
```

- Deleted lines: 2<br />
- Added lines: 9<br />
- Diff added/deleted: 7


- Nb. undetected lines: 3/3 ( 140 144 1019 )

## Bug 57

- Nb. modified sources: 1

- Nb. nopol ranking entries: 0

###  org.apache.commons.lang.LocaleUtils

```
223c223
<         return cAvailableLocaleSet.contains(locale);
---
>         return availableLocaleList().contains(locale);
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 223 | org.apache.commons.lang.LocaleUtils:223 -> 1.0 (ep: 0, ef: 11, np: 1617, nf: 62) | 1 |

- Nb. undetected lines: 0/1

## Bug 58

- Nb. modified sources: 1

- Nb. nopol ranking entries: 36

###  org.apache.commons.lang.math.NumberUtils

```
454,455c454
<                         && isDigits(numeric.substring(1))
<                         && (numeric.charAt(0) == '-' || Character.isDigit(numeric.charAt(0)))) {
---
>                         && (numeric.charAt(0) == '-' && isDigits(numeric.substring(1)) || isDigits(numeric))) {
```

- Deleted lines: 2<br />
- Added lines: 1<br />
- Diff added/deleted: -1


- Nb. undetected lines: 2/2 ( 454 455 )

## Bug 59

- Nb. modified sources: 1

- Nb. nopol ranking entries: 11

###  org.apache.commons.lang.text.StrBuilder

```
884c884
<                 str.getChars(0, strLen, buffer, size);
---
>                 str.getChars(0, width, buffer, size);
```

- Deleted lines: 1<br />
- Added lines: 1<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 884 | org.apache.commons.lang.text.StrBuilder:884 -> 0.5773502691896258 (ep: 2, ef: 1, np: 1622, nf: 62) | 6 |

- Nb. undetected lines: 0/1

## Bug 60

- Nb. modified sources: 1

- Nb. nopol ranking entries: 44

###  org.apache.commons.lang.text.StrBuilder

```
1673c1673
<         for (int i = 0; i < thisBuf.length; i++) {
---
>         for (int i = 0; i < this.size; i++) {
1730c1730
<         for (int i = startIndex; i < thisBuf.length; i++) {
---
>         for (int i = startIndex; i < size; i++) {
```

- Deleted lines: 4<br />
- Added lines: 2<br />
- Diff added/deleted: -2

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 1673 | org.apache.commons.lang.text.StrBuilder:1673 -> 0.7071067811865475 (ep: 2, ef: 2, np: 1619, nf: 61) | 2 |

- Nb. undetected lines: 1/2 ( 1730 )

## Bug 61

- Nb. modified sources: 1

- Nb. nopol ranking entries: 45

###  org.apache.commons.lang.text.StrBuilder

```
1775a1776
>         int len = size - strLen + 1;
1777c1778
<         for (int i = startIndex; i < thisBuf.length - strLen; i++) {
---
>         for (int i = startIndex; i < len; i++) {
```

- Deleted lines: 2<br />
- Added lines: 2<br />
- Diff added/deleted: 0

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 1775 | org.apache.commons.lang.text.StrBuilder:1775 -> 0.47140452079103173 (ep: 7, ef: 2, np: 1612, nf: 62) | 20 |
| 1777 | org.apache.commons.lang.text.StrBuilder:1777 -> 0.47140452079103173 (ep: 14, ef: 4, np: 1605, nf: 60) | 21 |

- Nb. undetected lines: 0/2

## Bug 62

- Nb. modified sources: 1

- Nb. nopol ranking entries: 62

###  org.apache.commons.lang.Entities

```
849a850,852
>                             if (entityValue > 0xFFFF) {
>                                 entityValue = -1;
>                             }
919a923
>                                         break;
924a929,931
>                                 if (entityValue > 0xFFFF) {
>                                     entityValue = -1;
>                                 }
926c933
<                                 // ignore the escaped value content
---
>                                 entityValue = -1;
```

- Deleted lines: 1<br />
- Added lines: 8<br />
- Diff added/deleted: 7


- Nb. undetected lines: 4/4 ( 849 919 924 926 )

## Bug 63

- Nb. modified sources: 1

- Nb. nopol ranking entries: 110

###  org.apache.commons.lang.time.DurationFormatUtils

```
306c306,312
<             days += 31; // such overshooting is taken care of later on
---
>             end.add(Calendar.MONTH, -1);
>             days += end.getActualMaximum(Calendar.DAY_OF_MONTH);
> //days += 31; // TODO: Need tests to show this is bad and the new code is good.
> // HEN: It's a tricky subject. Jan 15th to March 10th. If I count days-first it is 
> // 1 month and 26 days, but if I count month-first then it is 1 month and 23 days.
> // Also it's contextual - if asked for no M in the format then I should probably 
> // be doing no calculating here.
307a314
>             end.add(Calendar.MONTH, 1);
314,322d320
<         // take estimates off of end to see if we can equal start, when it overshoots recalculate
<         milliseconds -= reduceAndCorrect(start, end, Calendar.MILLISECOND, milliseconds);
<         seconds -= reduceAndCorrect(start, end, Calendar.SECOND, seconds);
<         minutes -= reduceAndCorrect(start, end, Calendar.MINUTE, minutes);
<         hours -= reduceAndCorrect(start, end, Calendar.HOUR_OF_DAY, hours);
<         days -= reduceAndCorrect(start, end, Calendar.DAY_OF_MONTH, days);
<         months -= reduceAndCorrect(start, end, Calendar.MONTH, months);
<         years -= reduceAndCorrect(start, end, Calendar.YEAR, years);
< 
430,452d427
<     /**
<      * Reduces by difference, then if it overshot, calculates the overshot amount and 
<      * fixes and returns the amount to change by.
<      *
<      * @param start Start of period being formatted
<      * @param end End of period being formatted
<      * @param field Field to reduce, as per constants in {@link java.util.Calendar}
<      * @param difference amount to reduce by
<      * @return int reduced value
<      */
<     static int reduceAndCorrect(Calendar start, Calendar end, int field, int difference) {
<         end.add( field, -1 * difference );
<         int endValue = end.get(field);
<         int startValue = start.get(field);
<         if (endValue < startValue) {
<             int newdiff = startValue - endValue;
<             end.add( field, newdiff );
<             return newdiff;
<         } else {
<             return 0;
<         }
<     }
< 
```

- Deleted lines: 33<br />
- Added lines: 8<br />
- Diff added/deleted: -25

| Line | Nopol log | Nopol rank |
|------|-----------|------|
| 306 | org.apache.commons.lang.time.DurationFormatUtils:306 -> 1.0 (ep: 0, ef: 1, np: 1608, nf: 62) | 1 |
| 307 | org.apache.commons.lang.time.DurationFormatUtils:307 -> 1.0 (ep: 0, ef: 1, np: 1608, nf: 62) | 2 |
| 315 | org.apache.commons.lang.time.DurationFormatUtils:315 -> 0.5773502691896258 (ep: 2, ef: 1, np: 1606, nf: 62) | 40 |
| 316 | org.apache.commons.lang.time.DurationFormatUtils:316 -> 0.5773502691896258 (ep: 2, ef: 1, np: 1606, nf: 62) | 41 |
| 317 | org.apache.commons.lang.time.DurationFormatUtils:317 -> 0.5773502691896258 (ep: 2, ef: 1, np: 1606, nf: 62) | 42 |
| 318 | org.apache.commons.lang.time.DurationFormatUtils:318 -> 0.5773502691896258 (ep: 2, ef: 1, np: 1606, nf: 62) | 43 |
| 319 | org.apache.commons.lang.time.DurationFormatUtils:319 -> 0.5773502691896258 (ep: 2, ef: 1, np: 1606, nf: 62) | 44 |
| 320 | org.apache.commons.lang.time.DurationFormatUtils:320 -> 0.5773502691896258 (ep: 2, ef: 1, np: 1606, nf: 62) | 45 |
| 321 | org.apache.commons.lang.time.DurationFormatUtils:321 -> 0.5773502691896258 (ep: 2, ef: 1, np: 1606, nf: 62) | 46 |
| 441 | org.apache.commons.lang.time.DurationFormatUtils:441 -> 0.5773502691896258 (ep: 2, ef: 1, np: 1606, nf: 62) | 54 |
| 442 | org.apache.commons.lang.time.DurationFormatUtils:442 -> 0.5773502691896258 (ep: 2, ef: 1, np: 1606, nf: 62) | 55 |
| 443 | org.apache.commons.lang.time.DurationFormatUtils:443 -> 0.5773502691896258 (ep: 2, ef: 1, np: 1606, nf: 62) | 56 |
| 444 | org.apache.commons.lang.time.DurationFormatUtils:444 -> 0.5773502691896258 (ep: 2, ef: 1, np: 1606, nf: 62) | 57 |
| 445 | org.apache.commons.lang.time.DurationFormatUtils:445 -> 1.0 (ep: 0, ef: 1, np: 1608, nf: 62) | 5 |
| 446 | org.apache.commons.lang.time.DurationFormatUtils:446 -> 1.0 (ep: 0, ef: 1, np: 1608, nf: 62) | 6 |
| 447 | org.apache.commons.lang.time.DurationFormatUtils:447 -> 1.0 (ep: 0, ef: 1, np: 1608, nf: 62) | 7 |
| 449 | org.apache.commons.lang.time.DurationFormatUtils:449 -> 0.5773502691896258 (ep: 2, ef: 1, np: 1606, nf: 62) | 58 |

- Nb. undetected lines: 17/34 ( 314 322 430 431 432 433 434 435 436 437 438 439 440 448 450 451 452 )

## Bug 64

- Nb. modified sources: 1

- Nb. nopol ranking entries: 41

###  org.apache.commons.lang.enums.ValuedEnum

```
182a183,192
>         if (other == this) {
>             return 0;
>         }
>         if (other.getClass() != this.getClass()) {
>             if (other.getClass().getName().equals(this.getClass().getName())) {
>                 return iValue - getValueInOtherClassLoader(other);
>             }
>             throw new ClassCastException(
>                     "Different enum class '" + ClassUtils.getShortClassName(other.getClass()) + "'");
>         }
186a197,217
>      * <p>Use reflection to return an objects value.</p>
>      *
>      * @param other  the object to determine the value for
>      * @return the value
>      */
>     private int getValueInOtherClassLoader(Object other) {
>         try {
>             Method mth = other.getClass().getMethod("getValue", null);
>             Integer value = (Integer) mth.invoke(other, null);
>             return value.intValue();
>         } catch (NoSuchMethodException e) {
>             // ignore - should never happen
>         } catch (IllegalAccessException e) {
>             // ignore - should never happen
>         } catch (InvocationTargetException e) {
>             // ignore - should never happen
>         }
>         throw new IllegalStateException("This should not happen");
>     }
> 
>     /**
```

- Deleted lines: 1<br />
- Added lines: 31<br />
- Diff added/deleted: 30


- Nb. undetected lines: 2/2 ( 182 186 )

## Bug 65

- Nb. modified sources: 1

- Nb. nopol ranking entries: 22

###  org.apache.commons.lang.time.DateUtils

```
623a624,668
>         if (field == Calendar.MILLISECOND) {
>             return;
>         }
> 
>         // ----------------- Fix for LANG-59 ---------------------- START ---------------
>         // see http://issues.apache.org/jira/browse/LANG-59
>         //
>         // Manually truncate milliseconds, seconds and minutes, rather than using
>         // Calendar methods.
> 
>         Date date = val.getTime();
>         long time = date.getTime();
>         boolean done = false;
> 
>         // truncate milliseconds
>         int millisecs = val.get(Calendar.MILLISECOND);
>         if (!round || millisecs < 500) {
>             time = time - millisecs;
>             if (field == Calendar.SECOND) {
>                 done = true;
>             }
>         }
> 
>         // truncate seconds
>         int seconds = val.get(Calendar.SECOND);
>         if (!done && (!round || seconds < 30)) {
>             time = time - (seconds * 1000L);
>             if (field == Calendar.MINUTE) {
>                 done = true;
>             }
>         }
> 
>         // truncate minutes
>         int minutes = val.get(Calendar.MINUTE);
>         if (!done && (!round || minutes < 30)) {
>             time = time - (minutes * 60000L);
>         }
> 
>         // reset time
>         if (date.getTime() != time) {
>             date.setTime(time);
>             val.setTime(date);
>         }
>         // ----------------- Fix for LANG-59 ----------------------- END ----------------
> 
691a737
>             if (offset != 0) {
693a740
>         }
```

- Deleted lines: 3<br />
- Added lines: 47<br />
- Diff added/deleted: 44


- Nb. undetected lines: 3/3 ( 623 691 693 )

