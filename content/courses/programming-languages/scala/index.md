+++
slide = true
title = "Introduction to Scala"
+++

# Scala

- Java is a *simple* and *impure* object-oriented programming language.

- Scala

    - designed by _Martin Odersky_
    
    - first released in 2004
    
    - a *pure* object-oriented programming language

    - high degree of complexity

# Object-oriented programming (OOP)

>> All types are classes.

>> All data are objects.

>> All computation are method invocations.

# Java as an OOP

Type as class:

```java
class String {
    String substring(int start, int end) { ... }
}
```

Data as object:

```java
String message = "Hello world";
```

Computations as method invocations:

```java
System.out.println(message.substring(3, 6));
```

# Java as non-OOP

1. Types are not classes:

    > - `int`, `float`, etc. are not classes.
    >
    > - Try: `List<int> numbers;`

2. Data are not objects:

    > - `"Hello world".hashCode()` works because `"Hello world"` is an object,
    >    and all objects are with the method `int hashCode()`.
    >
    > - `123.hashCode()` fails.

3. Computation is not method invocation:

    > ```java
    i = 1 + 2
    ```
    The integer addition `+` is not a method.


# Scala

- Every type is a class.

```scala
List[Int]
Array[Float]
```
[!](note)
Parameteric types

- Everything is an object.

```scala
print(1.toBinaryString)
```
[!](note) Invoking a method of integer that accepts no arguments.

- All operators are methods.

```scala
1 + 2
1.+(2)
```
[!](note)
Addition `+` is a method of an integer `1`.


