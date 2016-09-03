+++
slide = true
+++

# Computation in practice

- Languages based on stateful computation

- Languages based on functional computation

- Hybrid languages

# Stateful computation

[!](columns 4:)

Languages

> - Javascript
> - Python

Task

> Quicksort

[!](split)

```python
X = [6, 3, 4, 8, 1, 4]

def quicksort(X, i, j):
  if i < j:
    p = partition(X, i, j)
    quicksort(X, i, p-1)
    quicksort(X, p+1, j)

def partition(X, i, j):
  pivot = X[j]
  m = i
  for n in range(i, j):
    if X[n] <= pivot:
      X[m], X[n] = X[n], X[m]
      m += 1
  X[m], X[j] = X[j], X[m]
  return m

def QuickSort(X):
  return quicksort(X, 0, len(X)-1)
```

# Breakdown of python 

<div pdf="qsort-py.pdf" scale=0.8></div>



# Python v.s. Javascript

[!](columns 6:)

<script
src="https://gist.github.com/kenpu/e2e3fcc9feea16fb14a84c7ec98cdd75.js?file=qsort.py"></script>

[!](split)

<div style=height:600px;overflow:auto>
<script
src="https://gist.github.com/kenpu/e2e3fcc9feea16fb14a84c7ec98cdd75.js?file=qsort.js"></script>
</div>


