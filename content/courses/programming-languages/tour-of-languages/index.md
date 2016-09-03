+++
title = "Tour of langauges"
slide = true
+++

# A tour of programming languages

[!](highlight)

# Stateful languages

Principles of a TM

- Memory:

    > the infinite tape

- Mutable data: 

    > cells of the tape stores data, which can be **modified**.
    
- Flow control:

    > control logic is an automaton which can branch and loop

# Stateful languages

[!](box)
Describing computation based on the principles of a TM s called _imperative_
programming.

- C / C++
- Java
- Ruby
- Python
- ...

# Stateful languages

| Elements of TM | Programming construct | Jargon |
|----------------|-----------------------|--------|
| Memory         | Array, struct         | Builtin aggregate types |
| Multable       | Assignments           | lvalues |
| Flow control   | if-else, while, for   | Branche and loops |

# Stateful languages

**Extensions to the TM**

They are necessary for humans to author and reason about the program.

- Variables: Give _names_ to represent specific memory addresses.

- Types: Give restruction to the type of data that can be stored in memory.

- Functions: Grouping of multiple statements in isolation.

- Scoping: Isolation of the usage of _names_ (for variables and functions).

- Code organization: Hierarchical management of large number of statements

[!](box) Procedural programming languages

# Variables (in procedural languages)

> Ultimately, _variables_ are names which are aliases for memory addresses.

[!](-----)


**Declaration**

```c
int i;
int[10] j;
```

**Read / Write**

```c
i = 10;
j[2] = i * j[0];
```
# Types

```c
typedef Point2D struct {
    float x;
    float y;
};
```

[!](note) This declares a struct aggregate type in C


```go
type Point2D struct {
    X float
    Y float
}
```
[!](note) Same structure in Go

```scala
class Point2D(val x:Float, val y:Float)
```

[!](note) Same structure in Scala



> We can build arbitrarily complex data structures using user-defined types.


# Functions

```c
Point2D rotate(Point2D p, float a) {
    Point2D p2;
    p2.x = p.x * cos(a) - p.y * sin(a);
    p2.y = p.x * sin(a) + p.y * cos(a);
    return p2;
}
```

[!](note 3) A function in C


```go
func rotate(p Point2D, a float) (p2 Point2D) {
    p2.X = p.X * math.Cos(a) - p.Y * math.Sin(a)
    p2.Y = p.X * math.Sin(a) + p.Y * math.Cos(a)
    return
}
```

[!](note 3) A function in Go. Note the name binding in the return type.

```scala
def rotate(p: Point2D, a : Float) : Point2D {
    val x = p.x * cos(a) - p.y * sin(a);
    val y = p.x * sin(a) + p.y * cos(a);
    Point2D(x, y)
}
```

[!](note 3) A function in Scala.  Note the `val` keyword, and the lack
of explicit return


