+++
slide = true
title = "Sorting numbers"
+++

# Radix Sort

[!](highlight)

- [!](comfort)
- A scalable and efficient sorting algorithm.
- Assumes all the elements are **integers** bounded by the number of digits.

	> This is much more practical than the assumption of `COUNTING_SORT`.

# Radix Sort

Intuition:

> Write each integer as `$x = x_n x_{n-1} \dots x_3 x_2 x_1$` base $k$.  The least significant digit is $x_1$.

Example:

> Consider $x = $ one thousand four hundred and thirty seven.
>
> We can write 
> 
> - $x$ in base-10: $x = 1437$.
> - $x$ in base-16: $x = 59d$.
> - $x$ in base-2: $x = 10110011101$

# Radix Sort

Intuition:

> 1. Write each element in $A$ with $n$ digits of base $k$.
>
> 2. Repeatly sort the array, $A$, $n$ times, sorting by only one digit.  Start sorting by the least significant digit, and finish by the most significant digit.
>
> 3. The digit sorting algorithm used **must** be **stable**.  Use `COUNTING_SORT`.
>
> 1. [!](comfort)

# Radix Sort

Some help from Python:

```{python clipboard}
# convert a number to its binary representation
def radix2(num):
    return "{0:b}".format(num)

# Get the i-th digit of binary string x
def digit(num, i):
    x = radix2(num)
    if i >= len(x):
        return 0
    else:
        d = x[-(i+1)]
        return 0 if d == '0' else 1
```



# Radix Sort

Modify `COUNTING_SORT(A, i)`:

[!](columns 8:)

```{python clipboard}
# Sort A using binary digit i
def COUNTING_SORT(A, i):
    n = len(A)
    k = 2
    B = empty_array(size=n)
    C = empty_array(size=k, init=0)

    for a in A:
        d = digit(a, i)
        C[d] = C[d] + 1

    for j in range(1,k):
        C[j] = C[j] + C[j-1]

    for a in reversed(A):
        d = digit(a, i)
        B[C[d]-1] = a
        C[d] = C[d] - 1

    return B
```

[!](split note)

- Note that $k = 2$, we always assume binary encoding.  This is just for convenience.
- Instead of computing the (cumulative) frequency of elements of `A`, we use the $i$-th digit, 
  `digit(a, i)`.
- [!](comfortable)

# Radix Sort

Finally the radix sort algorithm:

```{python clipboard}
def RADIX_SORT(A):
    n = max(len(radix2(x)) for x in A)
    for i in range(n):
        A = COUNTING_SORT(A, i)
    return A
```

# On Radix Sort


> We introduced a very important sorting algorithm that is capable of sorting collections of very large integers (e.g. 64-bit values).

- Stable
- Very efficient: beats the best comparison based sorting algorithms


# Sorting the Reals

[!](highlight)

- Sorting decimal numbers between [0, 1]
- Bucket sort
- Efficient in the average case
- Inefficient in the worst case

# Sorting the Reals

Real numbers:

> Any number, with arbitrary precision

---

Assumption:

> We are concerned with sorting arrays of real numbers whose values are between $[0, 1]$.

---

As long as the values are bounded by any interview $[a, b]$, we can apply the algorithm developed here by means of normalization:

$$ x' = \frac{x - a}{b - a}$$

# Intuition

- Partition the interval [0, 1] into $n$ equally divided intervals:

    $$B = \big[0, \frac{1}{n}\big), \big[\frac{1}{n}, \frac{2}{n}\big), \dots, \big[\frac{n-1}{n}, 1\big]$$

    with $B_i = [\frac{i}{n}, \frac{i+1}{n})$.

- Given an array $A$, distribute $x\in A$ into the respective buckets $B_i$

- Sort each $B_i$ individually, and then concatenate all sorted buckets.

---

This is *surprisingly* effective.

# Bucket Sort

```{python clipboard}
def bucketsort(A, n):
    buckets = [[] for i in range(n)]
    # distribute the buckets
    for a in A:
        i = int(math.floor(a * n))
        bucket[i].append(a)
    # sort each bucket
    for bucket in buckets:
        bucket.sort()

    # place the elements from the sorted buckets
    # back to the array
    i = 0
    for bucket in buckets:
        for a in bucket:
            A[i] = a
            i += 1
```

# Bucket Sort

We will defer the analysis of bucket sort to later as it will greatly benefit from some probability and asympotic notations.

# Summary

[!](highlight)

- Numbers are _easier_ to sort than blackboxed elements.
- For bounded integers, we can use radix sort even if the bound is very very large (e.g. 256-bit integers).
- For bounded reals, we can use bucket sort.
