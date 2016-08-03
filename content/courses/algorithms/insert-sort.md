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

We need functions.


