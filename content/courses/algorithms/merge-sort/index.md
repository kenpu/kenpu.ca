+++
slide = true
+++

# Mergesort

- [!](comfortable)
- Divide and conquer, when and when not...
- Bottom-up
- Top-down
- Correctness
- Complexity analysis

# Divide and conquer

> It's a way to instruct "simple" solver to solve a complex problem.

[!](columns 4:)

<img data-src="Minion.jpg"></img>

[!](split)

<img data-src="office-messy-desk.jpg"></img>

# Divide and conquer (and combine)

Divide:

> Given a problem $P$, the division of a problem is a procedure
> that produces a collection of _smaller_ problems `$\mathbf{Q} = \{Q_1, Q_2, \dots\}$`.

Conquer:

> Each sub-problem `$Q_i\in\mathbf{Q}$` (hopefully) is easier to solve.
> Let `$S_i = \mathrm{solve}(Q_i)$`

Combine:

> Hopefully, the solutions of subproblems, $\{S_i\}$, are not useless toward the
> solution of $P$.
>
> We need a procedure to combine:
>
> `$$\mathrm{solve}(P) = \mathrm{combine}(S_1, S_2, S_3, \dots)$$`




# Example: cleaning a mess

<img src="Minion.jpg" style="float:left;width:80px;margin:0 20px 0px 0"></img>
Consider how you can instruct a minion to clean a messy office.  The minion
is overwhelmed by the mess of the entire office.  Divide and conquer is a great
way to solve the cleaning problem.

[!](---------)

Here are some assumptions:

1. The minion can clean up a very small section of an office - like a drawer, or
   a book shelf.

2. If every section of an office is organized, we deem the whole office
   organized.


# Example: cleaning a mess

- Divide(Office) = `{Bookshelf, Desk, Floor, Cabinet, Drawer, $\dots$}`

- Conquer: the minion can clean up each section

- Combine: Nothing needs to be done








# Sorting with Divide and Conquer

[!](columns 8:)

Divide & Conquer:

> A list of numbers can be divided into smaller lists.
> If a list is so small, we can sort it trivially.

[!](split note)

*How small does a list need to be for us to know how to sort it?*


# Sorting with Divide and Conquer

Combine:

> If we have two lists that are already sorted, can we figure out how to combine
> them in a sorted way?

[!](----)

```{nosyntax}
+---+---+---+---+
| 1 | 5 | 6 | 8 |          \
+---+---+---+---+          |
                           |
                           +------>  combined sorted list
                           |
+---+---+---+---+----+     |
| 3 | 4 | 5 | 8 | 10 |     /
+---+---+---+---+----+
```

# Sorting with Divide and Conquer

Combine:

[!](columns 10:)

```{python clipboard}
def merge(list1, list2):
    i, j = 0, 0
    list3 = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            list3.append(list1[i])
            i += 1
        else:
            list3.append(list2[j])
            j += 1

    if i < len(list1): list3.extend(list1[i:])

    if j < len(list2): list3.extend(list2[j:])

    return list3
```

[!](split note)

We want to be able to merge to sorted list into a larger list.

[!](break)

{{<gist "kenpu" "df50d5b42ed4abb0c4749284111005d6" "merge.py">}}


# Bottom-up Mergesort

[!](highlight)



# Bottom-up Mergesort

We start with a list of arbitrary lenght $n$.

- Observe that *all* sublist of length 1 is already sorted.

- Use `merge()` to improve the _sortedness_ of the list to length 2.

- Use `merge()` to improve the _sortedness_ of the list to length 4, 8, 16, ...
  until the whole list is sorted.


# Bottom-up Mergesort

```{python clipboard}
def mergesort(list):
    sortedness = 1

    while sortedness < len(list):
        for i in range(0, len(list), 2*sortedness):
            list1 = list[i:i+sortedness]
            list2 = list[i+sortedness:i+2*sortedness]
            list3 = merge(list1, list2)
            list[i:i+len(list3)] = list3
        sortedness = 2 * sortedness

    return list
```

# Bottom-up Mergesort

{{<gist "kenpu" "df50d5b42ed4abb0c4749284111005d6" "mergesort.py">}}

# Bottom-up Mergesort


- A hierarchy of subproblems

    > Small subproblems: sublist of length 1
    >
    > Larger subproblems: sublist of length 2, 4, ...
    >
    > The largest subproblem: the whole list

[!](columns 8:)

- Why is it called _bottom-up_?

    > The procedure, `mergesort()`, recognizes the smallest subproblems *first*.
    >
    > The **divide** stage starts at the bottom of the hierarchy.

[!](split)

[!](-------)

The **conquer** stage _always_ starts with the bottom of the hierarchy.



# Analysis: correctness

[!](columns 8:)

```{python sm}
def mergesort(list):
    sortedness = 1

    while sortedness < len(list):
        for i in range(0, len(list), 2*sortedness):
            list1 = list[i:i+sortedness]
            list2 = list[i+sortedness:i+2*sortedness]
            list3 = merge(list1, list2)
            list[i:i+len(list3)] = list3
        sortedness = 2 * sortedness

    return list
```

[!](split note)

Loop-invariance:

> At the end of each loop,
>
> for all $L[i\Delta \dots (i+1)\Delta]$ is sorted for all $i$,
where $\Delta$ is the sortedness at the end of the iteration.

Overall correctness

> The loop terminates when $\Delta$ exceeds the length of the list, so the
> entire list is sorted by the loop invariance.

Guaranteed termination

> Each iteration strictly increases the sortedness $\Delta$ (by doubling it).

# Analysis: performance

[!](columns 8:)

```{python sm}
def mergesort(list):
    sortedness = 1

    while sortedness < len(list):
        for i in range(0, len(list), 2*sortedness):
            list1 = list[i:i+sortedness]
            list2 = list[i+sortedness:i+2*sortedness]
            list3 = merge(list1, list2)
            list[i:i+len(list3)] = list3
        sortedness = 2 * sortedness

    return list
```

[!](split note)

How many iterations if there are $n$ elements in the list?

> Each iteration grows the _sortedness_ by a factor of 2 up to $n$.
> So, we need $\log_2(n)$ iterations.

How many instructions does each iteration take?

> Each iteration has four steps.  Each step requires no more than a linear scan
> of the list.
> We can guarantee that number of instructions do not exceed: $k\cdot n$ for some
> constant $k$.

---

Putting it together:

> `mergesort()` requires no more than $k\cdot n\log(n)$ number of instructions.


# Top-down mergesort

[!](highlight)


# Top-down mergesort

- Revisit the hierarchy of subproblems of sorting a list

- We can specify the *Divide-and-conquer* top-down:

    > 1. Divide sorting of $L$ to the first sublist $L[0 \dots \frac{n}{2}]$
        and the second sublist $L[\frac{n}{2} \dots n]$

    > 2. If the sub-lists are not easy enough, then break down again.

- *Recursion*


```{python clipboard}
def mergesort(L):
    n = len(L)
    if n <= 1:
        return L
    else:
        L1 = mergesort(L[:n/2])
        L2 = mergesort(L[n/2:])
        return merge(L1, L2)
```

# Top-down mergesort: Analysis

[!](columns 7:)

```{python clipboard}
def mergesort(L):
    n = len(L)
    if n <= 1:
        return L
    else:
        L1 = mergesort(L[:n/2])
        L2 = mergesort(L[n/2:])
        return merge(L1, L2)
```

[!](split note)

## Correctness:

Induction on depth of recursion.

Base case: depth = 0

> If there is no recursion, than the list $L$ is such that $|L|\leq 1$.

Inductive case: depth = $k$, and assume that all mergesort at level $< k$ are
correct.

> Let $L_1$ and $L_2$ be the two sublists.  The invocations `mergesort($L_i$)`
> use $< k$ recursions, and thus, are *correct*.
>
> Since $L_1$ and $L_2$ are properly sorted, and that `merge()` is correct,
> we conclude that `mergesort(L)` is correct.

# Top-down mergesort: Analysis

[!](columns 6:)

```{python sm clipboard}
def mergesort(L):
    n = len(L)
    if n <= 1:
        return L
    else:
        L1 = mergesort(L[:n/2])
        L2 = mergesort(L[n/2:])
        return merge(L1, L2)
```

[!](split note)

## Performance

Let $n = |L|$.  How much time does it take to complete top-down
`mergesort($L$)`?

Let $T(n)$ = time of `mergesort($L$)`.

`\begin{eqnarray*}
T(n) &\simeq& T(n/2) + T(n/2) + n \\
  &=& 2 T(n/2) + n
\end{eqnarray*}`

[!](----)

> We will develop an array of techniques to solve _recurrence equations_ to
> analyze recursive algorithms.

[!](----)

Spoiler Alert:

> $$ T(n) = n\log(n) + n $$














# Conclusion

[!](highlight)

- Divide and conquer

- Bottom-up mergesort

- Top-down mergesort


# Challenge

Is `MERGESORT` a stable sorting algorithm?

Recall:

> Stable sorting requires an additional condition on the permutation:
>
> `$$ \forall i,j\in [0, \mathrm{length}(x)],\ i < j\ \mathrm{and}\ f(x[i], x[j]) = 0 \implies \pi(i) < \pi(j) $$`
