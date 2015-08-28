This informal document presents the manual analysis of patches synthesized with automatic repair.

# [Chart 1](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#chart-1) 

## Problem

The bug is located in an if condition for checking whether a variable ```dataset``` is null. In that case, a statement ```return null``` avoids processing a null dataset. However, the bug in the condition produces that the condition expression is true when dataset is not null, skipping processing the dataset.
The test suite never exercises the case when ```dataset``` is true.

## Human Fix:
The developer changes the if condition: the fix now check if the variable is true.

## jGenProg
jGenProg removes the if condition and/or removes the return statement (Both are semantically equivalent). As the test never exercises the case when dataset is null, this jGenProg’s fix has the same behavior than that one from the human patch. However, if the dataset is null (never tested by the test suite) it would produce a NPE when, after the if, the variable dataset be referenced.

## jKali 
jKali produces several patches (remember it has 3 operators). Some are equivalent to that one from GenProg. Another semantically equivalent, replaces the if condition per 'false'. Again, it the dataset is null, the execution will fail.

## Correctness
Incorrect


# [Chart 3](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#chart-3)

## Problem

The failing test creates an instance of object ```TimeSeries```, then it creates one copy of it using  method ‘createCopy’. Finally it asserts whether the original object is equal to the copy, which fails.


## Human Fix
In the createCopy method, for copying of an object, the developer creates an new instance, then he copies the values using ```add``` method, e.g, copy.add()
The patch initializes some fields e.g., ```copy.minY = Double.NaN;```, before initialize the object.


## jGenProg 

jGenProg adds a method invocation to findBoundsByIteration() in the mentioned add method.
findBoundsByIteration() contains the same initialization that the developer has written as fix, and additional code that does not have collateral effects.

## Correctness
Unknown. It could be correct, but the test case does not assert those collateral effects.


## Nopol
Nopol changes an if condition inside method removeAgedItems(), of which its then branch contains a method call to the mentioned findBoundsByIteration().
In the test cases, the condition always is true so, it always initializes the initialized fields.

## Correctness
It seems incorrect, due the under-specification of test which assert removeAgedItems().

# [Chart 5](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#chart-5)

## Problem
An exception is thrown when the program aims at adding an element in position -1 of a list of size 1.

## Human Patch
In human patch, if the field allowDuplicateXValues, the tuple (X, Y) is directly added (at the end of the list)  and the execution of the method is stopped with a return null.


## jKali
It changes an if condition to false. The else branch always adds at element at the end of the list (The then branch tries to add an element at position `index', which in the test case execution takes the value -1). 

## jGenProg
it replaces the mentioned if per the statement that adds an element at the end of the list. As consequence, is equivalent to jKali patch.



## Nopol patch
Nopol replaces an if condition by !allowDuplicateXValues and in the else block the tuple (X, Y) is added the execution of the method continue and return null at the end.
The behavior of the method is not changed because, if changed ```if``` is a portion which is prefixed by a condition which protect the behavior of the method.


# [Chart 6](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#chart-6)

## Problem
Problems to compare two object of type ShapeList. When the elements of two list are the same, the method equals returns false.

## Human
The developer change the implementation of ShapeList equals method. Now, it compares each Shape of the lists using a specific comparator . Before, the parent's equals was used. 

## jGenProg
jGenProg modifies the method ```set(int index, Object object)```, which is used to add elements to the ShapeList. The added line empties the list before add a new element (```java.util.Arrays.fill(this.objects, null))```). The test cases uses two lists for asserting this method. As the last element of both lists are 'null', then it compares two lists with a single ```null``` elements, which returns true.

## Correctness
Incorrect. The test suite does not assert the set element correctly.


# [Chart 7](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#chart-7)

## Problem

The method ```getMaxMiddleIndex()``` does not work well. The result is different than that one expected by the test. 

## Human Fix
The developer has used wrong fields in the process of calculating the bounds of a period. 
This calculus modifies the field maxMiddleIndex, which is asserted in the test cases.

## GenProg
In the getter method of the mentioned field maxMiddleIndex, jGenProg replace the return statement by a return taken from other getter (i.e., the return now involves another variable). By change, this variable contains the value expected by the test cases, so, that produce the failing test cases now passes.

## Correctness
Incorrect


# [Chart 9](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#chart-9) 

## Problem

The buggy method is a method used to update a range of a structure. If the end index of the interval is smaller than the start index, the interval was considered as correct

## Human patch

The human fix checks if the end index is smaller than the start index then the result is empty.

## jGenProg

jGenProg replaces an return statement by another. Even all test pass with that replacement, it is not a correct patch.

## Nopol patch

Nopol generates a patch which does not impact the passing test cases but 
disable a line for all failing test cases. Nopol manages to create a condition that match only the failing test cases that was possible because all failing test cases use a specific amount of data.

## Correctness

Incorrect

# [Chart 13](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#chart-13)

## Problem

The application throws an exception when in a range, a lower value is greater than the upper value.
The buggy statement contains an instantiation of a range which may contain a negative value in upper.

## Human patch

The human patch checks the issue value if the value is negative, the program uses 0 instead of the negative value. 

## Nopol patch

The Nopol patch  adds a precondition before the code that initializes a wrong range (with a lower value greater than the upper). The condition of this if is always false. So, it avoids the execution of the buggy code.

## jKali
Similar to Nopol, jKali patch removes the code that initializes a wrong range.

## jGenProg
The mentioned code that  initialized the range is located inside a if block (then branch). 
The condition of this if checks whether variable leftBlock is not null.
jGenProg adds an assignment that assigns null to that variable. 
This statement is executed before the if, as result, the buggy code is not executed.


## Correctness

Incorrect all patches.


# [Chart 15](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#chart-15)

## Problem
To draw a plot, a variable ```dataset``` from must be not null. The test case exercises one scenario that the variable is null. An exception is thrown.

## Human Fix
Add a precondition to check the variable is not null. The developer adds code for initializing the dataset in case it is null.

## Kali
Kali removes the statement that draws the plot or adds a return statement before this statement that avoid executing the rest of the method's code. 
As consequence, the dataset variable is never accessed. The test cases only asserts whether an exception was thrown, but it does not verify the correctness of the results.

## GenProg
It replaces the statement that draws the plot by a method invocation which does not produce collateral defect. As consequence, this patch is equivalent to removing the mentioned draw statement.

## Correctness 
Incorrect. The test is under specified.


# [Chart 17](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#chart-17)

## Problem

The clone method does not return a perfect clone of the current object.

## Human patch

The human patch uses the clone method of its parent and uses an utility class to copy the other specific data (a list of objects).

## Nopol patch

Nopol adds a precondition or change the condition before an exception. The precondition or the condition are false only for the failing test cases.

## Correctness

Incorrect

# [Chart 21](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#chart-21)

## Problem

Unknown

## Human patch

The human patch adds a precondition over a major part of the buggy method and create a new method which used to update data.

## Nopol patch

I don't understand the Nopol patch because the generated precondition is complex and the Nopol patch does not apply on the same file as human patch.

## Correctness

Probably incorrect

# [Chart 25](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#chart-25) 

## Problem

The buggy method may throws NullPointerException.

## Human patch

The human patch adds tree not null checks.

## NopolPC patch

The precondition Nopol patch adds a precondition always false before the call of the buggy method

## NopolC patch

Unknown but does not change the same file as human patch.

## jGenProg parch
jGenProg removes an method invocation that setup an object data. The mentioned null pointer exception came from the manipulation of data taken from this object. The suppression produces any exception is thrown.
The jGenProg patch produces that the failing test cases now passes due to this test only asserts the presence of exception.
The patch is not correct due to the test does not assert the functionality and, as we suspect, the patch breaks it.

## jKali patches
jKali patches skip executing code adding return statements. As the case of jGenProg patch, the patches are accepted due to the test suite is under specified.


## Correctness

Incorrect

# [Chart 26](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#chart-26)

## Problem
When the method ``draw'' from a chart is call, a Null pointer exception is thrown when the plot owner is null. For drawing the top axes of a chart, it uses information form owner.

## Human Patch
Adds a if condition to check if the owner is not null. 

## Nopol patch

## jKali
jKali adds a return statement in method ``draw'' before  drawing (i.e. executing the logic method).
The test cases only assert the presence of exceptions, but not the correct behavior of the method.

## Correctness
Incorrect. Test under-specified.

## Nopol
It adds a precondition -this is always false- before the addition of elements in the top axes of the chart.
As result, the chart never has element in the top axes, avoiding drawing it (and by consequence the exception)

## Correctness
Incorrect. Test under-specified.


# [Lang 39](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#lang-39)

## Problem
Null pointer exception when an element of the array is null.

## Human Patch
The loop over the array continue if the element is null.

## Nopol patch
Nopol adds precondition which is false for the failing assert before the statement that produces the null pointer exception.

## Correctness

Incorrect


# [Lang 44](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#lang-44)

## Human patch
The human patch adds a check at the beginning of the method which parses a String to a number (String to int, long, float or double). The string can end with a ```l``` , ```f``` or a ```d``` in order to specify the expected type. If the string only contains the char ```l``` which specifies the type ```long``` the method returns 0 instead of throws an exception, the others types are already correctly handled.

The patch written by the developer throws an exception if the string contains only one char and this char is not a digit.

## NopolC patch
The patch generated by Nopol adds a precondition before the method call which parses the string to a long. The method is only executed when the length of the string is bigger than 1. If the condition is not respected the program continues and throws the expected exception.

## Correctness

Correct


# [Lang 46](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#lang-46)

The human patch adds a parameter to the method, this parameter (```escapeForwardSlash```) is used to determine if the method has to escape the forward slashes. The method has also an other parameter (```escapeSingleQuotes```) which is used to determine if the method has to escape simple quotes.

In the test cases, the action of escaping forward slashes is always correlated to the action of escaping simple quotes. 
The generated patches is thus a precondition before the line which escapes forward slashes with ```escapeSingleQuotes``` as condition.

## Correctness

Incorrect


# [Lang 51](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#lang-51)

The buggy method is an utility method which parse a string (no, on, yes, true, false) and returns a boolean. The method contains a switch on the length of the string to parse (```switch(str.length())```). If the string contains 3 characters (```case 3```), the method checks if the string begin with 'y' if this condition is not respected then the next case is executed. The human fix consists to add a ```return false``` after the if condition. Inside the condition the method compare the two others characters to 'e' and 's'.  

## NopolC patch
The generated patch replaces the condition by a condition that are always true in this context (```str != null```). With this patches, the method returns true for each string of 3 characters which ends by ```"es"```. None test is written to test this scenario.

## Correctness

Incorrect

# [Lang 53](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#lang-53)

## Problem

We do not have the expertise the understand the problem.

## Human patch 

The human patch moves two if outside an if. Inside the if the variable ```done``` is assigned to ```true```.

## Nopol patch

We think that this patch is incorrect because there is not relational between the Nopol patch and the human patch.

## Correctness

Incorrect

# [Lang 55](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#lang-55)

## Problem

An assignment has to be done only in certain conditions.

## Human patch 

The human adds a precondition before the assignment.

## Nopol patch

Nopol generates a precondition before the buggy assignment. The generated precondition is equivalent to the human patch.

## Correctness

Correct

# [Lang 58](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#lang-58)

The buggy method which parses a string to a number throws an exception when one integer is followed by ```l```. The ```l``` is used to specify the expected type of the output (```l``` for long, ```f```: float, ```d```: double, none: integer).

## Human patch 

The human fixes the condition which invalidates the string ```1l```.

## NopolPC patch

Precondition Nopol  adds an always false precondition before the exception.

## NopolC patch

Condition Nopol simplifies the condition, remove the buggy part, and relies on checks available in called methods.

## Correctness

NopolPC: Incorrect, NopolP: Correct



# [Math 2](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-2)

## Problem

The bug is exposed through an failing assertion.

## Human patch 

The fix changes a mathematical formula from method ```getNumericalMean``` by including parenthesis for prioritizing the multiplication operation over a division.

## jGenProg/Kali patch

jGenProg and Kali fixes modify another method w.r.t. the human fix location.
The patch removes an assignment statement that modifies the variable called ```upper```. 
The output value of this method depends on this variable.
The removed statements modifies ```upper``` using in the right part of the assignment the output of the (buggy) method ```getNumericalMean```.
Removing the assignment means the result of the buggy method does not affect other statements.

## Correctness

Not correct.
The test cases is quite simple for determining whether the patch is correct or not.

# [Math 5](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-5)

## Problem
In class Complex, the reciprocal function had a bug: for zero value, the function returned zero. 
The test cases asserts this behavior expecting an infinite value.

## Human
The developer replaces the statement ```return 0``` per ```return infinite```.

## jGenProg
Idem to human patch.

## Correctness
Correct.



# [Math 8](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-8)
```Java
public T[] sample(int sampleSize) 
throws NotStrictlyPositiveException {
//## Human patch 

 
//public Object[] sample(int sampleSize) 
//throws NotStrictlyPositiveException { 
  if (sampleSize <= 0) {
    throw new NotStrictlyPositiveException([...]);
  }
  //Human patch 

 final Object[] out = new Object[sampleSize];
  final T[]out = 
  (T[]) Array.newInstance(singletons.get(0).getClass(), sampleSize);

  for (int i = 0; i < sampleSize; i++) {
    out[i] = sample();//The KALI FIX REMOVES THE LINE
  }
  return out;
}
```
Code snippet of Bug Math-8. The manually-written patch is shown in the ```Human FIX``` comment at Line 2 (change of method declaration) and line 6 (Change variable type. The Fix proposed by Kali consists on removing line 11. 
    
    
Bug M8 fails to create an array of random sample from the discrete distribution.
The method sample from class ```DiscreteDistribution<T>``` receives the number of random values to generate (sampleSize parameter), and it returns an array of type ```T[]``` with that number of random values.
For carry out this functionality, the method first declares a variable  array of type ```T[]``` (line Y) and instantiates its using function Array.newInstance(Class<\?> componentType, int length)
Then it assigns a sample  value  (obtained through method DiscreteDistribution.sample() to each array position(line X).

The bug occurs when 
1. the first element is of type ```T1```, an sub-class of ```T``` (so, the array instance is of type ```T1```), 
and 
2. one of the samples is an object which is of type ```T2```, an sub-class of T, but not of type ```T1```.

In the Human fix the developer changes  the array's type in its declaration (from T to Object) and the way the array is instantiated.
The patch generated by Kali removes the statement which assigns samples to the array (and that also throws the exception).
As consequence, the result of method sample is an empty array.
The patch produces that the failing test case now passes.
The reason of this is case has only one assertion: it asserts the array size is equal to 1. 
The patch is not correct due the test cases never assert the content of the array.


## Correctness

Not valid.


# [Math 28](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-28)

## Problem
An exception is thrown when a counter exceeds to the maxNumberofIteraction.

## Human
The developer add two if statement before two `for' (He wrote: "to check if there's an artificial variable that can be forced out of the basis.").

## JGenProg
JGenProg removes an return statement which is located inside the mentioned for block.
As consequence, the execution of the `for' has not collateral changes.


## jKali
JKali replaces an if condition per true. The test is under specified.

## Correctness
Incorrect.


# [Math 32](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-32)

## Problem

## Human patch 

Add a not null check

## jKali
Replaces a if condition per false. That means force the else execution.
Incorrect due the test is under specified: the then branch of the modified if is not correctly tested.

## Nopol patch

Unknown


# [Math 33](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-33)

## Problem

A if condition contains a method call which uses an incorrect parameter

## Human patch 

Change the incorrect parameter

## Nopol patch

Nopol adds a precondition before the buggy statement. The condition of the precondition is ```true``` for the usual case but ```false``` for the failing assert.

## Correctness

Incorrect



# [Math 40](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-40)

## Problem

A loop  reaches the maximum number of iterations prefixed by the application.
When it happens, the application throws an exception.

## Human patch

The human fix modifies the right part of one variable's assignment. This variable is further used to exit the loop.

## jGenProg patch

jGenProg fix adds an assignment over another variable that also is used for breaking the loop execution.

## jKali patch

JKali changes the if condition to True. That means only the then branch is executed and the test cases never assert the else branch, so, it is under specified.

### Nopol patch

Nopol patch is semantically equivalent to jKali patch: It changes the if condition to one that given the test cases inputs,  the patched if condition is always true.

## Correctness

It seems invalid, the modified code is extremely complex from our knowledge.


# [Math 42](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-42)

## Problem

A case is not managed when a value is equals to 0 or null.

## Human patch 

Manages the case  when a value is equals to 0 or null.

## Nopol patch

Nopol adds a precondition before a ```return null``` in a method called by the buggy method. 
The value null is no more used in the buggy method, the bug no longer occurs in the tests suite.

## Summary

Nopol generates a patch that uses variables which are not use in its direct context. The patch is probably incorrect.

## Correctness

Unknown but probably incorrect.

# [Math 44](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-44)

## Problem


The bug is exposed through a failing assertion.

## Human patch 

Before a return statement of the method ```acceptStep``` (called inside loop block), 
the patch done by developers adds a method call that modifies the internal state of EventState instances.

## GenProg patch

Inside the mentioned ```acceptStep``` method, the fix changes a boolean field.
This changes forces the later execution of a code block similar to the human fix code (that is, it changes the internal state of instances) in later execution of ```acceptStep``` method (remember it is called inside a loop).

## Correctness

I do not know. I can be valid. The code is too complex.

# [Math 49](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-49)

## Problem

An exception occurs by trying to modify one vector structure (implemented similar to a map) which, at the same time, it is iterated.
Inside the method for multiplying vectors, an instance of this structure vector is created for store the results of the multiplication, and it is preloaded with one of the vector of the multiplication.
For multiply vectors, the method  iterates the result vector, so, when it tries to set the result there, the mentioned exception is thrown. 

## Human patch 

It changes the iterator:  the fix does not iterate the result vector but the term vector of the  multiplication.

## jGenProg/jKali/Nopol patches

The fix proposed by GenProg, Kali, Nopol removes one statement that increments a variable for counting the number of elements of the structure.
The iterator reads this variable to know whether the structure has changed while the iteration. If it changes, the iterator throws an exception.
As the fix removes the incrementation of this variable, the iterator does not realize that the structure receives modification and never throws that exception.


## Summary

The test case does not have any assertion.
So, it assures the not presence of the bug by a) invoking the failing method and b) waiting the exception does not occur. 
However, it does not assess the result of the vector multiplication.

## Correctness

Not valid.

# [Math 50](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-50)

## Problem

## Human patch

Remove a complete if condition

## GenProg/Kali patch

Remove one statement (assignment) from a if condition (that one removed by the human patch).

## Nopol

Nopol replaces a condition of  if by an always false condition.
The human patch removes the complete if condition

## Summary

Both human and jGenProg/jKali patches are the same and correct. 
The test has assertions to validate them.

## Correctness

jGenProg and jKali valid.

# [Math 53](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-53)

## Problem
A method produces wrong computation when it receives as argument a NaN (Not a number) value.

## Human fix 
He adds a precondition to check whether the argument is a Nan, and returns an appropriate value.

## GenProg fix
jGenProg generates the same fix that the developer.

## Correctness
Correct



# [Math 57](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-57)

## Problem

The multiplication of two integer may produce an integer overflow.

## Human patch

The human patch changes the type to double of the variable which contains the result of the multiplication.

## Nopol patch 

The Nopol patch changes the comportment of the ```equals``` method of an other class. With the patch, the method returns always true when the two objects are the same type and have the same length.

## Summary

The equals method is not tested

## Correctness

Incorrect

# [Math 58](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-58)

## Problem

bad parameter in a method call

## Human patch

The human patch removes one parameter of the method call.

## Nopol patch 

The Nopol patch is to complex to be understood. 

The execution path:
test -> buggy method -> call parent class -> call on parent class of an attribute ( constructor parameter) -> call the parent class of the parent class-> call children class -> call the auto fixed method (240 LOC)

## Correctness

Probably incorrect

# [Math 69](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-69)

## Problem

bad value in array assignment

## Human patch

The human patch changes the assignment value

## Summary

I don't see the link between the human fix method and the NopolPC fix method.

## Correctness

Unknown

# [Math 70](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-70)

## Problem

The application throws a Null pointer exception.

## Human/jGenProg patch

Both human and GenProg propose the same fix, that is, to replace a method invocation by a overloaded version.
The ```BisectionSolver``` has a field of type ```UnivariateRealFunction``` to operate inside the method ```solver```. 
The class has two constructors: one that receives an object of type ```UnivariateRealFunction``` (and set in the mentioned field), another without this kind of argument. 
The method solver also is overloaded: one receives a UnivariateRealFunction, the other no.  
The field UnivariateRealFunction is null when the constructor without that argument was called.
The fixes proposed to use the UnivariateRealFunction received as parameter instead of the class field.

## Correctness

jGenProg patch is valid.

# [Math 71](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-71)

## Problem
The manipulation of small values (as the developer wrote "much probably exactly 0" ) produces unexpected results. 

## Human patch
The developer sets up an artificial value. He commented: "we cannot simply truncate the step, reject the current computation and let the loop compute another state with the truncated step.it is so small (much probably exactly 0 due to limited accuracy) that the code above would fail handling it. So we set up an artificial 0 size step by copying states"

## jGenProg patch

The mentioned conflicted code has a precondition. jGenProg modifies the boolean method evaluated in that precondition. It adds one precondition that avoid executing the conflictive code.

## Nopol patch

Nopol modifies the comportment of a method that return a value which is use in the condition before the call of the buggy method.

## Correctness.
Unknown. An expert could determine whether the patch is valid or not.



# [Math 73](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-73)

## Problem

An assertion failing exposes the bug. 
The test case waits for an exception when it calls the method ```solve``` with two arguments that represent a "bad interval".

## Human patch 

It adds one if precondition before to check whether the arguments are invalid and, in that case, throws an exception.  
The precondition is added just before calling a overloaded version of ```solve``` method.

## jGenProg patch

Replace the call to 'solve' method by an overloaded version.
The fix method call has less parameters and in its body it has  a similar precondition than the humans fix.
As consequence, the method called by the fix is who detects the invalid arguments.

## jGenProg Correctness

Correct.


## Nopol patch

Nopol changes an if condition that validates that 3 values form a increasing sequence.  If that condition is false, it throws an exception.
The Nopol patch force to throw the exception. As test expects an exception, the patch do passing the test.

## Nopol Correctness 

Incorrect


# [Math 78](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-78)

##Human patch 

The human patch adds a if condition with a large code block inside method ```stepAccepted```.
There, it modifies tree fields and method's variables: ```ta```, ```ga```, and one field from object interpolator.


## jKali  and jGenProg patches
Regarding to jKali, it removes one assignment from a method ```evaluateStep```, that is executed before the mentioned method ```stepAccepted```. 
This statements modifies variable ```t0```. Then in  ```stepAccepted``` method, ```t0``` is assigned to ```ta```.


## Nopol patch

Nopol adds a precondition in method solver of class BrentSolver. The precondition affects the result returned by the method (it return a double). This method is called in the mentioned method ```evaluateStep``.



## Correctness


Human patch is larger than jGenProg and jKali patches (+10 lines vs 1 line).
This patch includes some precondition for detecting illegal states.
Unknown whether jGenProg and  jKali patches are valid.
The Nopol patch seems to be incorrect, the modified code is not equivalent to  


# [Math 80](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-80)

## Problem

Assertion failure.

## Human patch

The method ```flipIfWarranted``` flips an array as follows:
The array elements are grouped in rows, for instance, one row the first four elements, the second row the next 4 elements and so on.
The methods aims at flipping the elements inside a row.
The developers have changed the expression that represent the number of rows.

## jGenProg patch

jGenProg removes one of the assignments of the flip method.

## jKali patch

jKali removes most of the code for flipping.

## Nopol patch

The Nopol patch adds a precondition to avoid executing the flip code. This patch has the same effect than jKali's patch.  


## Correctness

Incorrect: jGenProg patches is wrong due to it alternates the array.

Unknown: jKali and Nopol do not modify the array at all. That means is not necessary to flip the array w.r.t. the executed tests.

# [Math 81](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-81)

## Problem

Array index out of bound exception.
The variable ```b2``` is modified with a value of an array element (The variable has a value before that assignment). The test cases exposes an illegal access.

## Human patch 

The developers updates the if conditions which block contains the mentioned assignment.
In the commit that includes the fix, the developer also includes other source code changes.

## jKali/jGenProg patch

It removes the assignment statements.

## Nopol patch

Add a precondition to avoid executing the assignment.

## Summary

The test cases seems to not identify the slightly variability in the variable's values due to the assignment removement.

## Correctness

Generated patches are  not corrects. 

# [Math 82](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-82)

## Problem

One test case exposes the bug through a failing assertion.

The class SimpleTableaux has one field that is a double matrix (array of two dimensions).
The method ```doIteration``` accesses to this matrix. For that, it calls two methods for obtaining the row and column indexes, respectively.

## Human patch 
 
It consists on changing a if condition from >= to > into the method for retrieving the row index.

## jKali/jGenProg/Nopol patch

jGP, jKali and Nopol modifies the value of the column index. 

## Summary

The automated generated patched version and the human patches generate  different indexes, but by coincidence, the double matrix has the same value on those indexes.

## Correctness

The generated patches are not valid.

# [Math 84](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-84)

## Problem

A test cases has two cases that expose a bug:
In one, an assert fails, in the other, it receives an exception.
In both cases, a while reaches the maximum number of iterations allowed. 

## Human patch

Human patch adds a condition the end of the while block for exit from the while .

## jGenProg patch

jGenProg's fix adds a return statement at the end of the while block. 
As consequence, the while iterates only one.

## jKali 

Same patch generated than jGenProg.

## Correctness

Incorrect.

# [Math 85](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-85)

## Problem

The test case receives an exception calling to a method.

## Human patch 

The developer changes an if condition by replacing the operator >= for >. The block of this condition throws the mentioned exception.
After the patch, given a set of input values defined in the test case, the if condition is never true, and the exception is never thrown.

## Nopol patch

Nopol adds a precondition before the buggy ```if``` condition, the precondition fix the bug of condition.
Nopol adds a precondition which look like this: ```if(a*b=!0)``` before a if like this```if(a*b>=0)```. This is equivalent to the human patch: ```if(a*b>0)```. But instead of use 0 the patch uses the variable ```lowerBound``` which is always ```0``` is this test context.

## jGenProg/jKali patch
jKali and jGenProg patches remove the mentioned if and/or the statement that throws the exception. As consequence, after enter to the if block, the execution remains. 

## Summary

The Generated patches are corrected for the test input, but incorrect for other cases not specific in the test cases. The test case does not include a case for evaluating the detection of a CoverageException.

# [Math 87](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-87)

## Human Patch
The human patch change the logic of the body of a for loop.

## Nopol patch

The Nopol patch adds a precondition before an assignment, which is not related to the human patch. The patch is probably incorrect.

## Correctness

Incorrect.

# [Math 88](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-88)

## Problem
The developer has done a complex patch. It removes one method and change another adding domain specific code.

## Nopol patch

Nopol patch adds a method precondition before a return statement.  The condition of this if uses variables not related with the method logic. As consequence, the patch is incorrect.

## Correctness

Incorrect.

# [Math 95](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-95)

A test case receives a IllegalArgumentException

## Human patch 

The developers modifies a method ``getInitialDomain'' for always returning positive double values.
A negative value causes an letter Illegal exception.

## jGenProg patch

jGenProg replaces the return statement of the method by a ``return numeratorDegreesOfFreedom```. During the test cases execution, numeratorDegreesOfFreedom variable is always positive.

## jKali
jKali add an return statement  ```return 0``` just before the return statement of the method by a ```return 0```.

## Summary

The test cases successfully assess the validity of the patched method.
The jGenProg and jKali patches' results (0.9750000000640364) is slightly different from the real patched result (0.9750000261341519), 
but the test case does not compare at a grade to detect those differences ```assertEquals(0.975, x, 1.0e-5);```
It seems that the test cases pass for every positive double returned by the method ``getInitialDomain''.


# [Math 97](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-97)

## Problem
The developer has done a complex patch. It changes the logic of the buggy method.


## Nopol patch
Nopol patch adds a precondition before an exception.
The condition of the precondition overfits the values used in the failing test case.


## Correctness

Incorrect.

# [Math 104](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-104)

## Problem
The number of allowed numerical error is too height

## Human patch
Reduces the constant value ```DEFAULT_EPSILON```

## Nopol patch

The Nopol patch is probably incorrect because it has no relation with the human patch, it applies on an other file.

## Correctness

Incorrect.


# [Math 105](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#math-105)

## Problem
The getSumSquaredErrors may return a negative number

## Human patch
The human patch adds ```return 0``` if the result of the method ```getSumSquaredErrors()``` is lower than 0.

## Nopol patch
The Nopol patch is probably incorrect because there is no direct relation between the patched line by Nopol and the line patched by the human patch.

## Correctness

Incorrect.

# [Time 4](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#time-4) Test Under specified

## Problem
The class Partial has two constructors with similar arguments (the difference is one receive an array, the other one instance). One of those constructors carries on some validations, throwing exceptions when it finds invalid data. The other constructor does not have the validation code.
The test case exercises the scenario of passing incorrect data, and expects the exception.

## Human Patch
The developer now uses the constructor with validations.

## jGenProg patch.
jGenProg changes the value of a return, that produces an exception is thrown.
As the test case expects an exception, it proceeds as the patch now recognized the incorrect data.

## jKali
JKali adds an return statement. Similarly to jGenProg patch, this change produces an exception, expected by the test case.

## Correctness
Incorrect.

# [Time 11](https://github.com/Spirals-Team/defects4j-repair/blob/master/results/2015-august/readme.md#time-11) Test Under specified

## Problem
Null pointer exception when it is executed method 'verbose' from ZoneInfoCompiler.

## Human  patch
The developer forces the the initialization of the thread that throws the exception.

## jGenProg and jKali
Both repair systems propose patches that remove or skip statements that call ```verbose``` method.

## Nopol patch 

Nopol adds an always false precondition before statement that calls the ```verbose``` method.

## Correctness
Incorrect.