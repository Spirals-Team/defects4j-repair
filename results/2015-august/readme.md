# Summary

BugId             | NopolPC   | NopolC    | BrutpolPC | BrutpolC  | Genprog   | Kali      | Total
----------------- | --------- | --------- | --------- | --------- | --------- | --------- | ------
[C1](#chart-1)    | TIMEOUT   | TIMEOUT   | No        | No        | Yes       | Yes       |      2
[C3](#chart-3)    | TIMEOUT   | Yes       | No        | No        | Yes       | No       |      2
[C4](#chart-4)    | TIMEOUT   | TIMEOUT   | Yes       | No        | No       | No       |      1
[C5](#chart-5)    | TIMEOUT   | Yes       | No        | Yes       | Yes       | Yes       |      4
[C6](#chart-6)    | Yes       | Yes       | Yes       | Yes       | Yes       | No       |      5
[C7](#chart-7)    | TIMEOUT   | TIMEOUT   | No        | No        | Yes       | No       |      1
[C8](#chart-8)    | TIMEOUT   | No        | No        | No        | Yes       | TIMEOUT   |      1
[C9](#chart-9)    | TIMEOUT   | TIMEOUT   | Yes       | Yes       | Yes       | No       |      3
[C13](#chart-13)  | Yes       | Yes       | Yes       | No        | Yes       | Yes       |      5
[C15](#chart-15)  | TIMEOUT   | TIMEOUT   | No        | No        | Yes       | Yes       |      2
[C17](#chart-17)  | TIMEOUT   | No        | Yes       | Yes       | No       | No       |      2
[C21](#chart-21)  | Yes       | Yes       | No        | No        | Yes       | Yes       |      4
[C25](#chart-25)  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes       |      6
[C26](#chart-26)  | Yes       | Yes       | No        | Yes       | No    | Yes       |      4
[L39](#lang-39)   | Yes       | No        | Yes       | No        | No       | No       |      2
[L44](#lang-44)   | Yes       | Yes       | No        | No        | No    | No    |      2
[L46](#lang-46)   | Yes       | No        | No        | No        | No    | No    |      1
[L51](#lang-51)   | No        | Yes       | No        | No        | No    | No    |      1
[L53](#lang-53)   | Yes       | TIMEOUT   | No        | No        | No       | No       |      1
[L55](#lang-55)   | Yes       | No        | No        | No        | No    | No    |      1
[L58](#lang-58)   | Yes       | Yes       | No        | No        | No       | No       |      2
[M2](#math-2)     | TIMEOUT   | TIMEOUT   | TIMEOUT   | ERROR     | Yes       | Yes       |      2
[M5](#math-5)     | TIMEOUT   | No        | No        | No        | Yes       | No       |      1
[M8](#math-8)     | TIMEOUT   | No        | No        | No        | Yes       | Yes       |      2
[M28](#math-28)   | No        | TIMEOUT   | No        | No        | Yes       | Yes       |      2
[M32](#math-32)   | Yes       | No        | No        | Yes       | No    | Yes       |      3
[M33](#math-33)   | Yes       | Yes       | Yes       | No        | No       | No       |      3
[M40](#math-40)   | No        | Yes       | No        | No        | Yes       | Yes       |      3
[M41](#math-41)   | No       | No       | Yes       | Yes       | No       | No       |      2
[M42](#math-42)   | Yes       | TIMEOUT   | Yes       | Yes       | No       | No       |      3
[M44](#math-44)   | TIMEOUT   | No        | No        | No        | Yes       | Yes       |      2
[M46](#math-46)   | No        | No        | Yes       | No        | No       | No       |      1
[M49](#math-49)   | Yes       | Yes       | Yes       | No        | Yes       | Yes       |      5
[M50](#math-50)   | Yes       | Yes       | Yes       | No        | Yes       | Yes       |      5
[M53](#math-53)   | No        | No        | No        | No        | Yes       | No       |      1
[M56](#math-56)   | No        | No        | No        | No        | Yes       | No       |      1
[M57](#math-57)   | Yes       | Yes       | No        | No        | No       | No       |      2
[M58](#math-58)   | Yes       | Yes       | Yes       | ERROR     | No    | TIMEOUT   |      3
[M69](#math-69)   | Yes       | No        | No        | No        | No       | No       |      1
[M70](#math-70)   | No        | No        | No        | No        | Yes       | No       |      1
[M71](#math-71)   | No        | Yes       | Yes       | No        | Yes       | TIMEOUT   |      3
[M73](#math-73)   | No        | Yes       | No        | No        | Yes       | No       |      2
[M78](#math-78)   | Yes       | TIMEOUT   | Yes       | No        | Yes       | Yes       |      4
[M80](#math-80)   | Yes       | TIMEOUT   | No        | No        | Yes       | Yes       |      3
[M81](#math-81)   | Yes       | Yes       | TIMEOUT   | TIMEOUT   | Yes       | Yes       |      4
[M82](#math-82)   | Yes       | No        | No        | No        | Yes       | Yes       |      3
[M84](#math-84)   | No        | No        | No        | No        | Yes       | Yes       |      2
[M85](#math-85)   | Yes       | Yes       | Yes       | Yes       | Yes       | Yes       |      6
[M87](#math-87)   | Yes       | Yes       | Yes       | No        | No       | No       |      3
[M88](#math-88)   | Yes       | No        | Yes       | No        | No       | No       |      2
[M95](#math-95)   | TIMEOUT   | No        | No        | No        | Yes       | Yes       |      2
[M96](#math-96)   | No        | No        | No        | Yes       | No       | No       |      1
[M97](#math-97)   | Yes       | Yes       | Yes       | Yes       | No       | No       |      4
[M99](#math-99)   | Yes       | Yes       | Yes       | Yes       | No       | No       |      4
[M104](#math-104) | No        | Yes       | No        | No        | No    | No       |      1
[M105](#math-105) | Yes       | No        | Yes       | No        | No       | No       |      2
[T4](#time-4)     | No        | No        | No        | No        | Yes       | Yes       |      2
[T7](#time-7)     | TIMEOUT   | TIMEOUT   | Yes       | ERROR     | No       | No       |      1
[T11](#time-11)   | Yes       | Yes       | Yes       | Yes       | Yes       | Yes       |      6
Total             | 30 (13%)  | 25 (11%)  | 24 (10%)  | 14 (6%)   | 33 (14%)  | 24 (10%)  |    150
Fixed bugs: 59/224 (26%)

Nb bugs ends with an execution error: 15

Nb bugs ends with an empty log: 0

Nb bugs ends with the Grid5000 timeout: 149

Total execution time: 36 days, 23:03:34.852000
# Complete data

BugId             | NopolPC   | NopolC    | BrutpolPC | BrutpolC  | Genprog   | Kali      | Total
----------------- | --------- | --------- | --------- | --------- | --------- | --------- | ------
[C1](#chart-1)    | TIMEOUT   | TIMEOUT   | No        | No        | Yes       | Yes       |      2
[C2](#chart-2)    | TIMEOUT   | TIMEOUT   | No        | No        | No       | No       |      0
[C3](#chart-3)    | TIMEOUT   | Yes       | No        | No        | Yes       | No       |      2
[C4](#chart-4)    | TIMEOUT   | TIMEOUT   | Yes       | No        | No       | No       |      1
[C5](#chart-5)    | TIMEOUT   | Yes       | No        | Yes       | Yes       | Yes       |      4
[C6](#chart-6)    | Yes       | Yes       | Yes       | Yes       | Yes       | No       |      5
[C7](#chart-7)    | TIMEOUT   | TIMEOUT   | No        | No        | Yes       | No       |      1
[C8](#chart-8)    | TIMEOUT   | No        | No        | No        | Yes       | TIMEOUT   |      1
[C9](#chart-9)    | TIMEOUT   | TIMEOUT   | Yes       | Yes       | Yes       | No       |      3
[C10](#chart-10)  | TIMEOUT   | No        | No        | No        | No       | No       |      0
[C11](#chart-11)  | TIMEOUT   | TIMEOUT   | No        | No        | No       | No       |      0
[C12](#chart-12)  | TIMEOUT   | No        | No        | No        | No       | No       |      0
[C13](#chart-13)  | Yes       | Yes       | Yes       | No        | Yes       | Yes       |      5
[C14](#chart-14)  | TIMEOUT   | No        | No        | No        | No       | No       |      0
[C15](#chart-15)  | TIMEOUT   | TIMEOUT   | No        | No        | Yes       | Yes       |      2
[C16](#chart-16)  | TIMEOUT   | TIMEOUT   | No        | No        | No       | No       |      0
[C17](#chart-17)  | TIMEOUT   | No        | Yes       | Yes       | No       | No       |      2
[C18](#chart-18)  | TIMEOUT   | No        | No        | No        | No       | No       |      0
[C19](#chart-19)  | TIMEOUT   | No        | No        | No        | No       | No       |      0
[C20](#chart-20)  | TIMEOUT   | No        | No        | No        | No       | No       |      0
[C21](#chart-21)  | Yes       | Yes       | No        | No        | Yes       | Yes       |      4
[C22](#chart-22)  | TIMEOUT   | No        | No        | No        | No       | No       |      0
[C23](#chart-23)  | TIMEOUT   | No        | No        | No        | No       | No       |      0
[C24](#chart-24)  | TIMEOUT   | No        | No        | No        | No       | No       |      0
[C25](#chart-25)  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes       |      6
[C26](#chart-26)  | Yes       | Yes       | No        | Yes       | No    | Yes       |      4
[L1](#lang-1)     | No        | No        | No        | No        | No       | No       |      0
[L2](#lang-2)     | TIMEOUT   | No        | No        | No        | No       | No       |      0
[L3](#lang-3)     | TIMEOUT   | No        | No        | No        | No       | No       |      0
[L4](#lang-4)     | TIMEOUT   | No        | No        | No        | No       | No       |      0
[L5](#lang-5)     | TIMEOUT   | No        | No        | No        | No       | No       |      0
[L6](#lang-6)     | No        | No        | No        | No        | No       | No    |      0
[L7](#lang-7)     | TIMEOUT   | No        | No        | No        | No    | No       |      0
[L8](#lang-8)     | TIMEOUT   | No        | No        | No        | No       | No       |      0
[L9](#lang-9)     | TIMEOUT   | No        | No        | No        | No       | No       |      0
[L10](#lang-10)   | TIMEOUT   | TIMEOUT   | No       | No       | No       | No    |      0
[L11](#lang-11)   | No        | No        | No        | No        | No       | No       |      0
[L12](#lang-12)   | No        | No        | No        | No        | No       | No       |      0
[L13](#lang-13)   | No        | No        | No        | No        | No       | No       |      0
[L14](#lang-14)   | No        | No        | No        | No        | No       | No       |      0
[L15](#lang-15)   | No        | No        | No        | No        | No       | No       |      0
[L16](#lang-16)   | No        | No        | No        | No        | No    | TIMEOUT   |      0
[L17](#lang-17)   | No        | No        | No        | No        | No    | TIMEOUT   |      0
[L18](#lang-18)   | TIMEOUT   | No        | No        | No        | No    | No    |      0
[L19](#lang-19)   | No        | No        | No        | No        | No       | No       |      0
[L20](#lang-20)   | No        | No        | No        | No        | No    | No    |      0
[L21](#lang-21)   | No        | No        | No        | No        | No    | No    |      0
[L22](#lang-22)   | TIMEOUT   | TIMEOUT   | No        | No        | No    | No    |      0
[L23](#lang-23)   | No        | TIMEOUT   | No        | TIMEOUT   | No       | No       |      0
[L24](#lang-24)   | No        | No        | No        | No        | No       | No       |      0
[L25](#lang-25)   | No        | No        | No        | No        | No    | No    |      0
[L26](#lang-26)   | TIMEOUT   | No        | No        | No        | No       | No       |      0
[L27](#lang-27)   | No        | No        | No        | No        | No       | No       |      0
[L28](#lang-28)   | No        | No        | No        | No        | No       | No       |      0
[L29](#lang-29)   | No        | No        | No        | No        | No       | No       |      0
[L30](#lang-30)   | No        | No        | No        | No        | No       | No       |      0
[L31](#lang-31)   | No        | No        | No        | No        | No       | No       |      0
[L32](#lang-32)   | No        | No        | No        | No        | No       | No       |      0
[L33](#lang-33)   | No        | No        | No        | No        | No       | No       |      0
[L34](#lang-34)   | TIMEOUT   | No        | No        | No        | No       | No       |      0
[L35](#lang-35)   | No        | No        | No        | No        | No    | No    |      0
[L36](#lang-36)   | No        | No        | No        | No        | No       | No       |      0
[L37](#lang-37)   | No        | No        | No        | No        | No       | No       |      0
[L38](#lang-38)   | No        | No        | No        | No        | No       | No       |      0
[L39](#lang-39)   | Yes       | No        | Yes       | No        | No       | No       |      2
[L40](#lang-40)   | No        | No        | No        | No        | No    | No    |      0
[L41](#lang-41)   | No        | No        | No        | No        | No       | No       |      0
[L42](#lang-42)   | No        | No        | No        | No        | No       | No       |      0
[L43](#lang-43)   | No        | No        | No        | No        | No    | No    |      0
[L44](#lang-44)   | Yes       | Yes       | No        | No        | No    | No    |      2
[L45](#lang-45)   | No        | No        | No        | No        | No    | No    |      0
[L46](#lang-46)   | Yes       | No        | No        | No        | No    | No    |      1
[L47](#lang-47)   | No        | No        | No        | No        | No    | No    |      0
[L48](#lang-48)   | No        | No        | No        | No        | No       | No       |      0
[L49](#lang-49)   | TIMEOUT   | No        | No        | No        | No    | TIMEOUT   |      0
[L50](#lang-50)   | No        | No        | No        | No        | No    | No    |      0
[L51](#lang-51)   | No        | Yes       | No        | No        | No    | No    |      1
[L52](#lang-52)   | No        | No        | No        | No        | No    | No    |      0
[L53](#lang-53)   | Yes       | TIMEOUT   | No        | No        | No       | No       |      1
[L54](#lang-54)   | No        | No        | No        | No        | No    | TIMEOUT   |      0
[L55](#lang-55)   | Yes       | No        | No        | No        | No    | No    |      1
[L56](#lang-56)   | No        | No        | No        | No        | No    | No    |      0
[L57](#lang-57)   | No        | No        | No        | No        | No    | No    |      0
[L58](#lang-58)   | Yes       | Yes       | No        | No        | No       | No       |      2
[L59](#lang-59)   | No        | No        | No        | No        | No    | No    |      0
[L60](#lang-60)   | No        | No        | No        | No        | No    | No    |      0
[L61](#lang-61)   | No        | No        | No        | No        | No    | No    |      0
[L62](#lang-62)   | No        | No        | No        | No        | No       | No       |      0
[L63](#lang-63)   | TIMEOUT   | No        | No        | No        | No    | No    |      0
[L64](#lang-64)   | No        | No        | No        | No        | No    | No    |      0
[L65](#lang-65)   | No        | No        | No        | No        | No       | No       |      0
[M1](#math-1)     | TIMEOUT   | No        | No        | No        | No       | No       |      0
[M2](#math-2)     | TIMEOUT   | TIMEOUT   | TIMEOUT   | ERROR     | Yes       | Yes       |      2
[M3](#math-3)     | TIMEOUT   | No        | No        | No        | No       | No       |      0
[M4](#math-4)     | TIMEOUT   | TIMEOUT   | No        | No        | No       | No       |      0
[M5](#math-5)     | TIMEOUT   | No        | No        | No        | Yes       | No       |      1
[M6](#math-6)     | TIMEOUT   | No        | No        | No        | ERROR     | ERROR     |      0
[M7](#math-7)     | TIMEOUT   | TIMEOUT   | No        | No        | No    | TIMEOUT   |      0
[M8](#math-8)     | TIMEOUT   | No        | No        | No        | Yes       | Yes       |      2
[M9](#math-9)     | TIMEOUT   | No        | No        | No        | No       | No    |      0
[M10](#math-10)   | TIMEOUT   | No        | No        | No        | No       | No       |      0
[M11](#math-11)   | TIMEOUT   | TIMEOUT   | No        | No        | No       | No       |      0
[M12](#math-12)   | TIMEOUT   | TIMEOUT   | TIMEOUT   | ERROR     | No       | TIMEOUT   |      0
[M13](#math-13)   | TIMEOUT   | No        | No        | No        | No       | TIMEOUT   |      0
[M14](#math-14)   | TIMEOUT   | No        | No        | No        | No       | TIMEOUT   |      0
[M15](#math-15)   | TIMEOUT   | No        | No        | TIMEOUT   | No       | TIMEOUT   |      0
[M16](#math-16)   | TIMEOUT   | TIMEOUT   | No        | No        | No       | TIMEOUT   |      0
[M17](#math-17)   | No        | TIMEOUT   | No        | No        | No       | No       |      0
[M18](#math-18)   | TIMEOUT   | No        | TIMEOUT   | TIMEOUT   | No       | TIMEOUT   |      0
[M19](#math-19)   | No        | No        | No        | No        | No       | No       |      0
[M20](#math-20)   | TIMEOUT   | TIMEOUT   | TIMEOUT   | TIMEOUT   | ERROR     | ERROR     |      0
[M21](#math-21)   | No        | No        | No        | No        | No       | No       |      0
[M22](#math-22)   | No        | No        | No        | No        | No       | No       |      0
[M23](#math-23)   | No        | TIMEOUT   | No        | No        | No       | No    |      0
[M24](#math-24)   | No        | No        | No        | No        | No    | TIMEOUT   |      0
[M25](#math-25)   | No        | No        | No        | No        | No       | No       |      0
[M26](#math-26)   | No        | No        | No        | No        | No    | No       |      0
[M27](#math-27)   | TIMEOUT   | TIMEOUT   | No        | No        | No       | No       |      0
[M28](#math-28)   | No        | TIMEOUT   | No        | No        | Yes       | Yes       |      2
[M29](#math-29)   | No        | TIMEOUT   | No        | TIMEOUT   | No       | No       |      0
[M30](#math-30)   | No        | No        | No        | TIMEOUT   | No    | No    |      0
[M31](#math-31)   | No        | No        | No        | No        | No       | No       |      0
[M32](#math-32)   | Yes       | No        | No        | Yes       | No    | Yes       |      3
[M33](#math-33)   | Yes       | Yes       | Yes       | No        | No       | No       |      3
[M34](#math-34)   | No        | No        | No        | No        | No       | No       |      0
[M35](#math-35)   | No        | No        | No        | No        | No       | No       |      0
[M36](#math-36)   | No        | No        | No        | No        | No       | No       |      0
[M37](#math-37)   | No        | No        | No        | No        | No       | No       |      0
[M38](#math-38)   | TIMEOUT   | No        | No        | No        | No       | No       |      0
[M39](#math-39)   | ERROR     | ERROR     | No        | No        | No       | TIMEOUT   |      0
[M40](#math-40)   | No        | Yes       | No        | No        | Yes       | Yes       |      3
[M41](#math-41)   | No       | No       | Yes       | Yes       | No       | No       |      2
[M42](#math-42)   | Yes       | TIMEOUT   | Yes       | Yes       | No       | No       |      3
[M43](#math-43)   | No        | No        | No        | No        | No       | No       |      0
[M44](#math-44)   | TIMEOUT   | No        | No        | No        | Yes       | Yes       |      2
[M45](#math-45)   | No        | No        | No        | No        | No       | No       |      0
[M46](#math-46)   | No        | No        | Yes       | No        | No       | No       |      1
[M47](#math-47)   | No        | No        | No        | No        | No       | No       |      0
[M48](#math-48)   | TIMEOUT   | TIMEOUT   | No        | No        | No       | No       |      0
[M49](#math-49)   | Yes       | Yes       | Yes       | No        | Yes       | Yes       |      5
[M50](#math-50)   | Yes       | Yes       | Yes       | No        | Yes       | Yes       |      5
[M51](#math-51)   | TIMEOUT   | TIMEOUT   | TIMEOUT   | No        | ERROR     | ERROR     |      0
[M52](#math-52)   | No        | No        | No        | No        | No       | No       |      0
[M53](#math-53)   | No        | No        | No        | No        | Yes       | No       |      1
[M54](#math-54)   | TIMEOUT   | TIMEOUT   | No        | No        | No       | TIMEOUT   |      0
[M55](#math-55)   | No        | No        | No        | No        | No       | No       |      0
[M56](#math-56)   | No        | No        | No        | No        | Yes       | No       |      1
[M57](#math-57)   | Yes       | Yes       | No        | No        | No       | No       |      2
[M58](#math-58)   | Yes       | Yes       | Yes       | ERROR     | No    | TIMEOUT   |      3
[M59](#math-59)   | No        | No        | No        | No        | No       | TIMEOUT   |      0
[M60](#math-60)   | No        | No        | No        | No        | No       | No       |      0
[M61](#math-61)   | No        | No        | No        | No        | No       | No       |      0
[M62](#math-62)   | No        | No        | No        | No        | No       | No       |      0
[M63](#math-63)   | No        | No        | No        | No        | No       | No       |      0
[M64](#math-64)   | TIMEOUT   | No        | No        | No        | No       | No       |      0
[M65](#math-65)   | No        | No        | No        | No        | No       | No       |      0
[M66](#math-66)   | No        | No        | No        | No        | No       | No       |      0
[M67](#math-67)   | No        | No        | No        | No        | No       | No       |      0
[M68](#math-68)   | No        | No        | No        | No        | No       | No       |      0
[M69](#math-69)   | Yes       | No        | No        | No        | No       | No       |      1
[M70](#math-70)   | No        | No        | No        | No        | Yes       | No       |      1
[M71](#math-71)   | No        | Yes       | Yes       | No        | Yes       | TIMEOUT   |      3
[M72](#math-72)   | No        | No        | No        | No        | No    | No       |      0
[M73](#math-73)   | No        | Yes       | No        | No        | Yes       | No       |      2
[M74](#math-74)   | TIMEOUT   | No        | TIMEOUT   | TIMEOUT   | No       | No       |      0
[M75](#math-75)   | No        | No        | No        | No        | No       | No       |      0
[M76](#math-76)   | No        | No        | No        | No        | No       | No       |      0
[M77](#math-77)   | No        | No        | No        | No        | No       | No       |      0
[M78](#math-78)   | Yes       | TIMEOUT   | Yes       | No        | Yes       | Yes       |      4
[M79](#math-79)   | No        | No        | No        | No        | No    | No       |      0
[M80](#math-80)   | Yes       | TIMEOUT   | No        | No        | Yes       | Yes       |      3
[M81](#math-81)   | Yes       | Yes       | TIMEOUT   | TIMEOUT   | Yes       | Yes       |      4
[M82](#math-82)   | Yes       | No        | No        | No        | Yes       | Yes       |      3
[M83](#math-83)   | No        | No        | No        | No        | No       | No       |      0
[M84](#math-84)   | No        | No        | No        | No        | Yes       | Yes       |      2
[M85](#math-85)   | Yes       | Yes       | Yes       | Yes       | Yes       | Yes       |      6
[M86](#math-86)   | No        | No        | No        | No        | No       | No       |      0
[M87](#math-87)   | Yes       | Yes       | Yes       | No        | No       | No       |      3
[M88](#math-88)   | Yes       | No        | Yes       | No        | No       | No       |      2
[M89](#math-89)   | No        | No        | No        | No        | No       | No       |      0
[M90](#math-90)   | No        | No        | No        | No        | No       | No       |      0
[M91](#math-91)   | No        | No        | No        | No        | No       | No       |      0
[M92](#math-92)   | No        | No        | No        | No        | No       | No       |      0
[M93](#math-93)   | No        | No        | No        | No        | No       | No       |      0
[M94](#math-94)   | No        | No        | No        | No        | No       | No       |      0
[M95](#math-95)   | TIMEOUT   | No        | No        | No        | Yes       | Yes       |      2
[M96](#math-96)   | No        | No        | No        | Yes       | No       | No       |      1
[M97](#math-97)   | Yes       | Yes       | Yes       | Yes       | No       | No       |      4
[M98](#math-98)   | No        | No        | No        | No        | No       | No       |      0
[M99](#math-99)   | Yes       | Yes       | Yes       | Yes       | No       | No       |      4
[M100](#math-100) | No        | No        | No        | No        | No       | No       |      0
[M101](#math-101) | No        | No        | No        | No        | No       | No       |      0
[M102](#math-102) | TIMEOUT   | No        | No        | No        | No       | No       |      0
[M103](#math-103) | No        | No        | No        | No        | No       | No       |      0
[M104](#math-104) | No        | Yes       | No        | No        | No    | No       |      1
[M105](#math-105) | Yes       | No        | Yes       | No        | No       | No       |      2
[M106](#math-106) | No        | TIMEOUT   | No        | No        | No       | No       |      0
[T1](#time-1)     | No        | TIMEOUT   | No        | ERROR     | No    | No       |      0
[T2](#time-2)     | No        | No        | No        | No        | No    | No       |      0
[T3](#time-3)     | TIMEOUT   | TIMEOUT   | No        | No        | No       | No       |      0
[T4](#time-4)     | No        | No        | No        | No        | Yes       | Yes       |      2
[T5](#time-5)     | No        | No        | No        | No        | No       | No       |      0
[T6](#time-6)     | No        | No        | No        | No        | No       | No       |      0
[T7](#time-7)     | TIMEOUT   | TIMEOUT   | Yes       | ERROR     | No       | No       |      1
[T8](#time-8)     | No        | No        | No        | No        | No       | No       |      0
[T9](#time-9)     | No        | No        | No        | No        | No       | No       |      0
[T10](#time-10)   | TIMEOUT   | No        | No        | No        | No       | No       |      0
[T11](#time-11)   | Yes       | Yes       | Yes       | Yes       | Yes       | Yes       |      6
[T12](#time-12)   | ERROR     | TIMEOUT   | No        | No        | No       | No       |      0
[T13](#time-13)   | No        | No        | No        | No        | No       | No       |      0
[T14](#time-14)   | TIMEOUT   | No        | No        | No        | No       | No       |      0
[T15](#time-15)   | No        | No        | No        | No        | No       | No       |      0
[T16](#time-16)   | TIMEOUT   | TIMEOUT   | TIMEOUT   | No        | No       | No       |      0
[T17](#time-17)   | TIMEOUT   | No        | No        | No        | No       | No    |      0
[T18](#time-18)   | TIMEOUT   | TIMEOUT   | No        | No        | No       | No    |      0
[T19](#time-19)   | TIMEOUT   | TIMEOUT   | No        | ERROR     | No       | TIMEOUT   |      0
[T20](#time-20)   | No        | No        | No        | No        | No       | No       |      0
[T21](#time-21)   | TIMEOUT   | No        | No        | No        | No       | TIMEOUT   |      0
[T22](#time-22)   | No        | No        | No        | No        | No    | No    |      0
[T23](#time-23)   | No        | TIMEOUT   | No        | No        | No       | No       |      0
[T24](#time-24)   | No        | No        | No        | No        | No       | No    |      0
[T25](#time-25)   | No        | TIMEOUT   | No        | No        | No       | TIMEOUT   |      0
[T26](#time-26)   | No        | No        | No        | No        | No       | No       |      0
[T27](#time-27)   | No        | No        | No        | No        | No    | No       |      0
Total             | 30 (13%)  | 25 (11%)  | 24 (10%)  | 14 (6%)   | 33 (14%)  | 24 (10%)  |    150
Fixed bugs: 59/224 (26%)

Nb bugs ends with an execution error: 15

Nb bugs ends with an empty log: 0

Nb bugs ends with the Grid5000 timeout: 149

Total execution time: 36 days, 23:03:34.852000



# Chart 1

Nb Executed tests: 4402

Nb Failing tests: 2

>	org.jfree.chart.renderer.category.junit.AbstractCategoryItemRendererTests#test2947660
>	org.jfree.chart.renderer.category.junit.AbstractCategoryItemRendererTests#test2947660

## Human Patch 

```Java
Index: org/jfree/chart/renderer/category/AbstractCategoryItemRenderer.java
===================================================================
--- org/jfree/chart/renderer/category/AbstractCategoryItemRenderer.java	(revision 2266)
+++ org/jfree/chart/renderer/category/AbstractCategoryItemRenderer.java	(revision 2264)
@@ -1794,7 +1794,7 @@
         }
         int index = this.plot.getIndexOf(this);
         CategoryDataset dataset = this.plot.getDataset(index);
-        if (dataset == null) {
+        if (dataset != null) {
             return result;
         }
         int seriesCount = dataset.getRowCount();

```

## Genprog 

org.jfree.chart.renderer.category.AbstractCategoryItemRenderer:1797 (Suspicious rank: ample 28, jaccard 28, ochiai 32, naish1 25667, gp13 28, naish2 28, tarantula 28, )
DELETE
```Java
remove
```

Grid5000 node: graphene-75.nancy.grid5000.fr

## Kali 

org.jfree.chart.renderer.category.AbstractCategoryItemRenderer:1797 (Suspicious rank: ample 28, jaccard 28, ochiai 32, naish1 25667, gp13 28, naish2 28, tarantula 28, )
DELETE
```Java
remove
```

org.jfree.chart.renderer.category.AbstractCategoryItemRenderer:1797 (Suspicious rank: ample 28, jaccard 28, ochiai 32, naish1 25667, gp13 28, naish2 28, tarantula 28, )
REPLACE
```Java
if (false) {
	return result;
} 
```

org.jfree.chart.renderer.category.AbstractCategoryItemRenderer:1798 (Suspicious rank: ample 33, jaccard 33, ochiai 33, naish1 25673, gp13 33, naish2 33, tarantula 33, )
DELETE
```Java
remove
```

Grid5000 node: graphene-67.nancy.grid5000.fr

# Chart 3

Nb Executed tests: 4390

Nb Failing tests: 2

>	org.jfree.data.time.junit.TimeSeriesTests#testCreateCopy3
>	org.jfree.data.time.junit.TimeSeriesTests#testCreateCopy3

## Human Patch 

```Java
Index: org/jfree/data/time/TimeSeries.java
===================================================================
--- org/jfree/data/time/TimeSeries.java	(revision 2227)
+++ org/jfree/data/time/TimeSeries.java	(revision 2225)
@@ -1054,8 +1054,7 @@
             throw new IllegalArgumentException("Requires start <= end.");
         }
         TimeSeries copy = (TimeSeries) super.clone();
-        copy.minY = Double.NaN;
-        copy.maxY = Double.NaN;
+
         copy.data = new java.util.ArrayList();
         if (this.data.size() > 0) {
             for (int index = start; index <= end; index++) {

```

## NopolC 

org.jfree.data.time.TimeSeries:885 (Suspicious rank: ample 41, jaccard 41, ochiai 41, naish1 25131, gp13 41, naish2 41, tarantula 41, )
```Java
org.jfree.data.time.TimeSeries.this.data!=null
```

Nb Angelic value: 1

Nb analyzed Statement: 35

Execution time: 0:00:49.829000

Grid5000 node: griffon-38.nancy.grid5000.fr

## Genprog 

org.jfree.data.time.TimeSeries:579 (Suspicious rank: ample 59, jaccard 59, ochiai 53, naish1 25132, gp13 59, naish2 59, tarantula 59, )
INSERT_BEFORE
```Java
findBoundsByIteration()
```

Grid5000 node: graphene-75.nancy.grid5000.fr

# Chart 4

Nb Executed tests: 4374

Nb Failing tests: 44

>	org.jfree.chart.junit.JFreeChartTests#testSerialization4
>	org.jfree.chart.junit.ScatterPlotTests#testDrawWithNullInfo
>	org.jfree.chart.junit.ScatterPlotTests#testSetSeriesToolTipGenerator
>	org.jfree.chart.junit.ScatterPlotTests#testReplaceDataset
>	org.jfree.chart.junit.TimeSeriesChartTests#testDrawWithNullInfo
>	org.jfree.chart.junit.TimeSeriesChartTests#testSetSeriesToolTipGenerator
>	org.jfree.chart.junit.TimeSeriesChartTests#testReplaceDataset
>	org.jfree.chart.junit.XYAreaChartTests#testDrawWithNullInfo
>	org.jfree.chart.junit.XYAreaChartTests#testSetSeriesToolTipGenerator
>	org.jfree.chart.junit.XYAreaChartTests#testReplaceDataset
>	org.jfree.chart.junit.XYStepAreaChartTests#testDrawWithNullInfo
>	org.jfree.chart.junit.XYStepAreaChartTests#testSetSeriesToolTipGenerator
>	org.jfree.chart.junit.XYStepAreaChartTests#testReplaceDataset
>	org.jfree.chart.junit.XYStepChartTests#testDrawWithNullInfo
>	org.jfree.chart.junit.XYStepChartTests#testSetSeriesToolTipGenerator
>	org.jfree.chart.junit.XYStepChartTests#testReplaceDataset
>	org.jfree.chart.axis.junit.LogAxisTests#testXYAutoRange1
>	org.jfree.chart.axis.junit.LogAxisTests#testXYAutoRange2
>	org.jfree.chart.junit.XYStepAreaChartTests#testDrawWithNullInfo
>	org.jfree.chart.junit.XYStepAreaChartTests#testSetSeriesToolTipGenerator
>	org.jfree.chart.junit.XYStepAreaChartTests#testReplaceDataset
>	org.jfree.chart.plot.junit.XYPlotTests#testDrawRangeGridlines
>	org.jfree.chart.junit.JFreeChartTests#testSerialization4
>	org.jfree.chart.junit.ScatterPlotTests#testDrawWithNullInfo
>	org.jfree.chart.junit.ScatterPlotTests#testSetSeriesToolTipGenerator
>	org.jfree.chart.junit.ScatterPlotTests#testReplaceDataset
>	org.jfree.chart.plot.junit.XYPlotTests#testDrawRangeGridlines
>	org.jfree.chart.junit.TimeSeriesChartTests#testDrawWithNullInfo
>	org.jfree.chart.junit.TimeSeriesChartTests#testSetSeriesToolTipGenerator
>	org.jfree.chart.junit.TimeSeriesChartTests#testReplaceDataset
>	org.jfree.chart.axis.junit.LogAxisTests#testXYAutoRange1
>	org.jfree.chart.axis.junit.LogAxisTests#testXYAutoRange2
>	org.jfree.chart.axis.junit.NumberAxisTests#testXYAutoRange1
>	org.jfree.chart.axis.junit.NumberAxisTests#testXYAutoRange2
>	org.jfree.chart.axis.junit.ValueAxisTests#testAxisMargins
>	org.jfree.chart.junit.XYAreaChartTests#testDrawWithNullInfo
>	org.jfree.chart.junit.XYAreaChartTests#testSetSeriesToolTipGenerator
>	org.jfree.chart.junit.XYAreaChartTests#testReplaceDataset
>	org.jfree.chart.axis.junit.ValueAxisTests#testAxisMargins
>	org.jfree.chart.junit.XYStepChartTests#testDrawWithNullInfo
>	org.jfree.chart.junit.XYStepChartTests#testSetSeriesToolTipGenerator
>	org.jfree.chart.junit.XYStepChartTests#testReplaceDataset
>	org.jfree.chart.axis.junit.NumberAxisTests#testXYAutoRange1
>	org.jfree.chart.axis.junit.NumberAxisTests#testXYAutoRange2

## Human Patch 

```Java
Index: org/jfree/chart/plot/XYPlot.java
===================================================================
--- org/jfree/chart/plot/XYPlot.java	(revision 2183)
+++ org/jfree/chart/plot/XYPlot.java	(revision 2182)
@@ -4490,14 +4490,12 @@
                     }
                 }
                 
-                if (r != null) {
-                    Collection c = r.getAnnotations();
-                    Iterator i = c.iterator();
-                    while (i.hasNext()) {
-                        XYAnnotation a = (XYAnnotation) i.next();
-                        if (a instanceof XYAnnotationBoundsInfo) {
-                            includedAnnotations.add(a);
-                        }
+                Collection c = r.getAnnotations();
+                Iterator i = c.iterator();
+                while (i.hasNext()) {
+                    XYAnnotation a = (XYAnnotation) i.next();
+                    if (a instanceof XYAnnotationBoundsInfo) {
+                        includedAnnotations.add(a);
                     }
                 }
             }

```

## BrutpolPC 

org.jfree.chart.plot.XYPlot:1607 (Suspicious rank: ample 1109, jaccard 571, ochiai 583, naish1 24663, gp13 706, naish2 706, tarantula 425, )
```Java
this.domainMinorGridlinesVisible
```

Nb Angelic value: 1

Nb analyzed Statement: 583

Execution time: 0:07:21.284000

Grid5000 node: graphene-97.nancy.grid5000.fr

# Chart 5

Nb Executed tests: 4081

Nb Failing tests: 2

>	org.jfree.data.xy.junit.XYSeriesTests#testBug1955483
>	org.jfree.data.xy.junit.XYSeriesTests#testBug1955483

## Human Patch 

```Java
Index: org/jfree/data/xy/XYSeries.java
===================================================================
--- org/jfree/data/xy/XYSeries.java	(revision 1696)
+++ org/jfree/data/xy/XYSeries.java	(revision 1695)
@@ -541,15 +537,9 @@
         if (x == null) {
             throw new IllegalArgumentException("Null 'x' argument.");
         }
-        if (this.allowDuplicateXValues) {
-            add(x, y);
-            return null;
-        }
-
-        // if we get to here, we know that duplicate X values are not permitted
         XYDataItem overwritten = null;
         int index = indexOf(x);
-        if (index >= 0) {
+        if (index >= 0 && !this.allowDuplicateXValues) {
             XYDataItem existing = (XYDataItem) this.data.get(index);
             try {
                 overwritten = (XYDataItem) existing.clone();

```

## NopolC 

org.jfree.data.xy.XYSeries:561 (Suspicious rank: ample 3, jaccard 3, ochiai 3, naish1 24208, gp13 3, naish2 3, tarantula 3, )
```Java
overwritten!=null
```

Nb Angelic value: 1

Nb analyzed Statement: 4

Execution time: 0:00:34.849000

Grid5000 node: graphene-57.nancy.grid5000.fr

## BrutpolC 

org.jfree.data.xy.XYSeries:561 (Suspicious rank: ample 3, jaccard 3, ochiai 3, naish1 24208, gp13 3, naish2 3, tarantula 3, )
```Java
this.equals(x)
```

Nb Angelic value: 1

Nb analyzed Statement: 4

Execution time: 0:01:43.868000

Grid5000 node: graphene-82.nancy.grid5000.fr

## Genprog 

org.jfree.data.xy.XYSeries:562 (Suspicious rank: ample 1, jaccard 1, ochiai 1, naish1 24209, gp13 1, naish2 1, tarantula 1, )
REPLACE
```Java
this.data.add(new org.jfree.data.xy.XYDataItem(x , y))
```

Grid5000 node: graphene-68.nancy.grid5000.fr

## Kali 

org.jfree.data.xy.XYSeries:561 (Suspicious rank: ample 3, jaccard 3, ochiai 3, naish1 24208, gp13 3, naish2 3, tarantula 3, )
REPLACE
```Java
if (false) {
	this.data.add(((-index) - 1), new org.jfree.data.xy.XYDataItem(x , y));
} else {
	this.data.add(new org.jfree.data.xy.XYDataItem(x , y));
}
```

Grid5000 node: graphene-68.nancy.grid5000.fr

# Chart 6

Nb Executed tests: 3789

Nb Failing tests: 4

>	org.jfree.chart.util.junit.ShapeListTests#testSerialization
>	org.jfree.chart.util.junit.ShapeListTests#testEquals
>	org.jfree.chart.util.junit.ShapeListTests#testSerialization
>	org.jfree.chart.util.junit.ShapeListTests#testEquals

## Human Patch 

```Java
Index: org/jfree/chart/util/ShapeList.java
===================================================================
--- org/jfree/chart/util/ShapeList.java	(revision 1166)
+++ org/jfree/chart/util/ShapeList.java	(revision 1164)
@@ -96,27 +93,26 @@
     /**
      * Tests the list for equality with another object (typically also a list).
      *
-     * @param obj  the other object (<code>null</code> permitted).
+     * @param obj  the other object.
      *
      * @return A boolean.
      */
     public boolean equals(Object obj) {
 
+        if (obj == null) {
+            return false;
+        }
+
         if (obj == this) {
             return true;
         }
-        if (!(obj instanceof ShapeList)) {
-            return false;
+
+        if (obj instanceof ShapeList) {
+            return super.equals(obj);
         }
-        ShapeList that = (ShapeList) obj;
-        int listSize = size();
-        for (int i = 0; i < listSize; i++) {
-           if (!ShapeUtilities.equal((Shape) get(i), (Shape) that.get(i))) {
-               return false;
-           }
-        }
-        return true;
 
+        return false;
+
     }
 
     /**

```

## NopolPC 

org.jfree.chart.util.ShapeList:81 (Suspicious rank: ample 1, jaccard 16, ochiai 15, naish1 22144, gp13 1, naish2 1, tarantula 16, )
```Java
(-1) != (-1)
```

Nb Angelic value: 1

Nb analyzed Statement: 16

Execution time: 0:00:36.412000

Grid5000 node: graphene-89.nancy.grid5000.fr

## NopolC 

org.jfree.chart.util.ShapeList:109 (Suspicious rank: ample 7, jaccard 83, ochiai 50, naish1 22146, gp13 7, naish2 7, tarantula 83, )
```Java
obj!=null
```

Nb Angelic value: 1

Nb analyzed Statement: 51

Execution time: 0:00:39.572000

Grid5000 node: graphene-61.nancy.grid5000.fr

## BrutpolPC 

org.jfree.chart.util.AbstractObjectList:193 (Suspicious rank: ample 4, jaccard 40, ochiai 19, naish1 22174, gp13 4, naish2 4, tarantula 40, )
```Java
0 == this.increment
```

Nb Angelic value: 3

Nb analyzed Statement: 19

Execution time: 0:04:04.386000

Grid5000 node: griffon-72.nancy.grid5000.fr

## BrutpolC 

org.jfree.chart.util.AbstractObjectList:193 (Suspicious rank: ample 4, jaccard 40, ochiai 19, naish1 22174, gp13 4, naish2 4, tarantula 40, )
```Java
0 == this.increment
```

Nb Angelic value: 1

Nb analyzed Statement: 19

Execution time: 0:01:45.013000

Grid5000 node: graphene-99.nancy.grid5000.fr

## Genprog 

org.jfree.chart.util.AbstractObjectList:131 (Suspicious rank: ample 13, jaccard 89, ochiai 59, naish1 22075, gp13 13, naish2 13, tarantula 91, )
INSERT_BEFORE
```Java
java.util.Arrays.fill(this.objects, null)
```

Grid5000 node: graphene-57.nancy.grid5000.fr

# Chart 7

Nb Executed tests: 3641

Nb Failing tests: 2

>	org.jfree.data.time.junit.TimePeriodValuesTests#testGetMaxMiddleIndex
>	org.jfree.data.time.junit.TimePeriodValuesTests#testGetMaxMiddleIndex

## Human Patch 

```Java
Index: org/jfree/data/time/TimePeriodValues.java
===================================================================
--- org/jfree/data/time/TimePeriodValues.java	(revision 1087)
+++ org/jfree/data/time/TimePeriodValues.java	(revision 1086)
@@ -297,9 +296,9 @@
         }
         
         if (this.maxMiddleIndex >= 0) {
-            long s = getDataItem(this.maxMiddleIndex).getPeriod().getStart()
+            long s = getDataItem(this.minMiddleIndex).getPeriod().getStart()
                 .getTime();
-            long e = getDataItem(this.maxMiddleIndex).getPeriod().getEnd()
+            long e = getDataItem(this.minMiddleIndex).getPeriod().getEnd()
                 .getTime();
             long maxMiddle = s + (e - s) / 2;
             if (middle > maxMiddle) {

```

## Genprog 

org.jfree.data.time.TimePeriodValues:552 (Suspicious rank: ample 1, jaccard 1, ochiai 1, naish1 22060, gp13 1, naish2 1, tarantula 1, )
REPLACE
```Java
return this.maxEndIndex
```

Grid5000 node: graphene-75.nancy.grid5000.fr

# Chart 8

Nb Executed tests: 3641

Nb Failing tests: 0


## Human Patch 

```Java
Index: org/jfree/data/time/Week.java
===================================================================
--- org/jfree/data/time/Week.java	(revision 1085)
+++ org/jfree/data/time/Week.java	(revision 1084)
@@ -172,7 +171,7 @@
      */
     public Week(Date time, TimeZone zone) {
         // defer argument checking...
-        this(time, zone, Locale.getDefault());
+        this(time, RegularTimePeriod.DEFAULT_TIME_ZONE, Locale.getDefault());
     }
 
     /**

```

## Genprog 

org.jfree.data.xy.MatrixSeries:88
INSERT_BEFORE
```Java
fireSeriesChanged()
```

Grid5000 node: graphene-64.nancy.grid5000.fr

# Chart 9

Nb Executed tests: 3641

Nb Failing tests: 2

>	org.jfree.data.time.junit.TimeSeriesTests#testBug1864222
>	org.jfree.data.time.junit.TimeSeriesTests#testBug1864222

## Human Patch 

```Java
Index: org/jfree/data/time/TimeSeries.java
===================================================================
--- org/jfree/data/time/TimeSeries.java	(revision 1083)
+++ org/jfree/data/time/TimeSeries.java	(revision 1082)
@@ -674,7 +672,7 @@
      */
     public TimeSeriesDataItem addOrUpdate(RegularTimePeriod period,
                                           double value) {
-        return addOrUpdate(period, new Double(value));
+        return this.addOrUpdate(period, new Double(value));
     }
 
     /**
@@ -941,7 +937,7 @@
             endIndex = -(endIndex + 1); // this is first item AFTER end period
             endIndex = endIndex - 1;    // so this is last item BEFORE end
         }
-        if ((endIndex < 0)  || (endIndex < startIndex)) {
+        if (endIndex < 0) {
             emptyRange = true;
         }
         if (emptyRange) {
@@ -970,13 +966,15 @@
             return false;
         }
         TimeSeries s = (TimeSeries) object;
-        if (!ObjectUtilities.equal(getDomainDescription(),
-                s.getDomainDescription())) {
+        if (!ObjectUtilities.equal(
+            getDomainDescription(), s.getDomainDescription()
+        )) {
             return false;
         }
 
-        if (!ObjectUtilities.equal(getRangeDescription(),
-                s.getRangeDescription())) {
+        if (!ObjectUtilities.equal(
+            getRangeDescription(), s.getRangeDescription()
+        )) {
             return false;
         }
 

```

## BrutpolPC 

org.jfree.data.time.TimeSeries:883 (Suspicious rank: ample 11, jaccard 11, ochiai 16, naish1 22017, gp13 11, naish2 11, tarantula 11, )
```Java
this.data.contains(this)
```

Nb Angelic value: 1

Nb analyzed Statement: 1

Execution time: 0:01:46.827000

Grid5000 node: griffon-72.nancy.grid5000.fr

## BrutpolC 

org.jfree.data.time.TimeSeries:940 (Suspicious rank: ample 15, jaccard 15, ochiai 10, naish1 22044, gp13 15, naish2 15, tarantula 15, )
```Java
emptyRange
```

Nb Angelic value: 3

Nb analyzed Statement: 7

Execution time: 0:03:51.520000

Grid5000 node: graphene-99.nancy.grid5000.fr

## Genprog 

org.jfree.data.time.SpreadsheetDate:457 (Suspicious rank: ample 95, jaccard 95, ochiai 99, naish1 21980, gp13 95, naish2 95, tarantula 95, )
REPLACE
```Java
return this.day
```

Grid5000 node: graphene-53.nancy.grid5000.fr

# Chart 13

Nb Executed tests: 3597

Nb Failing tests: 2

>	org.jfree.chart.block.junit.BorderArrangementTests#testSizingWithWidthConstraint
>	org.jfree.chart.block.junit.BorderArrangementTests#testSizingWithWidthConstraint

## Human Patch 

```Java
Index: org/jfree/chart/block/BorderArrangement.java
===================================================================
--- org/jfree/chart/block/BorderArrangement.java	(revision 822)
+++ org/jfree/chart/block/BorderArrangement.java	(revision 817)
@@ -114,102 +112,114 @@
             }
         }
     }
-
+    
     /**
-     * Arranges the items in the specified container, subject to the given
+     * Arranges the items in the specified container, subject to the given 
      * constraint.
-     *
+     * 
      * @param container  the container.
      * @param g2  the graphics device.
      * @param constraint  the constraint.
-     *
+     * 
      * @return The block size.
      */
-    public Size2D arrange(BlockContainer container,
-                          Graphics2D g2,
+    public Size2D arrange(BlockContainer container, 
+                          Graphics2D g2, 
                           RectangleConstraint constraint) {
-        RectangleConstraint contentConstraint
-                = container.toContentConstraint(constraint);
+        RectangleConstraint contentConstraint 
+            = container.toContentConstraint(constraint);
         Size2D contentSize = null;
         LengthConstraintType w = contentConstraint.getWidthConstraintType();
         LengthConstraintType h = contentConstraint.getHeightConstraintType();
         if (w == LengthConstraintType.NONE) {
             if (h == LengthConstraintType.NONE) {
-                contentSize = arrangeNN(container, g2);
+                contentSize = arrangeNN(container, g2);  
             }
             else if (h == LengthConstraintType.FIXED) {
-                throw new RuntimeException("Not implemented.");
+                throw new RuntimeException("Not implemented.");  
             }
             else if (h == LengthConstraintType.RANGE) {
-                throw new RuntimeException("Not implemented.");
+                throw new RuntimeException("Not implemented.");  
             }
         }
         else if (w == LengthConstraintType.FIXED) {
             if (h == LengthConstraintType.NONE) {
-                contentSize = arrangeFN(container, g2, constraint.getWidth());
+                contentSize = arrangeFN(container, g2, constraint.getWidth());  
             }
             else if (h == LengthConstraintType.FIXED) {
-                contentSize = arrangeFF(container, g2, constraint);
+                contentSize = arrangeFF(container, g2, constraint);  
             }
             else if (h == LengthConstraintType.RANGE) {
-                contentSize = arrangeFR(container, g2, constraint);
+                contentSize = arrangeFR(container, g2, constraint);  
             }
         }
         else if (w == LengthConstraintType.RANGE) {
             if (h == LengthConstraintType.NONE) {
-                throw new RuntimeException("Not implemented.");
+                throw new RuntimeException("Not implemented.");  
             }
             else if (h == LengthConstraintType.FIXED) {
-                throw new RuntimeException("Not implemented.");
+                throw new RuntimeException("Not implemented.");  
             }
             else if (h == LengthConstraintType.RANGE) {
-                contentSize = arrangeRR(container, constraint.getWidthRange(),
-                        constraint.getHeightRange(), g2);
+                contentSize = arrangeRR(
+                    container, constraint.getWidthRange(),
+                    constraint.getHeightRange(), g2
+                );  
             }
         }
-        return new Size2D(container.calculateTotalWidth(contentSize.getWidth()),
-                container.calculateTotalHeight(contentSize.getHeight()));
+        return new Size2D(
+            container.calculateTotalWidth(contentSize.getWidth()),
+            container.calculateTotalHeight(contentSize.getHeight())
+        );
     }
-
+    
     /**
      * Performs an arrangement without constraints.
-     *
+     * 
      * @param container  the container.
      * @param g2  the graphics device.
-     *
+     * 
      * @return The container size after the arrangement.
      */
     protected Size2D arrangeNN(BlockContainer container, Graphics2D g2) {
         double[] w = new double[5];
         double[] h = new double[5];
         if (this.topBlock != null) {
-            Size2D size = this.topBlock.arrange(g2, RectangleConstraint.NONE);
+            Size2D size = this.topBlock.arrange(
+                g2, RectangleConstraint.NONE
+            );
             w[0] = size.width;
             h[0] = size.height;
         }
         if (this.bottomBlock != null) {
-            Size2D size = this.bottomBlock.arrange(g2,
-                    RectangleConstraint.NONE);
+            Size2D size = this.bottomBlock.arrange(
+                g2, RectangleConstraint.NONE
+            );
             w[1] = size.width;
             h[1] = size.height;
         }
         if (this.leftBlock != null) {
-            Size2D size = this.leftBlock.arrange(g2, RectangleConstraint.NONE);
+            Size2D size = this.leftBlock.arrange(
+                g2, RectangleConstraint.NONE
+            );
             w[2] = size.width;
             h[2] = size.height;
        }
         if (this.rightBlock != null) {
-            Size2D size = this.rightBlock.arrange(g2, RectangleConstraint.NONE);
+            Size2D size = this.rightBlock.arrange(
+                g2, RectangleConstraint.NONE
+            );
             w[3] = size.width;
             h[3] = size.height;
         }
-
+        
         h[2] = Math.max(h[2], h[3]);
         h[3] = h[2];
-
+        
         if (this.centerBlock != null) {
-            Size2D size = this.centerBlock.arrange(g2,
-                    RectangleConstraint.NONE);
+            Size2D size = this.centerBlock.arrange(
+                g2, RectangleConstraint.NONE
+            );
             w[4] = size.width;
             h[4] = size.height;
         }
@@ -217,68 +227,76 @@
         double centerHeight = Math.max(h[2], Math.max(h[3], h[4]));
         double height = h[0] + h[1] + centerHeight;
         if (this.topBlock != null) {
-            this.topBlock.setBounds(new Rectangle2D.Double(0.0, 0.0, width,
-                    h[0]));
+            this.topBlock.setBounds(
+                new Rectangle2D.Double(0.0, 0.0, width, h[0])
+            );
         }
         if (this.bottomBlock != null) {
-            this.bottomBlock.setBounds(new Rectangle2D.Double(0.0,
-                    height - h[1], width, h[1]));
+            this.bottomBlock.setBounds(
+                new Rectangle2D.Double(0.0, height - h[1], width, h[1])
+            );
         }
         if (this.leftBlock != null) {
-            this.leftBlock.setBounds(new Rectangle2D.Double(0.0, h[0], w[2],
-                    centerHeight));
+            this.leftBlock.setBounds(
+                new Rectangle2D.Double(0.0, h[0], w[2], centerHeight)
+            );
         }
         if (this.rightBlock != null) {
-            this.rightBlock.setBounds(new Rectangle2D.Double(width - w[3],
-                    h[0], w[3], centerHeight));
+            this.rightBlock.setBounds(
+                new Rectangle2D.Double(width - w[3], h[0], w[3], centerHeight)
+            );
         }
-
+        
         if (this.centerBlock != null) {
-            this.centerBlock.setBounds(new Rectangle2D.Double(w[2], h[0],
-                    width - w[2] - w[3], centerHeight));
+            this.centerBlock.setBounds(
+                new Rectangle2D.Double(
+                    w[2], h[0], width - w[2] - w[3], centerHeight
+                )
+            );
         }
         return new Size2D(width, height);
     }
 
     /**
      * Performs an arrangement with a fixed width and a range for the height.
-     *
+     * 
      * @param container  the container.
      * @param g2  the graphics device.
      * @param constraint  the constraint.
-     *
+     * 
      * @return The container size after the arrangement.
      */
     protected Size2D arrangeFR(BlockContainer container, Graphics2D g2,
                                RectangleConstraint constraint) {
         Size2D size1 = arrangeFN(container, g2, constraint.getWidth());
         if (constraint.getHeightRange().contains(size1.getHeight())) {
-            return size1;
+            return size1;   
         }
         else {
             double h = constraint.getHeightRange().constrain(size1.getHeight());
             RectangleConstraint c2 = constraint.toFixedHeight(h);
-            return arrange(container, g2, c2);
+            return arrange(container, g2, c2);   
         }
     }
-
-    /**
-     * Arranges the container width a fixed width and no constraint on the
+    
+    /** 
+     * Arranges the container width a fixed width and no constraint on the 
      * height.
-     *
+     * 
      * @param container  the container.
      * @param g2  the graphics device.
      * @param width  the fixed width.
-     *
+     * 
      * @return The container size after arranging the contents.
      */
     protected Size2D arrangeFN(BlockContainer container, Graphics2D g2,
                                double width) {
         double[] w = new double[5];
         double[] h = new double[5];
-        RectangleConstraint c1 = new RectangleConstraint(width, null,
-                LengthConstraintType.FIXED, 0.0, null,
-                LengthConstraintType.NONE);
+        RectangleConstraint c1 = new RectangleConstraint(
+            width, null, LengthConstraintType.FIXED,
+            0.0, null, LengthConstraintType.NONE
+        );
         if (this.topBlock != null) {
             Size2D size = this.topBlock.arrange(g2, c1);
             w[0] = size.width;
@@ -289,9 +307,10 @@
             w[1] = size.width;
             h[1] = size.height;
         }
-        RectangleConstraint c2 = new RectangleConstraint(0.0,
-                new Range(0.0, width), LengthConstraintType.RANGE,
-                0.0, null, LengthConstraintType.NONE);
+        RectangleConstraint c2 = new RectangleConstraint(
+            0.0, new Range(0.0, width), LengthConstraintType.RANGE,
+            0.0, null, LengthConstraintType.NONE
+        );
         if (this.leftBlock != null) {
             Size2D size = this.leftBlock.arrange(g2, c2);
             w[2] = size.width;
@@ -299,22 +318,24 @@
         }
         if (this.rightBlock != null) {
             double maxW = Math.max(width - w[2], 0.0);
-            RectangleConstraint c3 = new RectangleConstraint(0.0,
-                    new Range(Math.min(w[2], maxW), maxW),
-                    LengthConstraintType.RANGE, 0.0, null,
-                    LengthConstraintType.NONE);
+            RectangleConstraint c3 = new RectangleConstraint(
+                0.0, new Range(Math.min(w[2], maxW), maxW), 
+                LengthConstraintType.RANGE,
+                0.0, null, LengthConstraintType.NONE
+            );    
             Size2D size = this.rightBlock.arrange(g2, c3);
             w[3] = size.width;
             h[3] = size.height;
         }
-
+        
         h[2] = Math.max(h[2], h[3]);
         h[3] = h[2];
-
+        
         if (this.centerBlock != null) {
-            RectangleConstraint c4 = new RectangleConstraint(width - w[2]
-                    - w[3], null, LengthConstraintType.FIXED, 0.0, null,
-                    LengthConstraintType.NONE);
+            RectangleConstraint c4 = new RectangleConstraint(
+                width - w[2] - w[3], null, LengthConstraintType.FIXED,
+                0.0, null, LengthConstraintType.NONE
+            );    
             Size2D size = this.centerBlock.arrange(g2, c4);
             w[4] = size.width;
             h[4] = size.height;
@@ -324,62 +345,67 @@
     }
 
     /**
-     * Performs an arrangement with range constraints on both the vertical
+     * Performs an arrangement with range constraints on both the vertical 
      * and horizontal sides.
-     *
+     * 
      * @param container  the container.
      * @param widthRange  the allowable range for the container width.
      * @param heightRange  the allowable range for the container height.
      * @param g2  the graphics device.
-     *
+     * 
      * @return The container size.
      */
-    protected Size2D arrangeRR(BlockContainer container,
-                               Range widthRange, Range heightRange,
+    protected Size2D arrangeRR(BlockContainer container, 
+                               Range widthRange, Range heightRange, 
                                Graphics2D g2) {
         double[] w = new double[5];
         double[] h = new double[5];
         if (this.topBlock != null) {
-            RectangleConstraint c1 = new RectangleConstraint(widthRange,
-                    heightRange);
+            RectangleConstraint c1 = new RectangleConstraint(
+                widthRange, heightRange
+            );
             Size2D size = this.topBlock.arrange(g2, c1);
             w[0] = size.width;
             h[0] = size.height;
         }
         if (this.bottomBlock != null) {
             Range heightRange2 = Range.shift(heightRange, -h[0], false);
-            RectangleConstraint c2 = new RectangleConstraint(widthRange,
-                    heightRange2);
+            RectangleConstraint c2 = new RectangleConstraint(
+                widthRange, heightRange2
+            );  
             Size2D size = this.bottomBlock.arrange(g2, c2);
             w[1] = size.width;
             h[1] = size.height;
         }
         Range heightRange3 = Range.shift(heightRange, -(h[0] + h[1]));
         if (this.leftBlock != null) {
-            RectangleConstraint c3 = new RectangleConstraint(widthRange,
-                    heightRange3);
+            RectangleConstraint c3 = new RectangleConstraint(
+                widthRange, heightRange3
+            );
             Size2D size = this.leftBlock.arrange(g2, c3);
             w[2] = size.width;
             h[2] = size.height;
         }
         Range widthRange2 = Range.shift(widthRange, -w[2], false);
         if (this.rightBlock != null) {
-            RectangleConstraint c4 = new RectangleConstraint(widthRange2,
-                    heightRange3);
+            RectangleConstraint c4 = new RectangleConstraint(
+                widthRange2, heightRange3
+            );
             Size2D size = this.rightBlock.arrange(g2, c4);
             w[3] = size.width;
             h[3] = size.height;
         }
-
+        
         h[2] = Math.max(h[2], h[3]);
         h[3] = h[2];
         Range widthRange3 = Range.shift(widthRange, -(w[2] + w[3]), false);
         if (this.centerBlock != null) {
-            RectangleConstraint c5 = new RectangleConstraint(widthRange3,
-                    heightRange3);
-            // TODO:  the width and height ranges should be reduced by the
+            RectangleConstraint c5 = new RectangleConstraint(
+                widthRange3, heightRange3
+            );
+            // TODO:  the width and height ranges should be reduced by the 
             // height required for the top and bottom, and the width required
-            // by the left and right
+            // by the left and right 
             Size2D size = this.centerBlock.arrange(g2, c5);
             w[4] = size.width;
             h[4] = size.height;
@@ -387,36 +413,43 @@
         double width = Math.max(w[0], Math.max(w[1], w[2] + w[4] + w[3]));
         double height = h[0] + h[1] + Math.max(h[2], Math.max(h[3], h[4]));
         if (this.topBlock != null) {
-            this.topBlock.setBounds(new Rectangle2D.Double(0.0, 0.0, width,
-                    h[0]));
+            this.topBlock.setBounds(
+                new Rectangle2D.Double(0.0, 0.0, width, h[0])
+            );
         }
         if (this.bottomBlock != null) {
-            this.bottomBlock.setBounds(new Rectangle2D.Double(0.0,
-                    height - h[1], width, h[1]));
+            this.bottomBlock.setBounds(
+                new Rectangle2D.Double(0.0, height - h[1], width, h[1])
+            );
         }
         if (this.leftBlock != null) {
-            this.leftBlock.setBounds(new Rectangle2D.Double(0.0, h[0], w[2],
-                    h[2]));
+            this.leftBlock.setBounds(
+                new Rectangle2D.Double(0.0, h[0], w[2], h[2])
+            );
         }
         if (this.rightBlock != null) {
-            this.rightBlock.setBounds(new Rectangle2D.Double(width - w[3],
-                    h[0], w[3], h[3]));
+            this.rightBlock.setBounds(
+                new Rectangle2D.Double(width - w[3], h[0], w[3], h[3])
+            );
         }
-
+        
         if (this.centerBlock != null) {
-            this.centerBlock.setBounds(new Rectangle2D.Double(w[2], h[0],
-                    width - w[2] - w[3], height - h[0] - h[1]));
+            this.centerBlock.setBounds(
+                new Rectangle2D.Double(
+                    w[2], h[0], width - w[2] - w[3], height - h[0] - h[1]
+                )
+            );
         }
         return new Size2D(width, height);
     }
 
     /**
      * Arranges the items within a container.
-     *
+     * 
      * @param container  the container.
      * @param constraint  the constraint.
      * @param g2  the graphics device.
-     *
+     * 
      * @return The container size after the arrangement.
      */
     protected Size2D arrangeFF(BlockContainer container, Graphics2D g2,
@@ -425,69 +458,79 @@
         double[] h = new double[5];
         w[0] = constraint.getWidth();
         if (this.topBlock != null) {
-            RectangleConstraint c1 = new RectangleConstraint(w[0], null,
-                    LengthConstraintType.FIXED, 0.0,
-                    new Range(0.0, constraint.getHeight()),
-                    LengthConstraintType.RANGE);
+            RectangleConstraint c1 = new RectangleConstraint(
+                w[0], null, LengthConstraintType.FIXED,
+                0.0, new Range(0.0, constraint.getHeight()), 
+                LengthConstraintType.RANGE
+            );
             Size2D size = this.topBlock.arrange(g2, c1);
             h[0] = size.height;
         }
         w[1] = w[0];
         if (this.bottomBlock != null) {
-            RectangleConstraint c2 = new RectangleConstraint(w[0], null,
-                    LengthConstraintType.FIXED, 0.0, new Range(0.0,
-                    constraint.getHeight() - h[0]), LengthConstraintType.RANGE);
+            RectangleConstraint c2 = new RectangleConstraint(
+                w[0], null, LengthConstraintType.FIXED,
+                0.0, new Range(0.0, constraint.getHeight() - h[0]), 
+                LengthConstraintType.RANGE
+            );
             Size2D size = this.bottomBlock.arrange(g2, c2);
             h[1] = size.height;
         }
         h[2] = constraint.getHeight() - h[1] - h[0];
         if (this.leftBlock != null) {
-            RectangleConstraint c3 = new RectangleConstraint(0.0,
-                    new Range(0.0, constraint.getWidth()),
-                    LengthConstraintType.RANGE, h[2], null,
-                    LengthConstraintType.FIXED);
+            RectangleConstraint c3 = new RectangleConstraint(
+                0.0, new Range(0.0, constraint.getWidth()), 
+                LengthConstraintType.RANGE,
+                h[2], null, LengthConstraintType.FIXED
+            );
             Size2D size = this.leftBlock.arrange(g2, c3);
-            w[2] = size.width;
+            w[2] = size.width;            
         }
         h[3] = h[2];
         if (this.rightBlock != null) {
-            RectangleConstraint c4 = new RectangleConstraint(0.0,
-                    new Range(0.0, Math.max(constraint.getWidth() - w[2], 0.0)),
-                    LengthConstraintType.RANGE, h[2], null,
-                    LengthConstraintType.FIXED);
+            RectangleConstraint c4 = new RectangleConstraint(
+                0.0, new Range(0.0, constraint.getWidth() - w[2]), 
+                LengthConstraintType.RANGE,
+                h[2], null, LengthConstraintType.FIXED
+            );
             Size2D size = this.rightBlock.arrange(g2, c4);
-            w[3] = size.width;
+            w[3] = size.width;            
         }
         h[4] = h[2];
         w[4] = constraint.getWidth() - w[3] - w[2];
         RectangleConstraint c5 = new RectangleConstraint(w[4], h[4]);
         if (this.centerBlock != null) {
-            this.centerBlock.arrange(g2, c5);
+            this.centerBlock.arrange(g2, c5);   
         }
-
+       
         if (this.topBlock != null) {
-            this.topBlock.setBounds(new Rectangle2D.Double(0.0, 0.0, w[0],
-                    h[0]));
+            this.topBlock.setBounds(
+                new Rectangle2D.Double(0.0, 0.0, w[0], h[0])
+            );
         }
         if (this.bottomBlock != null) {
-            this.bottomBlock.setBounds(new Rectangle2D.Double(0.0, h[0] + h[2],
-                    w[1], h[1]));
+            this.bottomBlock.setBounds(
+                new Rectangle2D.Double(0.0, h[0] + h[2], w[1], h[1])
+            );
         }
         if (this.leftBlock != null) {
-            this.leftBlock.setBounds(new Rectangle2D.Double(0.0, h[0], w[2],
-                    h[2]));
+            this.leftBlock.setBounds(
+                new Rectangle2D.Double(0.0, h[0], w[2], h[2])
+            );
         }
         if (this.rightBlock != null) {
-            this.rightBlock.setBounds(new Rectangle2D.Double(w[2] + w[4], h[0],
-                    w[3], h[3]));
+            this.rightBlock.setBounds(
+                new Rectangle2D.Double(w[2] + w[4], h[0], w[3], h[3])
+            );
         }
         if (this.centerBlock != null) {
-            this.centerBlock.setBounds(new Rectangle2D.Double(w[2], h[0], w[4],
-                    h[4]));
+            this.centerBlock.setBounds(
+                new Rectangle2D.Double(w[2], h[0], w[4], h[4])
+            );
         }
         return new Size2D(constraint.getWidth(), constraint.getHeight());
     }
-
+    
     /**
      * Clears the layout.
      */
@@ -498,36 +541,36 @@
         this.leftBlock = null;
         this.rightBlock = null;
     }
-
+    
     /**
      * Tests this arrangement for equality with an arbitrary object.
-     *
+     * 
      * @param obj  the object (<code>null</code> permitted).
-     *
+     * 
      * @return A boolean.
      */
     public boolean equals(Object obj) {
         if (obj == this) {
-            return true;
+            return true;   
         }
         if (!(obj instanceof BorderArrangement)) {
-            return false;
+            return false;   
         }
         BorderArrangement that = (BorderArrangement) obj;
         if (!ObjectUtilities.equal(this.topBlock, that.topBlock)) {
-            return false;
+            return false;   
         }
         if (!ObjectUtilities.equal(this.bottomBlock, that.bottomBlock)) {
-            return false;
+            return false;   
         }
         if (!ObjectUtilities.equal(this.leftBlock, that.leftBlock)) {
-            return false;
+            return false;   
         }
         if (!ObjectUtilities.equal(this.rightBlock, that.rightBlock)) {
-            return false;
+            return false;   
         }
         if (!ObjectUtilities.equal(this.centerBlock, that.centerBlock)) {
-            return false;
+            return false;   
         }
         return true;
     }

```

## NopolPC 

org.jfree.chart.block.BorderArrangement:492 (Suspicious rank: ample 32, jaccard 32, ochiai 43, naish1 21836, gp13 32, naish2 32, tarantula 32, )
```Java
null!=null
```

Nb Angelic value: 1

Nb analyzed Statement: 21

Execution time: 0:00:38.609000

Grid5000 node: graphene-59.nancy.grid5000.fr

## NopolC 

org.jfree.chart.block.BorderArrangement:492 (Suspicious rank: ample 32, jaccard 32, ochiai 43, naish1 21836, gp13 32, naish2 32, tarantula 32, )
```Java
null!=null
```

Nb Angelic value: 1

Nb analyzed Statement: 21

Execution time: 0:00:37.314000

Grid5000 node: graphene-76.nancy.grid5000.fr

## BrutpolPC 

org.jfree.chart.block.AbstractBlock:162 (Suspicious rank: ample 78, jaccard 78, ochiai 75, naish1 21887, gp13 78, naish2 78, tarantula 78, )
```Java
this.bounds.contains(width, this.height)
```

Nb Angelic value: 4

Nb analyzed Statement: 78

Execution time: 0:02:23.264000

Grid5000 node: griffon-20.nancy.grid5000.fr

## Genprog 

org.jfree.chart.block.BorderArrangement:330 (Suspicious rank: ample 37, jaccard 37, ochiai 21, naish1 21855, gp13 37, naish2 37, tarantula 37, )
INSERT_BEFORE
```Java
this.leftBlock = null
```

Grid5000 node: graphene-76.nancy.grid5000.fr

## Kali 

org.jfree.chart.block.BorderArrangement:482 (Suspicious rank: ample 49, jaccard 49, ochiai 38, naish1 21885, gp13 49, naish2 49, tarantula 49, )
DELETE
```Java
remove
```

org.jfree.chart.block.BorderArrangement:482 (Suspicious rank: ample 49, jaccard 49, ochiai 38, naish1 21885, gp13 49, naish2 49, tarantula 49, )
REPLACE
```Java
if (false) {
	org.jfree.chart.block.RectangleConstraint c3 = new org.jfree.chart.block.RectangleConstraint(0.0 , new org.jfree.data.Range(0.0 , constraint.getWidth()) , org.jfree.chart.block.LengthConstraintType.RANGE , h[2] , null , org.jfree.chart.block.LengthConstraintType.FIXED);
	org.jfree.chart.util.Size2D size = this.leftBlock.arrange(g2, c3);
	w[2] = size.width;
} 
```

org.jfree.chart.block.BorderArrangement:489 (Suspicious rank: ample 13, jaccard 13, ochiai 41, naish1 21774, gp13 13, naish2 13, tarantula 13, )
DELETE
```Java
remove
```

org.jfree.chart.block.BorderArrangement:492 (Suspicious rank: ample 32, jaccard 32, ochiai 43, naish1 21836, gp13 32, naish2 32, tarantula 32, )
DELETE
```Java
remove
```

org.jfree.chart.block.BorderArrangement:492 (Suspicious rank: ample 32, jaccard 32, ochiai 43, naish1 21836, gp13 32, naish2 32, tarantula 32, )
REPLACE
```Java
if (false) {
	org.jfree.chart.block.RectangleConstraint c4 = new org.jfree.chart.block.RectangleConstraint(0.0 , new org.jfree.data.Range(0.0 , ((constraint.getWidth()) - (w[2]))) , org.jfree.chart.block.LengthConstraintType.RANGE , h[2] , null , org.jfree.chart.block.LengthConstraintType.FIXED);
	org.jfree.chart.util.Size2D size = this.rightBlock.arrange(g2, c4);
	w[3] = size.width;
} 
```

Grid5000 node: graphene-62.nancy.grid5000.fr

# Chart 15

Nb Executed tests: 3579

Nb Failing tests: 2

>	org.jfree.chart.plot.junit.PiePlot3DTests#testDrawWithNullDataset
>	org.jfree.chart.plot.junit.PiePlot3DTests#testDrawWithNullDataset

## Human Patch 

```Java
Index: org/jfree/chart/plot/PiePlot.java
===================================================================
--- org/jfree/chart/plot/PiePlot.java	(revision 749)
+++ org/jfree/chart/plot/PiePlot.java	(revision 747)
@@ -1375,9 +1373,6 @@
      * @return The percent.
      */
     public double getMaximumExplodePercent() {
-        if (this.dataset == null) {
-            return 0.0;
-        }
         double result = 0.0;
         Iterator iterator = this.dataset.getKeys().iterator();
         while (iterator.hasNext()) {
@@ -2051,10 +2046,8 @@
      
         PiePlotState state = new PiePlotState(info);
         state.setPassesRequired(2);
-        if (this.dataset != null) {
-            state.setTotal(DatasetUtilities.calculatePieDatasetTotal(
-                    plot.getDataset()));
-        }
+        state.setTotal(DatasetUtilities.calculatePieDatasetTotal(
+                plot.getDataset()));
         state.setLatestAngle(plot.getStartAngle());
         return state;
         

```

## Genprog 

org.jfree.chart.JFreeChart:1219 (Suspicious rank: ample 457, jaccard 457, ochiai 333, naish1 21756, gp13 457, naish2 457, tarantula 457, )
REPLACE
```Java
fireChartChanged()
```

Grid5000 node: graphene-69.nancy.grid5000.fr

## Kali 

org.jfree.chart.plot.PiePlot3D:230 (Suspicious rank: ample 19, jaccard 19, ochiai 7, naish1 21751, gp13 19, naish2 19, tarantula 19, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.PiePlot3D:231 (Suspicious rank: ample 20, jaccard 20, ochiai 8, naish1 21752, gp13 20, naish2 20, tarantula 20, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.PiePlot3D:233 (Suspicious rank: ample 18, jaccard 18, ochiai 9, naish1 21750, gp13 18, naish2 18, tarantula 18, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.PiePlot3D:234 (Suspicious rank: ample 21, jaccard 21, ochiai 10, naish1 21753, gp13 21, naish2 21, tarantula 21, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.PiePlot3D:239 (Suspicious rank: ample 22, jaccard 22, ochiai 11, naish1 21754, gp13 22, naish2 22, tarantula 22, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.PiePlot3D:241 (Suspicious rank: ample 13, jaccard 13, ochiai 12, naish1 21552, gp13 13, naish2 13, tarantula 13, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.PiePlot3D:242 (Suspicious rank: ample 12, jaccard 12, ochiai 13, naish1 21551, gp13 12, naish2 12, tarantula 12, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.PiePlot3D:245 (Suspicious rank: ample 11, jaccard 11, ochiai 14, naish1 21550, gp13 11, naish2 11, tarantula 11, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.PiePlot3D:246 (Suspicious rank: ample 10, jaccard 10, ochiai 15, naish1 21549, gp13 10, naish2 10, tarantula 10, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.PiePlot3D:247 (Suspicious rank: ample 9, jaccard 9, ochiai 16, naish1 21548, gp13 9, naish2 9, tarantula 9, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.PiePlot3D:248 (Suspicious rank: ample 14, jaccard 14, ochiai 17, naish1 21553, gp13 14, naish2 14, tarantula 14, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.PiePlot3D:250 (Suspicious rank: ample 24, jaccard 24, ochiai 18, naish1 21812, gp13 24, naish2 24, tarantula 24, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.PiePlot3D:252 (Suspicious rank: ample 25, jaccard 25, ochiai 19, naish1 21813, gp13 25, naish2 25, tarantula 25, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.PiePlot3D:266 (Suspicious rank: ample 8, jaccard 8, ochiai 20, naish1 21526, gp13 8, naish2 8, tarantula 8, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.PiePlot3D:267 (Suspicious rank: ample 7, jaccard 7, ochiai 21, naish1 21525, gp13 7, naish2 7, tarantula 7, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.PiePlot3D:268 (Suspicious rank: ample 6, jaccard 6, ochiai 22, naish1 21524, gp13 6, naish2 6, tarantula 6, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.PiePlot3D:269 (Suspicious rank: ample 5, jaccard 5, ochiai 23, naish1 21523, gp13 5, naish2 5, tarantula 5, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.PiePlot3D:272 (Suspicious rank: ample 23, jaccard 23, ochiai 24, naish1 21791, gp13 23, naish2 23, tarantula 23, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.PiePlot3D:280 (Suspicious rank: ample 16, jaccard 16, ochiai 25, naish1 21575, gp13 16, naish2 16, tarantula 16, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1195 (Suspicious rank: ample 62, jaccard 62, ochiai 51, naish1 21479, gp13 62, naish2 62, tarantula 62, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1197 (Suspicious rank: ample 63, jaccard 63, ochiai 52, naish1 21480, gp13 63, naish2 63, tarantula 63, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1204 (Suspicious rank: ample 216, jaccard 216, ochiai 170, naish1 21493, gp13 216, naish2 216, tarantula 216, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1205 (Suspicious rank: ample 217, jaccard 217, ochiai 171, naish1 21494, gp13 217, naish2 217, tarantula 217, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1207 (Suspicious rank: ample 218, jaccard 218, ochiai 172, naish1 21495, gp13 218, naish2 218, tarantula 218, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1136 (Suspicious rank: ample 349, jaccard 349, ochiai 312, naish1 21414, gp13 349, naish2 349, tarantula 349, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1140 (Suspicious rank: ample 420, jaccard 420, ochiai 313, naish1 21615, gp13 420, naish2 420, tarantula 420, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1146 (Suspicious rank: ample 419, jaccard 419, ochiai 314, naish1 21614, gp13 419, naish2 419, tarantula 419, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1147 (Suspicious rank: ample 418, jaccard 418, ochiai 315, naish1 21613, gp13 418, naish2 418, tarantula 418, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1149 (Suspicious rank: ample 417, jaccard 417, ochiai 316, naish1 21612, gp13 417, naish2 417, tarantula 417, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1152 (Suspicious rank: ample 331, jaccard 331, ochiai 317, naish1 21341, gp13 331, naish2 331, tarantula 331, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1153 (Suspicious rank: ample 443, jaccard 443, ochiai 318, naish1 21704, gp13 443, naish2 443, tarantula 443, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1154 (Suspicious rank: ample 442, jaccard 442, ochiai 319, naish1 21703, gp13 442, naish2 442, tarantula 442, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1157 (Suspicious rank: ample 330, jaccard 330, ochiai 320, naish1 21340, gp13 330, naish2 330, tarantula 330, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1171 (Suspicious rank: ample 340, jaccard 340, ochiai 321, naish1 21376, gp13 340, naish2 340, tarantula 340, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1186 (Suspicious rank: ample 456, jaccard 456, ochiai 322, naish1 21733, gp13 456, naish2 456, tarantula 456, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1187 (Suspicious rank: ample 455, jaccard 455, ochiai 323, naish1 21732, gp13 455, naish2 455, tarantula 455, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1188 (Suspicious rank: ample 454, jaccard 454, ochiai 324, naish1 21731, gp13 454, naish2 454, tarantula 454, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1190 (Suspicious rank: ample 374, jaccard 374, ochiai 325, naish1 21476, gp13 374, naish2 374, tarantula 374, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1191 (Suspicious rank: ample 375, jaccard 375, ochiai 326, naish1 21477, gp13 375, naish2 375, tarantula 375, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1194 (Suspicious rank: ample 376, jaccard 376, ochiai 327, naish1 21478, gp13 376, naish2 376, tarantula 376, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1202 (Suspicious rank: ample 377, jaccard 377, ochiai 328, naish1 21491, gp13 377, naish2 377, tarantula 377, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1203 (Suspicious rank: ample 378, jaccard 378, ochiai 329, naish1 21492, gp13 378, naish2 378, tarantula 378, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1212 (Suspicious rank: ample 458, jaccard 458, ochiai 330, naish1 21757, gp13 458, naish2 458, tarantula 458, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1215 (Suspicious rank: ample 460, jaccard 460, ochiai 331, naish1 21760, gp13 460, naish2 460, tarantula 460, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1216 (Suspicious rank: ample 459, jaccard 459, ochiai 332, naish1 21759, gp13 459, naish2 459, tarantula 459, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1219 (Suspicious rank: ample 457, jaccard 457, ochiai 333, naish1 21756, gp13 457, naish2 457, tarantula 457, )
DELETE
```Java
remove
```

org.jfree.chart.JFreeChart:1219 (Suspicious rank: ample 457, jaccard 457, ochiai 333, naish1 21756, gp13 457, naish2 457, tarantula 457, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

Grid5000 node: graphene-73.nancy.grid5000.fr

# Chart 17

Nb Executed tests: 3499

Nb Failing tests: 2

>	org.jfree.data.time.junit.TimeSeriesTests#testBug1832432
>	org.jfree.data.time.junit.TimeSeriesTests#testBug1832432

## Human Patch 

```Java
Index: org/jfree/data/time/TimeSeries.java
===================================================================
--- org/jfree/data/time/TimeSeries.java	(revision 622)
+++ org/jfree/data/time/TimeSeries.java	(revision 621)
@@ -854,8 +853,7 @@
      *         subclasses may differ.
      */
     public Object clone() throws CloneNotSupportedException {
-        TimeSeries clone = (TimeSeries) super.clone();
-        clone.data = (List) ObjectUtilities.deepClone(this.data);
+        Object clone = createCopy(0, getItemCount() - 1);
         return clone;
     }
 

```

## BrutpolPC 

org.jfree.data.time.TimeSeries:880 (Suspicious rank: ample 1, jaccard 1, ochiai 1, naish1 21647, gp13 1, naish2 1, tarantula 1, )
```Java
this.data.contains(this)
```

Nb Angelic value: 1

Nb analyzed Statement: 1

Execution time: 0:01:49.194000

Grid5000 node: griffon-92.nancy.grid5000.fr

## BrutpolC 

org.jfree.data.time.TimeSeries:879 (Suspicious rank: ample 3, jaccard 3, ochiai 4, naish1 21611, gp13 3, naish2 3, tarantula 3, )
```Java
this.data.contains(this)
```

Nb Angelic value: 1

Nb analyzed Statement: 3

Execution time: 0:01:47.024000

Grid5000 node: griffon-17.nancy.grid5000.fr

# Chart 21

Nb Executed tests: 3303

Nb Failing tests: 2

>	org.jfree.data.statistics.junit.DefaultBoxAndWhiskerCategoryDatasetTests#testGetRangeBounds
>	org.jfree.data.statistics.junit.DefaultBoxAndWhiskerCategoryDatasetTests#testGetRangeBounds

## Human Patch 

```Java
Index: org/jfree/data/statistics/DefaultBoxAndWhiskerCategoryDataset.java
===================================================================
--- org/jfree/data/statistics/DefaultBoxAndWhiskerCategoryDataset.java	(revision 231)
+++ org/jfree/data/statistics/DefaultBoxAndWhiskerCategoryDataset.java	(revision 227)
@@ -120,14 +119,12 @@
      *
      * @param list  a collection of values from which the various medians will 
      *              be calculated.
-     * @param rowKey  the row key (<code>null</code> not permitted).
-     * @param columnKey  the column key (<code>null</code> not permitted).
-     * 
-     * @see #add(BoxAndWhiskerItem, Comparable, Comparable)
+     * @param rowKey  the row key.
+     * @param columnKey  the column key.
      */
     public void add(List list, Comparable rowKey, Comparable columnKey) {
-        BoxAndWhiskerItem item = BoxAndWhiskerCalculator
-                .calculateBoxAndWhiskerStatistics(list);
+        BoxAndWhiskerItem item 
+            = BoxAndWhiskerCalculator.calculateBoxAndWhiskerStatistics(list);
         add(item, rowKey, columnKey);
     }
     
@@ -136,60 +133,62 @@
      * table.  The various median values are calculated.
      *
      * @param item  a box and whisker item (<code>null</code> not permitted).
-     * @param rowKey  the row key (<code>null</code> not permitted).
-     * @param columnKey  the column key (<code>null</code> not permitted).
-     * 
-     * @see #add(List, Comparable, Comparable)
+     * @param rowKey  the row key.
+     * @param columnKey  the column key.
      */
-    public void add(BoxAndWhiskerItem item, Comparable rowKey, 
-            Comparable columnKey) {
+    public void add(BoxAndWhiskerItem item, 
+                    Comparable rowKey, 
+                    Comparable columnKey) {
 
         this.data.addObject(item, rowKey, columnKey);
         
         // update cached min and max values
         int r = this.data.getRowIndex(rowKey);
         int c = this.data.getColumnIndex(columnKey);
-        if ((this.maximumRangeValueRow == r && this.maximumRangeValueColumn 
-                == c) || (this.minimumRangeValueRow == r 
-                && this.minimumRangeValueColumn == c))  {
-            updateBounds();
+        if (this.maximumRangeValueRow == r 
+                && this.maximumRangeValueColumn == c) {
+            this.maximumRangeValue = Double.NaN;
         }
-        else {
+        if (this.minimumRangeValueRow == r 
+                && this.minimumRangeValueColumn == c) {
+            this.minimumRangeValue = Double.NaN;
+        }
         
-            double minval = Double.NaN;
-            if (item.getMinOutlier() != null) {
-                minval = item.getMinOutlier().doubleValue();
-            }
-            double maxval = Double.NaN;
-            if (item.getMaxOutlier() != null) {
-                maxval = item.getMaxOutlier().doubleValue();
-            }
         
-            if (Double.isNaN(this.maximumRangeValue)) {
-                this.maximumRangeValue = maxval;
-                this.maximumRangeValueRow = r;
-                this.maximumRangeValueColumn = c;
-            }
-            else if (maxval > this.maximumRangeValue) {
-                this.maximumRangeValue = maxval;
-                this.maximumRangeValueRow = r;
-                this.maximumRangeValueColumn = c;
-            }
+        double minval = Double.NaN;
+        if (item.getMinOutlier() != null) {
+            minval = item.getMinOutlier().doubleValue();
+        }
+        double maxval = Double.NaN;
+        if (item.getMaxOutlier() != null) {
+            maxval = item.getMaxOutlier().doubleValue();
+        }
         
-            if (Double.isNaN(this.minimumRangeValue)) {
-                this.minimumRangeValue = minval;
-                this.minimumRangeValueRow = r;
-                this.minimumRangeValueColumn = c;
-            }
-            else if (minval < this.minimumRangeValue) {
-                this.minimumRangeValue = minval;
-                this.minimumRangeValueRow = r;
-                this.minimumRangeValueColumn = c;
-            }
+        if (Double.isNaN(this.maximumRangeValue)) {
+            this.maximumRangeValue = maxval;
+            this.maximumRangeValueRow = r;
+            this.maximumRangeValueColumn = c;
         }
+        else if (maxval > this.maximumRangeValue) {
+            this.maximumRangeValue = maxval;
+            this.maximumRangeValueRow = r;
+            this.maximumRangeValueColumn = c;
+        }
         
+        if (Double.isNaN(this.minimumRangeValue)) {
+            this.minimumRangeValue = minval;
+            this.minimumRangeValueRow = r;
+            this.minimumRangeValueColumn = c;
+        }
+        else if (minval < this.minimumRangeValue) {
+            this.minimumRangeValue = minval;
+            this.minimumRangeValueRow = r;
+            this.minimumRangeValueColumn = c;
+        }
+        
         this.rangeBounds = new Range(this.minimumRangeValue,
               this.maximumRangeValue);
+
         fireDatasetChanged();
 
     }
@@ -735,52 +678,6 @@
     }
     
     /**
-     * Resets the cached bounds, by iterating over the entire dataset to find
-     * the current bounds.
-     */
-    private void updateBounds() {
-        this.minimumRangeValue = Double.NaN;
-        this.minimumRangeValueRow = -1;
-        this.minimumRangeValueColumn = -1;
-        this.maximumRangeValue = Double.NaN;
-        this.maximumRangeValueRow = -1;
-        this.maximumRangeValueColumn = -1;
-        int rowCount = getRowCount();
-        int columnCount = getColumnCount();
-        for (int r = 0; r < rowCount; r++) {
-            for (int c = 0; c < columnCount; c++) {
-                BoxAndWhiskerItem item = getItem(r, c);
-                if (item != null) {
-                    Number min = item.getMinOutlier();
-                    if (min != null) {
-                        double minv = min.doubleValue();
-                        if (!Double.isNaN(minv)) {
-                            if (minv < this.minimumRangeValue || Double.isNaN(
-                                    this.minimumRangeValue)) {
-                                this.minimumRangeValue = minv;
-                                this.minimumRangeValueRow = r;
-                                this.minimumRangeValueColumn = c;
-                            }
-                        }
-                    }
-                    Number max = item.getMaxOutlier();
-                    if (max != null) {
-                        double maxv = max.doubleValue();
-                        if (!Double.isNaN(maxv)) {
-                            if (maxv > this.maximumRangeValue || Double.isNaN(
-                                    this.maximumRangeValue)) {
-                                this.maximumRangeValue = maxv;
-                                this.maximumRangeValueRow = r;
-                                this.maximumRangeValueColumn = c;
-                            }
-                        }
-                    }
-                }
-            }
-        }
-    }
-    
-    /**
      * Tests this dataset for equality with an arbitrary object.
      * 
      * @param obj  the object to test against (<code>null</code> permitted).

```

## NopolPC 

org.jfree.data.Range:334 (Suspicious rank: ample 75, jaccard 75, ochiai 73, naish1 20594, gp13 75, naish2 75, tarantula 75, )
```Java
0 == 1
```

Nb Angelic value: 1

Nb analyzed Statement: 73

Execution time: 0:00:44.899000

Grid5000 node: graphene-56.nancy.grid5000.fr

## NopolC 

org.jfree.data.Range:334 (Suspicious rank: ample 75, jaccard 75, ochiai 73, naish1 20594, gp13 75, naish2 75, tarantula 75, )
```Java
0 == 1
```

Nb Angelic value: 1

Nb analyzed Statement: 73

Execution time: 0:00:41.548000

Grid5000 node: graphene-39.nancy.grid5000.fr

## Genprog 

org.jfree.data.Range:334 (Suspicious rank: ample 75, jaccard 75, ochiai 73, naish1 20594, gp13 75, naish2 75, tarantula 75, )
DELETE
```Java
remove
```

Grid5000 node: graphene-57.nancy.grid5000.fr

## Kali 

org.jfree.data.Range:335 (Suspicious rank: ample 9, jaccard 9, ochiai 9, naish1 20593, gp13 9, naish2 9, tarantula 9, )
DELETE
```Java
remove
```

org.jfree.data.Range:334 (Suspicious rank: ample 75, jaccard 75, ochiai 73, naish1 20594, gp13 75, naish2 75, tarantula 75, )
DELETE
```Java
remove
```

org.jfree.data.Range:334 (Suspicious rank: ample 75, jaccard 75, ochiai 73, naish1 20594, gp13 75, naish2 75, tarantula 75, )
REPLACE
```Java
if (false) {
	return false;
} 
```

Grid5000 node: griffon-77.nancy.grid5000.fr

# Chart 25

Nb Executed tests: 3243

Nb Failing tests: 8

>	org.jfree.chart.renderer.category.junit.StatisticalBarRendererTests#testDrawWithNullMeanVertical
>	org.jfree.chart.renderer.category.junit.StatisticalBarRendererTests#testDrawWithNullDeviationVertical
>	org.jfree.chart.renderer.category.junit.StatisticalBarRendererTests#testDrawWithNullMeanHorizontal
>	org.jfree.chart.renderer.category.junit.StatisticalBarRendererTests#testDrawWithNullDeviationHorizontal
>	org.jfree.chart.renderer.category.junit.StatisticalBarRendererTests#testDrawWithNullMeanVertical
>	org.jfree.chart.renderer.category.junit.StatisticalBarRendererTests#testDrawWithNullDeviationVertical
>	org.jfree.chart.renderer.category.junit.StatisticalBarRendererTests#testDrawWithNullMeanHorizontal
>	org.jfree.chart.renderer.category.junit.StatisticalBarRendererTests#testDrawWithNullDeviationHorizontal

## Human Patch 

```Java
Index: org/jfree/chart/renderer/category/StatisticalBarRenderer.java
===================================================================
--- org/jfree/chart/renderer/category/StatisticalBarRenderer.java	(revision 164)
+++ org/jfree/chart/renderer/category/StatisticalBarRenderer.java	(revision 162)
@@ -256,9 +255,6 @@
 
         // BAR X
         Number meanValue = dataset.getMeanValue(row, column);
-        if (meanValue == null) {
-            return;
-        }
 
         double value = meanValue.doubleValue();
         double base = 0.0;
@@ -315,44 +311,41 @@
         }
 
         // standard deviation lines
-        Number n = dataset.getStdDevValue(row, column);
-        if (n != null) {
-            double valueDelta = n.doubleValue();
-            double highVal = rangeAxis.valueToJava2D(meanValue.doubleValue() 
-                    + valueDelta, dataArea, yAxisLocation);
-            double lowVal = rangeAxis.valueToJava2D(meanValue.doubleValue() 
-                    - valueDelta, dataArea, yAxisLocation);
+        double valueDelta = dataset.getStdDevValue(row, column).doubleValue();
+        double highVal = rangeAxis.valueToJava2D(meanValue.doubleValue() 
+                + valueDelta, dataArea, yAxisLocation);
+        double lowVal = rangeAxis.valueToJava2D(meanValue.doubleValue() 
+                - valueDelta, dataArea, yAxisLocation);
 
-            if (this.errorIndicatorStroke != null) {
-                g2.setStroke(this.errorIndicatorStroke);
-            }
-            else {
-                g2.setStroke(getItemOutlineStroke(row, column));
-            }
-            if (this.errorIndicatorPaint != null) {
-                g2.setPaint(this.errorIndicatorPaint);  
-            }
-            else {
-                g2.setPaint(getItemOutlinePaint(row, column));   
-            }
-        
-            Line2D line = null;
-            line = new Line2D.Double(lowVal, rectY + rectHeight / 2.0d, 
-                                     highVal, rectY + rectHeight / 2.0d);
-            g2.draw(line);
-            line = new Line2D.Double(highVal, rectY + rectHeight * 0.25, 
-                                     highVal, rectY + rectHeight * 0.75);
-            g2.draw(line);
-            line = new Line2D.Double(lowVal, rectY + rectHeight * 0.25, 
-                                     lowVal, rectY + rectHeight * 0.75);
-            g2.draw(line);
+        if (this.errorIndicatorStroke != null) {
+            g2.setStroke(this.errorIndicatorStroke);
         }
+        else {
+            g2.setStroke(getItemOutlineStroke(row, column));
+        }
+        if (this.errorIndicatorPaint != null) {
+            g2.setPaint(this.errorIndicatorPaint);  
+        }
+        else {
+            g2.setPaint(getItemOutlinePaint(row, column));   
+        }
         
+        Line2D line = null;
+        line = new Line2D.Double(lowVal, rectY + rectHeight / 2.0d, 
+                                 highVal, rectY + rectHeight / 2.0d);
+        g2.draw(line);
+        line = new Line2D.Double(highVal, rectY + rectHeight * 0.25, 
+                                 highVal, rectY + rectHeight * 0.75);
+        g2.draw(line);
+        line = new Line2D.Double(lowVal, rectY + rectHeight * 0.25, 
+                                 lowVal, rectY + rectHeight * 0.75);
+        g2.draw(line);
+        
         CategoryItemLabelGenerator generator = getItemLabelGenerator(row, 
                 column);
         if (generator != null && isItemLabelVisible(row, column)) {
             drawItemLabel(g2, dataset, row, column, plot, generator, bar, 
-                    (value < 0.0));
+                (value < 0.0));
         }        
 
         // add an item entity, if this information is being collected
@@ -406,9 +399,6 @@
 
         // BAR Y
         Number meanValue = dataset.getMeanValue(row, column);
-        if (meanValue == null) {
-            return;
-        }
 
         double value = meanValue.doubleValue();
         double base = 0.0;
@@ -465,43 +455,40 @@
         }
 
         // standard deviation lines
-        Number n = dataset.getStdDevValue(row, column);
-        if (n != null) {
-            double valueDelta = n.doubleValue();
-            double highVal = rangeAxis.valueToJava2D(meanValue.doubleValue() 
-                    + valueDelta, dataArea, yAxisLocation);
-            double lowVal = rangeAxis.valueToJava2D(meanValue.doubleValue() 
-                    - valueDelta, dataArea, yAxisLocation);
+        double valueDelta = dataset.getStdDevValue(row, column).doubleValue();
+        double highVal = rangeAxis.valueToJava2D(meanValue.doubleValue() 
+                + valueDelta, dataArea, yAxisLocation);
+        double lowVal = rangeAxis.valueToJava2D(meanValue.doubleValue() 
+                - valueDelta, dataArea, yAxisLocation);
 
-            if (this.errorIndicatorStroke != null) {
-                g2.setStroke(this.errorIndicatorStroke);
-            }
-            else {
-                g2.setStroke(getItemOutlineStroke(row, column));
-            }
-            if (this.errorIndicatorPaint != null) {
-                g2.setPaint(this.errorIndicatorPaint);  
-            }
-            else {
-                g2.setPaint(getItemOutlinePaint(row, column));   
-            }
-            Line2D line = null;
-            line = new Line2D.Double(rectX + rectWidth / 2.0d, lowVal,
-                                     rectX + rectWidth / 2.0d, highVal);
-            g2.draw(line);
-            line = new Line2D.Double(rectX + rectWidth / 2.0d - 5.0d, highVal,
-                                     rectX + rectWidth / 2.0d + 5.0d, highVal);
-            g2.draw(line);
-            line = new Line2D.Double(rectX + rectWidth / 2.0d - 5.0d, lowVal,
-                                     rectX + rectWidth / 2.0d + 5.0d, lowVal);
-            g2.draw(line);
+        if (this.errorIndicatorStroke != null) {
+            g2.setStroke(this.errorIndicatorStroke);
         }
+        else {
+            g2.setStroke(getItemOutlineStroke(row, column));
+        }
+        if (this.errorIndicatorPaint != null) {
+            g2.setPaint(this.errorIndicatorPaint);  
+        }
+        else {
+            g2.setPaint(getItemOutlinePaint(row, column));   
+        }
+        Line2D line = null;
+        line = new Line2D.Double(rectX + rectWidth / 2.0d, lowVal,
+                                 rectX + rectWidth / 2.0d, highVal);
+        g2.draw(line);
+        line = new Line2D.Double(rectX + rectWidth / 2.0d - 5.0d, highVal,
+                                 rectX + rectWidth / 2.0d + 5.0d, highVal);
+        g2.draw(line);
+        line = new Line2D.Double(rectX + rectWidth / 2.0d - 5.0d, lowVal,
+                                 rectX + rectWidth / 2.0d + 5.0d, lowVal);
+        g2.draw(line);
         
         CategoryItemLabelGenerator generator = getItemLabelGenerator(row, 
                 column);
         if (generator != null && isItemLabelVisible(row, column)) {
             drawItemLabel(g2, dataset, row, column, plot, generator, bar, 
-                    (value < 0.0));
+                (value < 0.0));
         }        
 
         // add an item entity, if this information is being collected

```

## NopolPC 

org.jfree.chart.renderer.category.StatisticalBarRenderer:207 (Suspicious rank: ample 4, jaccard 4, ochiai 4, naish1 19842, gp13 4, naish2 4, tarantula 50, )
```Java
0 == -1
```

Nb Angelic value: 1

Nb analyzed Statement: 2

Execution time: 0:00:32.361000

Grid5000 node: graphene-91.nancy.grid5000.fr

## NopolC 

org.jfree.data.statistics.DefaultStatisticalCategoryDataset:110 (Suspicious rank: ample 17, jaccard 17, ochiai 8, naish1 19962, gp13 17, naish2 17, tarantula 63, )
```Java
result!=null
```

Nb Angelic value: 1

Nb analyzed Statement: 20

Execution time: 0:00:37.503000

Grid5000 node: graphene-72.nancy.grid5000.fr

## BrutpolPC 

org.jfree.data.statistics.DefaultStatisticalCategoryDataset:111 (Suspicious rank: ample 18, jaccard 18, ochiai 9, naish1 19963, gp13 18, naish2 18, tarantula 64, )
```Java
this.equals(masd)
```

Nb Angelic value: 2

Nb analyzed Statement: 19

Execution time: 0:08:34.755000

Grid5000 node: griffon-22.nancy.grid5000.fr

## BrutpolC 

org.jfree.data.statistics.DefaultStatisticalCategoryDataset:110 (Suspicious rank: ample 17, jaccard 17, ochiai 8, naish1 19962, gp13 17, naish2 17, tarantula 63, )
```Java
this.equals(masd)
```

Nb Angelic value: 1

Nb analyzed Statement: 20

Execution time: 0:01:52.873000

Grid5000 node: griffon-59.nancy.grid5000.fr

## Genprog 

org.jfree.data.statistics.DefaultStatisticalCategoryDataset:301 (Suspicious rank: ample 65, jaccard 144, ochiai 102, naish1 19848, gp13 65, naish2 65, tarantula 160, )
DELETE
```Java
remove
```

Grid5000 node: graphene-53.nancy.grid5000.fr

## Kali 

org.jfree.chart.renderer.category.StatisticalBarRenderer:200 (Suspicious rank: ample 5, jaccard 5, ochiai 1, naish1 19843, gp13 5, naish2 5, tarantula 51, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.renderer.category.StatisticalBarRenderer:204 (Suspicious rank: ample 2, jaccard 2, ochiai 2, naish1 19840, gp13 2, naish2 2, tarantula 48, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.renderer.category.StatisticalBarRenderer:206 (Suspicious rank: ample 3, jaccard 3, ochiai 3, naish1 19841, gp13 3, naish2 3, tarantula 49, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.renderer.category.StatisticalBarRenderer:207 (Suspicious rank: ample 4, jaccard 4, ochiai 4, naish1 19842, gp13 4, naish2 4, tarantula 50, )
DELETE
```Java
remove
```

org.jfree.chart.renderer.category.StatisticalBarRenderer:207 (Suspicious rank: ample 4, jaccard 4, ochiai 4, naish1 19842, gp13 4, naish2 4, tarantula 50, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.data.statistics.DefaultStatisticalCategoryDataset:107 (Suspicious rank: ample 8, jaccard 8, ochiai 6, naish1 18755, gp13 8, naish2 8, tarantula 54, )
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.jfree.data.statistics.DefaultStatisticalCategoryDataset:108 (Suspicious rank: ample 7, jaccard 7, ochiai 7, naish1 18754, gp13 7, naish2 7, tarantula 53, )
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.jfree.data.statistics.DefaultStatisticalCategoryDataset:110 (Suspicious rank: ample 17, jaccard 17, ochiai 8, naish1 19962, gp13 17, naish2 17, tarantula 63, )
DELETE
```Java
remove
```

org.jfree.data.statistics.DefaultStatisticalCategoryDataset:110 (Suspicious rank: ample 17, jaccard 17, ochiai 8, naish1 19962, gp13 17, naish2 17, tarantula 63, )
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.jfree.data.statistics.DefaultStatisticalCategoryDataset:110 (Suspicious rank: ample 17, jaccard 17, ochiai 8, naish1 19962, gp13 17, naish2 17, tarantula 63, )
REPLACE
```Java
if (false) {
	result = masd.getMean();
} 
```

org.jfree.data.statistics.DefaultStatisticalCategoryDataset:111 (Suspicious rank: ample 18, jaccard 18, ochiai 9, naish1 19963, gp13 18, naish2 18, tarantula 64, )
DELETE
```Java
remove
```

org.jfree.data.statistics.DefaultStatisticalCategoryDataset:111 (Suspicious rank: ample 18, jaccard 18, ochiai 9, naish1 19963, gp13 18, naish2 18, tarantula 64, )
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.jfree.data.statistics.DefaultStatisticalCategoryDataset:113 (Suspicious rank: ample 19, jaccard 19, ochiai 10, naish1 19964, gp13 19, naish2 19, tarantula 65, )
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.jfree.data.statistics.DefaultStatisticalCategoryDataset:126 (Suspicious rank: ample 9, jaccard 9, ochiai 11, naish1 18831, gp13 9, naish2 9, tarantula 55, )
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.jfree.data.statistics.DefaultStatisticalCategoryDataset:264 (Suspicious rank: ample 16, jaccard 16, ochiai 19, naish1 19775, gp13 16, naish2 16, tarantula 62, )
INSERT_BEFORE
```Java
if (true)
	return 0;

```

org.jfree.data.statistics.DefaultStatisticalCategoryDataset:273 (Suspicious rank: ample 13, jaccard 13, ochiai 20, naish1 19432, gp13 13, naish2 13, tarantula 59, )
INSERT_BEFORE
```Java
if (true)
	return 0;

```

org.jfree.data.statistics.MeanAndStandardDeviation:95 (Suspicious rank: ample 12, jaccard 12, ochiai 21, naish1 19247, gp13 12, naish2 12, tarantula 58, )
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.jfree.data.statistics.DefaultStatisticalCategoryDataset:301 (Suspicious rank: ample 65, jaccard 144, ochiai 102, naish1 19848, gp13 65, naish2 65, tarantula 160, )
DELETE
```Java
remove
```

org.jfree.data.KeyedObjects2D:229 (Suspicious rank: ample 77, jaccard 170, ochiai 123, naish1 20005, gp13 77, naish2 77, tarantula 172, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.data.KeyedObjects2D:108 (Suspicious rank: ample 90, jaccard 185, ochiai 180, naish1 19094, gp13 90, naish2 90, tarantula 186, )
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.jfree.data.KeyedObjects2D:109 (Suspicious rank: ample 91, jaccard 186, ochiai 181, naish1 19095, gp13 91, naish2 91, tarantula 187, )
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.jfree.data.KeyedObjects2D:110 (Suspicious rank: ample 97, jaccard 192, ochiai 182, naish1 20204, gp13 97, naish2 97, tarantula 193, )
DELETE
```Java
remove
```

org.jfree.data.KeyedObjects2D:110 (Suspicious rank: ample 97, jaccard 192, ochiai 182, naish1 20204, gp13 97, naish2 97, tarantula 193, )
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.jfree.data.KeyedObjects2D:110 (Suspicious rank: ample 97, jaccard 192, ochiai 182, naish1 20204, gp13 97, naish2 97, tarantula 193, )
REPLACE
```Java
if (false) {
	java.lang.Comparable columnKey = ((java.lang.Comparable)(this.columnKeys.get(column)));
	if (columnKey != null) {
		result = rowData.getObject(columnKey);
	} 
} 
```

org.jfree.data.KeyedObjects2D:111 (Suspicious rank: ample 96, jaccard 191, ochiai 183, naish1 20203, gp13 96, naish2 96, tarantula 192, )
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.jfree.data.KeyedObjects2D:112 (Suspicious rank: ample 94, jaccard 189, ochiai 184, naish1 19621, gp13 94, naish2 94, tarantula 190, )
DELETE
```Java
remove
```

org.jfree.data.KeyedObjects2D:112 (Suspicious rank: ample 94, jaccard 189, ochiai 184, naish1 19621, gp13 94, naish2 94, tarantula 190, )
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.jfree.data.KeyedObjects2D:112 (Suspicious rank: ample 94, jaccard 189, ochiai 184, naish1 19621, gp13 94, naish2 94, tarantula 190, )
REPLACE
```Java
if (false) {
	result = rowData.getObject(columnKey);
} 
```

org.jfree.data.KeyedObjects2D:113 (Suspicious rank: ample 93, jaccard 188, ochiai 185, naish1 19619, gp13 93, naish2 93, tarantula 189, )
DELETE
```Java
remove
```

org.jfree.data.KeyedObjects2D:113 (Suspicious rank: ample 93, jaccard 188, ochiai 185, naish1 19619, gp13 93, naish2 93, tarantula 189, )
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.jfree.data.KeyedObjects2D:116 (Suspicious rank: ample 98, jaccard 193, ochiai 186, naish1 20205, gp13 98, naish2 98, tarantula 194, )
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.jfree.data.KeyedObjects2D:86 (Suspicious rank: ample 119, jaccard 215, ochiai 193, naish1 19731, gp13 119, naish2 119, tarantula 215, )
INSERT_BEFORE
```Java
if (true)
	return 0;

```

org.jfree.data.KeyedObjects2D:95 (Suspicious rank: ample 103, jaccard 198, ochiai 194, naish1 18564, gp13 103, naish2 103, tarantula 199, )
INSERT_BEFORE
```Java
if (true)
	return 0;

```

org.jfree.chart.renderer.category.AbstractCategoryItemRenderer:248 (Suspicious rank: ample 141, jaccard 237, ochiai 237, naish1 19926, gp13 141, naish2 141, tarantula 237, )
INSERT_BEFORE
```Java
if (true)
	return 0;

```

org.jfree.data.KeyedObjects2D:236 (Suspicious rank: ample 154, jaccard 250, ochiai 249, naish1 18725, gp13 154, naish2 154, tarantula 250, )
DELETE
```Java
remove
```

org.jfree.data.KeyedObjects2D:236 (Suspicious rank: ample 154, jaccard 250, ochiai 249, naish1 18725, gp13 154, naish2 154, tarantula 250, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.data.KeyedObjects2D:237 (Suspicious rank: ample 155, jaccard 251, ochiai 250, naish1 18726, gp13 155, naish2 155, tarantula 251, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.data.KeyedObjects2D:238 (Suspicious rank: ample 149, jaccard 245, ochiai 251, naish1 18720, gp13 149, naish2 149, tarantula 245, )
DELETE
```Java
remove
```

org.jfree.data.KeyedObjects2D:238 (Suspicious rank: ample 149, jaccard 245, ochiai 251, naish1 18720, gp13 149, naish2 149, tarantula 245, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.data.KeyedObjects2D:238 (Suspicious rank: ample 149, jaccard 245, ochiai 251, naish1 18720, gp13 149, naish2 149, tarantula 245, )
REPLACE
```Java
if (false) {
	this.columnKeys.add(columnKey);
} 
```

org.jfree.data.KeyedObjects2D:239 (Suspicious rank: ample 150, jaccard 246, ochiai 252, naish1 18721, gp13 150, naish2 150, tarantula 246, )
DELETE
```Java
remove
```

org.jfree.data.KeyedObjects2D:239 (Suspicious rank: ample 150, jaccard 246, ochiai 252, naish1 18721, gp13 150, naish2 150, tarantula 246, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2865 (Suspicious rank: ample 166, jaccard 262, ochiai 259, naish1 19694, gp13 166, naish2 166, tarantula 263, )
DELETE
```Java
remove
```

org.jfree.chart.plot.CategoryPlot:2865 (Suspicious rank: ample 166, jaccard 262, ochiai 259, naish1 19694, gp13 166, naish2 166, tarantula 263, )
INSERT_BEFORE
```Java
if (true)
	return false;

```

org.jfree.chart.plot.CategoryPlot:2866 (Suspicious rank: ample 167, jaccard 263, ochiai 260, naish1 19695, gp13 167, naish2 167, tarantula 264, )
DELETE
```Java
remove
```

org.jfree.chart.plot.CategoryPlot:2866 (Suspicious rank: ample 167, jaccard 263, ochiai 260, naish1 19695, gp13 167, naish2 167, tarantula 264, )
INSERT_BEFORE
```Java
if (true)
	return false;

```

org.jfree.chart.plot.CategoryPlot:2867 (Suspicious rank: ample 168, jaccard 264, ochiai 261, naish1 19696, gp13 168, naish2 168, tarantula 265, )
DELETE
```Java
remove
```

org.jfree.chart.plot.CategoryPlot:2867 (Suspicious rank: ample 168, jaccard 264, ochiai 261, naish1 19696, gp13 168, naish2 168, tarantula 265, )
INSERT_BEFORE
```Java
if (true)
	return false;

```

org.jfree.chart.plot.CategoryPlot:2868 (Suspicious rank: ample 169, jaccard 265, ochiai 262, naish1 19701, gp13 169, naish2 169, tarantula 266, )
DELETE
```Java
remove
```

org.jfree.chart.plot.CategoryPlot:2868 (Suspicious rank: ample 169, jaccard 265, ochiai 262, naish1 19701, gp13 169, naish2 169, tarantula 266, )
INSERT_BEFORE
```Java
if (true)
	return false;

```

org.jfree.chart.JFreeChart:1373 (Suspicious rank: ample 264, jaccard 361, ochiai 276, naish1 19595, gp13 264, naish2 264, tarantula 379, )
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.jfree.chart.JFreeChart:1391 (Suspicious rank: ample 245, jaccard 341, ochiai 277, naish1 19226, gp13 245, naish2 245, tarantula 360, )
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.jfree.chart.JFreeChart:1392 (Suspicious rank: ample 243, jaccard 339, ochiai 278, naish1 19224, gp13 243, naish2 243, tarantula 358, )
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.jfree.chart.JFreeChart:1393 (Suspicious rank: ample 244, jaccard 340, ochiai 279, naish1 19225, gp13 244, naish2 244, tarantula 359, )
DELETE
```Java
remove
```

org.jfree.chart.JFreeChart:1393 (Suspicious rank: ample 244, jaccard 340, ochiai 279, naish1 19225, gp13 244, naish2 244, tarantula 359, )
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.jfree.chart.plot.CategoryPlot:2857 (Suspicious rank: ample 218, jaccard 314, ochiai 284, naish1 18439, gp13 218, naish2 218, tarantula 333, )
INSERT_BEFORE
```Java
if (true)
	return false;

```

org.jfree.chart.plot.CategoryPlot:2858 (Suspicious rank: ample 217, jaccard 313, ochiai 285, naish1 18428, gp13 217, naish2 217, tarantula 332, )
INSERT_BEFORE
```Java
if (true)
	return false;

```

org.jfree.chart.plot.CategoryPlot:2860 (Suspicious rank: ample 273, jaccard 370, ochiai 286, naish1 19697, gp13 273, naish2 273, tarantula 388, )
INSERT_BEFORE
```Java
if (true)
	return false;

```

org.jfree.chart.plot.CategoryPlot:2861 (Suspicious rank: ample 274, jaccard 371, ochiai 287, naish1 19698, gp13 274, naish2 274, tarantula 389, )
INSERT_BEFORE
```Java
if (true)
	return false;

```

org.jfree.chart.plot.CategoryPlot:2862 (Suspicious rank: ample 275, jaccard 372, ochiai 288, naish1 19699, gp13 275, naish2 275, tarantula 390, )
INSERT_BEFORE
```Java
if (true)
	return false;

```

org.jfree.chart.plot.CategoryPlot:2863 (Suspicious rank: ample 276, jaccard 373, ochiai 289, naish1 19700, gp13 276, naish2 276, tarantula 391, )
DELETE
```Java
remove
```

org.jfree.chart.plot.CategoryPlot:2863 (Suspicious rank: ample 276, jaccard 373, ochiai 289, naish1 19700, gp13 276, naish2 276, tarantula 391, )
INSERT_BEFORE
```Java
if (true)
	return false;

```

org.jfree.chart.plot.CategoryPlot:2864 (Suspicious rank: ample 272, jaccard 369, ochiai 290, naish1 19693, gp13 272, naish2 272, tarantula 387, )
DELETE
```Java
remove
```

org.jfree.chart.plot.CategoryPlot:2864 (Suspicious rank: ample 272, jaccard 369, ochiai 290, naish1 19693, gp13 272, naish2 272, tarantula 387, )
INSERT_BEFORE
```Java
if (true)
	return false;

```

org.jfree.data.general.DatasetUtilities:574 (Suspicious rank: ample 302, jaccard 399, ochiai 413, naish1 18963, gp13 302, naish2 302, tarantula 419, )
DELETE
```Java
remove
```

org.jfree.data.general.DatasetUtilities:575 (Suspicious rank: ample 301, jaccard 398, ochiai 414, naish1 18962, gp13 301, naish2 301, tarantula 418, )
DELETE
```Java
remove
```

org.jfree.data.general.DatasetUtilities:576 (Suspicious rank: ample 300, jaccard 397, ochiai 415, naish1 18961, gp13 300, naish2 300, tarantula 417, )
DELETE
```Java
remove
```

org.jfree.data.general.DatasetUtilities:576 (Suspicious rank: ample 300, jaccard 397, ochiai 415, naish1 18961, gp13 300, naish2 300, tarantula 417, )
REPLACE
```Java
if (false) {
	return false;
} 
```

org.jfree.data.general.DatasetUtilities:577 (Suspicious rank: ample 308, jaccard 405, ochiai 416, naish1 19259, gp13 308, naish2 308, tarantula 425, )
DELETE
```Java
remove
```

org.jfree.chart.plot.CategoryPlot:2569 (Suspicious rank: ample 330, jaccard 440, ochiai 424, naish1 19539, gp13 330, naish2 330, tarantula 447, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2558 (Suspicious rank: ample 402, jaccard 517, ochiai 529, naish1 18340, gp13 402, naish2 402, tarantula 543, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2559 (Suspicious rank: ample 403, jaccard 518, ochiai 530, naish1 18341, gp13 403, naish2 403, tarantula 544, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2560 (Suspicious rank: ample 536, jaccard 651, ochiai 531, naish1 19538, gp13 536, naish2 536, tarantula 677, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2560 (Suspicious rank: ample 536, jaccard 651, ochiai 531, naish1 19538, gp13 536, naish2 536, tarantula 677, )
REPLACE
```Java
if (true) {
	return ;
} 
```

org.jfree.chart.plot.CategoryPlot:2565 (Suspicious rank: ample 535, jaccard 650, ochiai 532, naish1 19537, gp13 535, naish2 535, tarantula 676, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2571 (Suspicious rank: ample 389, jaccard 504, ochiai 533, naish1 18267, gp13 389, naish2 389, tarantula 530, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2574 (Suspicious rank: ample 387, jaccard 502, ochiai 534, naish1 18265, gp13 387, naish2 387, tarantula 528, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2575 (Suspicious rank: ample 388, jaccard 503, ochiai 535, naish1 18266, gp13 388, naish2 388, tarantula 529, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2578 (Suspicious rank: ample 390, jaccard 505, ochiai 536, naish1 18268, gp13 390, naish2 390, tarantula 531, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2579 (Suspicious rank: ample 391, jaccard 506, ochiai 537, naish1 18269, gp13 391, naish2 391, tarantula 532, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2580 (Suspicious rank: ample 589, jaccard 706, ochiai 538, naish1 20081, gp13 589, naish2 589, tarantula 730, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2582 (Suspicious rank: ample 588, jaccard 705, ochiai 539, naish1 20080, gp13 588, naish2 588, tarantula 729, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2586 (Suspicious rank: ample 591, jaccard 708, ochiai 540, naish1 20083, gp13 591, naish2 591, tarantula 732, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2587 (Suspicious rank: ample 590, jaccard 707, ochiai 541, naish1 20082, gp13 590, naish2 590, tarantula 731, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2593 (Suspicious rank: ample 476, jaccard 591, ochiai 542, naish1 18860, gp13 476, naish2 476, tarantula 617, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2596 (Suspicious rank: ample 474, jaccard 589, ochiai 543, naish1 18858, gp13 474, naish2 474, tarantula 615, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2597 (Suspicious rank: ample 475, jaccard 590, ochiai 544, naish1 18859, gp13 475, naish2 475, tarantula 616, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2599 (Suspicious rank: ample 473, jaccard 588, ochiai 545, naish1 18857, gp13 473, naish2 473, tarantula 614, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2601 (Suspicious rank: ample 614, jaccard 731, ochiai 546, naish1 20284, gp13 614, naish2 614, tarantula 755, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2602 (Suspicious rank: ample 615, jaccard 732, ochiai 547, naish1 20285, gp13 615, naish2 615, tarantula 756, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2608 (Suspicious rank: ample 612, jaccard 729, ochiai 548, naish1 20282, gp13 612, naish2 612, tarantula 753, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2609 (Suspicious rank: ample 613, jaccard 730, ochiai 549, naish1 20283, gp13 613, naish2 613, tarantula 754, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2613 (Suspicious rank: ample 500, jaccard 615, ochiai 550, naish1 19183, gp13 500, naish2 500, tarantula 641, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2614 (Suspicious rank: ample 499, jaccard 614, ochiai 551, naish1 19182, gp13 499, naish2 499, tarantula 640, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2616 (Suspicious rank: ample 498, jaccard 613, ochiai 552, naish1 19181, gp13 498, naish2 498, tarantula 639, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2617 (Suspicious rank: ample 497, jaccard 612, ochiai 553, naish1 19180, gp13 497, naish2 497, tarantula 638, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2621 (Suspicious rank: ample 602, jaccard 719, ochiai 554, naish1 20211, gp13 602, naish2 602, tarantula 743, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2624 (Suspicious rank: ample 550, jaccard 665, ochiai 555, naish1 19666, gp13 550, naish2 550, tarantula 691, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2625 (Suspicious rank: ample 601, jaccard 718, ochiai 556, naish1 20210, gp13 601, naish2 601, tarantula 742, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2628 (Suspicious rank: ample 598, jaccard 715, ochiai 557, naish1 20207, gp13 598, naish2 598, tarantula 739, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2629 (Suspicious rank: ample 599, jaccard 716, ochiai 558, naish1 20208, gp13 599, naish2 599, tarantula 740, )
DELETE
```Java
remove
```

org.jfree.chart.plot.CategoryPlot:2629 (Suspicious rank: ample 599, jaccard 716, ochiai 558, naish1 20208, gp13 599, naish2 599, tarantula 740, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2661 (Suspicious rank: ample 361, jaccard 476, ochiai 559, naish1 18003, gp13 361, naish2 361, tarantula 502, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2662 (Suspicious rank: ample 359, jaccard 474, ochiai 560, naish1 18001, gp13 359, naish2 359, tarantula 500, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2663 (Suspicious rank: ample 360, jaccard 475, ochiai 561, naish1 18002, gp13 360, naish2 360, tarantula 501, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2664 (Suspicious rank: ample 364, jaccard 479, ochiai 562, naish1 18006, gp13 364, naish2 364, tarantula 505, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2665 (Suspicious rank: ample 365, jaccard 480, ochiai 563, naish1 18007, gp13 365, naish2 365, tarantula 506, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2666 (Suspicious rank: ample 362, jaccard 477, ochiai 564, naish1 18004, gp13 362, naish2 362, tarantula 503, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2667 (Suspicious rank: ample 363, jaccard 478, ochiai 565, naish1 18005, gp13 363, naish2 363, tarantula 504, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2672 (Suspicious rank: ample 508, jaccard 623, ochiai 566, naish1 19270, gp13 508, naish2 508, tarantula 649, )
DELETE
```Java
remove
```

org.jfree.chart.plot.CategoryPlot:2672 (Suspicious rank: ample 508, jaccard 623, ochiai 566, naish1 19270, gp13 508, naish2 508, tarantula 649, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2673 (Suspicious rank: ample 507, jaccard 622, ochiai 567, naish1 19269, gp13 507, naish2 507, tarantula 648, )
DELETE
```Java
remove
```

org.jfree.chart.plot.CategoryPlot:2673 (Suspicious rank: ample 507, jaccard 622, ochiai 567, naish1 19269, gp13 507, naish2 507, tarantula 648, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

Grid5000 node: graphene-66.nancy.grid5000.fr

# Chart 26

Nb Executed tests: 3191

Nb Failing tests: 46

>	org.jfree.data.time.junit.MonthTests#testParseMonth
>	org.jfree.chart.junit.StackedAreaChartTests#testDrawWithNullInfo
>	org.jfree.chart.junit.StackedBarChart3DTests#testDrawWithNullInfo
>	org.jfree.chart.junit.AreaChartTests#testDrawWithNullInfo
>	org.jfree.chart.junit.BarChartTests#testDrawWithNullInfo
>	org.jfree.chart.junit.BarChart3DTests#testDrawWithNullInfo
>	org.jfree.chart.junit.GanttChartTests#testDrawWithNullInfo
>	org.jfree.chart.junit.GanttChartTests#testDrawWithNullInfo2
>	org.jfree.chart.junit.LineChartTests#testDrawWithNullInfo
>	org.jfree.chart.junit.LineChart3DTests#testDrawWithNullInfo
>	org.jfree.chart.junit.StackedAreaChartTests#testDrawWithNullInfo
>	org.jfree.chart.junit.StackedBarChartTests#testDrawWithNullInfo
>	org.jfree.chart.junit.StackedBarChart3DTests#testDrawWithNullInfo
>	org.jfree.chart.junit.WaterfallChartTests#testDrawWithNullInfo
>	org.jfree.chart.junit.AreaChartTests#testDrawWithNullInfo
>	org.jfree.chart.junit.GanttChartTests#testDrawWithNullInfo
>	org.jfree.chart.junit.GanttChartTests#testDrawWithNullInfo2
>	org.jfree.chart.plot.junit.CategoryPlotTests#test1654215
>	org.jfree.chart.plot.junit.CategoryPlotTests#testSerialization3
>	org.jfree.chart.plot.junit.CategoryPlotTests#testSerialization4
>	org.jfree.chart.junit.LineChart3DTests#testDrawWithNullInfo
>	org.jfree.chart.renderer.category.junit.LayeredBarRendererTests#testDrawWithNullInfo
>	org.jfree.chart.renderer.category.junit.BoxAndWhiskerRendererTests#testDrawWithNullInfo
>	org.jfree.chart.renderer.category.junit.GroupedStackedBarRendererTests#testDrawWithNullInfo
>	org.jfree.chart.renderer.category.junit.IntervalBarRendererTests#testDrawWithNullInfo
>	org.jfree.chart.renderer.category.junit.LayeredBarRendererTests#testDrawWithNullInfo
>	org.jfree.chart.renderer.category.junit.LevelRendererTests#testDrawWithNullInfo
>	org.jfree.chart.renderer.category.junit.MinMaxCategoryRendererTests#testDrawWithNullInfo
>	org.jfree.chart.renderer.category.junit.StatisticalBarRendererTests#testDrawWithNullInfo
>	org.jfree.chart.renderer.category.junit.StatisticalLineAndShapeRendererTests#testDrawWithNullInfo
>	org.jfree.chart.plot.junit.CategoryPlotTests#test1654215
>	org.jfree.chart.plot.junit.CategoryPlotTests#testSerialization3
>	org.jfree.chart.plot.junit.CategoryPlotTests#testSerialization4
>	org.jfree.chart.junit.StackedBarChartTests#testDrawWithNullInfo
>	org.jfree.chart.renderer.category.junit.StatisticalLineAndShapeRendererTests#testDrawWithNullInfo
>	org.jfree.chart.renderer.category.junit.GroupedStackedBarRendererTests#testDrawWithNullInfo
>	org.jfree.chart.renderer.category.junit.StatisticalBarRendererTests#testDrawWithNullInfo
>	org.jfree.chart.junit.LineChartTests#testDrawWithNullInfo
>	org.jfree.chart.junit.BarChartTests#testDrawWithNullInfo
>	org.jfree.chart.renderer.category.junit.MinMaxCategoryRendererTests#testDrawWithNullInfo
>	org.jfree.chart.renderer.category.junit.IntervalBarRendererTests#testDrawWithNullInfo
>	org.jfree.chart.renderer.category.junit.BoxAndWhiskerRendererTests#testDrawWithNullInfo
>	org.jfree.chart.junit.WaterfallChartTests#testDrawWithNullInfo
>	org.jfree.data.time.junit.MonthTests#testParseMonth
>	org.jfree.chart.renderer.category.junit.LevelRendererTests#testDrawWithNullInfo
>	org.jfree.chart.junit.BarChart3DTests#testDrawWithNullInfo

## Human Patch 

```Java
Index: org/jfree/chart/axis/Axis.java
===================================================================
--- org/jfree/chart/axis/Axis.java	(revision 103)
+++ org/jfree/chart/axis/Axis.java	(revision 102)
@@ -1188,13 +1187,11 @@
 
         }
         if (plotState != null && hotspot != null) {
-            ChartRenderingInfo owner = plotState.getOwner();
-            if (owner != null) {
-                EntityCollection entities = owner.getEntityCollection();
-                if (entities != null) {
-                    entities.add(new AxisLabelEntity(this, hotspot, 
-                            this.labelToolTip, this.labelURL));
-                }
+            EntityCollection entities = plotState.getOwner()
+                    .getEntityCollection();
+            if (entities != null) {
+                entities.add(new AxisLabelEntity(this, hotspot, 
+                        this.labelToolTip, this.labelURL));
             }
         }
         return state;

```

## NopolPC 

org.jfree.chart.axis.AxisCollection:132 (Suspicious rank: ample 185, jaccard 249, ochiai 244, naish1 17995, gp13 185, naish2 185, tarantula 761, )
```Java
-1 == org.jfree.chart.axis.AxisCollection.this.axesAtLeft.size()
```

Nb Angelic value: 1

Nb analyzed Statement: 228

Execution time: 0:23:09.326000

Grid5000 node: graphene-57.nancy.grid5000.fr

## NopolC 

org.jfree.chart.plot.CategoryPlot:2538 (Suspicious rank: ample 39, jaccard 39, ochiai 54, naish1 15332, gp13 39, naish2 39, tarantula 266, )
```Java
org.jfree.chart.plot.CategoryPlot.DEFAULT_CROSSHAIR_STROKE!=null
```

Nb Angelic value: 1

Nb analyzed Statement: 79

Execution time: 0:01:01.433000

Grid5000 node: graphene-84.nancy.grid5000.fr

## BrutpolC 

org.jfree.chart.axis.Axis:1101 (Suspicious rank: ample 199, jaccard 267, ochiai 327, naish1 15242, gp13 199, naish2 199, tarantula 912, )
```Java
this.tickLabelsVisible
```

Nb Angelic value: 3

Nb analyzed Statement: 291

Execution time: 0:43:36.171000

Grid5000 node: graphene-97.nancy.grid5000.fr

## Kali 

org.jfree.chart.plot.CategoryPlot:2547 (Suspicious rank: ample 1, jaccard 1, ochiai 1, naish1 15018, gp13 1, naish2 1, tarantula 1, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2536 (Suspicious rank: ample 40, jaccard 40, ochiai 52, naish1 15336, gp13 40, naish2 40, tarantula 267, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2537 (Suspicious rank: ample 41, jaccard 41, ochiai 53, naish1 15337, gp13 41, naish2 41, tarantula 268, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2538 (Suspicious rank: ample 39, jaccard 39, ochiai 54, naish1 15332, gp13 39, naish2 39, tarantula 266, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2538 (Suspicious rank: ample 39, jaccard 39, ochiai 54, naish1 15332, gp13 39, naish2 39, tarantula 266, )
REPLACE
```Java
if (true) {
	return ;
} 
```

org.jfree.chart.plot.CategoryPlot:2543 (Suspicious rank: ample 103, jaccard 103, ochiai 55, naish1 17403, gp13 103, naish2 103, tarantula 330, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2549 (Suspicious rank: ample 102, jaccard 102, ochiai 56, naish1 17399, gp13 102, naish2 102, tarantula 329, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2552 (Suspicious rank: ample 35, jaccard 35, ochiai 57, naish1 15199, gp13 35, naish2 35, tarantula 262, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2553 (Suspicious rank: ample 36, jaccard 36, ochiai 58, naish1 15200, gp13 36, naish2 36, tarantula 263, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2556 (Suspicious rank: ample 6, jaccard 6, ochiai 59, naish1 14556, gp13 6, naish2 6, tarantula 233, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2557 (Suspicious rank: ample 7, jaccard 7, ochiai 60, naish1 14559, gp13 7, naish2 7, tarantula 234, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2558 (Suspicious rank: ample 73, jaccard 73, ochiai 61, naish1 16068, gp13 73, naish2 73, tarantula 300, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2560 (Suspicious rank: ample 97, jaccard 97, ochiai 62, naish1 17232, gp13 97, naish2 97, tarantula 324, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2564 (Suspicious rank: ample 126, jaccard 126, ochiai 63, naish1 18425, gp13 126, naish2 126, tarantula 353, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2565 (Suspicious rank: ample 125, jaccard 125, ochiai 64, naish1 18424, gp13 125, naish2 125, tarantula 352, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.plot.CategoryPlot:2571 (Suspicious rank: ample 30, jaccard 30, ochiai 65, naish1 15031, gp13 30, naish2 30, tarantula 257, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.axis.AxisCollection:126 (Suspicious rank: ample 172, jaccard 236, ochiai 242, naish1 15939, gp13 172, naish2 172, tarantula 748, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.axis.AxisCollection:129 (Suspicious rank: ample 171, jaccard 235, ochiai 243, naish1 15938, gp13 171, naish2 171, tarantula 747, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.axis.AxisCollection:132 (Suspicious rank: ample 185, jaccard 249, ochiai 244, naish1 17995, gp13 185, naish2 185, tarantula 761, )
DELETE
```Java
remove
```

org.jfree.chart.axis.AxisCollection:132 (Suspicious rank: ample 185, jaccard 249, ochiai 244, naish1 17995, gp13 185, naish2 185, tarantula 761, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.axis.Axis:314 (Suspicious rank: ample 209, jaccard 277, ochiai 300, naish1 15655, gp13 209, naish2 209, tarantula 922, )
INSERT_BEFORE
```Java
if (true)
	return false;

```

org.jfree.chart.axis.Axis:1101 (Suspicious rank: ample 199, jaccard 267, ochiai 327, naish1 15242, gp13 199, naish2 199, tarantula 912, )
REPLACE
```Java
if (true) {
	return state;
} 
```

org.jfree.chart.axis.Axis:1113 (Suspicious rank: ample 262, jaccard 330, ochiai 335, naish1 17434, gp13 262, naish2 262, tarantula 975, )
DELETE
```Java
remove
```

org.jfree.chart.axis.Axis:1190 (Suspicious rank: ample 252, jaccard 320, ochiai 336, naish1 16802, gp13 252, naish2 252, tarantula 965, )
DELETE
```Java
remove
```

org.jfree.chart.axis.Axis:1190 (Suspicious rank: ample 252, jaccard 320, ochiai 336, naish1 16802, gp13 252, naish2 252, tarantula 965, )
REPLACE
```Java
if (false) {
	org.jfree.chart.entity.EntityCollection entities = plotState.getOwner().getEntityCollection();
	if (entities != null) {
		entities.add(new org.jfree.chart.entity.AxisLabelEntity(this , hotspot , this.labelToolTip , this.labelURL));
	} 
} 
```

org.jfree.chart.JFreeChart:1198 (Suspicious rank: ample 370, jaccard 494, ochiai 383, naish1 15946, gp13 370, naish2 370, tarantula 1434, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1199 (Suspicious rank: ample 371, jaccard 495, ochiai 384, naish1 15947, gp13 371, naish2 371, tarantula 1435, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1201 (Suspicious rank: ample 372, jaccard 496, ochiai 385, naish1 16091, gp13 372, naish2 372, tarantula 1436, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1130 (Suspicious rank: ample 496, jaccard 624, ochiai 582, naish1 15494, gp13 496, naish2 496, tarantula 1584, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1134 (Suspicious rank: ample 497, jaccard 625, ochiai 583, naish1 15495, gp13 497, naish2 497, tarantula 1585, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1140 (Suspicious rank: ample 560, jaccard 695, ochiai 584, naish1 17024, gp13 560, naish2 560, tarantula 1648, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1141 (Suspicious rank: ample 559, jaccard 694, ochiai 585, naish1 17023, gp13 559, naish2 559, tarantula 1647, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1143 (Suspicious rank: ample 558, jaccard 693, ochiai 586, naish1 17022, gp13 558, naish2 558, tarantula 1646, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1146 (Suspicious rank: ample 557, jaccard 692, ochiai 587, naish1 17021, gp13 557, naish2 557, tarantula 1645, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1147 (Suspicious rank: ample 556, jaccard 691, ochiai 588, naish1 17020, gp13 556, naish2 556, tarantula 1644, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1148 (Suspicious rank: ample 555, jaccard 690, ochiai 589, naish1 17019, gp13 555, naish2 555, tarantula 1643, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1151 (Suspicious rank: ample 482, jaccard 609, ochiai 590, naish1 14996, gp13 482, naish2 482, tarantula 1570, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1165 (Suspicious rank: ample 569, jaccard 704, ochiai 591, naish1 17196, gp13 569, naish2 569, tarantula 1657, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1180 (Suspicious rank: ample 607, jaccard 748, ochiai 592, naish1 18018, gp13 607, naish2 607, tarantula 1695, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1181 (Suspicious rank: ample 606, jaccard 747, ochiai 593, naish1 18017, gp13 606, naish2 606, tarantula 1694, )
DELETE
```Java
remove
```

org.jfree.chart.JFreeChart:1181 (Suspicious rank: ample 606, jaccard 747, ochiai 593, naish1 18017, gp13 606, naish2 606, tarantula 1694, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1182 (Suspicious rank: ample 605, jaccard 746, ochiai 594, naish1 18016, gp13 605, naish2 605, tarantula 1693, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1184 (Suspicious rank: ample 609, jaccard 750, ochiai 595, naish1 18020, gp13 609, naish2 609, tarantula 1697, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1185 (Suspicious rank: ample 608, jaccard 749, ochiai 596, naish1 18019, gp13 608, naish2 608, tarantula 1696, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1188 (Suspicious rank: ample 604, jaccard 745, ochiai 597, naish1 18015, gp13 604, naish2 604, tarantula 1692, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1196 (Suspicious rank: ample 512, jaccard 644, ochiai 598, naish1 15949, gp13 512, naish2 512, tarantula 1600, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1197 (Suspicious rank: ample 513, jaccard 645, ochiai 599, naish1 15950, gp13 513, naish2 513, tarantula 1601, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1206 (Suspicious rank: ample 518, jaccard 650, ochiai 600, naish1 16093, gp13 518, naish2 518, tarantula 1606, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1209 (Suspicious rank: ample 517, jaccard 649, ochiai 601, naish1 16090, gp13 517, naish2 517, tarantula 1605, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1210 (Suspicious rank: ample 611, jaccard 762, ochiai 602, naish1 18180, gp13 611, naish2 611, tarantula 1699, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.jfree.chart.JFreeChart:1213 (Suspicious rank: ample 610, jaccard 761, ochiai 603, naish1 18179, gp13 610, naish2 610, tarantula 1698, )
DELETE
```Java
remove
```

org.jfree.chart.JFreeChart:1213 (Suspicious rank: ample 610, jaccard 761, ochiai 603, naish1 18179, gp13 610, naish2 610, tarantula 1698, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

Grid5000 node: griffon-8.nancy.grid5000.fr

# Lang 39

Nb Executed tests: 1618

Nb Failing tests: 1

>	org.apache.commons.lang3.StringUtilsTest#testReplace_StringStringArrayStringArray

## Human Patch 

```Java
diff --git a/org/apache/commons/lang3/StringUtils.java b/org/apache/commons/lang3/StringUtils.java
index f6cabee..14563aa 100644
--- a/org/apache/commons/lang3/StringUtils.java
+++ b/org/apache/commons/lang3/StringUtils.java
@@ -3673,9 +3673,6 @@ public class StringUtils {
 
         // count the replacement text elements that are larger than their corresponding text being replaced
         for (int i = 0; i < searchList.length; i++) {
-            if (searchList[i] == null || replacementList[i] == null) {
-                continue;
-            }
             int greater = replacementList[i].length() - searchList[i].length();
             if (greater > 0) {
                 increase += 3 * greater; // assume 3 matches

```

## NopolPC 

org.apache.commons.lang3.StringUtils:3675 (Suspicious rank: ample 11, jaccard 11, ochiai 26, naish1 7828, gp13 11, naish2 11, tarantula 11, )
```Java
repeat
```

Nb Angelic value: 1

Nb analyzed Statement: 29

Execution time: 0:05:45.321000

Grid5000 node: graphene-75.nancy.grid5000.fr

## BrutpolPC 

org.apache.commons.lang3.StringUtils:3675 (Suspicious rank: ample 11, jaccard 11, ochiai 26, naish1 7828, gp13 11, naish2 11, tarantula 11, )
```Java
repeat
```

Nb Angelic value: 1

Nb analyzed Statement: 29

Execution time: 0:06:54.576000

Grid5000 node: graphene-99.nancy.grid5000.fr

# Lang 44

Nb Executed tests: 1879

Nb Failing tests: 1

>	org.apache.commons.lang.NumberUtilsTest#testLang457

## Human Patch 

```Java
diff --git a/org/apache/commons/lang/NumberUtils.java b/org/apache/commons/lang/NumberUtils.java
index c5ca8cd..18a05ef 100644
--- a/org/apache/commons/lang/NumberUtils.java
+++ b/org/apache/commons/lang/NumberUtils.java
@@ -142,9 +142,6 @@ public final class NumberUtils {
         if (val.length() == 0) {
             throw new NumberFormatException("\"\" is not a valid number.");
         }
-        if (val.length() == 1 && !Character.isDigit(val.charAt(0))) {
-            throw new NumberFormatException(val + " is not a valid number.");
-        }
         if (val.startsWith("--")) {
             // this is protection for poorness in java.lang.BigDecimal.
             // it accepts this as a legal value, but it does not appear 

```

## NopolPC 

org.apache.commons.lang.NumberUtils:193 (Suspicious rank: ample 18, jaccard 18, ochiai 18, naish1 9255, gp13 18, naish2 18, tarantula 18, )
```Java
(val.length()) != (1)
```

Nb Angelic value: 1

Nb analyzed Statement: 5

Execution time: 0:00:51.614000

Grid5000 node: griffon-38.nancy.grid5000.fr

## NopolC 

org.apache.commons.lang.NumberUtils:193 (Suspicious rank: ample 18, jaccard 18, ochiai 18, naish1 9255, gp13 18, naish2 18, tarantula 18, )
```Java
((dec == null) && (exp == null))
```

Nb Angelic value: 1

Nb analyzed Statement: 5

Execution time: 0:00:42.914000

Grid5000 node: graphene-92.nancy.grid5000.fr

# Lang 46

Nb Executed tests: 1829

Nb Failing tests: 1

>	org.apache.commons.lang.StringEscapeUtilsTest#testEscapeJavaWithSlash

## Human Patch 

```Java
diff --git a/org/apache/commons/lang/StringEscapeUtils.java b/org/apache/commons/lang/StringEscapeUtils.java
index d4f98ec..c30c663 100644
--- a/org/apache/commons/lang/StringEscapeUtils.java
+++ b/org/apache/commons/lang/StringEscapeUtils.java
@@ -83,7 +83,7 @@ public class StringEscapeUtils {
      * @return String with escaped values, <code>null</code> if null string input
      */
     public static String escapeJava(String str) {
-        return escapeJavaStyleString(str, false, false);
+        return escapeJavaStyleString(str, false);
     }
 
     /**
@@ -99,7 +99,7 @@ public class StringEscapeUtils {
      * @throws IOException if error occurs on underlying Writer
      */
     public static void escapeJava(Writer out, String str) throws IOException {
-        escapeJavaStyleString(out, str, false, false);
+        escapeJavaStyleString(out, str, false);
     }
 
     /**
@@ -124,7 +124,7 @@ public class StringEscapeUtils {
      * @return String with escaped values, <code>null</code> if null string input
      */
     public static String escapeJavaScript(String str) {
-        return escapeJavaStyleString(str, true, true);
+        return escapeJavaStyleString(str, true);
     }
 
     /**
@@ -140,7 +140,7 @@ public class StringEscapeUtils {
      * @throws IOException if error occurs on underlying Writer
      **/
     public static void escapeJavaScript(Writer out, String str) throws IOException {
-        escapeJavaStyleString(out, str, true, true);
+        escapeJavaStyleString(out, str, true);
     }
 
     /**
@@ -148,16 +148,15 @@ public class StringEscapeUtils {
      * 
      * @param str String to escape values in, may be null
      * @param escapeSingleQuotes escapes single quotes if <code>true</code>
-     * @param escapeForwardSlash TODO
      * @return the escaped string
      */
-    private static String escapeJavaStyleString(String str, boolean escapeSingleQuotes, boolean escapeForwardSlash) {
+    private static String escapeJavaStyleString(String str, boolean escapeSingleQuotes) {
         if (str == null) {
             return null;
         }
         try {
             StringWriter writer = new StringWriter(str.length() * 2);
-            escapeJavaStyleString(writer, str, escapeSingleQuotes, escapeForwardSlash);
+            escapeJavaStyleString(writer, str, escapeSingleQuotes);
             return writer.toString();
         } catch (IOException ioe) {
             // this should never ever happen while writing to a StringWriter
@@ -172,11 +171,9 @@ public class StringEscapeUtils {
      * @param out write to receieve the escaped string
      * @param str String to escape values in, may be null
      * @param escapeSingleQuote escapes single quotes if <code>true</code>
-     * @param escapeForwardSlash TODO
      * @throws IOException if an IOException occurs
      */
-    private static void escapeJavaStyleString(Writer out, String str, boolean escapeSingleQuote,
-            boolean escapeForwardSlash) throws IOException {
+    private static void escapeJavaStyleString(Writer out, String str, boolean escapeSingleQuote) throws IOException {
         if (out == null) {
             throw new IllegalArgumentException("The Writer must not be null");
         }
@@ -197,23 +194,23 @@ public class StringEscapeUtils {
                 out.write("\\u00" + hex(ch));
             } else if (ch < 32) {
                 switch (ch) {
-                    case '\b' :
+                    case '\b':
                         out.write('\\');
                         out.write('b');
                         break;
-                    case '\n' :
+                    case '\n':
                         out.write('\\');
                         out.write('n');
                         break;
-                    case '\t' :
+                    case '\t':
                         out.write('\\');
                         out.write('t');
                         break;
-                    case '\f' :
+                    case '\f':
                         out.write('\\');
                         out.write('f');
                         break;
-                    case '\r' :
+                    case '\r':
                         out.write('\\');
                         out.write('r');
                         break;
@@ -227,24 +224,22 @@ public class StringEscapeUtils {
                 }
             } else {
                 switch (ch) {
-                    case '\'' :
+                    case '\'':
                         if (escapeSingleQuote) {
-                            out.write('\\');
+                          out.write('\\');
                         }
                         out.write('\'');
                         break;
-                    case '"' :
+                    case '"':
                         out.write('\\');
                         out.write('"');
                         break;
-                    case '\\' :
+                    case '\\':
                         out.write('\\');
                         out.write('\\');
                         break;
-                    case '/' :
-                        if (escapeForwardSlash) {
-                            out.write('\\');
-                        }
+                    case '/':
+                        out.write('\\');
                         out.write('/');
                         break;
                     default :

```

## NopolPC 

org.apache.commons.lang.StringEscapeUtils:242 (Suspicious rank: ample 1, jaccard 1, ochiai 1, naish1 8911, gp13 1, naish2 1, tarantula 1, )
```Java
escapeSingleQuote
```

Nb Angelic value: 1

Nb analyzed Statement: 3

Execution time: 0:00:40.390000

Grid5000 node: graphene-74.nancy.grid5000.fr

# Lang 51

Nb Executed tests: 1725

Nb Failing tests: 1

>	org.apache.commons.lang.BooleanUtilsTest#test_toBoolean_String

## Human Patch 

```Java
diff --git a/org/apache/commons/lang/BooleanUtils.java b/org/apache/commons/lang/BooleanUtils.java
index 8b5028c..3fda4ec 100644
--- a/org/apache/commons/lang/BooleanUtils.java
+++ b/org/apache/commons/lang/BooleanUtils.java
@@ -679,7 +679,6 @@ public class BooleanUtils {
                         (str.charAt(1) == 'E' || str.charAt(1) == 'e') &&
                         (str.charAt(2) == 'S' || str.charAt(2) == 's');
                 }
-                return false;
             }
             case 4: {
                 char ch = str.charAt(0);

```

## NopolC 

org.apache.commons.lang.BooleanUtils:677 (Suspicious rank: ample 11, jaccard 11, ochiai 12, naish1 8395, gp13 11, naish2 11, tarantula 11, )
```Java
str!=null
```

Nb Angelic value: 1

Nb analyzed Statement: 8

Execution time: 0:00:39.035000

Grid5000 node: graphene-42.nancy.grid5000.fr

# Lang 53

Nb Executed tests: 1718

Nb Failing tests: 1

>	org.apache.commons.lang.time.DateUtilsTest#testRoundLang346

## Human Patch 

```Java
diff --git a/org/apache/commons/lang/time/DateUtils.java b/org/apache/commons/lang/time/DateUtils.java
index e5138b5..9ca1bc5 100644
--- a/org/apache/commons/lang/time/DateUtils.java
+++ b/org/apache/commons/lang/time/DateUtils.java
@@ -640,18 +640,18 @@ public class DateUtils {
         int millisecs = val.get(Calendar.MILLISECOND);
         if (!round || millisecs < 500) {
             time = time - millisecs;
-        }
-        if (field == Calendar.SECOND) {
-            done = true;
+            if (field == Calendar.SECOND) {
+                done = true;
+            }
         }
 
         // truncate seconds
         int seconds = val.get(Calendar.SECOND);
         if (!done && (!round || seconds < 30)) {
             time = time - (seconds * 1000L);
-        }
-        if (field == Calendar.MINUTE) {
-            done = true;
+            if (field == Calendar.MINUTE) {
+                done = true;
+            }
         }
 
         // truncate minutes

```

## NopolPC 

org.apache.commons.lang.time.DateUtils:666 (Suspicious rank: ample 14, jaccard 14, ochiai 22, naish1 8347, gp13 14, naish2 14, tarantula 14, )
```Java
(minutes <= org.apache.commons.lang.time.DateUtils.RANGE_WEEK_RELATIVE) || (!((round) && (minutes < seconds)))
```

Nb Angelic value: 1

Nb analyzed Statement: 24

Execution time: 0:00:51.537000

Grid5000 node: graphene-83.nancy.grid5000.fr

# Lang 55

Nb Executed tests: 1710

Nb Failing tests: 1

>	org.apache.commons.lang.time.StopWatchTest#testLang315

## Human Patch 

```Java
diff --git a/org/apache/commons/lang/time/StopWatch.java b/org/apache/commons/lang/time/StopWatch.java
index 0f0786a..607e9b6 100644
--- a/org/apache/commons/lang/time/StopWatch.java
+++ b/org/apache/commons/lang/time/StopWatch.java
@@ -115,9 +115,7 @@ public class StopWatch {
         if(this.runningState != STATE_RUNNING && this.runningState != STATE_SUSPENDED) {
             throw new IllegalStateException("Stopwatch is not running. ");
         }
-        if(this.runningState == STATE_RUNNING) {
-            stopTime = System.currentTimeMillis();
-        }
+        stopTime = System.currentTimeMillis();
         this.runningState = STATE_STOPPED;
     }
 

```

## NopolPC 

org.apache.commons.lang.time.StopWatch:118 (Suspicious rank: ample 8, jaccard 8, ochiai 7, naish1 8347, gp13 8, naish2 8, tarantula 8, )
```Java
-1 == org.apache.commons.lang.time.StopWatch.this.stopTime
```

Nb Angelic value: 1

Nb analyzed Statement: 9

Execution time: 0:01:22.023000

Grid5000 node: graphene-88.nancy.grid5000.fr

# Lang 58

Nb Executed tests: 1689

Nb Failing tests: 1

>	org.apache.commons.lang.math.NumberUtilsTest#testLang300

## Human Patch 

```Java
diff --git a/org/apache/commons/lang/math/NumberUtils.java b/org/apache/commons/lang/math/NumberUtils.java
index eb74e72..c0f06a4 100644
--- a/org/apache/commons/lang/math/NumberUtils.java
+++ b/org/apache/commons/lang/math/NumberUtils.java
@@ -451,7 +451,8 @@ public class NumberUtils {
                 case 'L' :
                     if (dec == null
                         && exp == null
-                        && (numeric.charAt(0) == '-' && isDigits(numeric.substring(1)) || isDigits(numeric))) {
+                        && isDigits(numeric.substring(1))
+                        && (numeric.charAt(0) == '-' || Character.isDigit(numeric.charAt(0)))) {
                         try {
                             return createLong(numeric);
                         } catch (NumberFormatException nfe) {

```

## NopolPC 

org.apache.commons.lang.math.NumberUtils:464 (Suspicious rank: ample 2, jaccard 2, ochiai 1, naish1 8378, gp13 2, naish2 2, tarantula 2, )
```Java
-1 < expPos
```

Nb Angelic value: 1

Nb analyzed Statement: 2

Execution time: 0:00:39.575000

Grid5000 node: graphene-52.nancy.grid5000.fr

## NopolC 

org.apache.commons.lang.math.NumberUtils:452 (Suspicious rank: ample 4, jaccard 4, ochiai 20, naish1 8361, gp13 4, naish2 4, tarantula 4, )
```Java
((dec == null) && (exp == null))
```

Nb Angelic value: 1

Nb analyzed Statement: 8

Execution time: 0:00:38.585000

Grid5000 node: graphene-89.nancy.grid5000.fr

# Math 2

Nb Executed tests: 5195

Nb Failing tests: 1

>	org.apache.commons.math3.distribution.HypergeometricDistributionTest#testMath1021

## Human Patch 

```Java
diff --git a/org/apache/commons/math3/distribution/HypergeometricDistribution.java b/org/apache/commons/math3/distribution/HypergeometricDistribution.java
index 81e180c..2769127 100644
--- a/org/apache/commons/math3/distribution/HypergeometricDistribution.java
+++ b/org/apache/commons/math3/distribution/HypergeometricDistribution.java
@@ -265,7 +265,7 @@ public class HypergeometricDistribution extends AbstractIntegerDistribution {
      * size {@code n}, the mean is {@code n * m / N}.
      */
     public double getNumericalMean() {
-        return getSampleSize() * (getNumberOfSuccesses() / (double) getPopulationSize());
+        return (double) (getSampleSize() * getNumberOfSuccesses()) / (double) getPopulationSize();
     }
 
     /**

```

## Genprog 

org.apache.commons.math3.distribution.AbstractIntegerDistribution:138 (Suspicious rank: ample 17, jaccard 17, ochiai 22, naish1 35438, gp13 17, naish2 17, tarantula 17, )
REPLACE
```Java
tmp = mu + (k * sigma)
```

Grid5000 node: graphene-37.nancy.grid5000.fr

## Kali 

org.apache.commons.math3.distribution.AbstractIntegerDistribution:137 (Suspicious rank: ample 22, jaccard 22, ochiai 21, naish1 35443, gp13 22, naish2 22, tarantula 22, )
DELETE
```Java
remove
```

org.apache.commons.math3.distribution.AbstractIntegerDistribution:137 (Suspicious rank: ample 22, jaccard 22, ochiai 21, naish1 35443, gp13 22, naish2 22, tarantula 22, )
REPLACE
```Java
if (false) {
	upper = ((int)(java.lang.Math.ceil(tmp))) - 1;
} 
```

org.apache.commons.math3.distribution.AbstractIntegerDistribution:138 (Suspicious rank: ample 17, jaccard 17, ochiai 22, naish1 35438, gp13 17, naish2 17, tarantula 17, )
DELETE
```Java
remove
```

org.apache.commons.math3.distribution.AbstractIntegerDistribution:129 (Suspicious rank: ample 24, jaccard 24, ochiai 26, naish1 35391, gp13 24, naish2 24, tarantula 24, )
DELETE
```Java
remove
```

org.apache.commons.math3.distribution.AbstractIntegerDistribution:129 (Suspicious rank: ample 24, jaccard 24, ochiai 26, naish1 35391, gp13 24, naish2 24, tarantula 24, )
REPLACE
```Java
if (false) {
	double k = org.apache.commons.math3.util.FastMath.sqrt(((1.0 - p) / p));
	double tmp = mu - (k * sigma);
	if (tmp > lower) {
		lower = ((int)(java.lang.Math.ceil(tmp))) - 1;
	} 
	k = 1.0 / k;
	tmp = mu + (k * sigma);
	if (tmp < upper) {
		upper = ((int)(java.lang.Math.ceil(tmp))) - 1;
	} 
} 
```

Grid5000 node: griffon-2.nancy.grid5000.fr

# Math 5

Nb Executed tests: 4949

Nb Failing tests: 1

>	org.apache.commons.math3.complex.ComplexTest#testReciprocalZero

## Human Patch 

```Java
diff --git a/org/apache/commons/math3/complex/Complex.java b/org/apache/commons/math3/complex/Complex.java
index ac8185b..22b23f2 100644
--- a/org/apache/commons/math3/complex/Complex.java
+++ b/org/apache/commons/math3/complex/Complex.java
@@ -302,7 +302,7 @@ public class Complex implements FieldElement<Complex>, Serializable  {
         }
 
         if (real == 0.0 && imaginary == 0.0) {
-            return INF;
+            return NaN;
         }
 
         if (isInfinite) {

```

## Genprog 

org.apache.commons.math3.complex.Complex:305 (Suspicious rank: ample 1, jaccard 1, ochiai 1, naish1 33968, gp13 1, naish2 1, tarantula 1, )
REPLACE
```Java
return org.apache.commons.math3.complex.Complex.INF
```

Grid5000 node: graphene-39.nancy.grid5000.fr

# Math 8

Nb Executed tests: 4850

Nb Failing tests: 1

>	org.apache.commons.math3.distribution.DiscreteRealDistributionTest#testIssue942

## Human Patch 

```Java
diff --git a/org/apache/commons/math3/distribution/DiscreteDistribution.java b/org/apache/commons/math3/distribution/DiscreteDistribution.java
index 879eb2a..8c08dbe 100644
--- a/org/apache/commons/math3/distribution/DiscreteDistribution.java
+++ b/org/apache/commons/math3/distribution/DiscreteDistribution.java
@@ -16,9 +16,9 @@
  */
 package org.apache.commons.math3.distribution;
 
+import java.lang.reflect.Array;
 import java.util.ArrayList;
 import java.util.List;
-
 import org.apache.commons.math3.exception.MathArithmeticException;
 import org.apache.commons.math3.exception.MathIllegalArgumentException;
 import org.apache.commons.math3.exception.NotPositiveException;
@@ -178,13 +178,13 @@ public class DiscreteDistribution<T> {
      * @throws NotStrictlyPositiveException if {@code sampleSize} is not
      * positive.
      */
-    public Object[] sample(int sampleSize) throws NotStrictlyPositiveException {
+    public T[] sample(int sampleSize) throws NotStrictlyPositiveException {
         if (sampleSize <= 0) {
             throw new NotStrictlyPositiveException(LocalizedFormats.NUMBER_OF_SAMPLES,
                     sampleSize);
         }
-
-        final Object[] out = new Object[sampleSize];
+        @SuppressWarnings("unchecked")
+        final T[]out = (T[]) Array.newInstance(singletons.get(0).getClass(), sampleSize);
 
         for (int i = 0; i < sampleSize; i++) {
             out[i] = sample();

```

## Genprog 

org.apache.commons.math3.distribution.DiscreteDistribution:189 (Suspicious rank: ample 3, jaccard 3, ochiai 3, naish1 33466, gp13 3, naish2 3, tarantula 3, )
DELETE
```Java
remove
```

Grid5000 node: graphene-4.nancy.grid5000.fr

## Kali 

org.apache.commons.math3.distribution.DiscreteDistribution:189 (Suspicious rank: ample 3, jaccard 3, ochiai 3, naish1 33466, gp13 3, naish2 3, tarantula 3, )
DELETE
```Java
remove
```

org.apache.commons.math3.distribution.DiscreteDistribution:190 (Suspicious rank: ample 4, jaccard 4, ochiai 4, naish1 33478, gp13 4, naish2 4, tarantula 4, )
DELETE
```Java
remove
```

Grid5000 node: graphene-64.nancy.grid5000.fr

# Math 28

Nb Executed tests: 3981

Nb Failing tests: 1

>	org.apache.commons.math3.optimization.linear.SimplexSolverTest#testMath828Cycle

## Human Patch 

```Java
diff --git a/org/apache/commons/math3/optimization/linear/SimplexSolver.java b/org/apache/commons/math3/optimization/linear/SimplexSolver.java
index dec310b..c2fa14d 100644
--- a/org/apache/commons/math3/optimization/linear/SimplexSolver.java
+++ b/org/apache/commons/math3/optimization/linear/SimplexSolver.java
@@ -116,14 +116,12 @@ public class SimplexSolver extends AbstractLinearOptimizer {
             // there's a degeneracy as indicated by a tie in the minimum ratio test
 
             // 1. check if there's an artificial variable that can be forced out of the basis
-            if (tableau.getNumArtificialVariables() > 0) {
-                for (Integer row : minRatioPositions) {
-                    for (int i = 0; i < tableau.getNumArtificialVariables(); i++) {
-                        int column = i + tableau.getArtificialVariableOffset();
-                        final double entry = tableau.getEntry(row, column);
-                        if (Precision.equals(entry, 1d, maxUlps) && row.equals(tableau.getBasicRow(column))) {
-                            return row;
-                        }
+            for (Integer row : minRatioPositions) {
+                for (int i = 0; i < tableau.getNumArtificialVariables(); i++) {
+                    int column = i + tableau.getArtificialVariableOffset();
+                    final double entry = tableau.getEntry(row, column);
+                    if (Precision.equals(entry, 1d, maxUlps) && row.equals(tableau.getBasicRow(column))) {
+                        return row;
                     }
                 }
             }
@@ -133,26 +131,20 @@ public class SimplexSolver extends AbstractLinearOptimizer {
             //
             // see http://www.stanford.edu/class/msande310/blandrule.pdf
             // see http://en.wikipedia.org/wiki/Bland%27s_rule (not equivalent to the above paper)
-            //
-            // Additional heuristic: if we did not get a solution after half of maxIterations
-            //                       revert to the simple case of just returning the top-most row
-            // This heuristic is based on empirical data gathered while investigating MATH-828.
-            if (getIterations() < getMaxIterations() / 2) {
-                Integer minRow = null;
-                int minIndex = tableau.getWidth();
-                for (Integer row : minRatioPositions) {
-                    int i = tableau.getNumObjectiveFunctions();
-                    for (; i < tableau.getWidth() - 1 && minRow != row; i++) {
-                        if (row == tableau.getBasicRow(i)) {
-                            if (i < minIndex) {
-                                minIndex = i;
-                                minRow = row;
-                            }
+            Integer minRow = null;
+            int minIndex = tableau.getWidth();
+            for (Integer row : minRatioPositions) {
+                for (int i = tableau.getNumObjectiveFunctions(); i < tableau.getWidth() - 1 && minRow != row; i++) {
+                    if (row == tableau.getBasicRow(i)) {
+                        if (i < minIndex) {
+                            minIndex = i;
+                            minRow = row;
                         }
                     }
                 }
-                return minRow;
             }
+
+            return minRow;
         }
         return minRatioPositions.get(0);
     }

```

## Genprog 

org.apache.commons.math3.optimization.linear.SimplexSolver:124 (Suspicious rank: ample 33, jaccard 33, ochiai 33, naish1 26751, gp13 33, naish2 33, tarantula 33, )
DELETE
```Java
remove
```

Grid5000 node: graphene-19.nancy.grid5000.fr

## Kali 

org.apache.commons.math3.optimization.linear.SimplexSolver:138 (Suspicious rank: ample 6, jaccard 6, ochiai 10, naish1 26541, gp13 6, naish2 6, tarantula 6, )
REPLACE
```Java
if (true) {
	if (i < minIndex) {
		minIndex = i;
		minRow = row;
	} 
} 
```

org.apache.commons.math3.optimization.linear.SimplexSolver:139 (Suspicious rank: ample 7, jaccard 7, ochiai 11, naish1 26542, gp13 7, naish2 7, tarantula 7, )
REPLACE
```Java
if (true) {
	minIndex = i;
	minRow = row;
} 
```

org.apache.commons.math3.optimization.linear.SimplexSolver:140 (Suspicious rank: ample 15, jaccard 15, ochiai 12, naish1 26645, gp13 15, naish2 15, tarantula 15, )
DELETE
```Java
remove
```

org.apache.commons.math3.optimization.linear.SimplexSolver:147 (Suspicious rank: ample 12, jaccard 12, ochiai 15, naish1 26642, gp13 12, naish2 12, tarantula 12, )
DELETE
```Java
remove
```

org.apache.commons.math3.optimization.linear.SimplexSolver:123 (Suspicious rank: ample 31, jaccard 31, ochiai 32, naish1 26749, gp13 31, naish2 31, tarantula 31, )
DELETE
```Java
remove
```

org.apache.commons.math3.optimization.linear.SimplexSolver:123 (Suspicious rank: ample 31, jaccard 31, ochiai 32, naish1 26749, gp13 31, naish2 31, tarantula 31, )
REPLACE
```Java
if (true) {
	return row;
} 
```

org.apache.commons.math3.optimization.linear.SimplexSolver:123 (Suspicious rank: ample 31, jaccard 31, ochiai 32, naish1 26749, gp13 31, naish2 31, tarantula 31, )
REPLACE
```Java
if (false) {
	return row;
} 
```

org.apache.commons.math3.optimization.linear.SimplexSolver:124 (Suspicious rank: ample 33, jaccard 33, ochiai 33, naish1 26751, gp13 33, naish2 33, tarantula 33, )
DELETE
```Java
remove
```

org.apache.commons.math3.optimization.linear.SimplexSolver:104 (Suspicious rank: ample 34, jaccard 34, ochiai 36, naish1 26523, gp13 34, naish2 34, tarantula 34, )
DELETE
```Java
remove
```

org.apache.commons.math3.optimization.linear.SimplexSolver:119 (Suspicious rank: ample 38, jaccard 38, ochiai 37, naish1 26771, gp13 38, naish2 38, tarantula 38, )
DELETE
```Java
remove
```

org.apache.commons.math3.optimization.linear.SimplexSolver:120 (Suspicious rank: ample 37, jaccard 37, ochiai 38, naish1 26748, gp13 37, naish2 37, tarantula 37, )
DELETE
```Java
remove
```

org.apache.commons.math3.optimization.linear.SimplexSolver:77 (Suspicious rank: ample 81, jaccard 81, ochiai 96, naish1 26582, gp13 81, naish2 81, tarantula 81, )
DELETE
```Java
remove
```

org.apache.commons.math3.optimization.linear.SimplexSolver:103 (Suspicious rank: ample 79, jaccard 79, ochiai 107, naish1 26572, gp13 79, naish2 79, tarantula 79, )
REPLACE
```Java
if (false) {
	minRatioPositions.add(i);
} else if (cmp < 0) {
	minRatio = ratio;
	minRatioPositions = new java.util.ArrayList<java.lang.Integer>();
	minRatioPositions.add(i);
} 
```

Grid5000 node: graphene-7.nancy.grid5000.fr

# Math 32

Nb Executed tests: 3593

Nb Failing tests: 1

>	org.apache.commons.math3.geometry.euclidean.threed.PolyhedronsSetTest#testIssue780

## Human Patch 

```Java
diff --git a/org/apache/commons/math3/geometry/euclidean/twod/PolygonsSet.java b/org/apache/commons/math3/geometry/euclidean/twod/PolygonsSet.java
index add24ac..6ba72be 100644
--- a/org/apache/commons/math3/geometry/euclidean/twod/PolygonsSet.java
+++ b/org/apache/commons/math3/geometry/euclidean/twod/PolygonsSet.java
@@ -132,9 +132,7 @@ public class PolygonsSet extends AbstractRegion<Euclidean2D, Euclidean1D> {
         final Vector2D[][] v = getVertices();
 
         if (v.length == 0) {
-            final BSPTree<Euclidean2D> tree = getTree(false);
-            if (tree.getCut() == null && (Boolean) tree.getAttribute()) {
-                // the instance covers the whole space
+            if ((Boolean) getTree(false).getAttribute()) {
                 setSize(Double.POSITIVE_INFINITY);
                 setBarycenter(Vector2D.NaN);
             } else {

```

## NopolPC 

org.apache.commons.math3.geometry.partitioning.AbstractRegion:214 (Suspicious rank: ample 201, jaccard 201, ochiai 221, naish1 24818, gp13 201, naish2 201, tarantula 201, )
```Java
((!(boundary.size() - plusList.size() < minusList.size())) && (1 <= plusList.size())) || (minusList.size() == boundary.size() + -1)
```

Nb Angelic value: 1

Nb analyzed Statement: 175

Execution time: 0:13:50.124000

Grid5000 node: graphene-88.nancy.grid5000.fr

## BrutpolC 

org.apache.commons.math3.geometry.euclidean.twod.PolygonsSet:135 (Suspicious rank: ample 3, jaccard 3, ochiai 1, naish1 24965, gp13 3, naish2 3, tarantula 3, )
```Java
this.isEmpty()
```

Nb Angelic value: 1

Nb analyzed Statement: 4

Execution time: 0:13:55.694000

Grid5000 node: graphene-92.nancy.grid5000.fr

## Kali 

org.apache.commons.math3.geometry.euclidean.twod.PolygonsSet:135 (Suspicious rank: ample 3, jaccard 3, ochiai 1, naish1 24965, gp13 3, naish2 3, tarantula 3, )
REPLACE
```Java
if (false) {
	setSize(java.lang.Double.POSITIVE_INFINITY);
	setBarycenter(org.apache.commons.math3.geometry.euclidean.twod.Vector2D.NaN);
} else {
	setSize(0);
	setBarycenter(new org.apache.commons.math3.geometry.euclidean.twod.Vector2D(0 , 0));
}
```

Grid5000 node: graphene-18.nancy.grid5000.fr

# Math 33

Nb Executed tests: 3575

Nb Failing tests: 1

>	org.apache.commons.math3.optimization.linear.SimplexSolverTest#testMath781

## Human Patch 

```Java
diff --git a/org/apache/commons/math3/optimization/linear/SimplexTableau.java b/org/apache/commons/math3/optimization/linear/SimplexTableau.java
index 327b2ae..9a6993a 100644
--- a/org/apache/commons/math3/optimization/linear/SimplexTableau.java
+++ b/org/apache/commons/math3/optimization/linear/SimplexTableau.java
@@ -335,7 +335,7 @@ class SimplexTableau implements Serializable {
         // positive cost non-artificial variables
         for (int i = getNumObjectiveFunctions(); i < getArtificialVariableOffset(); i++) {
             final double entry = tableau.getEntry(0, i);
-            if (Precision.compareTo(entry, 0d, epsilon) > 0) {
+            if (Precision.compareTo(entry, 0d, maxUlps) > 0) {
                 columnsToDrop.add(i);
             }
         }

```

## NopolPC 

org.apache.commons.math3.optimization.linear.SimplexTableau:339 (Suspicious rank: ample 6, jaccard 6, ochiai 6, naish1 24710, gp13 6, naish2 6, tarantula 6, )
```Java
(org.apache.commons.math3.optimization.linear.SimplexTableau.NEGATIVE_VAR_COLUMN_LABEL.length()) != (org.apache.commons.math3.optimization.linear.SimplexTableau.this.numArtificialVariables)
```

Nb Angelic value: 1

Nb analyzed Statement: 4

Execution time: 0:12:40.632000

Grid5000 node: graphene-89.nancy.grid5000.fr

## NopolC 

org.apache.commons.math3.optimization.linear.SimplexTableau:338 (Suspicious rank: ample 28, jaccard 28, ochiai 22, naish1 24709, gp13 28, naish2 28, tarantula 28, )
```Java
((org.apache.commons.math3.optimization.linear.SimplexTableau.NEGATIVE_VAR_COLUMN_LABEL.length()) != (org.apache.commons.math3.optimization.linear.SimplexTableau.this.numArtificialVariables)) && ((0.0 < entry) || (org.apache.commons.math3.optimization.linear.SimplexTableau.this.constraints.isEmpty()))
```

Nb Angelic value: 1

Nb analyzed Statement: 31

Execution time: 0:12:39.577000

Grid5000 node: graphene-5.nancy.grid5000.fr

## BrutpolPC 

org.apache.commons.math3.optimization.linear.SimplexTableau:339 (Suspicious rank: ample 6, jaccard 6, ochiai 6, naish1 24710, gp13 6, naish2 6, tarantula 6, )
```Java
this.numArtificialVariables != this.getNumObjectiveFunctions()
```

Nb Angelic value: 1

Nb analyzed Statement: 4

Execution time: 0:13:26.080000

Grid5000 node: graphene-39.nancy.grid5000.fr

# Math 40

Nb Executed tests: 3199

Nb Failing tests: 1

>	org.apache.commons.math.analysis.solvers.BracketingNthOrderBrentSolverTest#testIssue716

## Human Patch 

```Java
diff --git a/org/apache/commons/math/analysis/solvers/BracketingNthOrderBrentSolver.java b/org/apache/commons/math/analysis/solvers/BracketingNthOrderBrentSolver.java
index 59dc461..93dd3bb 100644
--- a/org/apache/commons/math/analysis/solvers/BracketingNthOrderBrentSolver.java
+++ b/org/apache/commons/math/analysis/solvers/BracketingNthOrderBrentSolver.java
@@ -232,16 +232,10 @@ public class BracketingNthOrderBrentSolver
             double targetY;
             if (agingA >= MAXIMAL_AGING) {
                 // we keep updating the high bracket, try to compensate this
-                final int p = agingA - MAXIMAL_AGING;
-                final double weightA = (1 << p) - 1;
-                final double weightB = p + 1;
-                targetY = (weightA * yA - weightB * REDUCTION_FACTOR * yB) / (weightA + weightB);
+                targetY = -REDUCTION_FACTOR * yB;
             } else if (agingB >= MAXIMAL_AGING) {
                 // we keep updating the low bracket, try to compensate this
-                final int p = agingB - MAXIMAL_AGING;
-                final double weightA = p + 1;
-                final double weightB = (1 << p) - 1;
-                targetY = (weightB * yB - weightA * REDUCTION_FACTOR * yA) / (weightA + weightB);
+                targetY = -REDUCTION_FACTOR * yA;
             } else {
                 // bracketing is balanced, try to find the root itself
                 targetY = 0;

```

## NopolC 

org.apache.commons.math.analysis.solvers.BracketingNthOrderBrentSolver:260 (Suspicious rank: ample 31, jaccard 31, ochiai 31, naish1 24155, gp13 31, naish2 31, tarantula 31, )
```Java
((signChangeIndex - start) >= (end - signChangeIndex)) || (xA <= yA)
```

Nb Angelic value: 1

Nb analyzed Statement: 46

Execution time: 0:08:21.370000

Grid5000 node: graphene-74.nancy.grid5000.fr

## Genprog 

org.apache.commons.math.analysis.solvers.BracketingNthOrderBrentSolver:235 (Suspicious rank: ample 25, jaccard 25, ochiai 25, naish1 24170, gp13 25, naish2 25, tarantula 25, )
INSERT_BEFORE
```Java
signChangeIndex++
```

Grid5000 node: graphene-27.nancy.grid5000.fr

## Kali 

org.apache.commons.math.analysis.solvers.BracketingNthOrderBrentSolver:260 (Suspicious rank: ample 31, jaccard 31, ochiai 31, naish1 24155, gp13 31, naish2 31, tarantula 31, )
REPLACE
```Java
if (true) {
	++start;
} else {
	--end;
}
```

Grid5000 node: graphene-20.nancy.grid5000.fr

# Math 41

Nb Executed tests: 3194

Nb Failing tests: 1

>	org.apache.commons.math.stat.descriptive.moment.VarianceTest#testEvaluateArraySegmentWeighted

## Human Patch 

```Java
diff --git a/org/apache/commons/math/stat/descriptive/moment/Variance.java b/org/apache/commons/math/stat/descriptive/moment/Variance.java
index 1de139f..e5518e3 100644
--- a/org/apache/commons/math/stat/descriptive/moment/Variance.java
+++ b/org/apache/commons/math/stat/descriptive/moment/Variance.java
@@ -517,7 +517,7 @@ public class Variance extends AbstractStorelessUnivariateStatistic implements Se
                 }
 
                 double sumWts = 0;
-                for (int i = begin; i < begin + length; i++) {
+                for (int i = 0; i < weights.length; i++) {
                     sumWts += weights[i];
                 }
 

```

## BrutpolPC 

org.apache.commons.math.stat.descriptive.moment.Variance:524 (Suspicious rank: ample 19, jaccard 19, ochiai 31, naish1 24206, gp13 19, naish2 19, tarantula 19, )
```Java
mean <= length
```

Nb Angelic value: 2

Nb analyzed Statement: 4

Execution time: 0:12:03.127000

Grid5000 node: graphene-34.nancy.grid5000.fr

## BrutpolC 

org.apache.commons.math.stat.descriptive.moment.Variance:509 (Suspicious rank: ample 11, jaccard 11, ochiai 20, naish1 24185, gp13 11, naish2 11, tarantula 11, )
```Java
mean <= length
```

Nb Angelic value: 1

Nb analyzed Statement: 15

Execution time: 0:09:17.290000

Grid5000 node: griffon-22.nancy.grid5000.fr

# Math 42

Nb Executed tests: 3173

Nb Failing tests: 1

>	org.apache.commons.math.optimization.linear.SimplexSolverTest#testMath713NegativeVariable

## Human Patch 

```Java
diff --git a/org/apache/commons/math/optimization/linear/SimplexTableau.java b/org/apache/commons/math/optimization/linear/SimplexTableau.java
index d96c916..fd89432 100644
--- a/org/apache/commons/math/optimization/linear/SimplexTableau.java
+++ b/org/apache/commons/math/optimization/linear/SimplexTableau.java
@@ -407,12 +407,7 @@ class SimplexTableau implements Serializable {
             continue;
           }
           Integer basicRow = getBasicRow(colIndex);
-          if (basicRow != null && basicRow == 0) {
-              // if the basic row is found to be the objective function row
-              // set the coefficient to 0 -> this case handles unconstrained 
-              // variables that are still part of the objective function
-              coefficients[i] = 0;
-          } else if (basicRows.contains(basicRow)) {
+          if (basicRows.contains(basicRow)) {
               // if multiple variables can take a given value
               // then we choose the first and set the rest equal to 0
               coefficients[i] = 0 - (restrictToNonNegative ? 0 : mostNegative);

```

## NopolPC 

org.apache.commons.math.optimization.linear.SimplexTableau:416 (Suspicious rank: ample 29, jaccard 29, ochiai 36, naish1 24101, gp13 29, naish2 29, tarantula 29, )
```Java
(org.apache.commons.math.optimization.linear.SimplexTableau.this.numSlackVariables) != (org.apache.commons.math.optimization.linear.SimplexTableau.this.numArtificialVariables)
```

Nb Angelic value: 9

Nb analyzed Statement: 28

Execution time: 0:37:04.382000

Grid5000 node: graphene-5.nancy.grid5000.fr

## BrutpolPC 

org.apache.commons.math.optimization.linear.SimplexTableau:347 (Suspicious rank: ample 2, jaccard 2, ochiai 1, naish1 24208, gp13 2, naish2 2, tarantula 2, )
```Java
0 != this.numSlackVariables
```

Nb Angelic value: 1

Nb analyzed Statement: 2

Execution time: 0:09:38.733000

Grid5000 node: graphene-92.nancy.grid5000.fr

## BrutpolC 

org.apache.commons.math.optimization.linear.SimplexTableau:338 (Suspicious rank: ample 6, jaccard 6, ochiai 7, naish1 23982, gp13 6, naish2 6, tarantula 6, )
```Java
(0 < entry) || (this.getHeight() == this.tableau.getFrobeniusNorm())
```

Nb Angelic value: 3

Nb analyzed Statement: 17

Execution time: 0:21:09.656000

Grid5000 node: graphene-34.nancy.grid5000.fr

# Math 44

Nb Executed tests: 3119

Nb Failing tests: 1

>	org.apache.commons.math.ode.events.EventStateTest#testIssue695

## Human Patch 

```Java
diff --git a/org/apache/commons/math/ode/AbstractIntegrator.java b/org/apache/commons/math/ode/AbstractIntegrator.java
index 8f315e3..2d878b1 100644
--- a/org/apache/commons/math/ode/AbstractIntegrator.java
+++ b/org/apache/commons/math/ode/AbstractIntegrator.java
@@ -40,6 +40,7 @@ import org.apache.commons.math.ode.sampling.AbstractStepInterpolator;
 import org.apache.commons.math.ode.sampling.StepHandler;
 import org.apache.commons.math.util.FastMath;
 import org.apache.commons.math.util.Incrementor;
+import org.apache.commons.math.util.MathUtils;
 import org.apache.commons.math.util.Precision;
 
 /**
@@ -277,6 +278,7 @@ public abstract class AbstractIntegrator implements FirstOrderIntegrator {
 
             double previousT = interpolator.getGlobalPreviousTime();
             final double currentT = interpolator.getGlobalCurrentTime();
+            resetOccurred = false;
 
             // initialize the events states if needed
             if (! statesInitialized) {
@@ -330,9 +332,6 @@ public abstract class AbstractIntegrator implements FirstOrderIntegrator {
                 if (isLastStep) {
                     // the event asked to stop integration
                     System.arraycopy(eventY, 0, y, 0, y.length);
-                    for (final EventState remaining : occuringEvents) {
-                        remaining.stepAccepted(eventT, eventY);
-                    }
                     return eventT;
                 }
 
@@ -342,9 +341,6 @@ public abstract class AbstractIntegrator implements FirstOrderIntegrator {
                     System.arraycopy(eventY, 0, y, 0, y.length);
                     computeDerivatives(eventT, y, yDot);
                     resetOccurred = true;
-                    for (final EventState remaining : occuringEvents) {
-                        remaining.stepAccepted(eventT, eventY);
-                    }
                     return eventT;
                 }
 

```

## Genprog 

org.apache.commons.math.ode.AbstractIntegrator:314 (Suspicious rank: ample 21, jaccard 21, ochiai 24, naish1 23469, gp13 21, naish2 21, tarantula 21, )
INSERT_BEFORE
```Java
statesInitialized = false
```

Grid5000 node: graphene-24.nancy.grid5000.fr

## Kali 

org.apache.commons.math.analysis.solvers.BracketingNthOrderBrentSolver:385 (Suspicious rank: ample 79, jaccard 79, ochiai 98, naish1 23556, gp13 79, naish2 79, tarantula 79, )
INSERT_BEFORE
```Java
if (true)
	return 0d;

```

org.apache.commons.math.analysis.solvers.BracketingNthOrderBrentSolver:386 (Suspicious rank: ample 80, jaccard 80, ochiai 99, naish1 23557, gp13 80, naish2 80, tarantula 80, )
INSERT_BEFORE
```Java
if (true)
	return 0d;

```

org.apache.commons.math.ode.AbstractIntegrator:284 (Suspicious rank: ample 366, jaccard 366, ochiai 352, naish1 23859, gp13 366, naish2 366, tarantula 366, )
REPLACE
```Java
if (true) {
	for (org.apache.commons.math.ode.events.EventState state : eventsStates) {
		state.reinitializeBegin(interpolator);
	}
	statesInitialized = true;
} 
```

org.apache.commons.math.ode.AbstractIntegrator:288 (Suspicious rank: ample 362, jaccard 362, ochiai 354, naish1 23853, gp13 362, naish2 362, tarantula 362, )
DELETE
```Java
remove
```

Grid5000 node: griffon-15.nancy.grid5000.fr

# Math 46

Nb Executed tests: 2997

Nb Failing tests: 2

>	org.apache.commons.math.complex.ComplexTest#testAtanI
>	org.apache.commons.math.complex.ComplexTest#testDivideZero

## Human Patch 

```Java
diff --git a/org/apache/commons/math/complex/Complex.java b/org/apache/commons/math/complex/Complex.java
index dd0b00a..137765c 100644
--- a/org/apache/commons/math/complex/Complex.java
+++ b/org/apache/commons/math/complex/Complex.java
@@ -256,8 +256,7 @@ public class Complex implements FieldElement<Complex>, Serializable  {
         }
 
         if (divisor.isZero) {
-            // return isZero ? NaN : INF; // See MATH-657
-            return NaN;
+            return isZero ? NaN : INF;
         }
 
         if (divisor.isInfinite() && !isInfinite()) {
@@ -293,8 +292,7 @@ public class Complex implements FieldElement<Complex>, Serializable  {
             return NaN;
         }
         if (divisor == 0d) {
-            // return isZero ? NaN : INF; // See MATH-657
-            return NaN;
+            return isZero ? NaN : INF;
         }
         if (Double.isInfinite(divisor)) {
             return !isInfinite() ? ZERO : NaN;

```

## BrutpolPC 

org.apache.commons.math.complex.Complex:259 (Suspicious rank: ample 1, jaccard 1, ochiai 1, naish1 23203, gp13 1, naish2 1, tarantula 2, )
```Java
0 == this.multiply(this).getReal()
```

Nb Angelic value: 1

Nb analyzed Statement: 2

Execution time: 0:06:59.821000

Grid5000 node: griffon-35.nancy.grid5000.fr

# Math 49

Nb Executed tests: 2954

Nb Failing tests: 1

>	org.apache.commons.math.linear.SparseRealVectorTest#testConcurrentModification

## Human Patch 

```Java
diff --git a/org/apache/commons/math/linear/OpenMapRealVector.java b/org/apache/commons/math/linear/OpenMapRealVector.java
index 13ebfd2..5db4884 100644
--- a/org/apache/commons/math/linear/OpenMapRealVector.java
+++ b/org/apache/commons/math/linear/OpenMapRealVector.java
@@ -342,7 +342,7 @@ public class OpenMapRealVector extends AbstractRealVector
     public OpenMapRealVector ebeDivide(RealVector v) {
         checkVectorDimensions(v.getDimension());
         OpenMapRealVector res = new OpenMapRealVector(this);
-        Iterator iter = entries.iterator();
+        Iterator iter = res.entries.iterator();
         while (iter.hasNext()) {
             iter.advance();
             res.setEntry(iter.key(), iter.value() / v.getEntry(iter.key()));
@@ -355,7 +355,7 @@ public class OpenMapRealVector extends AbstractRealVector
     public OpenMapRealVector ebeDivide(double[] v) {
         checkVectorDimensions(v.length);
         OpenMapRealVector res = new OpenMapRealVector(this);
-        Iterator iter = entries.iterator();
+        Iterator iter = res.entries.iterator();
         while (iter.hasNext()) {
             iter.advance();
             res.setEntry(iter.key(), iter.value() / v[iter.key()]);
@@ -367,7 +367,7 @@ public class OpenMapRealVector extends AbstractRealVector
     public OpenMapRealVector ebeMultiply(RealVector v) {
         checkVectorDimensions(v.getDimension());
         OpenMapRealVector res = new OpenMapRealVector(this);
-        Iterator iter = entries.iterator();
+        Iterator iter = res.entries.iterator();
         while (iter.hasNext()) {
             iter.advance();
             res.setEntry(iter.key(), iter.value() * v.getEntry(iter.key()));
@@ -380,7 +380,7 @@ public class OpenMapRealVector extends AbstractRealVector
     public OpenMapRealVector ebeMultiply(double[] v) {
         checkVectorDimensions(v.length);
         OpenMapRealVector res = new OpenMapRealVector(this);
-        Iterator iter = entries.iterator();
+        Iterator iter = res.entries.iterator();
         while (iter.hasNext()) {
             iter.advance();
             res.setEntry(iter.key(), iter.value() * v[iter.key()]);

```

## NopolPC 

org.apache.commons.math.linear.OpenMapRealVector:667 (Suspicious rank: ample 14, jaccard 14, ochiai 14, naish1 23318, gp13 14, naish2 14, tarantula 14, )
```Java
org.apache.commons.math.linear.OpenMapRealVector.this.epsilon == org.apache.commons.math.linear.OpenMapRealVector.DEFAULT_ZERO_TOLERANCE
```

Nb Angelic value: 1

Nb analyzed Statement: 14

Execution time: 0:05:05.272000

Grid5000 node: graphene-49.nancy.grid5000.fr

## NopolC 

org.apache.commons.math.linear.OpenMapRealVector:666 (Suspicious rank: ample 13, jaccard 13, ochiai 13, naish1 23317, gp13 13, naish2 13, tarantula 13, )
```Java
org.apache.commons.math.linear.OpenMapRealVector.DEFAULT_ZERO_TOLERANCE == org.apache.commons.math.linear.OpenMapRealVector.this.epsilon
```

Nb Angelic value: 1

Nb analyzed Statement: 15

Execution time: 0:04:56.944000

Grid5000 node: graphene-80.nancy.grid5000.fr

## BrutpolPC 

org.apache.commons.math.util.OpenIntToDoubleHashMap:213 (Suspicious rank: ample 32, jaccard 32, ochiai 33, naish1 23309, gp13 32, naish2 32, tarantula 32, )
```Java
this.size != this.probe(1, key)
```

Nb Angelic value: 5

Nb analyzed Statement: 28

Execution time: 0:26:36.481000

Grid5000 node: griffon-12.nancy.grid5000.fr

## Genprog 

org.apache.commons.math.linear.OpenMapRealVector:667 (Suspicious rank: ample 14, jaccard 14, ochiai 14, naish1 23318, gp13 14, naish2 14, tarantula 14, )
REPLACE
```Java
entries.put(index, value)
```

Grid5000 node: graphene-61.nancy.grid5000.fr

## Kali 

org.apache.commons.math.linear.OpenMapRealVector:664 (Suspicious rank: ample 21, jaccard 21, ochiai 20, naish1 23315, gp13 21, naish2 21, tarantula 21, )
REPLACE
```Java
if (true) {
	entries.put(index, value);
} else if (entries.containsKey(index)) {
	entries.remove(index);
} 
```

org.apache.commons.math.util.OpenIntToDoubleHashMap:399 (Suspicious rank: ample 38, jaccard 38, ochiai 44, naish1 23268, gp13 38, naish2 38, tarantula 38, )
DELETE
```Java
remove
```

org.apache.commons.math.util.OpenIntToDoubleHashMap:399 (Suspicious rank: ample 38, jaccard 38, ochiai 44, naish1 23268, gp13 38, naish2 38, tarantula 38, )
INSERT_BEFORE
```Java
if (true)
	return 0d;

```

Grid5000 node: graphene-62.nancy.grid5000.fr

# Math 50

Nb Executed tests: 2952

Nb Failing tests: 1

>	org.apache.commons.math.analysis.solvers.RegulaFalsiSolverTest#testIssue631

## Human Patch 

```Java
diff --git a/org/apache/commons/math/analysis/solvers/BaseSecantSolver.java b/org/apache/commons/math/analysis/solvers/BaseSecantSolver.java
index c781a90..b3a23a1 100644
--- a/org/apache/commons/math/analysis/solvers/BaseSecantSolver.java
+++ b/org/apache/commons/math/analysis/solvers/BaseSecantSolver.java
@@ -183,7 +183,14 @@ public abstract class BaseSecantSolver
                     f0 *= f1 / (f1 + fx);
                     break;
                 case REGULA_FALSI:
-                    // Nothing.
+                    if (x == x1) {
+                        final double delta = FastMath.max(rtol * FastMath.abs(x1),
+                                                          atol);
+                        // Update formula cannot make any progress: Update the
+                        // search interval.
+                        x0 = 0.5 * (x0 + x1 - delta);
+                        f0 = computeObjectiveValue(x0);
+                    }
                     break;
                 default:
                     // Should never happen.

```

## NopolPC 

org.apache.commons.math.analysis.solvers.BaseSecantSolver:186 (Suspicious rank: ample 6, jaccard 6, ochiai 6, naish1 23279, gp13 6, naish2 6, tarantula 6, )
```Java
!((x == 1) || ((1 < x) && (inverted)))
```

Nb Angelic value: 1

Nb analyzed Statement: 6

Execution time: 0:13:35.404000

Grid5000 node: graphene-80.nancy.grid5000.fr

## NopolC 

org.apache.commons.math.analysis.solvers.BaseSecantSolver:186 (Suspicious rank: ample 6, jaccard 6, ochiai 6, naish1 23279, gp13 6, naish2 6, tarantula 6, )
```Java
f0 < -1
```

Nb Angelic value: 1

Nb analyzed Statement: 6

Execution time: 0:08:04.495000

Grid5000 node: graphene-59.nancy.grid5000.fr

## BrutpolPC 

org.apache.commons.math.analysis.solvers.BaseSecantSolver:191 (Suspicious rank: ample 4, jaccard 4, ochiai 2, naish1 23311, gp13 4, naish2 4, tarantula 4, )
```Java
this.isBracketing(x0, f0)
```

Nb Angelic value: 1

Nb analyzed Statement: 3

Execution time: 0:06:11.155000

Grid5000 node: graphene-93.nancy.grid5000.fr

## Genprog 

org.apache.commons.math.analysis.solvers.BaseSecantSolver:191 (Suspicious rank: ample 4, jaccard 4, ochiai 2, naish1 23311, gp13 4, naish2 4, tarantula 4, )
DELETE
```Java
remove
```

Grid5000 node: graphene-78.nancy.grid5000.fr

## Kali 

org.apache.commons.math.analysis.solvers.BaseSecantSolver:191 (Suspicious rank: ample 4, jaccard 4, ochiai 2, naish1 23311, gp13 4, naish2 4, tarantula 4, )
DELETE
```Java
remove
```

Grid5000 node: griffon-10.nancy.grid5000.fr

# Math 53

Nb Executed tests: 2525

Nb Failing tests: 1

>	org.apache.commons.math.complex.ComplexTest#testAddNaN

## Human Patch 

```Java
diff --git a/org/apache/commons/math/complex/Complex.java b/org/apache/commons/math/complex/Complex.java
index ab58c78..e0a8e97 100644
--- a/org/apache/commons/math/complex/Complex.java
+++ b/org/apache/commons/math/complex/Complex.java
@@ -150,9 +150,6 @@ public class Complex implements FieldElement<Complex>, Serializable  {
     public Complex add(Complex rhs)
         throws NullArgumentException {
         MathUtils.checkNotNull(rhs);
-        if (isNaN || rhs.isNaN) {
-            return NaN;
-        }
         return createComplex(real + rhs.getReal(),
             imaginary + rhs.getImaginary());
     }

```

## Genprog 

org.apache.commons.math.complex.Complex:153 (Suspicious rank: ample 1, jaccard 1, ochiai 2, naish1 21135, gp13 1, naish2 1, tarantula 1, )
INSERT_BEFORE
```Java
if ((isNaN) || (rhs.isNaN)) {
	return org.apache.commons.math.complex.Complex.NaN;
} 
```

Grid5000 node: graphene-77.nancy.grid5000.fr

# Math 56

Nb Executed tests: 2400

Nb Failing tests: 1

>	org.apache.commons.math.util.MultidimensionalCounterTest#testIterationConsistency

## Human Patch 

```Java
diff --git a/org/apache/commons/math/util/MultidimensionalCounter.java b/org/apache/commons/math/util/MultidimensionalCounter.java
index fb0614e..56c9ffe 100644
--- a/org/apache/commons/math/util/MultidimensionalCounter.java
+++ b/org/apache/commons/math/util/MultidimensionalCounter.java
@@ -234,7 +234,13 @@ public class MultidimensionalCounter implements Iterable<Integer> {
             indices[i] = idx;
         }
 
-        indices[last] = index - count;
+        int idx = 1;
+        while (count < index) {
+            count += idx;
+            ++idx;
+        }
+        --idx;
+        indices[last] = idx;
 
         return indices;
     }

```

## Genprog 

org.apache.commons.math.util.MultidimensionalCounter:239 (Suspicious rank: ample 15, jaccard 15, ochiai 22, naish1 19577, gp13 15, naish2 15, tarantula 15, )
INSERT_BEFORE
```Java
while (count < index) {
	count += idx;
	++idx;
}
```

Grid5000 node: graphene-26.nancy.grid5000.fr

# Math 57

Nb Executed tests: 2383

Nb Failing tests: 1

>	org.apache.commons.math.stat.clustering.KMeansPlusPlusClustererTest#testSmallDistances

## Human Patch 

```Java
diff --git a/org/apache/commons/math/stat/clustering/KMeansPlusPlusClusterer.java b/org/apache/commons/math/stat/clustering/KMeansPlusPlusClusterer.java
index e09bbc3..b73ac9d 100644
--- a/org/apache/commons/math/stat/clustering/KMeansPlusPlusClusterer.java
+++ b/org/apache/commons/math/stat/clustering/KMeansPlusPlusClusterer.java
@@ -172,7 +172,7 @@ public class KMeansPlusPlusClusterer<T extends Clusterable<T>> {
         while (resultSet.size() < k) {
             // For each data point x, compute D(x), the distance between x and
             // the nearest center that has already been chosen.
-            double sum = 0;
+            int sum = 0;
             for (int i = 0; i < pointSet.size(); i++) {
                 final T p = pointSet.get(i);
                 final Cluster<T> nearest = getNearestCluster(resultSet, p);

```

## NopolPC 

org.apache.commons.math.stat.clustering.EuclideanIntegerPoint:86 (Suspicious rank: ample 18, jaccard 18, ochiai 44, naish1 19414, gp13 18, naish2 18, tarantula 18, )
```Java
(1) != (org.apache.commons.math.stat.clustering.EuclideanIntegerPoint.this.point.length)
```

Nb Angelic value: 1

Nb analyzed Statement: 16

Execution time: 0:14:49.461000

Grid5000 node: griffon-38.nancy.grid5000.fr

## NopolC 

org.apache.commons.math.stat.clustering.EuclideanIntegerPoint:85 (Suspicious rank: ample 47, jaccard 47, ochiai 50, naish1 19428, gp13 47, naish2 47, tarantula 47, )
```Java
(((point[i]) != (otherPoint[i])) || (1 <= 0)) && ((otherPoint.length) != (1))
```

Nb Angelic value: 1

Nb analyzed Statement: 45

Execution time: 0:09:01.587000

Grid5000 node: graphene-90.nancy.grid5000.fr

# Math 58

Nb Executed tests: 2354

Nb Failing tests: 1

>	org.apache.commons.math.optimization.fitting.GaussianFitterTest#testMath519

## Human Patch 

```Java
diff --git a/org/apache/commons/math/optimization/fitting/GaussianFitter.java b/org/apache/commons/math/optimization/fitting/GaussianFitter.java
index e1b54f4..8c107de 100644
--- a/org/apache/commons/math/optimization/fitting/GaussianFitter.java
+++ b/org/apache/commons/math/optimization/fitting/GaussianFitter.java
@@ -117,8 +117,8 @@ public class GaussianFitter extends CurveFitter {
      * observed points (in the same order as above).
      */
     public double[] fit() {
-        final double[] guess = (new ParameterGuesser(getObservations())).guess();
-        return fit(guess);
+        return fit(new Gaussian.Parametric(),
+                   (new ParameterGuesser(getObservations())).guess());
     }
 
     /**

```

## NopolPC 

org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizer:620 (Suspicious rank: ample 85, jaccard 85, ochiai 93, naish1 19199, gp13 85, naish2 85, tarantula 85, )
```Java
org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizer.this.orthoTolerance < gNorm
```

Nb Angelic value: 1

Nb analyzed Statement: 78

Execution time: 0:05:23.148000

Grid5000 node: graphene-72.nancy.grid5000.fr

## NopolC 

org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizer:613 (Suspicious rank: ample 77, jaccard 77, ochiai 92, naish1 18944, gp13 77, naish2 77, tarantula 77, )
```Java
(fp > 0) || ((!(org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizer.this.orthoTolerance < gNorm)) && (org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizer.this.permutation!=null))
```

Nb Angelic value: 1

Nb analyzed Statement: 79

Execution time: 0:08:12.653000

Grid5000 node: graphene-91.nancy.grid5000.fr

## BrutpolPC 

org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizer:620 (Suspicious rank: ample 85, jaccard 85, ochiai 93, naish1 19199, gp13 85, naish2 85, tarantula 85, )
```Java
this.costRelativeTolerance != this.orthoTolerance
```

Nb Angelic value: 1

Nb analyzed Statement: 78

Execution time: 0:06:39.119000

Grid5000 node: graphite-3.nancy.grid5000.fr

# Math 69

Nb Executed tests: 2186

Nb Failing tests: 2

>	org.apache.commons.math.stat.correlation.PearsonsCorrelationTest#testPValueNearZero
>	org.apache.commons.math.stat.correlation.SpearmansRankCorrelationTest#testPValueNearZero

## Human Patch 

```Java
diff --git a/org/apache/commons/math/stat/correlation/PearsonsCorrelation.java b/org/apache/commons/math/stat/correlation/PearsonsCorrelation.java
index dc83314..83b4c41 100644
--- a/org/apache/commons/math/stat/correlation/PearsonsCorrelation.java
+++ b/org/apache/commons/math/stat/correlation/PearsonsCorrelation.java
@@ -168,7 +168,7 @@ public class PearsonsCorrelation {
                 } else {
                     double r = correlationMatrix.getEntry(i, j);
                     double t = Math.abs(r * Math.sqrt((nObs - 2)/(1 - r * r)));
-                    out[i][j] = 2 * tDistribution.cumulativeProbability(-t);
+                    out[i][j] = 2 * (1 - tDistribution.cumulativeProbability(t));
                 }
             }
         }

```

## NopolPC 

org.apache.commons.math.stat.correlation.PearsonsCorrelation:193 (Suspicious rank: ample 18, jaccard 18, ochiai 18, naish1 16548, gp13 18, naish2 18, tarantula 18, )
```Java
1 - nVars < -1
```

Nb Angelic value: 1

Nb analyzed Statement: 15

Execution time: 0:00:52.496000

Grid5000 node: graphene-50.nancy.grid5000.fr

# Math 70

Nb Executed tests: 2184

Nb Failing tests: 1

>	org.apache.commons.math.analysis.solvers.BisectionSolverTest#testMath369

## Human Patch 

```Java
diff --git a/org/apache/commons/math/analysis/solvers/BisectionSolver.java b/org/apache/commons/math/analysis/solvers/BisectionSolver.java
index 180caef..3f66927 100644
--- a/org/apache/commons/math/analysis/solvers/BisectionSolver.java
+++ b/org/apache/commons/math/analysis/solvers/BisectionSolver.java
@@ -69,7 +69,7 @@ public class BisectionSolver extends UnivariateRealSolverImpl {
     /** {@inheritDoc} */
     public double solve(final UnivariateRealFunction f, double min, double max, double initial)
         throws MaxIterationsExceededException, FunctionEvaluationException {
-        return solve(f, min, max);
+        return solve(min, max);
     }
 
     /** {@inheritDoc} */

```

## Genprog 

org.apache.commons.math.analysis.solvers.BisectionSolver:72 (Suspicious rank: ample 1, jaccard 1, ochiai 1, naish1 16589, gp13 1, naish2 1, tarantula 1, )
REPLACE
```Java
return solve(f, min, max)
```

Grid5000 node: graphene-42.nancy.grid5000.fr

# Math 71

Nb Executed tests: 2169

Nb Failing tests: 2

>	org.apache.commons.math.ode.nonstiff.ClassicalRungeKuttaIntegratorTest#testMissedEndEvent
>	org.apache.commons.math.ode.nonstiff.DormandPrince853IntegratorTest#testMissedEndEvent

## Human Patch 

```Java
diff --git a/org/apache/commons/math/ode/nonstiff/AdamsBashforthIntegrator.java b/org/apache/commons/math/ode/nonstiff/AdamsBashforthIntegrator.java
index 6ee9bd5..935bb8b 100644
--- a/org/apache/commons/math/ode/nonstiff/AdamsBashforthIntegrator.java
+++ b/org/apache/commons/math/ode/nonstiff/AdamsBashforthIntegrator.java
@@ -271,16 +271,8 @@ public class AdamsBashforthIntegrator extends AdamsIntegrator {
                     if (manager.evaluateStep(interpolatorTmp)) {
                         final double dt = manager.getEventTime() - stepStart;
                         if (Math.abs(dt) <= Math.ulp(stepStart)) {
-                            // we cannot simply truncate the step, reject the current computation
-                            // and let the loop compute another state with the truncated step.
-                            // it is so small (much probably exactly 0 due to limited accuracy)
-                            // that the code above would fail handling it.
-                            // So we set up an artificial 0 size step by copying states
-                            interpolator.storeTime(stepStart);
-                            System.arraycopy(y, 0, yTmp, 0, y0.length);
-                            hNew     = 0;
-                            stepSize = 0;
-                            loop     = false;
+                            // rejecting the step would lead to a too small next step, we accept it
+                            loop = false;
                         } else {
                             // reject the step to match exactly the next switch time
                             hNew = dt;
diff --git a/org/apache/commons/math/ode/nonstiff/AdamsMoultonIntegrator.java b/org/apache/commons/math/ode/nonstiff/AdamsMoultonIntegrator.java
index e0e2f0d..27ade7b 100644
--- a/org/apache/commons/math/ode/nonstiff/AdamsMoultonIntegrator.java
+++ b/org/apache/commons/math/ode/nonstiff/AdamsMoultonIntegrator.java
@@ -289,16 +289,8 @@ public class AdamsMoultonIntegrator extends AdamsIntegrator {
                     if (manager.evaluateStep(interpolatorTmp)) {
                         final double dt = manager.getEventTime() - stepStart;
                         if (Math.abs(dt) <= Math.ulp(stepStart)) {
-                            // we cannot simply truncate the step, reject the current computation
-                            // and let the loop compute another state with the truncated step.
-                            // it is so small (much probably exactly 0 due to limited accuracy)
-                            // that the code above would fail handling it.
-                            // So we set up an artificial 0 size step by copying states
-                            interpolator.storeTime(stepStart);
-                            System.arraycopy(y, 0, yTmp, 0, y0.length);
-                            hNew     = 0;
-                            stepSize = 0;
-                            loop     = false;
+                            // rejecting the step would lead to a too small next step, we accept it
+                            loop = false;
                         } else {
                             // reject the step to match exactly the next switch time
                             hNew = dt;
diff --git a/org/apache/commons/math/ode/nonstiff/EmbeddedRungeKuttaIntegrator.java b/org/apache/commons/math/ode/nonstiff/EmbeddedRungeKuttaIntegrator.java
index e03be9e..34b3dc1 100644
--- a/org/apache/commons/math/ode/nonstiff/EmbeddedRungeKuttaIntegrator.java
+++ b/org/apache/commons/math/ode/nonstiff/EmbeddedRungeKuttaIntegrator.java
@@ -292,16 +292,8 @@ public abstract class EmbeddedRungeKuttaIntegrator
           if (manager.evaluateStep(interpolator)) {
               final double dt = manager.getEventTime() - stepStart;
               if (Math.abs(dt) <= Math.ulp(stepStart)) {
-                  // we cannot simply truncate the step, reject the current computation
-                  // and let the loop compute another state with the truncated step.
-                  // it is so small (much probably exactly 0 due to limited accuracy)
-                  // that the code above would fail handling it.
-                  // So we set up an artificial 0 size step by copying states
-                  interpolator.storeTime(stepStart);
-                  System.arraycopy(y, 0, yTmp, 0, y0.length);
-                  hNew     = 0;
-                  stepSize = 0;
-                  loop     = false;
+                  // rejecting the step would lead to a too small next step, we accept it
+                  loop = false;
               } else {
                   // reject the step to match exactly the next switch time
                   hNew = dt;
diff --git a/org/apache/commons/math/ode/nonstiff/RungeKuttaIntegrator.java b/org/apache/commons/math/ode/nonstiff/RungeKuttaIntegrator.java
index b61b0b1..3227b98 100644
--- a/org/apache/commons/math/ode/nonstiff/RungeKuttaIntegrator.java
+++ b/org/apache/commons/math/ode/nonstiff/RungeKuttaIntegrator.java
@@ -172,15 +172,8 @@ public abstract class RungeKuttaIntegrator extends AbstractIntegrator {
         if (manager.evaluateStep(interpolator)) {
             final double dt = manager.getEventTime() - stepStart;
             if (Math.abs(dt) <= Math.ulp(stepStart)) {
-                // we cannot simply truncate the step, reject the current computation
-                // and let the loop compute another state with the truncated step.
-                // it is so small (much probably exactly 0 due to limited accuracy)
-                // that the code above would fail handling it.
-                // So we set up an artificial 0 size step by copying states
-                interpolator.storeTime(stepStart);
-                System.arraycopy(y, 0, yTmp, 0, y0.length);
-                stepSize = 0;
-                loop     = false;
+                // rejecting the step would lead to a too small next step, we accept it
+                loop = false;
             } else {
                 // reject the step to match exactly the next switch time
                 stepSize = dt;

```

## NopolC 

org.apache.commons.math.analysis.solvers.BrentSolver:334 (Suspicious rank: ample 90, jaccard 188, ochiai 99, naish1 16023, gp13 90, naish2 90, tarantula 190, )
```Java
(dx > 0.0) || (org.apache.commons.math.analysis.solvers.BrentSolver.NON_BRACKETING_MESSAGE.length() < x1)
```

Nb Angelic value: 2

Nb analyzed Statement: 102

Execution time: 0:44:51.622000

Grid5000 node: graphene-58.nancy.grid5000.fr

## BrutpolPC 

org.apache.commons.math.ode.events.EventState:260 (Suspicious rank: ample 66, jaccard 163, ochiai 68, naish1 16213, gp13 66, naish2 66, tarantula 163, )
```Java
h <= this.nextAction
```

Nb Angelic value: 4

Nb analyzed Statement: 55

Execution time: 0:52:27.066000

Grid5000 node: graphene-25.nancy.grid5000.fr

## Genprog 

org.apache.commons.math.ode.events.EventState:188 (Suspicious rank: ample 68, jaccard 165, ochiai 91, naish1 16066, gp13 68, naish2 68, tarantula 165, )
INSERT_BEFORE
```Java
if ((pendingEvent) && ((java.lang.Math.abs((t1 - (pendingEventTime)))) <= (convergence))) {
	return false;
} 
```

Grid5000 node: griffon-23.nancy.grid5000.fr

# Math 73

Nb Executed tests: 2140

Nb Failing tests: 1

>	org.apache.commons.math.analysis.solvers.BrentSolverTest#testBadEndpoints

## Human Patch 

```Java
diff --git a/org/apache/commons/math/analysis/solvers/BrentSolver.java b/org/apache/commons/math/analysis/solvers/BrentSolver.java
index e0cb427..4e95ed5 100644
--- a/org/apache/commons/math/analysis/solvers/BrentSolver.java
+++ b/org/apache/commons/math/analysis/solvers/BrentSolver.java
@@ -32,11 +32,6 @@ import org.apache.commons.math.analysis.UnivariateRealFunction;
  */
 public class BrentSolver extends UnivariateRealSolverImpl {
 
-    /** Error message for non-bracketing interval. */
-    private static final String NON_BRACKETING_MESSAGE =
-        "function values at endpoints do not have different signs.  " +
-        "Endpoints: [{0}, {1}], Values: [{2}, {3}]";
-
     /** Serializable version identifier */
     private static final long serialVersionUID = 7694577816772532779L;
 
@@ -133,11 +128,6 @@ public class BrentSolver extends UnivariateRealSolverImpl {
             return solve(f, initial, yInitial, max, yMax, initial, yInitial);
         }
 
-        if (yMin * yMax > 0) {
-            throw MathRuntimeException.createIllegalArgumentException(
-                  NON_BRACKETING_MESSAGE, min, max, yMin, yMax);
-        }
-
         // full Brent algorithm starting with provided initial guess
         return solve(f, min, yMin, max, yMax, initial, yInitial);
 
@@ -186,7 +176,9 @@ public class BrentSolver extends UnivariateRealSolverImpl {
             } else {
                 // neither value is close to zero and min and max do not bracket root.
                 throw MathRuntimeException.createIllegalArgumentException(
-                        NON_BRACKETING_MESSAGE, min, max, yMin, yMax);
+                        "function values at endpoints do not have different signs.  " +
+                        "Endpoints: [{0}, {1}], Values: [{2}, {3}]",
+                        min, max, yMin, yMax);
             }
         } else if (sign < 0){
             // solve using only the first endpoint as initial guess

```

## NopolC 

org.apache.commons.math.analysis.solvers.UnivariateRealSolverImpl:225 (Suspicious rank: ample 16, jaccard 16, ochiai 16, naish1 15884, gp13 16, naish2 16, tarantula 16, )
```Java
((!((1) != (lower))) && (org.apache.commons.math.analysis.solvers.UnivariateRealSolverImpl.this.result < org.apache.commons.math.analysis.solvers.UnivariateRealSolverImpl.this.defaultFunctionValueAccuracy)) || (initial <= lower)
```

Nb Angelic value: 1

Nb analyzed Statement: 17

Execution time: 0:00:40.722000

Grid5000 node: graphene-82.nancy.grid5000.fr

## Genprog 

org.apache.commons.math.analysis.solvers.BrentSolver:132 (Suspicious rank: ample 1, jaccard 1, ochiai 1, naish1 15933, gp13 1, naish2 1, tarantula 1, )
REPLACE
```Java
return solve(f, min, max)
```

Grid5000 node: graphene-64.nancy.grid5000.fr

# Math 78

Nb Executed tests: 2106

Nb Failing tests: 2

>	org.apache.commons.math.random.AbstractRandomGeneratorTest#testNextPoissonConsistency
>	org.apache.commons.math.ode.events.EventStateTest#closeEvents

## Human Patch 

```Java
diff --git a/org/apache/commons/math/ode/events/EventState.java b/org/apache/commons/math/ode/events/EventState.java
index ff09646..44f6742 100644
--- a/org/apache/commons/math/ode/events/EventState.java
+++ b/org/apache/commons/math/ode/events/EventState.java
@@ -188,26 +187,6 @@ public class EventState {
                 if (g0Positive ^ (gb >= 0)) {
                     // there is a sign change: an event is expected during this step
 
-                    if (ga * gb > 0) {
-                        // this is a corner case:
-                        // - there was an event near ta,
-                        // - there is another event between ta and tb
-                        // - when ta was computed, convergence was reached on the "wrong side" of the interval
-                        // this implies that the real sign of ga is the same as gb, so we need to slightly
-                        // shift ta to make sure ga and gb get opposite signs and the solver won't complain
-                        // about bracketing
-                        final double epsilon = (forward ? 0.25 : -0.25) * convergence;
-                        for (int k = 0; (k < 4) && (ga * gb > 0); ++k) {
-                            ta += epsilon;
-                            interpolator.setInterpolatedTime(ta);
-                            ga = handler.g(ta, interpolator.getInterpolatedState());
-                        }
-                        if (ga * gb > 0) {
-                            // this should never happen
-                            throw MathRuntimeException.createInternalError(null);
-                        }
-                    }
-                         
                     // variation direction, with respect to the integration direction
                     increasing = gb >= ga;
 
@@ -226,9 +205,16 @@ public class EventState {
                     final BrentSolver solver = new BrentSolver();
                     solver.setAbsoluteAccuracy(convergence);
                     solver.setMaximalIterationCount(maxIterationCount);
-                    final double root = (ta <= tb) ? solver.solve(f, ta, tb) : solver.solve(f, tb, ta);
-                    if ((Math.abs(root - ta) <= convergence) &&
-                         (Math.abs(root - previousEventTime) <= convergence)) {
+                    double root;
+                    try {
+                        root = (ta <= tb) ? solver.solve(f, ta, tb) : solver.solve(f, tb, ta);
+                    } catch (IllegalArgumentException iae) {
+                        // the interval did not really bracket a root
+                        root = Double.NaN;
+                    }
+                    if (Double.isNaN(root) ||
+                        ((Math.abs(root - ta) <= convergence) &&
+                         (Math.abs(root - previousEventTime) <= convergence))) {
                         // we have either found nothing or found (again ?) a past event, we simply ignore it
                         ta = tb;
                         ga = gb;

```

## NopolPC 

org.apache.commons.math.analysis.solvers.BrentSolver:282 (Suspicious rank: ample 32, jaccard 32, ochiai 32, naish1 16567, gp13 32, naish2 32, tarantula 32, )
```Java
-1 <= delta
```

Nb Angelic value: 1

Nb analyzed Statement: 9

Execution time: 0:00:47.478000

Grid5000 node: graphene-55.nancy.grid5000.fr

## BrutpolPC 

org.apache.commons.math.ode.events.EventState:207 (Suspicious rank: ample 159, jaccard 159, ochiai 157, naish1 16589, gp13 159, naish2 159, tarantula 159, )
```Java
this.t0 <= this.maxIterationCount
```

Nb Angelic value: 2

Nb analyzed Statement: 33

Execution time: 0:04:04.720000

Grid5000 node: graphene-39.nancy.grid5000.fr

## Genprog 

org.apache.commons.math.ode.events.EventState:283 (Suspicious rank: ample 185, jaccard 185, ochiai 182, naish1 16660, gp13 185, naish2 185, tarantula 185, )
DELETE
```Java
remove
```

Grid5000 node: graphene-76.nancy.grid5000.fr

## Kali 

org.apache.commons.math.ode.events.EventState:283 (Suspicious rank: ample 185, jaccard 185, ochiai 182, naish1 16660, gp13 185, naish2 185, tarantula 185, )
DELETE
```Java
remove
```

Grid5000 node: graphene-64.nancy.grid5000.fr

# Math 80

Nb Executed tests: 2102

Nb Failing tests: 1

>	org.apache.commons.math.linear.EigenDecompositionImplTest#testMathpbx02

## Human Patch 

```Java
diff --git a/org/apache/commons/math/linear/EigenDecompositionImpl.java b/org/apache/commons/math/linear/EigenDecompositionImpl.java
index 9d1b797..3fc328d 100644
--- a/org/apache/commons/math/linear/EigenDecompositionImpl.java
+++ b/org/apache/commons/math/linear/EigenDecompositionImpl.java
@@ -1132,7 +1132,7 @@ public class EigenDecompositionImpl implements EigenDecomposition {
     private boolean flipIfWarranted(final int n, final int step) {
         if (1.5 * work[pingPong] < work[4 * (n - 1) + pingPong]) {
             // flip array
-            int j = 4 * (n - 1);
+            int j = 4 * n - 1;
             for (int i = 0; i < j; i += 4) {
                 for (int k = 0; k < 4; k += step) {
                     final double tmp = work[i + k];

```

## NopolPC 

org.apache.commons.math.linear.EigenDecompositionImpl:1139 (Suspicious rank: ample 1, jaccard 1, ochiai 18, naish1 16068, gp13 1, naish2 1, tarantula 1, )
```Java
org.apache.commons.math.linear.EigenDecompositionImpl.this.cachedD!=null
```

Nb Angelic value: 1

Nb analyzed Statement: 14

Execution time: 0:00:47.820000

Grid5000 node: graphene-55.nancy.grid5000.fr

## Genprog 

org.apache.commons.math.linear.EigenDecompositionImpl:1137 (Suspicious rank: ample 3, jaccard 3, ochiai 16, naish1 16070, gp13 3, naish2 3, tarantula 3, )
DELETE
```Java
remove
```

Grid5000 node: graphene-76.nancy.grid5000.fr

## Kali 

org.apache.commons.math.linear.EigenDecompositionImpl:1135 (Suspicious rank: ample 5, jaccard 5, ochiai 14, naish1 16072, gp13 5, naish2 5, tarantula 5, )
INSERT_BEFORE
```Java
if (true)
	return false;

```

org.apache.commons.math.linear.EigenDecompositionImpl:1136 (Suspicious rank: ample 4, jaccard 4, ochiai 15, naish1 16071, gp13 4, naish2 4, tarantula 4, )
DELETE
```Java
remove
```

org.apache.commons.math.linear.EigenDecompositionImpl:1136 (Suspicious rank: ample 4, jaccard 4, ochiai 15, naish1 16071, gp13 4, naish2 4, tarantula 4, )
INSERT_BEFORE
```Java
if (true)
	return false;

```

org.apache.commons.math.linear.EigenDecompositionImpl:1137 (Suspicious rank: ample 3, jaccard 3, ochiai 16, naish1 16070, gp13 3, naish2 3, tarantula 3, )
DELETE
```Java
remove
```

org.apache.commons.math.linear.EigenDecompositionImpl:1137 (Suspicious rank: ample 3, jaccard 3, ochiai 16, naish1 16070, gp13 3, naish2 3, tarantula 3, )
INSERT_BEFORE
```Java
if (true)
	return false;

```

org.apache.commons.math.linear.EigenDecompositionImpl:1138 (Suspicious rank: ample 2, jaccard 2, ochiai 17, naish1 16069, gp13 2, naish2 2, tarantula 2, )
INSERT_BEFORE
```Java
if (true)
	return false;

```

org.apache.commons.math.linear.EigenDecompositionImpl:1139 (Suspicious rank: ample 1, jaccard 1, ochiai 18, naish1 16068, gp13 1, naish2 1, tarantula 1, )
DELETE
```Java
remove
```

org.apache.commons.math.linear.EigenDecompositionImpl:1139 (Suspicious rank: ample 1, jaccard 1, ochiai 18, naish1 16068, gp13 1, naish2 1, tarantula 1, )
INSERT_BEFORE
```Java
if (true)
	return false;

```

org.apache.commons.math.linear.EigenDecompositionImpl:840 (Suspicious rank: ample 333, jaccard 333, ochiai 110, naish1 16586, gp13 333, naish2 333, tarantula 333, )
DELETE
```Java
remove
```

org.apache.commons.math.linear.EigenDecompositionImpl:1133 (Suspicious rank: ample 95, jaccard 95, ochiai 195, naish1 16073, gp13 95, naish2 95, tarantula 95, )
DELETE
```Java
remove
```

org.apache.commons.math.linear.EigenDecompositionImpl:1133 (Suspicious rank: ample 95, jaccard 95, ochiai 195, naish1 16073, gp13 95, naish2 95, tarantula 95, )
INSERT_BEFORE
```Java
if (true)
	return false;

```

org.apache.commons.math.linear.EigenDecompositionImpl:1133 (Suspicious rank: ample 95, jaccard 95, ochiai 195, naish1 16073, gp13 95, naish2 95, tarantula 95, )
REPLACE
```Java
if (false) {
	int j = (4 * n) - 1;
	for (int i = 0 ; i < j ; i += 4) {
		for (int k = 0 ; k < 4 ; k += step) {
			final double tmp = work[(i + k)];
			work[(i + k)] = work[(j - k)];
			work[(j - k)] = tmp;
		}
		j -= 4;
	}
	return true;
} 
```

Grid5000 node: graphene-72.nancy.grid5000.fr

# Math 81

Nb Executed tests: 2101

Nb Failing tests: 1

>	org.apache.commons.math.linear.EigenDecompositionImplTest#testMath308

## Human Patch 

```Java
diff --git a/org/apache/commons/math/linear/EigenDecompositionImpl.java b/org/apache/commons/math/linear/EigenDecompositionImpl.java
index 3fc328d..53a40f0 100644
--- a/org/apache/commons/math/linear/EigenDecompositionImpl.java
+++ b/org/apache/commons/math/linear/EigenDecompositionImpl.java
@@ -595,12 +595,8 @@ public class EigenDecompositionImpl implements EigenDecomposition {
         }
 
         final double dCurrent = main[m - 1];
-        final double lower = dCurrent - eCurrent;
-        work[lowerStart + m - 1] = lower;
-        lowerSpectra = Math.min(lowerSpectra, lower);
-        final double upper = dCurrent + eCurrent;
-        work[upperStart + m - 1] = upper;
-        upperSpectra = Math.max(upperSpectra, upper);
+        work[lowerStart + m - 1] = dCurrent - eCurrent;
+        work[upperStart + m - 1] = dCurrent + eCurrent;
         minPivot = MathUtils.SAFE_MIN * Math.max(1.0, eMax * eMax);
 
     }
@@ -903,8 +899,8 @@ public class EigenDecompositionImpl implements EigenDecomposition {
                     diagMax    = work[4 * i0];
                     offDiagMin = work[4 * i0 + 2];
                     double previousEMin = work[4 * i0 + 3];
-                    for (int i = 4 * i0; i < 4 * n0 - 16; i += 4) {
-                        if ((work[i + 3] <= TOLERANCE_2 * work[i]) ||
+                    for (int i = 4 * i0; i < 4 * n0 - 11; i += 4) {
+                        if ((work[i + 3] <= TOLERANCE_2 * work[i]) &&
                             (work[i + 2] <= TOLERANCE_2 * sigma)) {
                             // insert a split
                             work[i + 2]  = -sigma;
@@ -1541,7 +1537,7 @@ public class EigenDecompositionImpl implements EigenDecomposition {
                 double a2 = (work[np - 8] / b2) * (1 + work[np - 4] / b1);
 
                 // approximate contribution to norm squared from i < nn-2.
-                if (end - start > 3) {
+                if (end - start > 2) {
                     b2 = work[nn - 13] / work[nn - 15];
                     a2 = a2 + b2;
                     for (int i4 = nn - 17; i4 >= 4 * start + 2 + pingPong; i4 -= 4) {

```

## NopolPC 

org.apache.commons.math.linear.EigenDecompositionImpl:1541 (Suspicious rank: ample 4, jaccard 4, ochiai 11, naish1 16250, gp13 4, naish2 4, tarantula 4, )
```Java
(b2) != (org.apache.commons.math.linear.EigenDecompositionImpl.this.eMin)
```

Nb Angelic value: 1

Nb analyzed Statement: 5

Execution time: 0:00:44.052000

Grid5000 node: graphene-41.nancy.grid5000.fr

## NopolC 

org.apache.commons.math.linear.EigenDecompositionImpl:1540 (Suspicious rank: ample 3, jaccard 3, ochiai 10, naish1 16249, gp13 3, naish2 3, tarantula 3, )
```Java
org.apache.commons.math.linear.EigenDecompositionImpl.this.lowerSpectra < org.apache.commons.math.linear.EigenDecompositionImpl.this.splitTolerance
```

Nb Angelic value: 1

Nb analyzed Statement: 6

Execution time: 0:00:43.249000

Grid5000 node: graphene-80.nancy.grid5000.fr

## Genprog 

org.apache.commons.math.linear.EigenDecompositionImpl:1477 (Suspicious rank: ample 26, jaccard 26, ochiai 17, naish1 16501, gp13 26, naish2 26, tarantula 26, )
DELETE
```Java
remove
```

Grid5000 node: griffon-10.nancy.grid5000.fr

## Kali 

org.apache.commons.math.linear.EigenDecompositionImpl:1526 (Suspicious rank: ample 2, jaccard 2, ochiai 2, naish1 16239, gp13 2, naish2 2, tarantula 2, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.apache.commons.math.linear.EigenDecompositionImpl:1527 (Suspicious rank: ample 14, jaccard 14, ochiai 3, naish1 16486, gp13 14, naish2 14, tarantula 14, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.apache.commons.math.linear.EigenDecompositionImpl:1530 (Suspicious rank: ample 10, jaccard 10, ochiai 4, naish1 16432, gp13 10, naish2 10, tarantula 10, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.apache.commons.math.linear.EigenDecompositionImpl:1531 (Suspicious rank: ample 15, jaccard 15, ochiai 5, naish1 16536, gp13 15, naish2 15, tarantula 15, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.apache.commons.math.linear.EigenDecompositionImpl:1532 (Suspicious rank: ample 9, jaccard 9, ochiai 6, naish1 16431, gp13 9, naish2 9, tarantula 9, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.apache.commons.math.linear.EigenDecompositionImpl:1533 (Suspicious rank: ample 8, jaccard 8, ochiai 7, naish1 16430, gp13 8, naish2 8, tarantula 8, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.apache.commons.math.linear.EigenDecompositionImpl:1534 (Suspicious rank: ample 12, jaccard 12, ochiai 8, naish1 16434, gp13 12, naish2 12, tarantula 12, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.apache.commons.math.linear.EigenDecompositionImpl:1534 (Suspicious rank: ample 12, jaccard 12, ochiai 8, naish1 16434, gp13 12, naish2 12, tarantula 12, )
REPLACE
```Java
if (true) {
	return ;
} 
```

org.apache.commons.math.linear.EigenDecompositionImpl:1537 (Suspicious rank: ample 11, jaccard 11, ochiai 9, naish1 16433, gp13 11, naish2 11, tarantula 11, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.apache.commons.math.linear.EigenDecompositionImpl:1540 (Suspicious rank: ample 3, jaccard 3, ochiai 10, naish1 16249, gp13 3, naish2 3, tarantula 3, )
DELETE
```Java
remove
```

org.apache.commons.math.linear.EigenDecompositionImpl:1540 (Suspicious rank: ample 3, jaccard 3, ochiai 10, naish1 16249, gp13 3, naish2 3, tarantula 3, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.apache.commons.math.linear.EigenDecompositionImpl:1540 (Suspicious rank: ample 3, jaccard 3, ochiai 10, naish1 16249, gp13 3, naish2 3, tarantula 3, )
REPLACE
```Java
if (false) {
	b2 = (work[(nn - 13)]) / (work[(nn - 15)]);
	a2 = a2 + b2;
	for (int i4 = nn - 17 ; i4 >= (((4 * start) + 2) + (pingPong)) ; i4 -= 4) {
		if (b2 == 0.0) {
			break;
		} 
		b1 = b2;
		if ((work[i4]) > (work[(i4 - 2)])) {
			return ;
		} 
		b2 = b2 * ((work[i4]) / (work[(i4 - 2)]));
		a2 = a2 + b2;
		if (((100 * (java.lang.Math.max(b2, b1))) < a2) || (cnst1 < a2)) {
			break;
		} 
	}
	a2 = cnst3 * a2;
} 
```

org.apache.commons.math.linear.EigenDecompositionImpl:1541 (Suspicious rank: ample 4, jaccard 4, ochiai 11, naish1 16250, gp13 4, naish2 4, tarantula 4, )
DELETE
```Java
remove
```

org.apache.commons.math.linear.EigenDecompositionImpl:1541 (Suspicious rank: ample 4, jaccard 4, ochiai 11, naish1 16250, gp13 4, naish2 4, tarantula 4, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.apache.commons.math.linear.EigenDecompositionImpl:1477 (Suspicious rank: ample 26, jaccard 26, ochiai 17, naish1 16501, gp13 26, naish2 26, tarantula 26, )
DELETE
```Java
remove
```

org.apache.commons.math.linear.EigenDecompositionImpl:1481 (Suspicious rank: ample 22, jaccard 22, ochiai 19, naish1 16258, gp13 22, naish2 22, tarantula 22, )
DELETE
```Java
remove
```

org.apache.commons.math.linear.EigenDecompositionImpl:1517 (Suspicious rank: ample 37, jaccard 37, ochiai 40, naish1 16418, gp13 37, naish2 37, tarantula 37, )
DELETE
```Java
remove
```

org.apache.commons.math.linear.EigenDecompositionImpl:1517 (Suspicious rank: ample 37, jaccard 37, ochiai 40, naish1 16418, gp13 37, naish2 37, tarantula 37, )
REPLACE
```Java
if (false) {
	s = (gam * (1 - (java.lang.Math.sqrt(a2)))) / (1 + a2);
} 
```

org.apache.commons.math.linear.EigenDecompositionImpl:1518 (Suspicious rank: ample 39, jaccard 39, ochiai 41, naish1 16444, gp13 39, naish2 39, tarantula 39, )
DELETE
```Java
remove
```

Grid5000 node: graphene-61.nancy.grid5000.fr

# Math 82

Nb Executed tests: 2056

Nb Failing tests: 1

>	org.apache.commons.math.optimization.linear.SimplexSolverTest#testMath288

## Human Patch 

```Java
diff --git a/org/apache/commons/math/optimization/linear/SimplexSolver.java b/org/apache/commons/math/optimization/linear/SimplexSolver.java
index 60a1b3a..16d3bae 100644
--- a/org/apache/commons/math/optimization/linear/SimplexSolver.java
+++ b/org/apache/commons/math/optimization/linear/SimplexSolver.java
@@ -77,10 +77,9 @@ public class SimplexSolver extends AbstractLinearOptimizer {
         double minRatio = Double.MAX_VALUE;
         Integer minRatioPos = null;
         for (int i = tableau.getNumObjectiveFunctions(); i < tableau.getHeight(); i++) {
-            final double rhs = tableau.getEntry(i, tableau.getWidth() - 1);
-            final double entry = tableau.getEntry(i, col);
-            if (MathUtils.compareTo(entry, 0, epsilon) > 0) {
-                final double ratio = rhs / entry;
+            double rhs = tableau.getEntry(i, tableau.getWidth() - 1);
+            if (MathUtils.compareTo(tableau.getEntry(i, col), 0, epsilon) >= 0) {
+                double ratio = rhs / tableau.getEntry(i, col);
                 if (ratio < minRatio) {
                     minRatio = ratio;
                     minRatioPos = i; 

```

## NopolPC 

org.apache.commons.math.optimization.linear.SimplexSolver:63 (Suspicious rank: ample 37, jaccard 37, ochiai 47, naish1 16048, gp13 37, naish2 37, tarantula 37, )
```Java
(0) != (minValue)
```

Nb Angelic value: 2

Nb analyzed Statement: 54

Execution time: 0:05:45.875000

Grid5000 node: graphene-73.nancy.grid5000.fr

## Genprog 

org.apache.commons.math.optimization.linear.SimplexSolver:63 (Suspicious rank: ample 37, jaccard 37, ochiai 47, naish1 16048, gp13 37, naish2 37, tarantula 37, )
DELETE
```Java
remove
```

Grid5000 node: graphene-42.nancy.grid5000.fr

## Kali 

org.apache.commons.math.optimization.linear.SimplexSolver:63 (Suspicious rank: ample 37, jaccard 37, ochiai 47, naish1 16048, gp13 37, naish2 37, tarantula 37, )
DELETE
```Java
remove
```

Grid5000 node: graphene-65.nancy.grid5000.fr

# Math 84

Nb Executed tests: 2054

Nb Failing tests: 2

>	org.apache.commons.math.optimization.direct.MultiDirectionalTest#testMinimizeMaximize
>	org.apache.commons.math.optimization.direct.MultiDirectionalTest#testMath283

## Human Patch 

```Java
diff --git a/org/apache/commons/math/optimization/direct/MultiDirectional.java b/org/apache/commons/math/optimization/direct/MultiDirectional.java
index 929560c..955d0d8 100644
--- a/org/apache/commons/math/optimization/direct/MultiDirectional.java
+++ b/org/apache/commons/math/optimization/direct/MultiDirectional.java
@@ -61,7 +60,6 @@ public class MultiDirectional extends DirectSearchOptimizer {
     protected void iterateSimplex(final Comparator<RealPointValuePair> comparator)
         throws FunctionEvaluationException, OptimizationException, IllegalArgumentException {
 
-        final RealConvergenceChecker checker = getConvergenceChecker();
         while (true) {
 
             incrementIterationsCounter();
@@ -93,16 +91,6 @@ public class MultiDirectional extends DirectSearchOptimizer {
                 return;
             }
 
-            // check convergence
-            final int iter = getIterations();
-            boolean converged = true;
-            for (int i = 0; i < simplex.length; ++i) {
-                converged &= checker.converged(iter, original[i], simplex[i]);
-            }
-            if (converged) {
-                return;
-            }
-
         }
 
     }

```

## Genprog 

org.apache.commons.math.optimization.direct.MultiDirectional:90 (Suspicious rank: ample 16, jaccard 16, ochiai 7, naish1 16169, gp13 16, naish2 16, tarantula 16, )
REPLACE
```Java
return 
```

Grid5000 node: graphene-25.nancy.grid5000.fr

## Kali 

org.apache.commons.math.optimization.direct.MultiDirectional:90 (Suspicious rank: ample 16, jaccard 16, ochiai 7, naish1 16169, gp13 16, naish2 16, tarantula 16, )
INSERT_BEFORE
```Java
if (true)
	return ;

```

org.apache.commons.math.optimization.direct.MultiDirectional:90 (Suspicious rank: ample 16, jaccard 16, ochiai 7, naish1 16169, gp13 16, naish2 16, tarantula 16, )
REPLACE
```Java
if (true) {
	return ;
} 
```

Grid5000 node: graphene-71.nancy.grid5000.fr

# Math 85

Nb Executed tests: 1983

Nb Failing tests: 1

>	org.apache.commons.math.distribution.NormalDistributionTest#testMath280

## Human Patch 

```Java
diff --git a/org/apache/commons/math/analysis/solvers/UnivariateRealSolverUtils.java b/org/apache/commons/math/analysis/solvers/UnivariateRealSolverUtils.java
index e6398f6..5b76415 100644
--- a/org/apache/commons/math/analysis/solvers/UnivariateRealSolverUtils.java
+++ b/org/apache/commons/math/analysis/solvers/UnivariateRealSolverUtils.java
@@ -195,7 +195,7 @@ public class UnivariateRealSolverUtils {
         } while ((fa * fb > 0.0) && (numIterations < maximumIterations) && 
                 ((a > lowerBound) || (b < upperBound)));
    
-        if (fa * fb > 0.0 ) {
+        if (fa * fb >= 0.0 ) {
             throw new ConvergenceException(
                       "number of iterations={0}, maximum iterations={1}, " +
                       "initial={2}, lower bound={3}, upper bound={4}, final a value={5}, " +

```

## NopolPC 

org.apache.commons.math.analysis.solvers.UnivariateRealSolverUtils:198 (Suspicious rank: ample 41, jaccard 41, ochiai 46, naish1 15686, gp13 41, naish2 41, tarantula 41, )
```Java
((fa * fb)) != (lowerBound)
```

Nb Angelic value: 1

Nb analyzed Statement: 37

Execution time: 0:00:41.256000

Grid5000 node: graphene-73.nancy.grid5000.fr

## NopolC 

org.apache.commons.math.analysis.solvers.UnivariateRealSolverUtils:198 (Suspicious rank: ample 41, jaccard 41, ochiai 46, naish1 15686, gp13 41, naish2 41, tarantula 41, )
```Java
1 <= (fa * fb)
```

Nb Angelic value: 1

Nb analyzed Statement: 37

Execution time: 0:00:41.210000

Grid5000 node: graphene-67.nancy.grid5000.fr

## BrutpolPC 

org.apache.commons.math.analysis.solvers.UnivariateRealSolverUtils:199 (Suspicious rank: ample 4, jaccard 4, ochiai 1, naish1 15706, gp13 4, naish2 4, tarantula 4, )
```Java
initial == lowerBound
```

Nb Angelic value: 1

Nb analyzed Statement: 4

Execution time: 0:01:46.548000

Grid5000 node: griffon-59.nancy.grid5000.fr

## BrutpolC 

org.apache.commons.math.analysis.solvers.UnivariateRealSolverUtils:198 (Suspicious rank: ample 41, jaccard 41, ochiai 46, naish1 15686, gp13 41, naish2 41, tarantula 41, )
```Java
0.0 == fa
```

Nb Angelic value: 1

Nb analyzed Statement: 37

Execution time: 0:01:47.895000

Grid5000 node: graphene-81.nancy.grid5000.fr

## Genprog 

org.apache.commons.math.analysis.solvers.UnivariateRealSolverUtils:199 (Suspicious rank: ample 4, jaccard 4, ochiai 1, naish1 15706, gp13 4, naish2 4, tarantula 4, )
DELETE
```Java
remove
```

Grid5000 node: graphene-70.nancy.grid5000.fr

## Kali 

org.apache.commons.math.analysis.solvers.UnivariateRealSolverUtils:199 (Suspicious rank: ample 4, jaccard 4, ochiai 1, naish1 15706, gp13 4, naish2 4, tarantula 4, )
DELETE
```Java
remove
```

org.apache.commons.math.analysis.solvers.UnivariateRealSolverUtils:198 (Suspicious rank: ample 41, jaccard 41, ochiai 46, naish1 15686, gp13 41, naish2 41, tarantula 41, )
DELETE
```Java
remove
```

org.apache.commons.math.analysis.solvers.UnivariateRealSolverUtils:198 (Suspicious rank: ample 41, jaccard 41, ochiai 46, naish1 15686, gp13 41, naish2 41, tarantula 41, )
REPLACE
```Java
if (false) {
	throw new org.apache.commons.math.ConvergenceException(("number of iterations={0}, maximum iterations={1}, " + ("initial={2}, lower bound={3}, upper bound={4}, final a value={5}, " + "final b value={6}, f(a)={7}, f(b)={8}")) , numIterations , maximumIterations , initial , lowerBound , upperBound , a , b , fa , fb);
} 
```

Grid5000 node: graphene-70.nancy.grid5000.fr

# Math 87

Nb Executed tests: 1893

Nb Failing tests: 1

>	org.apache.commons.math.optimization.linear.SimplexSolverTest#testSingleVariableAndConstraint

## Human Patch 

```Java
diff --git a/org/apache/commons/math/optimization/linear/SimplexTableau.java b/org/apache/commons/math/optimization/linear/SimplexTableau.java
index b0d114e..a6d7419 100644
--- a/org/apache/commons/math/optimization/linear/SimplexTableau.java
+++ b/org/apache/commons/math/optimization/linear/SimplexTableau.java
@@ -272,10 +272,12 @@ class SimplexTableau implements Serializable {
     private Integer getBasicRow(final int col) {
         Integer row = null;
         for (int i = getNumObjectiveFunctions(); i < getHeight(); i++) {
-            if (MathUtils.equals(getEntry(i, col), 1.0, epsilon) && (row == null)) {
-                row = i;
-            } else if (!MathUtils.equals(getEntry(i, col), 0.0, epsilon)) {
-                return null;
+            if (!MathUtils.equals(getEntry(i, col), 0.0, epsilon)) {
+                if (row == null) {
+                    row = i;
+                } else {
+                    return null;
+                }
             }
         }
         return row;

```

## NopolPC 

org.apache.commons.math.optimization.linear.SimplexTableau:161 (Suspicious rank: ample 43, jaccard 43, ochiai 25, naish1 14789, gp13 43, naish2 43, tarantula 43, )
```Java
(1) != (org.apache.commons.math.optimization.linear.SimplexTableau.this.numSlackVariables)
```

Nb Angelic value: 2

Nb analyzed Statement: 75

Execution time: 0:06:04.981000

Grid5000 node: graphene-49.nancy.grid5000.fr

## NopolC 

org.apache.commons.math.optimization.linear.SimplexTableau:160 (Suspicious rank: ample 111, jaccard 111, ochiai 127, naish1 14790, gp13 111, naish2 111, tarantula 111, )
```Java
(((1) != (constraints.size())) || (org.apache.commons.math.optimization.linear.SimplexTableau.this.numSlackVariables < zIndex)) && (!(restrictToNonNegative))
```

Nb Angelic value: 1

Nb analyzed Statement: 128

Execution time: 0:00:53.415000

Grid5000 node: graphene-81.nancy.grid5000.fr

## BrutpolPC 

org.apache.commons.math.optimization.linear.SimplexTableau:161 (Suspicious rank: ample 43, jaccard 43, ochiai 25, naish1 14789, gp13 43, naish2 43, tarantula 43, )
```Java
this.numDecisionVariables != height
```

Nb Angelic value: 3

Nb analyzed Statement: 75

Execution time: 0:14:04.406000

Grid5000 node: griffon-91.nancy.grid5000.fr

# Math 88

Nb Executed tests: 1880

Nb Failing tests: 1

>	org.apache.commons.math.optimization.linear.SimplexSolverTest#testMath272

## Human Patch 

```Java
diff --git a/org/apache/commons/math/optimization/linear/SimplexTableau.java b/org/apache/commons/math/optimization/linear/SimplexTableau.java
index a6d7419..ba57722 100644
--- a/org/apache/commons/math/optimization/linear/SimplexTableau.java
+++ b/org/apache/commons/math/optimization/linear/SimplexTableau.java
@@ -323,27 +321,39 @@ class SimplexTableau implements Serializable {
      */
     protected RealPointValuePair getSolution() {
         double[] coefficients = new double[getOriginalNumDecisionVariables()];
-        Integer basicRow =
-            getBasicRow(getNumObjectiveFunctions() + getOriginalNumDecisionVariables());
-        double mostNegative = basicRow == null ? 0 : getEntry(basicRow, getRhsOffset());
-        Set<Integer> basicRows = new HashSet<Integer>();
+        double mostNegative = getDecisionVariableValue(getOriginalNumDecisionVariables());
         for (int i = 0; i < coefficients.length; i++) {
-            basicRow = getBasicRow(getNumObjectiveFunctions() + i);
-            if (basicRows.contains(basicRow)) {
-                // if multiple variables can take a given value 
-                // then we choose the first and set the rest equal to 0
-                coefficients[i] = 0;
-            } else {
-                basicRows.add(basicRow);
-                coefficients[i] =
-                    (basicRow == null ? 0 : getEntry(basicRow, getRhsOffset())) -
-                    (restrictToNonNegative ? 0 : mostNegative);
-            }
+            coefficients[i] =
+                getDecisionVariableValue(i) - (restrictToNonNegative ? 0 : mostNegative); 
         }
         return new RealPointValuePair(coefficients, f.getValue(coefficients));
     }
 
     /**
+     * Get the value of the given decision variable.  This is not the actual
+     * value as it is guaranteed to be >= 0 and thus must be corrected before
+     * being returned to the user.
+     * 
+     * @param decisionVariable The index of the decision variable
+     * @return The value of the given decision variable.
+     */
+    protected double getDecisionVariableValue(final int decisionVariable) {
+      int col = getNumObjectiveFunctions() + decisionVariable;  
+      Integer basicRow = getBasicRow(col);
+      if (basicRow == null) {
+          return 0;
+      }
+      // if there are multiple variables that can take the value on the RHS
+      // then we'll give the first variable that value
+      for (int i = getNumObjectiveFunctions(); i < col; i++) {
+          if (tableau.getEntry(basicRow, i) == 1) {
+              return 0;
+          }
+      }
+      return getEntry(basicRow, getRhsOffset()); 
+  }
+
+    /**
      * Subtracts a multiple of one row from another.
      * <p>
      * After application of this operation, the following will hold:

```

## NopolPC 

org.apache.commons.math.optimization.linear.SimplexTableau:352 (Suspicious rank: ample 1, jaccard 1, ochiai 1, naish1 14715, gp13 1, naish2 1, tarantula 1, )
```Java
org.apache.commons.math.optimization.linear.SimplexTableau.this.constraints.size() < org.apache.commons.math.optimization.linear.SimplexTableau.this.numDecisionVariables
```

Nb Angelic value: 1

Nb analyzed Statement: 1

Execution time: 0:00:31.932000

Grid5000 node: graphene-49.nancy.grid5000.fr

## BrutpolPC 

org.apache.commons.math.optimization.linear.SimplexTableau:352 (Suspicious rank: ample 1, jaccard 1, ochiai 1, naish1 14715, gp13 1, naish2 1, tarantula 1, )
```Java
this.numDecisionVariables != this.numSlackVariables
```

Nb Angelic value: 1

Nb analyzed Statement: 1

Execution time: 0:02:28.757000

Grid5000 node: graphene-82.nancy.grid5000.fr

# Math 95

Nb Executed tests: 1301

Nb Failing tests: 49

>	org.apache.commons.math.distribution.FDistributionTest#testSmallDegreesOfFreedom
>	org.apache.commons.math.fraction.FractionTest#testFloatValue
>	org.apache.commons.math.fraction.FractionTest#testAbs
>	org.apache.commons.math.fraction.FractionTest#testAdd
>	org.apache.commons.math.fraction.FractionTest#testSubtract
>	org.apache.commons.math.fraction.FractionTest#testReciprocal
>	org.apache.commons.math.fraction.FractionTest#testEpsilonLimitConstructor
>	org.apache.commons.math.fraction.FractionTest#testGetReducedFraction
>	org.apache.commons.math.fraction.FractionTest#testConstructorDouble
>	org.apache.commons.math.fraction.FractionTest#testCompareTo
>	org.apache.commons.math.fraction.FractionTest#testDoubleConstructor
>	org.apache.commons.math.fraction.FractionTest#testLongValue
>	org.apache.commons.math.fraction.FractionTest#testDigitLimitConstructor
>	org.apache.commons.math.fraction.FractionTest#testIntValue
>	org.apache.commons.math.fraction.FractionTest#testDivide
>	org.apache.commons.math.fraction.FractionTest#testMultiply
>	org.apache.commons.math.fraction.FractionTest#testEqualsAndHashCode
>	org.apache.commons.math.fraction.FractionTest#testNegate
>	org.apache.commons.math.fraction.FractionTest#testGoldenRatio
>	org.apache.commons.math.fraction.FractionTest#testIntegerOverflow
>	org.apache.commons.math.fraction.FractionTest#testDoubleValue
>	org.apache.commons.math.fraction.FractionTest#testConstructor
>	org.apache.commons.math.optimization.MultiDirectionalTest#testCostExceptions
>	org.apache.commons.math.optimization.MultiDirectionalTest#testRosenbrock
>	org.apache.commons.math.optimization.MultiDirectionalTest#testPowell
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatImproperNegative
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatImproper
>	org.apache.commons.math.fraction.FractionFormatTest#testParseProper
>	org.apache.commons.math.fraction.FractionFormatTest#testParseProperNegative
>	org.apache.commons.math.fraction.FractionFormatTest#testParse
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatZero
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatNegative
>	org.apache.commons.math.fraction.FractionFormatTest#testParseInteger
>	org.apache.commons.math.fraction.FractionFormatTest#testFormat
>	org.apache.commons.math.fraction.FractionFormatTest#testParseNegative
>	org.apache.commons.math.ode.nonstiff.AdamsMoultonIntegratorTest#testPredictorCoefficients
>	org.apache.commons.math.ode.nonstiff.AdamsMoultonIntegratorTest#testDimensionCheck
>	org.apache.commons.math.ode.nonstiff.AdamsMoultonIntegratorTest#testBackward
>	org.apache.commons.math.ode.nonstiff.AdamsMoultonIntegratorTest#testSmallStep
>	org.apache.commons.math.ode.nonstiff.AdamsMoultonIntegratorTest#testDecreasingSteps
>	org.apache.commons.math.ode.nonstiff.AdamsMoultonIntegratorTest#testBigStep
>	org.apache.commons.math.ode.nonstiff.AdamsMoultonIntegratorTest#testCorrectorCoefficients
>	junit.framework.TestSuite$1#warning
>	org.apache.commons.math.ode.nonstiff.AdamsBashforthIntegratorTest#testDimensionCheck
>	org.apache.commons.math.ode.nonstiff.AdamsBashforthIntegratorTest#testBackward
>	org.apache.commons.math.ode.nonstiff.AdamsBashforthIntegratorTest#testSmallStep
>	org.apache.commons.math.ode.nonstiff.AdamsBashforthIntegratorTest#testDecreasingSteps
>	org.apache.commons.math.ode.nonstiff.AdamsBashforthIntegratorTest#testBigStep
>	org.apache.commons.math.ode.nonstiff.AdamsBashforthIntegratorTest#testCoefficients

## Human Patch 

```Java
diff --git a/org/apache/commons/math/distribution/FDistributionImpl.java b/org/apache/commons/math/distribution/FDistributionImpl.java
index 59aeb07..3959403 100644
--- a/org/apache/commons/math/distribution/FDistributionImpl.java
+++ b/org/apache/commons/math/distribution/FDistributionImpl.java
@@ -141,13 +141,8 @@ public class FDistributionImpl
      * @return initial domain value
      */
     protected double getInitialDomain(double p) {
-        double ret = 1.0;
-        double d = getDenominatorDegreesOfFreedom();
-        if (d > 2.0) {
-            // use mean
-            ret = d / (d - 2.0);
-        }
-        return ret;
+        return getDenominatorDegreesOfFreedom() /
+            (getDenominatorDegreesOfFreedom() - 2.0);
     }
     
     /**

```

## Genprog 

org.apache.commons.math.distribution.FDistributionImpl:144 (Suspicious rank: ample 1393, jaccard 105, ochiai 105, naish1 8365, gp13 105, naish2 105, tarantula 83, )
REPLACE
```Java
return numeratorDegreesOfFreedom
```

Grid5000 node: graphene-65.nancy.grid5000.fr

## Kali 

org.apache.commons.math.distribution.FDistributionImpl:144 (Suspicious rank: ample 1393, jaccard 105, ochiai 105, naish1 8365, gp13 105, naish2 105, tarantula 83, )
INSERT_BEFORE
```Java
if (true)
	return 0d;

```

Grid5000 node: graphene-78.nancy.grid5000.fr

# Math 96

Nb Executed tests: 1272

Nb Failing tests: 47

>	org.apache.commons.math.fraction.FractionTest#testFloatValue
>	org.apache.commons.math.fraction.FractionTest#testAbs
>	org.apache.commons.math.fraction.FractionTest#testAdd
>	org.apache.commons.math.fraction.FractionTest#testSubtract
>	org.apache.commons.math.fraction.FractionTest#testReciprocal
>	org.apache.commons.math.fraction.FractionTest#testEpsilonLimitConstructor
>	org.apache.commons.math.fraction.FractionTest#testGetReducedFraction
>	org.apache.commons.math.fraction.FractionTest#testConstructorDouble
>	org.apache.commons.math.fraction.FractionTest#testCompareTo
>	org.apache.commons.math.fraction.FractionTest#testDoubleConstructor
>	org.apache.commons.math.fraction.FractionTest#testLongValue
>	org.apache.commons.math.fraction.FractionTest#testDigitLimitConstructor
>	org.apache.commons.math.fraction.FractionTest#testIntValue
>	org.apache.commons.math.fraction.FractionTest#testDivide
>	org.apache.commons.math.fraction.FractionTest#testMultiply
>	org.apache.commons.math.fraction.FractionTest#testEqualsAndHashCode
>	org.apache.commons.math.fraction.FractionTest#testNegate
>	org.apache.commons.math.fraction.FractionTest#testGoldenRatio
>	org.apache.commons.math.fraction.FractionTest#testIntegerOverflow
>	org.apache.commons.math.fraction.FractionTest#testDoubleValue
>	org.apache.commons.math.fraction.FractionTest#testConstructor
>	org.apache.commons.math.optimization.MultiDirectionalTest#testCostExceptions
>	org.apache.commons.math.optimization.MultiDirectionalTest#testRosenbrock
>	org.apache.commons.math.optimization.MultiDirectionalTest#testPowell
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatImproperNegative
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatImproper
>	org.apache.commons.math.fraction.FractionFormatTest#testParseProper
>	org.apache.commons.math.fraction.FractionFormatTest#testParseProperNegative
>	org.apache.commons.math.fraction.FractionFormatTest#testParse
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatZero
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatNegative
>	org.apache.commons.math.fraction.FractionFormatTest#testParseInteger
>	org.apache.commons.math.fraction.FractionFormatTest#testFormat
>	org.apache.commons.math.fraction.FractionFormatTest#testParseNegative
>	org.apache.commons.math.complex.ComplexTest#testMath221
>	org.apache.commons.math.ode.nonstiff.AdamsMoultonIntegratorTest#testPredictorCoefficients
>	org.apache.commons.math.ode.nonstiff.AdamsMoultonIntegratorTest#testDimensionCheck
>	org.apache.commons.math.ode.nonstiff.AdamsMoultonIntegratorTest#testSmallStep
>	org.apache.commons.math.ode.nonstiff.AdamsMoultonIntegratorTest#testDecreasingSteps
>	org.apache.commons.math.ode.nonstiff.AdamsMoultonIntegratorTest#testBigStep
>	org.apache.commons.math.ode.nonstiff.AdamsMoultonIntegratorTest#testCorrectorCoefficients
>	junit.framework.TestSuite$1#warning
>	org.apache.commons.math.ode.nonstiff.AdamsBashforthIntegratorTest#testDimensionCheck
>	org.apache.commons.math.ode.nonstiff.AdamsBashforthIntegratorTest#testSmallStep
>	org.apache.commons.math.ode.nonstiff.AdamsBashforthIntegratorTest#testDecreasingSteps
>	org.apache.commons.math.ode.nonstiff.AdamsBashforthIntegratorTest#testBigStep
>	org.apache.commons.math.ode.nonstiff.AdamsBashforthIntegratorTest#testCoefficients

## Human Patch 

```Java
diff --git a/org/apache/commons/math/complex/Complex.java b/org/apache/commons/math/complex/Complex.java
index 8b622cb..16b3873 100644
--- a/org/apache/commons/math/complex/Complex.java
+++ b/org/apache/commons/math/complex/Complex.java
@@ -255,7 +255,10 @@ public class Complex implements Serializable  {
                 if (rhs.isNaN()) {
                     ret = this.isNaN();
                 } else {
-                    ret = (real == rhs.real) && (imaginary == rhs.imaginary); 
+                ret = (Double.doubleToRawLongBits(real) ==
+                        Double.doubleToRawLongBits(rhs.getReal())) &&
+                    (Double.doubleToRawLongBits(imaginary) ==
+                        Double.doubleToRawLongBits(rhs.getImaginary())); 
                 }
             } catch (ClassCastException ex) {
                 // ignore exception

```

## BrutpolC 

org.apache.commons.math.complex.Complex:248 (Suspicious rank: ample 2269, jaccard 113, ochiai 112, naish1 8115, gp13 113, naish2 113, tarantula 113, )
```Java
0 == (1 + this.imaginary)
```

Nb Angelic value: 1

Nb analyzed Statement: 100

Execution time: 0:02:58.838000

Grid5000 node: griffon-74.nancy.grid5000.fr

# Math 97

Nb Executed tests: 1095

Nb Failing tests: 35

>	org.apache.commons.math.fraction.FractionTest#testFloatValue
>	org.apache.commons.math.fraction.FractionTest#testAbs
>	org.apache.commons.math.fraction.FractionTest#testAdd
>	org.apache.commons.math.fraction.FractionTest#testSubtract
>	org.apache.commons.math.fraction.FractionTest#testReciprocal
>	org.apache.commons.math.fraction.FractionTest#testEpsilonLimitConstructor
>	org.apache.commons.math.fraction.FractionTest#testGetReducedFraction
>	org.apache.commons.math.fraction.FractionTest#testConstructorDouble
>	org.apache.commons.math.fraction.FractionTest#testCompareTo
>	org.apache.commons.math.fraction.FractionTest#testDoubleConstructor
>	org.apache.commons.math.fraction.FractionTest#testLongValue
>	org.apache.commons.math.fraction.FractionTest#testDigitLimitConstructor
>	org.apache.commons.math.fraction.FractionTest#testIntValue
>	org.apache.commons.math.fraction.FractionTest#testDivide
>	org.apache.commons.math.fraction.FractionTest#testMultiply
>	org.apache.commons.math.fraction.FractionTest#testEqualsAndHashCode
>	org.apache.commons.math.fraction.FractionTest#testNegate
>	org.apache.commons.math.fraction.FractionTest#testGoldenRatio
>	org.apache.commons.math.fraction.FractionTest#testIntegerOverflow
>	org.apache.commons.math.fraction.FractionTest#testDoubleValue
>	org.apache.commons.math.fraction.FractionTest#testConstructor
>	org.apache.commons.math.optimization.MultiDirectionalTest#testCostExceptions
>	org.apache.commons.math.optimization.MultiDirectionalTest#testRosenbrock
>	org.apache.commons.math.optimization.MultiDirectionalTest#testPowell
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatImproperNegative
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatImproper
>	org.apache.commons.math.fraction.FractionFormatTest#testParseProper
>	org.apache.commons.math.fraction.FractionFormatTest#testParseProperNegative
>	org.apache.commons.math.fraction.FractionFormatTest#testParse
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatZero
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatNegative
>	org.apache.commons.math.fraction.FractionFormatTest#testParseInteger
>	org.apache.commons.math.fraction.FractionFormatTest#testFormat
>	org.apache.commons.math.fraction.FractionFormatTest#testParseNegative
>	org.apache.commons.math.analysis.BrentSolverTest#testRootEndpoints

## Human Patch 

```Java
diff --git a/org/apache/commons/math/analysis/BrentSolver.java b/org/apache/commons/math/analysis/BrentSolver.java
index 57f64a9..01a9ee5 100644
--- a/org/apache/commons/math/analysis/BrentSolver.java
+++ b/org/apache/commons/math/analysis/BrentSolver.java
@@ -128,41 +128,20 @@ public class BrentSolver extends UnivariateRealSolverImpl {
         clearResult();
         verifyInterval(min, max);
         
-        double ret = Double.NaN;
-        
         double yMin = f.value(min);
         double yMax = f.value(max);
         
         // Verify bracketing
-        double sign = yMin * yMax;
-        if (sign > 0) {
-            // check if either value is close to a zero
-            if (Math.abs(yMin) <= functionValueAccuracy) {
-                setResult(min, 0);
-                ret = min;
-            } else if (Math.abs(yMax) <= functionValueAccuracy) {
-                setResult(max, 0);
-                ret = max;
-            } else {
-                // neither value is close to zero and min and max do not bracket root.
-                throw new IllegalArgumentException
-                ("Function values at endpoints do not have different signs." +
-                        "  Endpoints: [" + min + "," + max + "]" + 
-                        "  Values: [" + yMin + "," + yMax + "]");
-            }
-        } else if (sign < 0){
-            // solve using only the first endpoint as initial guess
-            ret = solve(min, yMin, max, yMax, min, yMin);
-        } else {
-            // either min or max is a root
-            if (yMin == 0.0) {
-                ret = min;
-            } else {
-                ret = max;
-            }
+        if (yMin * yMax >= 0) {
+            throw new IllegalArgumentException
+            ("Function values at endpoints do not have different signs." +
+                    "  Endpoints: [" + min + "," + max + "]" + 
+                    "  Values: [" + yMin + "," + yMax + "]");       
         }
 
-        return ret;
+        // solve using only the first endpoint as initial guess
+        return solve(min, yMin, max, yMax, min, yMin);
+
     }
         
     /**

```

## NopolPC 

org.apache.commons.math.analysis.BrentSolver:136 (Suspicious rank: ample 924, jaccard 68, ochiai 68, naish1 6894, gp13 68, naish2 68, tarantula 68, )
```Java
min <= 1
```

Nb Angelic value: 1

Nb analyzed Statement: 68

Execution time: 0:00:31.820000

Grid5000 node: graphene-80.nancy.grid5000.fr

## NopolC 

org.apache.commons.math.analysis.BrentSolver:135 (Suspicious rank: ample 6982, jaccard 87, ochiai 90, naish1 6893, gp13 87, naish2 87, tarantula 87, )
```Java
((min <= 0) || (min == 1)) && ((yMin * yMax) >= 0)
```

Nb Angelic value: 1

Nb analyzed Statement: 86

Execution time: 0:00:49.504000

Grid5000 node: graphene-79.nancy.grid5000.fr

## BrutpolPC 

org.apache.commons.math.analysis.BrentSolver:136 (Suspicious rank: ample 924, jaccard 68, ochiai 68, naish1 6894, gp13 68, naish2 68, tarantula 68, )
```Java
min == 1
```

Nb Angelic value: 1

Nb analyzed Statement: 68

Execution time: 0:01:35.191000

Grid5000 node: graphene-40.nancy.grid5000.fr

## BrutpolC 

org.apache.commons.math.analysis.BrentSolver:135 (Suspicious rank: ample 6982, jaccard 87, ochiai 90, naish1 6893, gp13 87, naish2 87, tarantula 87, )
```Java
(max - yMin) <= yMin
```

Nb Angelic value: 1

Nb analyzed Statement: 86

Execution time: 0:01:53.521000

Grid5000 node: griffon-59.nancy.grid5000.fr

# Math 99

Nb Executed tests: 1180

Nb Failing tests: 35

>	org.apache.commons.math.fraction.FractionTest#testFloatValue
>	org.apache.commons.math.fraction.FractionTest#testAbs
>	org.apache.commons.math.fraction.FractionTest#testAdd
>	org.apache.commons.math.fraction.FractionTest#testSubtract
>	org.apache.commons.math.fraction.FractionTest#testReciprocal
>	org.apache.commons.math.fraction.FractionTest#testEpsilonLimitConstructor
>	org.apache.commons.math.fraction.FractionTest#testGetReducedFraction
>	org.apache.commons.math.fraction.FractionTest#testConstructorDouble
>	org.apache.commons.math.fraction.FractionTest#testCompareTo
>	org.apache.commons.math.fraction.FractionTest#testDoubleConstructor
>	org.apache.commons.math.fraction.FractionTest#testLongValue
>	org.apache.commons.math.fraction.FractionTest#testDigitLimitConstructor
>	org.apache.commons.math.fraction.FractionTest#testIntValue
>	org.apache.commons.math.fraction.FractionTest#testDivide
>	org.apache.commons.math.fraction.FractionTest#testMultiply
>	org.apache.commons.math.fraction.FractionTest#testEqualsAndHashCode
>	org.apache.commons.math.fraction.FractionTest#testNegate
>	org.apache.commons.math.fraction.FractionTest#testGoldenRatio
>	org.apache.commons.math.fraction.FractionTest#testIntegerOverflow
>	org.apache.commons.math.fraction.FractionTest#testDoubleValue
>	org.apache.commons.math.fraction.FractionTest#testConstructor
>	org.apache.commons.math.optimization.MultiDirectionalTest#testCostExceptions
>	org.apache.commons.math.optimization.MultiDirectionalTest#testRosenbrock
>	org.apache.commons.math.optimization.MultiDirectionalTest#testPowell
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatImproperNegative
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatImproper
>	org.apache.commons.math.fraction.FractionFormatTest#testParseProper
>	org.apache.commons.math.fraction.FractionFormatTest#testParseProperNegative
>	org.apache.commons.math.fraction.FractionFormatTest#testParse
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatZero
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatNegative
>	org.apache.commons.math.fraction.FractionFormatTest#testParseInteger
>	org.apache.commons.math.fraction.FractionFormatTest#testFormat
>	org.apache.commons.math.fraction.FractionFormatTest#testParseNegative
>	org.apache.commons.math.analysis.BrentSolverTest#testRootEndpoints

## Human Patch 

```Java
diff --git a/org/apache/commons/math/analysis/BrentSolver.java b/org/apache/commons/math/analysis/BrentSolver.java
index da8b3f5..01a9ee5 100644
--- a/org/apache/commons/math/analysis/BrentSolver.java
+++ b/org/apache/commons/math/analysis/BrentSolver.java
@@ -128,41 +128,20 @@ public class BrentSolver extends UnivariateRealSolverImpl {
         clearResult();
         verifyInterval(min, max);
         
-        double ret = Double.NaN;
-        
         double yMin = f.value(min);
         double yMax = f.value(max);
         
         // Verify bracketing
-        double sign = yMin * yMax;
-        if (sign > 0) {
-            // check if either value is close to a zero
-            if (Math.abs(yMin) <= functionValueAccuracy) {
-                setResult(min, 0);
-                ret = min;
-            } else if (Math.abs(yMax) <= functionValueAccuracy) {
-                setResult(max, 0);
-                ret = max;
-            } else {
-                // neither value is close to zero and min and max do not bracket root.
-                throw new IllegalArgumentException
-                ("Function values at endpoints do not have different signs." +
-                        "  Endpoints: [" + min + "," + max + "]" + 
-                        "  Values: [" + yMin + "," + yMax + "]");
-            }
-        } else if (sign < 0){
-            // solve using only the first endpoint as initial guess
-            ret = solve(min, yMin, max, yMax, min, yMin);
-        } else {
-            // either min or max is a root
-            if (yMin == 0.0) {
-                ret = min;
-            } else {
-                ret = max;
-            }
+        if (yMin * yMax >= 0) {
+            throw new IllegalArgumentException
+            ("Function values at endpoints do not have different signs." +
+                    "  Endpoints: [" + min + "," + max + "]" + 
+                    "  Values: [" + yMin + "," + yMax + "]");       
         }
 
-        return ret;
+        // solve using only the first endpoint as initial guess
+        return solve(min, yMin, max, yMax, min, yMin);
+
     }
         
     /**

```

## NopolPC 

org.apache.commons.math.analysis.BrentSolver:136 (Suspicious rank: ample 861, jaccard 68, ochiai 68, naish1 7155, gp13 68, naish2 68, tarantula 68, )
```Java
min <= 1
```

Nb Angelic value: 1

Nb analyzed Statement: 68

Execution time: 0:00:32.066000

Grid5000 node: graphene-99.nancy.grid5000.fr

## NopolC 

org.apache.commons.math.analysis.BrentSolver:135 (Suspicious rank: ample 5982, jaccard 88, ochiai 90, naish1 7186, gp13 88, naish2 88, tarantula 88, )
```Java
((yMin * yMax) >= 0) && (min <= 1)
```

Nb Angelic value: 1

Nb analyzed Statement: 86

Execution time: 0:00:55.209000

Grid5000 node: graphene-81.nancy.grid5000.fr

## BrutpolPC 

org.apache.commons.math.analysis.BrentSolver:136 (Suspicious rank: ample 861, jaccard 68, ochiai 68, naish1 7155, gp13 68, naish2 68, tarantula 68, )
```Java
min == 1
```

Nb Angelic value: 1

Nb analyzed Statement: 68

Execution time: 0:01:40.724000

Grid5000 node: griffon-1.nancy.grid5000.fr

## BrutpolC 

org.apache.commons.math.analysis.BrentSolver:135 (Suspicious rank: ample 5982, jaccard 88, ochiai 90, naish1 7186, gp13 88, naish2 88, tarantula 88, )
```Java
(max - yMin) <= yMin
```

Nb Angelic value: 1

Nb analyzed Statement: 86

Execution time: 0:01:53.439000

Grid5000 node: griffon-74.nancy.grid5000.fr

# Math 104

Nb Executed tests: 1003

Nb Failing tests: 29

>	org.apache.commons.math.fraction.FractionTest#testFloatValue
>	org.apache.commons.math.fraction.FractionTest#testAbs
>	org.apache.commons.math.fraction.FractionTest#testAdd
>	org.apache.commons.math.fraction.FractionTest#testSubtract
>	org.apache.commons.math.fraction.FractionTest#testReciprocal
>	org.apache.commons.math.fraction.FractionTest#testGetReducedFraction
>	org.apache.commons.math.fraction.FractionTest#testConstructorDouble
>	org.apache.commons.math.fraction.FractionTest#testCompareTo
>	org.apache.commons.math.fraction.FractionTest#testLongValue
>	org.apache.commons.math.fraction.FractionTest#testIntValue
>	org.apache.commons.math.fraction.FractionTest#testDivide
>	org.apache.commons.math.fraction.FractionTest#testMultiply
>	org.apache.commons.math.fraction.FractionTest#testEqualsAndHashCode
>	org.apache.commons.math.fraction.FractionTest#testNegate
>	org.apache.commons.math.fraction.FractionTest#testDoubleValue
>	org.apache.commons.math.fraction.FractionTest#testConstructor
>	org.apache.commons.math.optimization.MultiDirectionalTest#testRosenbrock
>	org.apache.commons.math.optimization.MultiDirectionalTest#testPowell
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatImproperNegative
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatImproper
>	org.apache.commons.math.fraction.FractionFormatTest#testParseProper
>	org.apache.commons.math.fraction.FractionFormatTest#testParseProperNegative
>	org.apache.commons.math.fraction.FractionFormatTest#testParse
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatZero
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatNegative
>	org.apache.commons.math.fraction.FractionFormatTest#testParseInteger
>	org.apache.commons.math.fraction.FractionFormatTest#testFormat
>	org.apache.commons.math.fraction.FractionFormatTest#testParseNegative
>	org.apache.commons.math.special.GammaTest#testRegularizedGammaPositivePositive

## Human Patch 

```Java
diff --git a/org/apache/commons/math/special/Beta.java b/org/apache/commons/math/special/Beta.java
index 904e156..4239c25 100644
--- a/org/apache/commons/math/special/Beta.java
+++ b/org/apache/commons/math/special/Beta.java
@@ -33,7 +33,7 @@ public class Beta implements Serializable {
     private static final long serialVersionUID = -3833485397404128220L;
 
     /** Maximum allowed numerical error. */
-    private static final double DEFAULT_EPSILON = 10e-15;
+    private static final double DEFAULT_EPSILON = 10e-9;
 
     /**
      * Default constructor.  Prohibit instantiation.
diff --git a/org/apache/commons/math/special/Gamma.java b/org/apache/commons/math/special/Gamma.java
index ba2c4db..8c565cb 100644
--- a/org/apache/commons/math/special/Gamma.java
+++ b/org/apache/commons/math/special/Gamma.java
@@ -34,7 +34,7 @@ public class Gamma implements Serializable {
     private static final long serialVersionUID = -6587513359895466954L;
 
     /** Maximum allowed numerical error. */
-    private static final double DEFAULT_EPSILON = 10e-15;
+    private static final double DEFAULT_EPSILON = 10e-9;
 
     /** Lanczos coefficients */
     private static double[] lanczos =

```

## NopolC 

org.apache.commons.math.special.Gamma:162 (Suspicious rank: ample 3683, jaccard 88, ochiai 88, naish1 6243, gp13 88, naish2 88, tarantula 88, )
```Java
((a == 1) || ((a >= 1.0) && (x > a))) && (org.apache.commons.math.special.Gamma.HALF_LOG_2_PI <= x)
```

Nb Angelic value: 1

Nb analyzed Statement: 88

Execution time: 0:20:51.552000

Grid5000 node: graphene-87.nancy.grid5000.fr

# Math 105

Nb Executed tests: 887

Nb Failing tests: 27

>	org.apache.commons.math.fraction.FractionTest#testFloatValue
>	org.apache.commons.math.fraction.FractionTest#testAbs
>	org.apache.commons.math.fraction.FractionTest#testAdd
>	org.apache.commons.math.fraction.FractionTest#testSubtract
>	org.apache.commons.math.fraction.FractionTest#testReciprocal
>	org.apache.commons.math.fraction.FractionTest#testGetReducedFraction
>	org.apache.commons.math.fraction.FractionTest#testConstructorDouble
>	org.apache.commons.math.fraction.FractionTest#testCompareTo
>	org.apache.commons.math.fraction.FractionTest#testLongValue
>	org.apache.commons.math.fraction.FractionTest#testIntValue
>	org.apache.commons.math.fraction.FractionTest#testDivide
>	org.apache.commons.math.fraction.FractionTest#testMultiply
>	org.apache.commons.math.fraction.FractionTest#testEqualsAndHashCode
>	org.apache.commons.math.fraction.FractionTest#testNegate
>	org.apache.commons.math.fraction.FractionTest#testDoubleValue
>	org.apache.commons.math.fraction.FractionTest#testConstructor
>	org.apache.commons.math.stat.regression.SimpleRegressionTest#testSSENonNegative
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatImproperNegative
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatImproper
>	org.apache.commons.math.fraction.FractionFormatTest#testParseProper
>	org.apache.commons.math.fraction.FractionFormatTest#testParseProperNegative
>	org.apache.commons.math.fraction.FractionFormatTest#testParse
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatZero
>	org.apache.commons.math.fraction.FractionFormatTest#testFormatNegative
>	org.apache.commons.math.fraction.FractionFormatTest#testParseInteger
>	org.apache.commons.math.fraction.FractionFormatTest#testFormat
>	org.apache.commons.math.fraction.FractionFormatTest#testParseNegative

## Human Patch 

```Java
diff --git a/org/apache/commons/math/stat/regression/SimpleRegression.java b/org/apache/commons/math/stat/regression/SimpleRegression.java
index d9fa592..c105a41 100644
--- a/org/apache/commons/math/stat/regression/SimpleRegression.java
+++ b/org/apache/commons/math/stat/regression/SimpleRegression.java
@@ -261,7 +246,7 @@ public class SimpleRegression implements Serializable {
      * @return sum of squared errors associated with the regression model
      */
     public double getSumSquaredErrors() {
-        return Math.max(0d, sumYY - sumXY * sumXY / sumXX);
+        return sumYY - sumXY * sumXY / sumXX;
     }
 
     /**

```

## NopolPC 

org.apache.commons.math.stat.regression.SimpleRegression:108 (Suspicious rank: ample 562, jaccard 79, ochiai 70, naish1 4336, gp13 79, naish2 79, tarantula 79, )
```Java
(org.apache.commons.math.stat.regression.SimpleRegression.this.xbar <= 1) || ((y < x) && (y < x))
```

Nb Angelic value: 4

Nb analyzed Statement: 80

Execution time: 0:04:00.684000

Grid5000 node: graphene-64.nancy.grid5000.fr

## BrutpolPC 

org.apache.commons.math.stat.regression.SimpleRegression:116 (Suspicious rank: ample 557, jaccard 74, ochiai 77, naish1 4327, gp13 74, naish2 74, tarantula 74, )
```Java
dy <= this.getRegressionSumSquares(x)
```

Nb Angelic value: 1

Nb analyzed Statement: 73

Execution time: 0:01:47.626000

Grid5000 node: griffon-5.nancy.grid5000.fr

# Time 4

Nb Executed tests: 12047

Nb Failing tests: 4

>	org.joda.time.TestPartial_Basics#testWith3
>	org.joda.time.TestPartial_Basics#testWith3
>	org.joda.time.TestPartial_Basics#testWith3
>	junit.framework.TestSuite$1#warning

## Human Patch 

```Java
diff --git a/org/joda/time/Partial.java b/org/joda/time/Partial.java
index 8e8e603..aaf0a0f 100644
--- a/org/joda/time/Partial.java
+++ b/org/joda/time/Partial.java
@@ -459,9 +459,8 @@ public final class Partial
             newValues[i] = value;
             System.arraycopy(iTypes, i, newTypes, i + 1, newTypes.length - i - 1);
             System.arraycopy(iValues, i, newValues, i + 1, newValues.length - i - 1);
-            // use public constructor to ensure full validation
-            // this isn't overly efficient, but is safe
-            Partial newPartial = new Partial(newTypes, newValues, iChronology);
+            
+            Partial newPartial = new Partial(iChronology, newTypes, newValues);
             iChronology.validate(newPartial, newValues);
             return newPartial;
         }

```

## Genprog 

org.joda.time.field.ZeroIsMaxDateTimeField:138 (Suspicious rank: ample 1, jaccard 1, ochiai 2, naish1 10426, gp13 1, naish2 1, tarantula 1, )
REPLACE
```Java
return (getWrappedField().getMaximumValue()) + 1
```

Grid5000 node: graphene-77.nancy.grid5000.fr

## Kali 

org.joda.time.field.ZeroIsMaxDateTimeField:178 (Suspicious rank: ample 3, jaccard 3, ochiai 3, naish1 10438, gp13 3, naish2 3, tarantula 3, )
INSERT_BEFORE
```Java
if (true)
	return 0;

```

Grid5000 node: graphene-108.nancy.grid5000.fr

# Time 7

Nb Executed tests: 11945

Nb Failing tests: 7

>	org.joda.time.format.TestDateTimeFormatter#testParseInto_monthDay_feb29_newYork_startOfYear
>	org.joda.time.format.TestDateTimeFormatter#testParseInto_monthDay_feb29_tokyo_endOfYear
>	junit.framework.TestSuite$1#warning
>	org.joda.time.format.TestDateTimeFormatter#testParseInto_monthDay_feb29_newYork_startOfYear
>	org.joda.time.format.TestDateTimeFormatter#testParseInto_monthDay_feb29_tokyo_endOfYear
>	org.joda.time.format.TestDateTimeFormatter#testParseInto_monthDay_feb29_newYork_startOfYear
>	org.joda.time.format.TestDateTimeFormatter#testParseInto_monthDay_feb29_tokyo_endOfYear

## Human Patch 

```Java
diff --git a/org/joda/time/format/DateTimeFormatter.java b/org/joda/time/format/DateTimeFormatter.java
index 913d036..553b035 100644
--- a/org/joda/time/format/DateTimeFormatter.java
+++ b/org/joda/time/format/DateTimeFormatter.java
@@ -705,12 +703,11 @@ public class DateTimeFormatter {
         
         long instantMillis = instant.getMillis();
         Chronology chrono = instant.getChronology();
-        int defaultYear = DateTimeUtils.getChronology(chrono).year().get(instantMillis);
         long instantLocal = instantMillis + chrono.getZone().getOffset(instantMillis);
         chrono = selectChronology(chrono);
         
         DateTimeParserBucket bucket = new DateTimeParserBucket(
-            instantLocal, chrono, iLocale, iPivotYear, defaultYear);
+            instantLocal, chrono, iLocale, iPivotYear, chrono.year().get(instantLocal));
         int newPos = parser.parseInto(bucket, text, position);
         instant.setMillis(bucket.computeMillis(false, text));
         if (iOffsetParsed && bucket.getOffsetInteger() != null) {

```

## BrutpolPC 

org.joda.time.format.DateTimeParserBucket:359 (Suspicious rank: ample 19, jaccard 19, ochiai 19, naish1 10152, gp13 19, naish2 19, tarantula 19, )
```Java
resetFields
```

Nb Angelic value: 1

Nb analyzed Statement: 18

Execution time: 0:02:06.621000

Grid5000 node: graphene-108.nancy.grid5000.fr

# Time 11

Nb Executed tests: 11852

Nb Failing tests: 4

>	org.joda.time.tz.TestCompiler#testDateTimeZoneBuilder
>	org.joda.time.tz.TestCompiler#testDateTimeZoneBuilder
>	junit.framework.TestSuite$1#warning
>	org.joda.time.tz.TestCompiler#testDateTimeZoneBuilder

## Human Patch 

```Java
diff --git a/org/joda/time/tz/ZoneInfoCompiler.java b/org/joda/time/tz/ZoneInfoCompiler.java
index 64da5ea..6efe071 100644
--- a/org/joda/time/tz/ZoneInfoCompiler.java
+++ b/org/joda/time/tz/ZoneInfoCompiler.java
@@ -65,11 +65,10 @@ public class ZoneInfoCompiler {
 
     static Chronology cLenientISO;
 
-    static ThreadLocal<Boolean> cVerbose = new ThreadLocal<Boolean>() {
-        protected Boolean initialValue() {
-            return Boolean.FALSE;
-        }
-    };
+    static ThreadLocal<Boolean> cVerbose = new ThreadLocal<Boolean>();
+    static {
+        cVerbose.set(Boolean.FALSE);
+    }
 
     /**
      * Gets a flag indicating that verbose logging is required.

```

## NopolPC 

org.joda.time.tz.DateTimeZoneBuilder:372 (Suspicious rank: ample 108, jaccard 108, ochiai 110, naish1 10249, gp13 108, naish2 108, tarantula 108, )
```Java
!((ruleSetCount <= 1) && ((tailZone!=null) || (outputID)))
```

Nb Angelic value: 3

Nb analyzed Statement: 25

Execution time: 0:02:46.620000

Grid5000 node: graphene-41.nancy.grid5000.fr

## NopolC 

org.joda.time.tz.DateTimeZoneBuilder:371 (Suspicious rank: ample 109, jaccard 109, ochiai 109, naish1 10250, gp13 109, naish2 109, tarantula 109, )
```Java
((tailZone == null) && (i == (ruleSetCount - 1))) && ((!(outputID)) || (0 < (ruleSetCount - 1)))
```

Nb Angelic value: 2

Nb analyzed Statement: 26

Execution time: 0:04:42.370000

Grid5000 node: graphene-26.nancy.grid5000.fr

## BrutpolPC 

org.joda.time.tz.DateTimeZoneBuilder:372 (Suspicious rank: ample 108, jaccard 108, ochiai 110, naish1 10249, gp13 108, naish2 108, tarantula 108, )
```Java
transitions.contains(this)
```

Nb Angelic value: 1

Nb analyzed Statement: 25

Execution time: 0:02:16.360000

Grid5000 node: graphene-112.nancy.grid5000.fr

## BrutpolC 

org.joda.time.tz.DateTimeZoneBuilder:309 (Suspicious rank: ample 49, jaccard 49, ochiai 99, naish1 10021, gp13 49, naish2 49, tarantula 49, )
```Java
0 != nameKey.length()
```

Nb Angelic value: 3

Nb analyzed Statement: 36

Execution time: 0:10:11.057000

Grid5000 node: griffon-29.nancy.grid5000.fr

## Genprog 

org.joda.time.tz.DateTimeZoneBuilder:1460
DELETE
```Java
remove
```

Grid5000 node: graphene-7.nancy.grid5000.fr

## Kali 

org.joda.time.tz.DateTimeZoneBuilder:1460
DELETE
```Java
remove
```

org.joda.time.tz.DateTimeZoneBuilder:1460
REPLACE
```Java
if (true) {
	java.lang.System.out.println(("Fixing duplicate recurrent name key - " + (tailZone.iStartRecurrence.getNameKey())));
} 
```

org.joda.time.tz.DateTimeZoneBuilder:1460
REPLACE
```Java
if (false) {
	java.lang.System.out.println(("Fixing duplicate recurrent name key - " + (tailZone.iStartRecurrence.getNameKey())));
} 
```

org.joda.time.tz.ZoneInfoCompiler:78 (Suspicious rank: ample 6, jaccard 6, ochiai 6, naish1 9931, gp13 6, naish2 6, tarantula 6, )
INSERT_BEFORE
```Java
if (true)
	return false;

```

org.joda.time.tz.DateTimeZoneBuilder:1154
DELETE
```Java
remove
```

org.joda.time.tz.DateTimeZoneBuilder:1154
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.joda.time.tz.DateTimeZoneBuilder:1458
DELETE
```Java
remove
```

org.joda.time.tz.DateTimeZoneBuilder:1458
REPLACE
```Java
if (false) {
	if (org.joda.time.tz.ZoneInfoCompiler.verbose()) {
		java.lang.System.out.println(("Fixing duplicate recurrent name key - " + (tailZone.iStartRecurrence.getNameKey())));
	} 
	if ((tailZone.iStartRecurrence.getSaveMillis()) > 0) {
		tailZone = new org.joda.time.tz.DateTimeZoneBuilder.DSTZone(tailZone.getID() , tailZone.iStandardOffset , tailZone.iStartRecurrence.renameAppend("-Summer") , tailZone.iEndRecurrence);
	} else {
		tailZone = new org.joda.time.tz.DateTimeZoneBuilder.DSTZone(tailZone.getID() , tailZone.iStandardOffset , tailZone.iStartRecurrence , tailZone.iEndRecurrence.renameAppend("-Summer"));
	}
} 
```

org.joda.time.tz.DateTimeZoneBuilder:827
INSERT_BEFORE
```Java
if (true)
	return 0;

```

org.joda.time.tz.DateTimeZoneBuilder:1141
DELETE
```Java
remove
```

org.joda.time.tz.DateTimeZoneBuilder:1141
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.joda.time.tz.DateTimeZoneBuilder:1141
REPLACE
```Java
if (false) {
	org.joda.time.tz.DateTimeZoneBuilder.Rule startRule = iRules.get(0);
	org.joda.time.tz.DateTimeZoneBuilder.Rule endRule = iRules.get(1);
	if (((startRule.getToYear()) == (java.lang.Integer.MAX_VALUE)) && ((endRule.getToYear()) == (java.lang.Integer.MAX_VALUE))) {
		return new org.joda.time.tz.DateTimeZoneBuilder.DSTZone(id , iStandardOffset , startRule.iRecurrence , endRule.iRecurrence);
	} 
} 
```

org.joda.time.tz.DateTimeZoneBuilder:1142
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.joda.time.tz.DateTimeZoneBuilder:1143
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.joda.time.tz.DateTimeZoneBuilder:1144
DELETE
```Java
remove
```

org.joda.time.tz.DateTimeZoneBuilder:1144
INSERT_BEFORE
```Java
if (true)
	return null;

```

org.joda.time.tz.DateTimeZoneBuilder:1144
REPLACE
```Java
if (false) {
	return new org.joda.time.tz.DateTimeZoneBuilder.DSTZone(id , iStandardOffset , startRule.iRecurrence , endRule.iRecurrence);
} 
```

org.joda.time.tz.DateTimeZoneBuilder:1457
DELETE
```Java
remove
```

org.joda.time.tz.DateTimeZoneBuilder:1457
REPLACE
```Java
if (false) {
	if (tailZone.iStartRecurrence.getNameKey().equals(tailZone.iEndRecurrence.getNameKey())) {
		if (org.joda.time.tz.ZoneInfoCompiler.verbose()) {
			java.lang.System.out.println(("Fixing duplicate recurrent name key - " + (tailZone.iStartRecurrence.getNameKey())));
		} 
		if ((tailZone.iStartRecurrence.getSaveMillis()) > 0) {
			tailZone = new org.joda.time.tz.DateTimeZoneBuilder.DSTZone(tailZone.getID() , tailZone.iStandardOffset , tailZone.iStartRecurrence.renameAppend("-Summer") , tailZone.iEndRecurrence);
		} else {
			tailZone = new org.joda.time.tz.DateTimeZoneBuilder.DSTZone(tailZone.getID() , tailZone.iStandardOffset , tailZone.iStartRecurrence , tailZone.iEndRecurrence.renameAppend("-Summer"));
		}
	} 
} 
```

org.joda.time.tz.DateTimeZoneBuilder:371 (Suspicious rank: ample 109, jaccard 109, ochiai 109, naish1 10250, gp13 109, naish2 109, tarantula 109, )
DELETE
```Java
remove
```

org.joda.time.tz.DateTimeZoneBuilder:371 (Suspicious rank: ample 109, jaccard 109, ochiai 109, naish1 10250, gp13 109, naish2 109, tarantula 109, )
REPLACE
```Java
if (false) {
	tailZone = rs.buildTailZone(id);
} 
```

org.joda.time.tz.DateTimeZoneBuilder:372 (Suspicious rank: ample 108, jaccard 108, ochiai 110, naish1 10249, gp13 108, naish2 108, tarantula 108, )
DELETE
```Java
remove
```

Grid5000 node: graphene-115.nancy.grid5000.fr

