+++
slide = true
+++

# Quicksort

[!](highlight)

# Quicksort

- Divide and conquer

    > Given a list $L$, we divide the sorting problem into two sub-problems.
    >
    > 1. Sort the elements in $L$ smaller than $x$: $L_1$
    >
    > 2. Sort the elements in $L$ larger than $x$: $L_2$

- Combine

    > `$\mathrm{sorted}(L) = \mathrm{sorted}(L_1) \oplus \{x\} \oplus \mathrm{sorted}(L_2)$`

# Partition

Given a list `$L$` and an element $x$ in $L$, _partitioning_ $L[p \dots r]$ by the _pivot_
element $x$ does the following:

> Rearrange the elements in $L[p\dots r]$ so that there exists a position $q$
> such that *after* rearrangment:
>
> 1. $L[q] = x$
> 2. $\forall i\in [p, q-1],\ L[i] \leq x$
> 3. $\forall i\in [q+1, r],\ L[i] \geq x$
> 4. [!](comfort)

[!](break)

## Version 0.1: simple, but takes more memory

Let's implement `partition(L, p, r)` with the minimal effort:

- Pick $x = L[r]$
- Filter the list for smaller elements: `$L_1 = \{y\in L[p\dots r-1]: y\leq x\}$`
- Filter the list for larger elements: `$L_2 = \{y\in L[p\dots r-1]: y > x\}$`
- Reconstruct: `$L[p \dots r] = L_1 \oplus \{x\} \oplus L_2$`
- [!](comfort)

```{python}
def partition(L, p, r):
    x = L[r]
    L1 = [y for y in L[p:r] if y <= x]
    L2 = [y for y in L[p:r] if y > x]
    L[p:r+1] = L1 + [x] + L2
```


[!](break)

## Version 0.2: more involved, but takes no additional memory

[!](columns 8:)

```{python clipboard}
def partition(L, p, r):
    x = L[r]
    i = p - 1
    for j in range(p, r):
        if L[j] <= x:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[r] = L[r], L[i+1]
```

[!](split)

It only involves element swapping, so it requires *zero* additional memory.

---

But its correctness is much less obvious.


# Analysis of partition

[!](columns 7:)

```{python clipboard}
def partition(L, p, r):
    x = L[r]
    i = p - 1
    for j in range(p, r):
        if L[j] <= x:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[r] = L[r], L[i+1]
```

[!](split)

Bookkeeping is the key:

- [!](comfort)
- $p$ and $r$ are the boundaries of the sublist to be partitioned.
- $r$ also holds the value of the pivot element.
- Elements in $[p\dots j]$ are processed.
- $i$ is a marker of the boundary between smaller and larger elements.







# Analysis of partition

[!](columns 7:)

```{python clipboard}
def partition(L, p, r):
    x = L[r]
    i = p - 1
    for j in range(p, r):
        if L[j] <= x:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[r] = L[r], L[i+1]
```

[!](split)

Loop invariance:

> After each iteration, $L[p, j]$ is properly partitioned:
>
> - $L[p, i] \leq x$
> - $L[i+1, j] > x$
> - [!](comfort)






# Quicksort

```{python}
def quicksort(L, p, r):
    if p < r:
        k = partition(L, p, r)
        quicksort(L, p, k-1)
        quicksort(L, k+1, r)
```


# Performance Analysis

[!](highlight)

> We will only give a terse outline of the analysis.  The full version is deferred to later lectures.

# Performance Analysis

Let there be $n$ elements in the array.

Key obsevation:

- `partition(L, p, r)` takes $(r - p)$ iterations.  Each iteration has a fixed number of instructions.  So, $T_\mathrm{partition} = c_1 (r-p) \leq c\cdot n$.

- At each *invocation* of `quicksort(L, p, k-1)` and `quicksort(L, k+1, r)`, we need to determine the number of elements: $k-1-p$, and $r-k-1$.

# Performance Analysis: Worst-case

- The worst case for $T_\mathrm{partition} = n$
- The worst case for $k-1-p = n-1$
- The worst case for $r-k-1 = n-1$

---

We have enough to set-up an equation to estimate the number of instructions of `quicksort(L, a, b)`:

Let $|L[a\dots b]| = n$.

`$$\begin{eqnarray}
T_\mathrm{quicksort}(n) &=& n + 2\cdot T_\mathrm{quicksort}(n-1)
\end{eqnarray}$$`

---

[!](columns 8:)

This leads to a (poor) performance characteristics of: $\approx n^2$

[!](split note)

> We will show how to solve such equations (known as recurrence equations) in the next section of this course.


# Performance Analysis: average case

Quicksort as the name suggests is actually quite quick (most of the time...)

---

Revisiting `k = partition(L, p, q)`.

> The pivot value should be somewhere in the middle of the subarray.
> Namely: $k\approx p+q/2$, and so $k-1-p \approx n/2$, and $q-k-1\approx n/2$.

---

Revisiting the recurrence equation:

> `$$\begin{eqnarray}
T_\mathrm{quicksort}(n) &=& n + 2\cdot T_\mathrm{quicksort}(n/2)
\end{eqnarray}$$`

---

This leads to a satisfying performance characteristics of: $\approx n\log(n)$

# Summary

[!](highlight)

- Partition: a simple version

- Partition: a zero-memory version

- Quicksort: a recursive sorting algorithm


# Challenge

Is `QUICKSORT` a stable sorting algorithm?

Recall:

> Stable sorting requires an additional condition on the permutation:
>
> `$$ \forall i,j\in [0, \mathrm{length}(x)],\ i < j\ \mathrm{and}\ f(x[i], x[j]) = 0 \implies \pi(i) < \pi(j) $$`
