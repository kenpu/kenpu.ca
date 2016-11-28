+++
title = "Greedy Algorithms"
slide = true
+++

# Greedy Algorithms

[!](highlight)

- Optimalization problems

- Performance gain v.s. optimality

# Dynamic programming

Let's review the structure of dynamic programming.

_Top down_ formulation

- Start with an instance of the problem: $P$

- Only finitely many subproblems of $P$ that need to be solved: $Q_i$.

    `$$ P \Rightarrow \{Q_1, Q_2, \dots Q_k\} $$`

- Based on the solution of all of $Q_i$, we can construct the solution of $P$.

[!](box) An naive recursive implementation will likely lead to an exponential
time complexity.

# ___________________

_Bottom up_ computation

> - We start by solving the smallest cases of the subproblems.
> 
> - Based on multiple small solutions, we build up larger solutions.
>
>   `$$\{\mathrm{solution}(Q_1), \mathrm{solution}(Q_2), \dots,
>   \mathrm{solution}(Q_k)\}  \Rightarrow
>   \mathrm{solution}(P)$$`
> 
> - Keep going until the instance $P$ is solved.

_Memoization_

> - During the recursion, we memorize the solutions of subproblems $Q_i$, so that
  we only perform the computation for the *first* time we encounter $Q_i$, but
  not subsequent calls.

[!](***)

[!](box) For many problems, bottom-up computation and memoization lead to
_polynomial time_ complexity.


# _______________________

- Dynamic problem computes the optimal solution.

- What if we want to trade-off optimality for performance?

    $\Rightarrow$ _Greedy algorithms_


# Greedy Algorithms

- The key is to _abandon_ the guarantee of optimality.

- Make *one* explorative computation that gives the most promising subproblem.

    $$ P \Rightarrow Q_i^* $$

    where $Q_i^*$ is the most promising subproblem to explore.

- If the problem is sufficiently well behaved, we might have the optimal
  solution.

# Example: activity selection

Consider the activity selection problem:

- We have a set of activities, each with a fixed starting time and finish time.

    $a_i = (s_i, f_i)$ where $s_i < f_i$.

- Two activities $a_i$ and $a_j$ are _compatible_ if their times do not overlap:

    ```nosyntax
    si             fi      sj       fj
    |              |       |        |
    +--------------+       +--------+
    ```

The problem is:

> Given a collection of activities `$A = \{a_1, a_2, \dots, a_n\}$`
  find the most number of mutually compatible activities.

# _______________________

Consider the following instance of the activity selection problem:

| i | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $s_i$ | 1 | 3 | 0 | 5 | 3 | 5 | 6 | 8 | 8 | 2 | 12 |
| $f_i$ | 4 | 5 | 6 | 7 | 9 | 9 | 10 | 11 | 12 | 14 | 16 |

Here are some examples of _mutually compatible_ selections:

- `$\{a_3, a_9, a_11\}$`: 3 activities
- `$\{a_1, a_4, a_8, a_11\}$`: 4 activities
- `$\{a_2, a_4, a_9, a_11\}$`: also 4 activities

---

It turns out that the maximal number of mutually compatible activities is **4**.

# _________________________

Let $P$ be the overall problem instance:

| i | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $s_i$ | 1 | 3 | 0 | 5 | 3 | 5 | 6 | 8 | 8 | 2 | 12 |
| $f_i$ | 4 | 5 | 6 | 7 | 9 | 9 | 10 | 11 | 12 | 14 | 16 |

We want to reduce $P\Rightarrow Q^*$.

We want to pick the _first_ activity _greedily_.  Do we pick $a_1$ or $a_2$ or
  $a_3$ to leave the most number of remaining activities?

[!](columns 10:)

- If we pick $a_1$, the remaining compatible activies are
    `$\{a_6, a_7, \dots a_{11}\}$`.

- If we pick $a_2$, the remaining compatible activies are
    `$\{a_6, a_7, \dots a_{11}\}$`.

- If we pick $a_3$, the remaining compatible activies are
    `$\{a_7, a_8, \dots a_{11}\}$`.

[!](split note)

So, the activity to select as the first should be either $a_1$ or $a_2$, so
that we leave the most number of compatible activities.

# ________________________

Pick the first activity (with earliest finish time), and the
subproblem is all remaining compatible activities.

```python
def subproblem(A):
    "assume A is sorted by finish time"
    activity = A[0]
    B = [a for a in A if a.start >= activity.finish]
    return activity, B
```

Keep generating subproblems until no more activities are left.

```python
def greedy_selection(A, selection):
    while len(A) > = 0:
        a, B = subproblem(A)
        selection.append(a)
        A = B
```

# ___________________________

_Theorem_

- The greedy solution of activity selection can be implemented in $\Theta(n)$.

- The solution is _optimal_.

