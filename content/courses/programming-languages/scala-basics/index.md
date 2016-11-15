+++
slide = true
title = "Basics of Scala"
+++

# Basics of Scala

[!](highlight)

# Objects

```scala
var name : String = "hello"
```
[!](note)
This creates a **variable**, with the type `String`, and it's initialized to
"hello".

```scala
name.CharAt(0)
```
[!](note)
Java-style method invocation

# ______

Scala uses the same scoping and symbol bindings.

There are two types of _symbols_.

[!](columns 6:)

**Variables**

Bindings to `var` can be updated.

```{scala sm}
var name:String = "Albert"
name = "Einstein"
```

[!](split)

**Values**

Bindings to `val` is permanent.

```{scala sm}
val name : String = "Alert"
name = "Einstein"
// error: reassignment to val
//       x = "Einstein"
```

[!](box) This is the same as Clojure, and it's preferred over `var`.

# Type Inference

*Definition*:

> A statically typed language is one that requires the compiler to have complete
> type information on all the symbols in the source code **at** compile-time.

- Java **and** Scala are statically typed languages.
- Clojure and Python are not statically typed, but typed (at runtime).

[!](&&&)

The compiler needs type information specified for *all* the symbols.

```java
String name;
```

```scala
val name : String = ...
```

# ____

Scala has a feature, known as _type inference_.

> At compile-time, the compiler makes a best attempt to fill in the missing type
> information.

```scala
val small_integer = 42
```
[!](note) The compiler will see that `small_integer` should be `Int`.

```scala
var x = y
```
[!](note) The compiler will use the type of `y` to infer the type of `x`.

In the interactive interpreter session, you can always inspect the type
information of existing symbols:

```scala
:t small_integer
Int
```

# Procedural programming

## IF

```scala
if (<cond>) {
  <expression>
} else if (<cond>) {
  <expression>
} else {
  <expression>
}
```
[!](note)
The classic Java-style branching.  Scala has better pattern matching
which is preferred over if-else.

`if-else` is an expression, not a statement.

[!](columns 6:)

```{scala sm}
val age = 65
var senior:String = ""
if(age < 65) {
  senior = "Not senior"
} else {
  senior = "Senior"
}
```

[!](split)

```{scala sm}
val age = 65
val senior = if(age < 65) 
               "Not senior"
             else
               "Senior"
```

# _____

## FOR

```scala
for(<val> <- <iterable>) {
    ...
}
```

1. All container data structures are iterables: arrays, lists, map, ... 
2. Scala has a nice way to generate iterables over integer ranges:

    ```scala
    1 to 10     // 1, 2, ... 10
    1 until 10  // 1, 2, ... 9
    ```

```{scala sm}
for(x <- 1 to 10) {
  println(x)
}
```
[!](note)
Scala's `for` loop is much more powerful then simple iteration.  More on this
in lectures on programming with sequences.

# _____________

## Loops

```scala
while(<cond>) {
    ...
}
```

```scala
do {
    ...
} while(<cond>)
```

# Syntax rules

Suppose that an object has zero or one argument.

```
obj.method()
obj.method(arg)
```

Then the parenthesis can be omitted:

```
obj.method
obj.method arg
```

The dot can also be omitted:

```
obj method
obj method arg
```

# _____

Example:

```
1 + 2
```
[!](note) This is actually a method invocation in disguise.

```
1.+(2)
```
[!](note) The equivalent syntax in method invocation.  The method name is `+`,
the object is `1`, and the argument is `2`.

This type of syntax rule allows us to introduce user-defined operators to
support programming constructs such as:

```
x multiplyWith y
```
[!](note) We assume that the object `x` has a method called `multiplyWith`.

We can also invoke Java methods like operators 

```
"hello" charAt 3
```

# Syntax rules

More syntax rules to come.

# Functions

Functions are in fact objects of a _function_ class.  Scala offers a succinct
syntax for defining functions.

```{scala sm}
import scala.math
val area = {(count:Int, radius:Float) => x * scala.math.Pi * radius * radius}
```

```{scala sm clipboard}
val area : (Int, Float) => Double = {
  (count, radius) => {
    var total: Double = 0
    for(i <- 0 until count) {
        total += scala.math.Pi * radius * radius
    }
    total
  }
}
```
> - The type of the `val` is `(Int, Float) => Double`.  This is also known as
> the _function signature_.
> - The value is a function (instance of a class Function2).
> - The inputs are bound to symbols `count` and `radius`.
>   Note the binding types are inferred based on the function signature.
> [!](note)

# Summary

[!](highlight)

- Bindings

- Procedural programming

- Object method invocation

- Function as data


