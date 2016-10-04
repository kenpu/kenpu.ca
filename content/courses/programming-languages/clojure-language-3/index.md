+++
slide = true
title = "Clojure 3"
+++

# Clojure Part III

[!](highlight)

# Data Read & ~~Write~~ & Transformation

- List

- Vector

- Map

- Set

# List

Create

> - `(...)`
> - `(list ...)`

Read

> - `(first seq)`
> - `(nth seq n)`

Transformation

> - `(cons elem seq)`
> - `(conj seq elem ...)`
> - `(rest)`

# Vector

[!](columns 6:)

Create

> - `[ ... ]`
> - `(vector ...)`
> - `(vec seq)`

Read: Vectors are _functions_.

> - `(v n)`
> - `(get v n)`
> - `(nth v n)`, `(first ...)` still apply.

[!](split)

Transformation

> - `conj`, `cons`, `rest` still apply.
- `(assoc v n val)`
- `(update v n func)`
- `(subvec v start end)`
- `(replace map v)`

# Map

[!](columns 6:)

Create

> - `{ ... }`
- `(hash-map ...)`
- `(array-map ...)`

Read: maps are functions, and keywords are functions!!

> - `(m key)`
- `(:keyword m)`
- `(get m key default-val)`
- `(keys m)`
- `(vals m)`
- `(contains? m key)`

[!](split)

Transform

> - `(assoc m key val)`
- `(assoc-in m [path] val)`
- `(dissoc m key)`
- `(merge m1 m2 ...)`
- `(merge-width f m1 m2 ...)`
- `(select-keys m [keys])`
- `(update m key func)`
- `(update-in m [path] func)`
- `(rename-keys m rename-map)`

# Sequences

[!](highlight)


