+++
slide = true
title = "From Lisp to Clojure"
+++

# From Lisp to Clojure

[!](highlight)

Lisp

> - Inspired by $\lambda$-Calculus
> - Hyper-productive syntax

Clojure

> - Extension to Lisp
> - Supports a slightly richer set of syntactic sugars for readability
> - Runs on JVM

# Lisp

- Invented by John McCarthy, 1958

- It's been the foundation of A.I. research ever since.

# Lisp

<img src="quote1.jpg"></img>

# Lisp

<img src="quote2.jpg"></img>

# Review of LC

[!](columns 6:)

## Abstraction

$\lambda x. e$

> Example:
>
>
> $\lambda x.\lambda y. x+y$ 
>
> $\lambda xy. x+y$ (with syntactic abbreviation)

[!](split)

## Application

$(e_1 e_2)$

> Example:
>
> $(((\lambda xy. x+y)\ 1)\ 2)$
>
> $((\lambda xy. x+y)\ 1\ 2)$ (abbreviation)

*Observation*:

Application is always a **list** of expressions.  The first expression is the function, and the rest of the list is arguments.


# Design of Lisp

LISP = <span style=color:red>LIS</span>t <span style=color:red>P</span>rocessing

- [!](comfort)
- Function applications are _lists_.
- Unless specified, lists are treated as function applications.

---

The entire language only needs one data structure: lists.

# Lisp

