+++
slide = true
title = "Clojure: the language"
+++

# Clojure: the language

[!](highlight)

- Life cycle of Lisp code
- Raw basics
- Syntactic sugars

# Review of Lisp

- A program is a (nested) list.

- Not all lists are valid programs.  Only certain type of lists can be interpreted as programs.

	- Valid: `(+ 1 2 (* 3 5))`

	- Invalid: `(1 2 +)`

- Sometimes the validity of a list depends on the dialect of Lisp:

	- `(defun add (a b) (+ a b))`

		> Valid for _Common Lisp_, but not _Racket_.

	- `(define (add a b) (+ a b))`

		> Valid for _Racket_, but not _Common Lisp_.

# Lifecycle of lists in Lisp

The unified representation of programs using a data structure that programs can manipulate, Lisp has a uniquely self-referencial nature that makes it exceedingly powerful (and intellectually challenging).

[!](box) <i style=font-size:200%;vertical-align:middle class="fa fa-bolt"></i> Lisp rewrites itself, and it *grows* by itself.

# Two-phase compilation

![pre-expanded](lisp-pre-expand.jpg)

[!](note 3) During expansion, functions, known as _macros_, evaluate certain fragments in the program.  These fragments are the extensions to the language.

# Two-phase compilation

[!](columns 7:)	

![post-expanded](lisp-post-expand.jpg)

[!](split note)

The macro functions converts the entire nested list to a valid Lisp program.

```{lisp sm}
(... (macro (quote (... invalid-list ...))))
```

gets evaluated to:

```{lisp sm}
(... (... valid-list ...))

```

# Core Clojure

[!](highlight)

- List-only core syntax (low-level and verbose)
- (Sensible) syntactic extensions
- Tons of macros

# Clojure

**Definition:** (Atoms)

> An _atom_ is a value that can be an element of a list.

[!](*******)

Let's go through the different atoms of the core-clojure langauge.

# Numbers

| Numbers | Example |
|-------------|----------|
| Long numbers | `3.1415` |
| Ratio        | `1/3`    |
| BigInt       | 10000N   |
| BigDecimal   | 3.1415M  |

# Strings

Simple strings:

```
"Hello world."
``` 

```
"I say \"Hello\" to the world"
```

Multiline string:

```clojure
"Hello,
This is a big world of long
sentences."
```

## Character

```
\a
```

# Keywords

Keywords are a staple of Clojure programs.  They are quick and efficient way to create _constants_.
They are similar to the Java `enum` values.

[!](columns 8:)

Keywords have the same rule as variable names (aka _symbols_), except they must start with `:`.

```
:red
:blue
:green
```

or

```
:big-red-apple
:blue-sky
:important-field!
```

[!](split note)

Later, we will introduce namespaces.  Like symbols, keywords can be specialized by a namespace.

# Symbols

Symbols are variables which are labels referring to some data or function.

> [!](note) It's natural to think of Clojure symbols as variables.  But Clojure can do *more* with its symbols than other languages can do with variables.

Clojure has some very relaxed rules in naming symbols:

```{clojure sm}
a                 ; looks like a variable.
*a*               ; can have (almost) any characters except whitespaces
int->float        ; good names can be extremely satisfying
java.lang/Integer ; a symbol that has a namespace "java.lang", and name "Integer"
```

# More about symbols

*Var* s are symbols which represent other expressions

~~~{nosyntax}
a => 42
~~~

(Almost) each time a *var* appears, it is evaluated to its expression.

**Other languages**

In other programming languages, one can *only* access the expression referred by variables.

**Lisp**

In Lisp, we can (and need) to access (and create) the variable *itself* using Lisp.

~~~{clojure sm}
(var a)
~~~

# Beyond parentheses in Clojure

Clojure uses other brackets to improve the parentheses overload.

[!](columns 6:)

```lisp
(let ((a 10)
      (b 20))
  (+ a b))
```

[!](note) Common Lisp

[!](split)

```clojure
(let [a 10
      b 20]
  (+ a b))
```

[!](note) Clojure

# Lambda Calculus in Clojure


We will focus on the core Clojure - which is a Turing-complete implementation of Lambda Calculus.

[!](***)

- [!](comfort)
- Function application
- Function abstraction
- Symbol binding

# Function application

~~~clojure
(f <arg> <arg> ...)
~~~

Example:

```clojure
(+ 1 2 3 4)
(/ (+ 1 2 3 4) 4.0)
```

# Function Abstraction

~~~{clojure}
(fn <alias?> [ <args> ] <body>)
~~~

Example:

```{clojure}
(fn [a b] (/ (+ a b) 2))
```

[!](note) Computing the average of two numbers.

```clojure
(fn factorial [n]
  (if (< n 2) n (* n (factorial (dec n)))))
```

[!](note) Recursion function that uses an alias `factorial` for itself.  The alias is only valid in the body of the `fn` defintion.

# Symbol binding

Symbols are just names, and they can be used to represent anything, such as:

1. expressions
2. functions
3. variables
4. lists (or programs)

---

**Definition**: _Symbols Binding_

> When we associate a symbol to something else, the *association* is called a _binding_.

