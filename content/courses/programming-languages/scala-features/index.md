+++
slide = true
title = "More features of Scala"
+++

# Matching

```{scala template}
__expression__ match {
case __pattern__ => ...
case __pattern__ => ...
    ...
}
```

This generalizes `if-else if- ...else` completely.

# ____________

Consider

```scala
val num:Int = ...
val message = if(num == 0) 
                    "zero"
                else if(num > 10) 
                    "greater than 10"
                else
                    "other cases"
```

It can be nicely expressed as:

```scala
val num:Int = ...

val message = num match {
case 0           => "zero"
case x if x > 10 => "greater than 10"
case _           => "other cases"
}
```

# ____________________

Patterns used in `match` case clauses can be very powerful.

```scala
val x: List[Int] = ...

expr match {
  case Nil         => println("empty list")
  case List(1,2,3) => println("ready, set, go")
  case List(0, _*) => println("Starts with zero")
  case head::tail  => println(s"First element is ${head}, 
                              | followed by ${tail}")
}
```

# ______________________

Destructuring with match:

```scala
val point: Tuple[Float, Float] = (3.14, 8)

point match {
  case (x, y) => println(s"First coordinate is ${x}")
}
```

# ________________________

Guarded patterns

```scala
point match {
  case (x, y) if x > 0 and y > 0 => {
    println("Point is in the first quadrant.")
  }
  case (x, y) => println(s"${x} or ${y} is negative.")
}
```

# ________________________

Matching against types

If `obj` is a symbol of type `T`, then we know that the data `obj` is bound to
must be an instance of `T` or any of its subtypes.

`match` patterns can be used to examine which subtype an object is bound to.

```scala
val names: Iterable[String] = Set("Jack", "John", "Joe")

val type = names match {
             case x:List[String] => "list"
             case x:Set[String] => "set"
             case _ => "some other iterable"
           }
```
