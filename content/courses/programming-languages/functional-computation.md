+++
slide = true
+++

# $\lambda$-Calculus: symbolic computation

[!](break)

# $\lambda$-Calculus

- Proposed by Alonzo Church in ~1930.

    > intented to formalize mathematics.

- Syntactic expressions that represent *functions*.

    > designed to represent the entire foundation of mathematics.

- Rules of rewriting the syntactic expression 

    > rewrite rules represent mathematical reasoning.

[!](break)

# Expressions

Values

> - Literals: 1, 2, 3, "Hello world"
> - Variables: $x, y, z, \dots$

Functions

> - $+ : (x,y)\mapsto x+y$
> - $\mathrm{inc} : x\mapsto x+1$
> - $\dots$
>
> ---
>
> - Always returns *one* value.
> - Takes a fixed number of inputs: arity of the function 
    <span style=color:red>*</span>

[!](break)

# Value as function

A value is a zero-arity function.

<br><br>

# Function as value

We want to extend the idea of *things* to include functions.

> *This is a central idea in functional programming*.

<br><br>

## Value $\equiv$ Function = Everything

[!](break)

# Syntax for expressions (value / function)

[!](columns 8:)

> - $1, 2, 3, +, -, \dots$ are expressions
> - $x, y, z, \dots$ are expressions

Abstraction:

> - If $x$ is a variable, and $e$ is an expression, then
    $\lambda x. e$ is an expression

Application:

> - If $e_1$ is a function with arity 1, 
    `$e_2$` is an expression, then
    $e_1 e_2$ is an expression

[!](split note)

We assume that all functions are with arity 1.

> This is not a restriction.

[!](break)

# The *weird* syntax of $\lambda$ calculus

- $\lambda x: e$

    > This is a function taking *one* input, represented by the variable $x$.
    > It returns *one* value, which is evaluated as the expression $e$.
    > The expression $e$ usually makes uses of $x$, but not necessarily.

- `$e_1 e_2$`

    > This is passing $e_2$ as an argument to the expression $e_1$.  Recall that
    > everything is a function.  So $e_1$ is a function with *one* argument.

- `$e_1 e_2 e_3 = ((e_1 e_2) e_3)$`

    > This shows that $e_1$ takes one argument ($e_2$), and returns an
    > expression which is yet again a function which takes $e_3$ as an input.

[!](break)

# Defining things

- Identity function

- Functions with multiple arity

[!](break)

# Computing with $\lambda$-Calculus


