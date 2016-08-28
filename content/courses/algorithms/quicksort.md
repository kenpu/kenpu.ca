+++
slide = true
title = "Quicksort"
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
    L[p:r] = L1 + [x] + L2
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
    L[i+1], L[r] = L[r], L[i]
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
    L[i+1], L[r] = L[r], L[i]
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
    L[i+1], L[r] = L[r], L[i]
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







# Summary

[!](highlight)

- Partition: a simple version

- Partition: a zero-memory version

- Quicksort: a recursive sorting algorithm


