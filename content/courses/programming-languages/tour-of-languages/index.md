+++
title = "Tour of langauges"
slide = true
+++

# A tour of programming languages

[!](highlight)

> We will examine the influence of TM and LC on the design of programming languages.

# Stateful languages

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

# More on functions

[!](columns 3:)

*In modern languages*, functions can be values and can be constructed and passed around like values.

[!](split)

```{javascript sm}
var log = function(message) {
    console.info("Message: " + message);
}
```

[!](note) Function as value in Javascript.

```{go sm}
var log = func(msg string) {
    fmt.Println("Message:" + msg)
}
```

[!](note) Function as value in Go.

```{scala sm}
val log = {msg : String => println(msg)}
```

[!](note) Function as value in Scala.

# Expression vs Statement

```c
printf("hello world\n")
```

[!](note) This is a *statement*.  It is *invalid* to ask the value of a statement.  It's meant to do something, not represent something.

```c
get_age() > 65
```

[!](note) This is an *expression*. It doesn't (necessarily) do anything, but it represents a value of some type.  In this case, it's a boolean expression.


# Branching

```javascript
var discount = 0;
if(age < 10)
  discount = 0.4;
else if(age >= 65)
  discount = 0.2;
else
  discount = 0;
```

[!](note) Javascript branching with `if-else`.  C and Java have the same style of `if-else`.
Here `if-else` is an statement.  What it does is the assignment of some variable `discount`.

```scala
val discount = if(age < 10) 0.4
               else if(age >= 65) 0.2
               else 0
```

[!](note) In *Scala*, everything is an expression.  It represents the value of `discount`.

```scala
val discount = age match {
    case _ if age < 10 => 0.4
    case _ if age >= 65 => 0.2
    case _ => 0
}
```

[!](note) Scala supports *pattern matching*.


# Iteration

[!](columns 3:)

Possibly the most used and thought-out feature of procedural programming.

[!](split)

~~~{c sm}
for(int i=0; i < 100; i++)
  for(int j=0; j < 100; j++)
    if(i + j == 55) printf("%d, %d\n", i, j)
~~~

[!](note) `for` loop in C/Java/Javascript.  <i class="fa fa-thumbs-down"></i>

~~~{python sm}
for i in range(100):
  for j in range(100):
    if i + j == 55:  print i,j
~~~

[!](note) `for` loop in Python

~~~{python sm}
print [(i,j) for i in range(100) \
    for j in range(100) if i + j == 55]
~~~

[!](note) List comprehension in Python


# Scope

[!](columns 3:)

The scope of a variable is context in which the variable exists.  This will be discussed in depth later.

Scoping is not part of the syntax, but rules on variable life-time.

[!](split)

~~~{c sm}
int i = 0;
if(i == 0) {
    int i = 10;
    printf("%d", i);
}
printf("%d\n", i)
~~~

[!](note) C will print out `10 0`.  Note that there are *two* variables, both with the name `i`.

~~~{javascript sm}
function friendlyLogger() {
    var greeting = "Hi there, ";
    return function(message) {
        console.info(greeting + message);
    }
}

...

var logger = friendlyLogger();
logger("my name is Einstein.");
~~~

[!](note) For Javascript, scopes are nested, and the parent scope (`friendlyLogger`) is preserved in the scope of `function(message)`.  This is called _closure_.

# Functional languages

[!](highlight)

# Functional languages

**Principles of LC**

- No such thing as memory or mutable data

- Purely symbolic rewrites

- Functions are necessarily expressions, and most (actually *all*) expressions are functions.

- Totally unsupported by any computer hardware

# Functional languages

**LC influence on programming language design**

- Symbols

- Functions are *cheap* to create

- Functions are used *everywhere*

- Read-only semantics for data

# Functional languages

**Extensions to beyond LC**

- Functions as data
- Symbol binding
- Scopes
- Evaluate function application eagerly or lazily
- Data structures (especially Lists)
- *Native* functions which are implemented by imperative programming
- Organization of code through namespaces, polymorphism and object orientation.
- [!](comfort)

[!](box) We will illustrate these topics using <span style=color:red>**Clojure**</span>.

# Syntax: from LC to Lisp

[!](columns 4:)

LC is so syntactically clean that Lisp (and its dialets including Clojure) has borrowed the LC syntax almost verbatim.

[!](split)

## Abstraction
---

$\lambda x.e$

>[!](note 6)
>
> ~~~clojure
> (fn [x] e)
> ~~~

## Application
---

$f e$

>[!](note 6)
>
> ~~~clojure
> (f e)
> ~~~

# Functions as data

```clojure
(defn log [message]
  (println message))
```

[!](note) Declaring a function with a _name_.

```clojure
(fn [message] (println message))
```

[!](note) Creating a value which happens to be a function.  This function has no name, so we call such functions _anonymous functions_.

```clojure
#(println %1)
```

[!](note) A quicker way to create a function without a name.

# Name binding

```clojure
(def pi 3.1415)
```

[!](note) Global name binding

```clojure
(def log (fn [message]
           (println message)))
```

[!](note) This is another way to create a named function.

```clojure
(let [name "Einstein"]
  (println name))
```

[!](note) The `let` form helps to create name bindings with limited scopes.

# Immutable data

[!](columns 4:)

Data can only be:

- created
- bind to a name
- cloned

[!](---)

But never modified.

[!](split)

```clojure
(def x [1 2 3 4])
```
[!](note) Create a list of numbers, and bind it a name `x`.

```clojure
(conj x 5)
```
[!](note) This makes a copy of `x` and append 5.  But since it's not bound to any name, the result is lost.

```clojure
(def y (concat x [10 20 30]))
```
[!](note) `x` is still `[1,2,3,4]` (forever), and `y` is `[1,2,3,4,10,20,30]`

# Summary

[!](highlight)

- The influence of TM to imperative language design

- The influence of LC to functional language design

