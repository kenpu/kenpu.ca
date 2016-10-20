+++
slide = true
title = "Hash Tables"
+++

# Hash tables

[!](highlight)

# Dynamic sets

*Definition*

> A _dynamic set_, $S$, is a data structure that stores _distinct elements_.

We are interested to support the following functions:

- Insert: adds an element into `S`. 
  It does nothing if `x` is already in `S`.

    > `INSERT(S, x)`

- Search:

    > `SEARCH(S, x)`

- Delete:

    > `DELETE(S, x)`

# Direct Addressing

Consider the case of dynamic sets:

- Each element $x\in S$ is a pair 
  `$\left<\mathrm{KEY}[x], \mathrm{value}[x]\right>$`.

- The key $\mathrm{KEY}[x]$ is an integer in $[0, 1, \dots, N-1]$.

- No two elements have the *same* key:

    `$$\forall x, y\in S,\ x\not= y 
    \implies
    \mathrm{KEY}[x]\not=\mathrm{KEY}[y]$$`

[!](&&&)

[!](columns 6:)

A direct-address table is just an array $T$ of length $N$.

- Each slot corresponds to a key.

- For each element $x\in S$, $T[\mathrm{KEY}[x]] = x$.

[!](split)

<img src="direct-table.png"></img>

# Implementation of direct address tables

```python
def DIRECT_ADDRESS_SEARCH(T, k):
    return T[k]
```

```python
def DIRECT_ADDRESS_INSERT(T, x):
    index = x.key
    return T[index] = x
```

```python
def DIRECT_ADDRESS_DELETE(T, x):
    index = x.key
    T[index] = None
```

# Properties of direct address tables

- Fast methods

    > All operations are $\Theta(1)$.

- But it's impractical

    > Most key spaces are at least 32-bits (some are 64-bits or higher).
    >
    > $N = 2^{32}$, and each table slot must be at least 
    > $\log_2(|S|)$ bits, $\simeq 10$ bits.
    >
    > The total memory required is $\sim 10\cdot 2^{32} = 1$ GB.
    >
    > The space requirement is $\Theta(N)$

# Hashing

- Let $U$ be the universse of *all* possible values that can appear in the
  dynamic set.

- Elements in $U$ are called the keys.

- A *hash function* is a function, $h$, mapping keys to _hash values_.

    > For $x\in U$, $h(x)\in[0, 1, 2, \dots, N-1]$

# Hash function

<center>
    <img src="hashing.png" width="500px"></img>
</center>

# Hash Tables

- Still use an array $T$ as a table with $m$ slots.

    > But our objective is $m = \Theta(|S|)$, instead of $m = \Theta(N)$.

- Do not use _direct address_ policy.

- `T[index] = x`, where `index = $h$(x.key)`

---

[!](columns 6:)

**PROBLEM**: collision

> A _collision_ occurs if we have two $x, y\in S$ such that
  $x \not= y$, but $h(\mathrm{KEY}[x]) = h(\mathrm{KEY}[y])$.

[!](split)

<img src="collision.png"></img>

# Collision resolution

Before:

> Each slot in the table stores a single element in the dynamic set.

After:

> Each slot in the table stores a _list_ of elements in the dynamic set.
> This is called _chaining_.

<img src="chaining.png"></img>

# INSERT with chaining

```python
def HASHTABLE_INSERT(T, x):
    index = h(x.key)
    if T[index] == None:
        T[index] = []
    T[index].append(x)
```

# SEARCH with chaining

```python
def HASHTABLE_SEARCH(T, key):
    index = h(key)
    if T[index] == None:
        return False
    else:
        for x in T[index]:
            if x.key == key:
                return x
        return False
```

# DELETE with chaining

```python
def HASHTABLE_DELETE(T, key):
    index = h(key)
    if T[i] == None:
        return
    else:
        remove(T[i], key)
```

```python
def remove(array, key):
    for (i, x) in enumerate(array):
        if x.key == key:
            array[i:i+1] = []
            return
```

# Analysis 

[!](columns 6:)

```{python sm}
def HASHTABLE_INSERT(T, x):
    index = h(x.key)
    if T[index] == None:
        T[index] = []
    T[index].append(x)
```

[!](split)

`HASHTABLE_INSERT` is done in $\Theta(1)$.

# Analysis

[!](columns 6:)

```{python sm}
def HASHTABLE_SEARCH(T, key):
    index = h(key)
    if T[i] == None:
        return False
    else:
        for x in T[i]:
            if x.key == key:
                return x
        return False
```

[!](split)

`HASHTABLE_SEARCH` is done in $\Theta(L)$ where $L$ is the average length of the
lists.

If we assume uniform hash value distribution of the keys, we get:

$$ L = \frac{|S|}{|T|} $$

This is known as the load factor of the hash table.

Typically, we want to keep the load factor as 0.75:

$$ |T| \simeq 1.3 |S| $$

# Summary

- Dynamic sets

- Direct address table as an implementation

- Hash tables with chaining


