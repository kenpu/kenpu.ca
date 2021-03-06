+++
slide = true
title = "Clojure 4"
+++

# Turing Complete & Efficient Programming in Clojure

[!](highlight)

- Function and recursion
- Tail-recursion with `recur`
- `loop` and `recur`
- Infinite sequences with lazy-evaluation

# Turing-complete

[!](columns 8:)

Q:

> Given an input seq of elements, how do we compute 
the cummulative aggregates of each distinct element
seen in the input seq.

A:

> ???
>
> Maybe we can look for a built-in seq function to do this...

[!](split)

<div style="height:300px"></div>

_We need to be able to implement general purpose functions to match the power and
flexibility of Java / Python / ..._

# Looking back at procedural programming

```python
def count_seq(input_seq):
    counts = dict()
    
    for elem in input_seq:
        if elem in counts:
            counts[elem] += 1
        else:
            counts[elem] = 1

    return counts
```

# Rewriting Python with recursion

```{python sm}
def count_seq(input_seq):
    if len(input_seq) == 0:
        return {}
    else:
        first = input_seq[0]
        rest  = input_seq[1:]
        return increment(first, count_seq(rest))
```
[!](note) A recursive formulation

```{python sm}
def increment(key, counts):
    if key in counts:
        counts[key] += 1
    else:
        counts[key] = 1
    return counts
```
[!](note) Increments the count of a key in `counts`.

# Clojure's recursion (version 1)

```{clojure sm clipboard}
(defn inc-or-1 [n] (if (nil? n) 1 (inc n)))

(defn count-seq [xs]
  (if (empty? xs)
    {}
    (let [head (first xs)
          tail (rest xs)]
      (update (count-seq tail) head inc-or-1))))
```
[!](note) Make sure you understand this code.

---

- What is the time complexity?

    > Linear time.

- What is the space complexity?

    > Linear space (why?) and it uses the precious stack.

# Stack Overflow

```clojure
(count-seq (repeat 1000 :a))
; {:a 1000}

(count-seq (repeat 100000 :a))
; StackOverflowError   clojure.core/first--4339
```

[!](note) Can you understand why the stack is being filled up necessarily?

```python
def repeat(n, x): 
    return [x for i in range(n)]

count_seq(repeat(100, "a"))
# {"a": 100}

count_seq(repeat(1000, "a"))
# RuntimeError: maximum recursion depth exceeded
```
[!](note) Python has a more expensive function call, so it cannot hold as many
on its preallocated stack.  The reason is that Python doesn't encourage the
usage of recursion as a scalable programming pattern.

# Tail recursion

Definition: *tail recursion*

> A function `f` uses _tail recursion_ if its recursive call is *always* the last
> step in the function.  Namely, the function must necessarily call itself as:
>
> ```python
def f(...):
    ...
    ...
    return f(...)
    ...
    ...
    return f(...)
```

> Then we say that `f` is tail-recursive.

# Revisit `count_seq` in Python

```{python sm}
def count_seq(input_seq):
    if len(input_seq) == 0:
        return {}
    else:
        first = input_seq[0]
        rest  = input_seq[1:]
        return increment(first, count_seq(rest))
```
[!](note) This is *not* tail-recursion.  Why not?

# Tail recursion version for Python.

```{python sm}
def count_seq(seq, cnt):
    if len(seq) == 0:
        return cnt
    else:
        head = seq[0]
        tail = seq[1:]
        return count_seq(tail, increment(cnt, head))
```
[!](note) This is tail-recursive.

[!](***)

[!](columns 6:)

Good news:

> Tail recursion does not require taking up space on the stack.
>
> <span style=color:red> Why? </span>

[!](split)

Bad news:

> Python doesn't know about tail recursion.

# Tail recursion in Clojure

Clojure gives programmer a special way for a function to call itself if it is
tail-recursive.

```{clojure}
(defn f [<args>]
  ...  (recur <args>) ...)
```

---

```clojure
(defn count-seq [xs cnt]
  (if (empty? xs) 
    cnt 
    (let [head (first xs) 
          tail (rest xs)]
      (recur tail (update cnt head inc-or-1))))) 

(count-seq (repeat 1000000 :b) {})
; {:b 1000000}
```

It's tail-recursive.

# More on Clojure-style

[!](columns 5:)

We prefer:

> `(count-seq <seq>)`

But we had to do:

> `(count-seq <seq> {})`

[!](split)

The solution is to use the multi-arity feature:

```{clojure sm}
(defn count-seq
  ([xs] (count-seq xs {}))
  ([xs cnt] 
    (if (empty? xs)
      cnt
      (recur (rest xs)
             (update cnt 
                     (first xs) inc-or-1)))))
```

# Clojure's general purpose loop

We may want to define a recursion-based computation in an expression.
It's *okay* to define a function each time we need recursion.

```{clojure sm}
(defn count-seq [input-seq]
  (let [f (fn [xs cnt]
            (if (empty? xs)
              cnt
              (recur (rest xs)
                     (update cnt (first xs) inc-or-1))))]
    (f input-seq {})))
```

[!](&&&)

But we can do even better.

We can have a **loop-expression** that is a recursive construct that allows us
to specify:

1. The parameter symbols and their initial values.
2. The body to evaluate the new values for the parameters.


# Clojure's general purpose loop

```{clojure}
(loop [<p1> <exp>
       <p2> <exp> ...]
  (... (recur <new-p1> <new-p2>) ...))
```

[!](***)

Now, we can reimplement count-seq once more:

```{clojure}
(defn count-seq [input-seq]
  (loop [xs input-seq
         cnt {}]
    (if (empty? xs)
      cnt
      (recur (rest xs) (update cnt (first xs) inc-or-1)))))
```

# `count-seq` yet again version

<div style=height:200px></div>

```{clojure clipboard}
(defn increment [cnt key]
  (update cnt key inc-or-1))

(defn count-seq [input-seq]
  (reduce increment {} input-seq))
```

[!](note) If you have trouble understanding this, try it out with the sequence
'(:a :a :b), and work it out by hand.

# `count-seq` the last version

<div style=height:100px></div>

```{clojure}
(defn count-seq [input-seq] (frequencies input-seq))
```

[!](&&&&&&)

```{clojure }
(def count-seq frequencies)
```
[!](note) This is my favourite version :-)

# Lazy Evaluation

[!](highlight)

- Creating infinite sequences

- Tractable recursion without blowing up the stack

# Infinite sequences

```clojure
(def nat (iterate inc 0))
```
[!](note) This is an infinite sequence.  The function `iterate` is used to
create the infinite sequence.

```clojure
(def zeros (repeat 0))
```
[!](note) This is an infinite sequence of zeros.  The function `repeat` creates
the infinite sequence.

[!](***)

What makes _infinity_ possible?

> The computation of each element is performed *only* when that element is
> *required*.
>
> [!](box) This is called _lazy evaluation_.

# Infinite sequences

- How do we make infinite sequences?

- How do we make program with lazy evaluation?

# Introducing `lazy-seq`

```{nosyntax}
user=> (doc lazy-seq)
-------------------------
clojure.core/lazy-seq
([& body])
Macro
  Takes a body of expressions that returns an ISeq or nil, and yields
  a Seqable object that will invoke the body only the first time seq
  is called, and will cache the result and return it on all subsequent
  seq calls. See also - realized?
```

# Lazy-seq

Consider ways of creating a seq consisting of values returned by `(f i)` for
i=1, 2, 3.

```clojure
[(f 1) (f 2) (f 3)]
```
[!](note) Remember that vectors are seqs.

```clojure
`((f 1) (f 2) (f 3))
```
[!](note) Lists are also seqs.

```clojure
(map f (range 100))
```

Say `f` is a very expensive function to invoke:

```{clojure clipboard}
(defn f [x]
  (do (println "zzz..." x)
      (Thread/sleep 1500)
      (str "a long sleep (" x ")")))
```

# Lazy-seq

So what's wrong with this code?

```{clojure}
(take 2 (map f (range 100)))
```

or this code:

```{clojure}
(first (map f (range 10000)))
```

[!](&&&)

Lazy seq to the rescue:

# Lazy-seq

[!](columns 7:)

```{nosyntax sm}
user=> (doc lazy-seq)
-------------------------
clojure.core/lazy-seq
([& body])
Macro
  Takes a body of expressions that returns
  an ISeq or nil, and yields a Seqable
  object that will invoke the body only the 
  first time seq is called, and will cache 
  the result and return it on all subsequent 
  seq calls.
```

[!](split)

```{clojure}
(lazy-seq <expr>)
```

- `<expr>` returns a seq, but it will *not* be called
   until the first element is accessed.

# Creating a lazy-seq version

```clojure
(cons (f 1) nil)                          ;=> ((f 1))
(cons (f 1) (cons (f 2) nil)              ;=> ((f 1) (f 2))
(cons (f 1) (cons (f 2) (cons (f 3) nil)) ;=> ((f 1) (f 2) (f 3))
```

The problem is that they are not lazy.

[!](&&&)

```clojure
(lazy-seq 
  (cons 
    (f 1)
    (lazy-seq
      (cons
        (f 2)
        (lazy-seq
          (cons (f 3) nil))))))
```

[!](note) This is a lazy sequence.

# Creating a lazy-seq version

Let's generalize.

```{clojure clipboard}
(defn fs [n]
  (if (zero? n)
    nil
    (lazy-seq (cons (f n) (fs (dec n))))))
```
[!](note) Note that this is *not* tail-recursive.  But it's *okay*...

[!](***)

Now try out:

```{clojure}
(take 3 (fs 1000))
(first (fs 1000))
```

# Other forms of lazy evaluation

Clojure supports other forms of lazy evaluation.  See `(doc delay)`

# Summary

[!](highlight)

- Tail recursion with recur
- Loop/recur
- Lazy sequences
