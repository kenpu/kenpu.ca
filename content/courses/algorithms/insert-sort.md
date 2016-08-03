+++
slide = true
+++

# Basic programming

[!](columns 6:6)

We use *Python* for this course.

> Basic Python will do for the most part of this course.

[!](split)

If you are not used to Python (anymore), you are only *one* day away
of catching up.

- https://www.codecademy.com/learn/python

> [!](break) 
> No idea what to say about this
> ==============================================

# Programming & This Course


[!](columns 6:6)

We don't need much programming for this course because we absolutely will be
focused on the *algorithms*.

[!](split)

But ...


The reality is that *programming* is absolutely essential.

[!](break)
=================================================================

# Basic programming for this course


[!](columns 8:)

~~~python
x = [1, 2, 3]

print "The middle number is %d" % x[1]
~~~


[!](split)

We need arrays as a fundamental data structure.

[!](break)
================================================================


[!](columns 8:)

~~~python
class Student:
    name = "Unknown"
    age = 18

    def __init__(self, name):
        self.name = name

jack = Student("Jack")

print "%s: %s" % (jack.name, jack.age)
~~~

[!](split)

We need objects.

[!](break)
==================================================================

[!](columns 8:)

~~~python
i = 0
while i < 10:
  print i
  i += 1
~~~

~~~python
for i in range(10):
  print i
~~~


[!](split)

Various loops are needed.

[!](break)
==================================================================

[!](columns 8:)

~~~python
def reverse_string(s):
    reversed_s = ""
    for c in s:
      reversed_s += c
    return reversed_s
~~~

[!](split)

We need functions, mostly to better organize the implementation of an algorithm.


[!](break) ============

We may need to rely on external Python libraries for data generation and visualization of algorithmic actions.

[!](columns 4:)

<img src="random-graph.png"></img>

[!](split)

~~~python
import networkx as nx
import matplotlib.pyplot as plot

G = nx.erdos_renyi_graph(100, 0.015)
nx.draw(G)
plot.save("random-graph.png")
~~~

[!](break)
============================================================================

# The sorting problem

[!](columns 9:)

- Input:

    > An array of elements: $x$
    > where the elements are to be compared by a *comparator* function:
    >
    > `$$f(x_1, x_2) \in \left[
    \begin{array}{cc}
    -1 & x_1 < x_2 \\
    0 & x_1 = x_2 \\
    1 & x_1 > x_2
    \end{array}\right.$$`

- Output:

    > A permutation $y$ of the array of $x$, such that
    >
    > `$$\forall i,j\in[0, \mathrm{length}(y)],\quad i\leq j \implies y[i] \leq y[j]$$`

[!](split)

- This is called *comparison based sorting*.
- The comparison function can be arbitrary, and it defines the ordering.


[!](break)
============================================================================

# The sorting problem

- Permutation $\pi : [0, n] \to [0, n]$ such that `$i\not= j\implies \pi(i)\not=\pi(j)$`

- Given a sorting problem $(x, f)$, there can be multiple non-unique permutations that sorts $x$.

    > ~~~python
    > x = [3, 2, 2, 1]
    > ~~~

- Stable sorting requires an additional condition on the permutation:

    `$$ \forall i,j\in [0, \mathrm{length}(x)],\ i < j\ \mathrm{and}\ f(x[i], x[j]) = 0 \implies \pi(i) < \pi(j) $$`

[!](break)
===========================================================================

# Insertion sorting

> It's a highly *inefficient* sorting algorithm.

It's simple enough that:

1. It's intuitive.
2. It can be fully analyzed relatively easily.