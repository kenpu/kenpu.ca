+++
slide = true
title = "Clojure Language"
+++

# Clojure: Part II

[!](highlight)

# Data in Clojure

$\mathbf{D}$(`clojure`) = a sequence of (nested) _data_

```clojure
(1 2 3)
("abc" "def")
["abc" ("def" 1 2 3)]
```

[!](&&&)

Let's explore the definitions of _data_.

# Data in Clojure

Atoms

> - Numbers: 3.1415, 100, `2/3`, 100N, 3.1415M
> - Strings: `"hello world"`
> - Characters: `\a \b \c`
> - Symbols: `name`, `π`
> - Keywords: `:name`
> - Nil value: `nil`

# Lists

> ```
( ... )
```

Lists are _linked lists_.

- They are super efficient for prepend and append at the ends of the lists.
- But they are not efficient for random access.

# Lists

*Important*

- Clojure, by default, interpretates lists as function invocations.
- A list that is _just a list_ needs to be quoted.

[!](&&&&&)


```clojure
(println "hello" "world")
```

[!](note) This is a function invocation.

```clojure
(quote (println "hello" "world"))
```

[!](note) This is a list of three elements.

```clojure
'(println "hello" "world")
```

[!](note) This is the preferred way of quoting a list.



# Vectors

> ~~~
[ ... ]
~~~

Vectors are _arrays_.

- They are efficient for random access.
- But they are more costly for insertion in the middle and possibly at the ends.

# Hash-maps

> ~~~
{ <key> <value> <key> <value> ... }
~~~

Hash-map are _hash maps_ :)

- They are efficient for key look-up, but
- they are potential memory intensive.

# Hash-maps

Idiomatic Clojure prefers to use _keywords_ as keys.


> - It makes the code readable.
> 
> - Keyword lookup is also more efficient than strings.
>
> [!](note) 

```clojure
{:name   "Ken Pu"
 :office "UA4041"
 :role   :instructor}
```

# Sets

> ~~~
#{ ... }
~~~

Duplicates are *not* allowed.  Order doesn't matter.

> ~~~
(= #{3 2 1} #{1 2 3}) ; true
~~~

# An example

```{clojure sm}
{:type "a relational database"
 :name "csci3055u assignments"
 :tuples [ {:name "assignment 1"
            :due-date ("October" 21 2016)
            :url "http://..."}

           {:name "assignment 2"
            :due-date ("November" 20 2016)
            :url "http://..."}

           {:name "assignment 3"
            :due-date ("December" 6 2016)
            :url nil}
         ]
}
```
[!](note) A data value that describes a relational table.

# Functional Programming in Clojure

[!](highlight)

This is really important.

- Don't worry about the syntax.

- Focus on the _way_ of read-only data.

# Functional Programming in Clojure

_Data_ is (almost always) _immutable_.

**Example**:

[!](columns 6:)

Consider data:

```{clojure sm clipboard}
{:name "Albert Einstein"
 :profession "Patent Clerk"
 :age 24
 :publication ["Relativity"
               "Speed of light"]}
```

[!](split)

How can we update the `:profession` field, or age?

> - We cannot.
> - Clojure only supports convenient ways for us to 
>   to create a copy of the data with a modified `:profession`
>   field.

# Preview of what's to come...

```{clojure sm clipboard}
(def person {:name "Albert Einstein"
             :profession "Patent Clerk"
             :age 24
             :publication ["Relativity"]})
```

```{clojure sm clipboard}
(assoc person :profession "Physicist")
```

> [!](note 5)
> This does not change the person (as it cannot be changed - **ever**).
> Instead, `(assoc ...)` creates a new clone with the delta change of setting
> `:profession` being `Physicist`.

```{clojure sm clipboard}
(update person :age inc)
```

> [!](note 5)
> This makes a copy of `person`, with the change of incremental `:age` by **one**.

# Functional programming

- [!](comfort)

- Don't worry about "waste" of memory (for now).

- If you need to change data,

 	> Make a copy of the data, but with the change applied.
 	>
 	> No procedures, only functions.

- Functional programming has many benefits...


# Programs in Clojure

[!](highlight)

# Function invocations

General form:

~~~
( <fn> <arg> ... )
~~~

Examples:

```{clojure sm}
(list 1 2 3)
; (1 2 3)
```

[!](note) `list` constructs a list consisting of its arguments.

```{clojure sm}
(vector 1 2 3)
; [1 2 3]
```

[!](note) `vector` is like `list`, but returns a vector.

```{clojure sm}
(range 10)
; (0 1 2 3 4 5 6 7 8 9)
```

[!](note) Returns a list of a sequence of number.

# Function invocation - aka function application

We are going to meet our first _higher order_ function: `apply`.

```clojure
(apply <func> <arg-list>)
```

is equivalent to:

```
(<func> <arg> <arg> ...)
```

# Function declaration

```clojure
(defn f [args...] body)
```

[!](note) Binding a function to a symbol as in the global scope.

---

```clojure
(fn [args ...] body)
```

[!](note) Creating an anonymous function.

---

```clojure
#( ... )
```

[!](note) Creating an anonymous function.  In the local scope, the input arguments are bound to the symbols `%1`, `%2`, etc.  If there is only one argument, then it's bound to `%`.

# Function declaration

Recommended way:

```clojure
(defn add [x y]
  (+ x y))
```

More indirect, but still quite readable:

```clojure
(def add
  (fn [x y] (+ x y)))
```

Not recommended for this:

```clojure
(def add #(+ %1 %2))
```

[!](note) Irresponsible show-off of deep knowledge of Clojure syntax can quickly turn into unreadable spaghetti code.

# More on function declarations: variadic arguments

A function can have multiple versions:

```clojure
(defn f
  ([arg] body)
  ([arg arg] body)
  ([arg arg arg] body))
```

A function can also have non-deterministic number of arguments, and bind all the arguments in an array.

```clojure
(defn f [arg arg & args] body)
```

[!](note) In the scope of `body`, the symbol `args` is bound to a list consisting of the third, fourth, fifth arguments, and so on.

# Branching

> ```clojure
(if <cond> <expr> <expr>)
```

Example:

```clojure
(defn larger [x y]
  (if (< x y) y x))
```

```clojure
(defn largest [& xs]
  (if (= (count xs) 1)
    (first xs)
    (larger (first xs) (apply largest (rest xs)))))
```

# Branching: case by case

> ```clojure
(cond
  <cond> <expr>
  <cond> <expr>
  ...
  :else <expr>)
```

Example:

```clojure
(defn compare [x y]
  (cond
    (< x y) -1
    (> x y) 1
    :else   0))
```

# DO block

> ```clojure
(do expr
    expr
    ...
    expr)
```

Evaluates every expression in the `(do ...)` form.  The `(do ...)` form
evaluates to the last expression.

Example:

```{clojure sm}
(def x (do (println "Hello there.")
           (+ 1 2 3)))
; 6
```


# Iteration: a first look

> ```clojure
(for [i expr] body)
```

1. `expr` must evaluate to a sequence of elements.
2. `i` is the symbol that exists in the scope of `body`.  It is bound to elements in `expr` during each iteration.
3. At each iteration `body` is evaluated.
- [!](comfort)

**Note**:

> `(for ...)` is an expression.  It is evaluated to a _lazy_ sequence, consisting of elements of each evaluation of `body`.

# For-loop

Example:

```clojure
(for [i (range 10)]
  (str "Hi, this is the " i "th iteration."))
```

# For-loop super charged

```clojure
(for [sym seq-expr :when cond :while cond] body)
```

- `:when cond` causes the `for` iteration to evaluate `body` only when the
  condition is true.

- `:while cond` causes the `for` iteration to terminate when the conditon
  becomes false.

_Example_:

```{clojure sm clipboard}
(for [x (range 100)
      y (range 100)
      :when (= (+ x y) 42)]
  (println x y))
```

# More iterations:

> ```clojure
(doseq [i expr] body)
```

It is very similar to `(for [i expr] body)`, but it's non-functional.

`(doseq ...)` iterates over `expr`, and evaluates `body` for each iteration.

[!](box) But the result of each evaluation is **THROWN AWAY**...

# More iterations

> ```clojure
(dotimes [i n] body)
```

This is equivalent to:

> ```clojure
(doseq [i (range n)] body)
```


# Summary

[!](highlight)

- Data in Clojure
- Functions
- Branch
- Iteration

---

Things to come:

1. Data structural transformations
2. Sequences and lazy evaluation
3. Looping through recursion
