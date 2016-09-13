+++
slide = true
+++

# $\lambda$-Calculus: symbolic computation

[!](highlight)

# $\lambda$-Calculus

- Proposed by Alonzo Church in ~1930.

    > intented to formalize mathematics.

- Syntactic expressions that represent *functions*.

    > designed to represent the entire foundation of mathematics.

- Rules of rewriting the syntactic expression 

    > rewrite rules represent mathematical reasoning.

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

# Value as function

A value is a zero-arity function.

<br><br>

# Function as value

We want to extend the idea of *things* to include functions.

> *This is a central idea in functional programming*.

<br><br>

## Value $\equiv$ Function = Everything


# Syntax for expressions (value / function)

[!](columns 8:)

> > - $x, y, z, \dots$ are expressions

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


# The *weird* syntax of $\lambda$ calculus

- $\lambda x.e$

    > This is a function taking *one* input, represented by the variable $x$.
    > It returns *one* value, which is evaluated as the expression $e$.
    > The expression $e$ usually makes uses of $x$, but not necessarily.

- `$e_1 e_2$`

    > This is passing $e_2$ as an argument to the expression $e_1$.  Recall that
    > everything is a function.  So $e_1$ is a function with *one* argument.

- `$e_1 e_2 e_3 = ((e_1 e_2) e_3)$`

    > This shows that $e_1$ takes one argument ($e_2$), and returns an
    > expression which is yet again a function which takes $e_3$ as an input.


# Defining things

- Identity function

    > `$\lambda x.x$`

[!](columns 8:)

- Functions with multiple arity

    > Suppose we have a function $f(x,y,z) = e$ where the expression
    involves all three input variables $x, y, z$.
    >
    > We can use the following expression to build $f$:
    >
    > `$\lambda x.(\lambda y.(\lambda z. e))$`

    **This is a big deal.** <br>
    **Functions as values in action here.**

[!](split note)

<div style=height:220px></div>

We can write it conveniently as $\lambda xyz.e$


# Computing with $\lambda$-Calculus

[!](highlight)

> We rely on string-rewriting to evaluate
> LC expressions.


# Substitution of variables in function applications

**Notation**:

> $e[x/e']$ is the expression obtained by substituting all occurances of $x$ in
> the expression $e$ with the expression $e'$.

[!](columns 8:)

**Substition** as a way to evaluate function application:

> $(\lambda x. e) e' \implies e[x/e']$.
>
>
> *Example*:
>
> `\begin{eqnarray}
&& (\lambda x.x x) (\lambda y. y) \\
&\implies& (x x)[x/(\lambda y.y)] \\
&\implies& (\lambda y.y)(\lambda y.y) \\
&\implies& y[y/(\lambda y.y)] \\
&\implies& (\lambda y.y)
\end{eqnarray}`


[!](split note)

**Warning**

We can easily get into trouble.

Substitution cannot be used freely.


# Free & Bound Variables

_Variables in a function abstraction expression can be *free* or *bound*._

[!](-----)


> If a variable represents the input parameter in a function expression, then
> it's considered *bound*.  Otherwise, it's *free*.

- $\mathbf{FV}(e)$ are the free variables of $e$
- $\mathbf{BV}(e)$ are the bound variables
- [!](comfort)


# Variable Capturing

Consider an expression:

$$\lambda x. (\lambda x.x)$$

There are multiple occurrences of $x$, so let's label them so we can refer to
the individual occurrences.


$$\lambda x_1. (\lambda x_2.x_3)$$

> *Which input variable does $x_3$ refer to?*

[!](------)

[!](box) This is called capturing.

# Elimination of Variable Capturing

There is a rewrite rule that allows us to rename the parameter variables without
changing the meaning of the expression.

$$ \lambda x. x \equiv \lambda y.y \equiv \lambda \mathsf{hello}.\mathsf{hello} $$

**Renaming**

> Suppose that $x$ is a free variable of $e$, and $y$ does not appear in $e$ at
> all.
>
> Then $\lambda x.e \implies \lambda y.e[x/y]$ 



# Elimination of Variable Capturing

Back to:

$$\lambda x. (\lambda x.x)$$

[!](-----)

- [!](comfortable)
- First we consider the sub expression $\lambda x.x$.

    > Using renaming, we can rewrite it to $\lambda y.y$.

- Then we get:

    > $$\lambda x. (\lambda x.x) \implies \lambda x.\lambda y. y$$



[!](box)
Generally, we only apply **substitution** to evaluate function applications
if there is *no* variable capturing; and this can be achieved by **renaming**.

# How to perform computation using LC?

- [!](comfort)
- Natural numbers
- Arithmetics
- Loop and conditional branching

[!](-----)

**All can be done using LC**

> 1. Express the algorithm in terms of natural numbers, arithmetics,
     loops and conditional branches.
>
> 2. Encode the algorithm in LC.
>
> 3. Apply syntax rewriting until no more rewriting is possible.
> 4. [!](comfort)






# A glance of LC in action

A bit of notation:

> $\lambda x.\lambda y. \lambda z. e$ is written as as $\lambda xyz. e$.

---

Now we can encode numbers:

$0 \equiv \lambda sx. x$ (takes two inputs, but only keep the second one.)

$1 \equiv \lambda sx. sx$

$2 \equiv \lambda sx. ssx$

$\vdots$

# Arithmetics

Consider the simplest arithmetics: increment by 1.

[!](columns 4:)

```python
def succ(n):
    return n + 1
```

[!](split)

`$$S \equiv \lambda n. \lambda yx.y(nyx)$$`

---

Let's try this out.

`\begin{eqnarray}
S 0 &=& (\lambda n. \lambda yx.ynyx)0 \\
    &=& (\lambda yx.ynyx)[n/0] \\
    &=& \lambda yx.y(0yx) \\
    &=& \lambda yx.y((\lambda sz.z)yx) \\
    &=& \lambda yx.y(x) \\
    &=& 1
\end{eqnarray}`

# Arithmetics

[!](columns 4:)

```python
def add(n1, n2):
    return n1 + n2
```

[!](split)

Observe:

$2 S 3 = 5$ (work it out, it's quite incredible.)

So, we have:

$$+ \equiv \lambda mn. mSn$$

[!](------)

Can you guess the LC expression for multiplication?

# Recursion

- LC does not require assigning aliases to functions.

    > Technically, there is just **ONE** expression for the entire algorthm.

- Why it's hard to do recursion without aliases?

    ```python
    def factorial(n):
        if n <= 1:
            return n
        else:
            return n * factorial(n-1)
    ```

- Is it even possible?

    > Yes.  It's called the **Y**-combinator.
    >
    > $$ \mathbf{Y} \equiv (\lambda y.(\lambda x.y(xx))(\lambda x.y(xx)))$$

# Y-combinator

$$ \mathbf{Y} f = f (\mathbf{Y} f) $$

So,

$$ \mathbf{Y} f x \implies f (\mathbf{Y} f) x \implies f f \dots f x $$

> [!](note) $\mathbf{Y} f$ is a _fixed point_.

# Using Y-combinator to implement factorial

Consider a function $F$ as:

$$\lambda fx. (\mathrm{ifzero}\ x)\ 1\ (*\ x\ (f\ (\mathrm{dec}\ x)))$$

If we apply the Y-combinator to $F$, we get:

$$ (\mathbf{Y} F) n = F (\mathbf{Y} F) n $$

You can check the following:

$$ (\mathbf{Y} F) n = (\mathrm{ifzero}\ n)\ 1\ (*\ n\ ((\mathbf{Y} F)\ (\mathrm{dec}\ n))) $$

> [!](note) This is really quite amazing.  We have achieved Turing-completeness via recursion.  The amazing part is that we don't need variables to refer to any values.  So $F$ is just for convenience and readability.

# Summary

[!](highlight)

- [!](comfort)

- LC is purely symbolic.

- It carries out computation by very simple string rewrites:

    1. Function application
    2. Variable renaming

- It solves problem by:

    1. Encode the problem as a single (huge) string of LC expression.
    2. Using the rules to rewrite the string to a *normal* form.
    3. The resulting LC expression is the answer.

- No variables are needed.






