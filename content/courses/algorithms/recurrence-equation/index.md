+++
slide = "true"
title = "Recurrence Equation"
+++

# Recurrence Equations

[!](highlight)

- Analysis of recursive algorithms
- Solving recurrence equation by substitution
- Solving recurrence equation by recurrence tree

# Recursion

We have already seen recursion used in sorting:

1. Top-down mergesort
2. Quicksort.

---

*Definition*: Recursion

> Recursion is when a procedure that:
> 
> 1. Divides the input into smaller problems,
2. and applies itself on the smaller problems, until
3. the problem is so small that it can be solved quickly.

# On mergesort

[!](columns 5:)

```{python sm}
def mergesort(A):
    # Termination
    if len(A) <= 1: return A

    # Recursion
    A1 = mergesort(A[:n/2])
    A2 = mergesort(A[n/2:])
    return merge(A1, A2)
```

[!](split)

Let $T(n)$ be the time for mergsort to terminate given an input array with $n$
elements.

We know:

`$$T(n) = \left\{\begin{array} 
                 \ \Theta (1) & \mathrm{\ if\ } n \leq 1 \\
                 T(n/2) + T(n/2) + \Theta(n) & \mathrm{\ else}
                 \end{array}\right.$$`

[!](box)
What is a good $g(n)$ for $T(n) = \mathcal{O}(g)$?


# Recurrence equation

A recurrence equation is an equation that defines $f(n)$ based
on $f(m)$ for some $m < n$, and other complexity classes.

[!](&&&)

For example:

$$ T(n) = 2 T(n/2) + \Theta(n) $$

# Quicksort

[!](columns 6:)

```{python sm nu}
def quicksort(A, p, r):
    k = partition(A, p, r)
    quicksort(A[p:k+1], p, k)
    quicksort(A[k+1:r+1], k+1, r)
```

[!](split)

$T(n)$ is time of quicksort for array of length $n$.

Note: $k$ is between $p$ and $r$ (inclusively).

**Worst** case:

> $k = p$ or $k = r$, i.e. the pivot is placed at the ends of the
> subarray.

**Best** case:

> $k = (p+r)/2$.

**Average** case:

> $k = \alpha p + (1-\alpha) r$ for some $0\leq \alpha\leq 1$.

# Quicksort

[!](columns 6:)

```{python sm nu}
def quicksort(A, p, r):
    k = partition(A, p, r)
    quicksort(A[p:k+1], p, k)
    quicksort(A[k+1:r+1], k+1, r)
```

[!](split)

`$T(n) = \Theta(n) + T(n_\mathrm{line3}) + T(n_\mathrm{line4})$`

**Worst case**:

> - `$n_\mathrm{line3} = 1$`
> - `$n_\mathrm{line4} = n-1$`
> - `$T(n) = \Theta(n) + T(n-1)$`

**Best case**:

> - `$n_\mathrm{line3} = n/2$`
> - `$n_\mathrm{line4} = n/2$`

**Average (general) case**:

> - `$n_\mathrm{line3} = \alpha n$`
> - `$n_\mathrm{line4} = (1 - \alpha) n$`

# Quicksort

So we get:

**Worst-case**:

`$$T(n) = \Theta(n) + T(n-1)$$`

**General case**:

`$$\begin{eqnarray}
T(n) &=& \Theta(n) + T(\alpha n) + T((1-\alpha) n) \\
     &\leq& \Theta(n) + 2T(\alpha n)
\end{eqnarray}$$`

Note, without loss of generality, we assume `$\alpha \geq 1/2$`.

# Solving recurrence equations by substitution

1. Assume that $T(n) = \mathcal{O}(f(n))$ for some initial _guess_ of $f(n)$.
2. Show by induction on $n$, that the recurrence equation is satisfied.

[!](-----)

If we are just interested at the asymptotic upperbound, we can relax recurrence
equations to recurrence inequalities.

Example:


> `$T(n) = \Theta(n) + T(n-1)$`
> 
> becomes
> 
> `$T(n) \leq \Theta(n) + T(n-1)$`

