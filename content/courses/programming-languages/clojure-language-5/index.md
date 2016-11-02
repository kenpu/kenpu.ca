+++
title = "Symbols, bindings and namespaces"
slide = true
+++

# Symbols

- Symbols

- Binding & Scopes

- Resolution

# Clojure scoping rules

- (Many) global scope (called namespaces)

- `(fn [...] ...)`

- `(let [...] ...)`

# Resolution

- Lexical scoping rule

- Closure <span class="label label-primary" style=font-size:70%;margin-left:40px;padding:5px>IMPORTANT</span>

- Associating values with functions with closure in Clojure.

# Namespaces

- Overview of the namespace management

- Creating namespaces `(ns <name>)`

- Switching namespaces `(in-ns <quoted-sym>)`

- Quantified symbol names

- Resolution with namespaces

# Polymorphism

**Definition**: _Polymorphism_

> The implementation of a function is determined at _runtime_ based on the
> argument types.

[!](***)

**Example**


```{clojure sm}
(defn parking-fee [person num-months] ...)
```

There are two types of persons:

> - Faculty members, who pay $2000.00 / year for parking
- Students, who pay $40.00 / month for parking

What is the best way to implement `parking-fee`?

[!](note) Polymorphism is the solution...

# An non-polymorphic solution

Use branching `if`, `cond`, `case`, ...

```clojure
(defn parking-fee [person num-months]
  (case (:type person) 
    :faculty (* (/ 2000.0 12) num-months)
    :student (* 40 num-months)
    nil))
```

> This is bad for several reasons?
>
> - How many different types of `person` are there?
> - How much duplication in abstraction?
> - There is a single point failure.
> - How do we maintain consistency when new person type is added?
> [!](note)

Consider the matrix of dependencies:

> | Function | `:student` | `:faculty` | `:staff` | `:visitor` |
|----------|------------|------------|----------|------------|
| `parking-fee` | | | |
| `tuition` |
>
> [!](note 9)

# Polymorphism using multimethod

```clojure
(defmulti <fn> <dispatcher>)

...

(defmethod <fn> [dispatching-values...]
  [arg...]
  (__ body __))
  
(defmethod <fn> [dispatching-values...]
  [arg...]
  (__ body __))
```

# Example

```clojure
(defmulti parking-fee (fn [person num-months] (:type person)))

; faculty parking-fee rate is $2000/year
(defmethod parking-fee :faculty
  [person num-months]
  (* num-months (/ 2000.0 12)))

; student parking-fee rate is $40/month
(defmethod parking-fee :student
  [person num-months]
  (* num-months 40.0))

; no other types are supported
(defmethod parking-fee :default
  [person num-months]
  nil)
```

# Example

```clojure
; ============================
; test the code
; ============================

(let [einstein {:type :faculty
                :name "Albert Einstein"}
      jack {:type :student
            :name "Jack"}]
  (doseq [person [einstein jack]]
    (printf "%s pays $%.2f for 5 months of parking.\n" 
            (:name person)
            (parking-fee person 5))))
```

> ```nosyntax
Albert Einstein pays $833.33 for 5 months of parking.
Jack pays $200.00 for 5 months of parking.
```

# Protocols

[!](highlight)

## Clojure's solution to interfaces

# Protocols 

- A protocol defines a set of function _symbols_, and their "signatures".

    > Since Clojure does not support static types, a function signature
    is basically the arity of the function.

Protocol is a heavy-lifting language feature, many of which are impossible to do
in a language like _Java_.

1. We can define _types_ and _records_ that implement one or more _protocols_.

1. We can _extend_ an existing types to implement a protocol.

1. We can create an instance that implements one or more protocols without
  declaring a type.


# Defining the protocol

```clojure
(defprotocol <name>
    (<fun-name> [ <args> ... ])
    (<fun-name> [ <args> ... ])
    ...)
```

# Example

```clojure
(defprotocol IPayee
    (parking [person months])
    (tuition [person credits]))
```

[!](***)

How do we create implementations of `IPayee`?

> ```clojure
; total cost of completing a 40-credit semester in
; 4 months.
(let [x (... make-a-payee ...)]
    (+ (parking x 4) (tuition x 40)))
```

# Type

[!](highlight)

## Clojure's solution for _classes_

# Creating a type

A type consists of:

> 1. a constructor
> 2. a list of protocols that it implements
> 3. the set of functions 

[!](***)

```clojure
(deftype <type-name> [<args> ...]
  <protocol>
  (<method> [args ...] ( ... body ... ))
  (<method> [args ...] ( ... body ... ))
  ...)
```

# Example: implementation

[!](columns 5:)

```{clojure sm}
(defprotocol IPayee
  (parking [person months])
  (tuition [person credits]))
```

[!](split)

A type for faculty
```{clojure sm}
(deftype Faculty [name]
  IPayee
  (parking [person months]
    (if (= name "Albert Einstein")
      0
      (* months (/ 2000.0 12))))
  (tuition [person credits]
    (if (= name "Richard Feynman")
      0
      (* 1.0 credits))))
```

A type for student
```{clojure sm}
(deftype Student [name]
  IPayee
  (parking [person months] (* months 40.0))
  (tuition [person credits] (* credits 100.0)))
```

# Example: data

Constructor functions are automatically generated and bound to symbols
`<class-name>`<b style=color:red;font-size:200%>.</b>

```clojure
(let [albert (Faculty. "Albert Einstein")] ...)
```

# Example: data

[!](columns 6:)

```{clojure sm}
(deftype Faculty [name]
  IPayee
  (parking [person months]
    (if (= name "Albert Einstein")
      0
      (* months (/ 2000.0 12))))
  (tuition [person credits]
    (if (= name "Richard Feynman")
      0
      (* 1.0 credits))))
```

```{clojure sm}
(deftype Student [name]
  IPayee
  (parking [person months] 
    (* months 40.0))
  (tuition [person credits] 
    (* credits 100.0)))
```

[!](split)

```{clojure sm}
(let [p1 (Faculty. "Albert Einstein")
      p2 (Faculty. "Richard Feynman")
      p3 (Student. "Jack")]
  (println "P1" (parking p1 5))
  (println "P2" (parking p2 5))
  (println "P3" (parking p3 5)))
```

[!](***)

*Issues* (or features)

> In the scope of methods, we can access the `name` symbol (and its binding).
>
> But outside the scope, we *cannot* access the `name` symbol.

# Records

[!](highlight)

## Clojure's solution to classes with properties

# Records

Records are defined like _types_, but behaves (almost) like _hash-maps_.

---

### Declaration of record _type_

```clojure
(defrecord <name> [args ...]
  <protocol>
  (method ...)
  (method ...)
  ...)
```

# Example:

[!](columns 6:)

The type implementation

```{clojure sm}
(deftype Faculty [name]
  IPayee
  (parking [person months]
    (if (= name "Albert Einstein")
      0
      (* months (/ 2000.0 12))))
  (tuition [person credits]
    (if (= name "Richard Feynman")
      0
      (* 1.0 credits))))
```

[!](split)

The record implementation

<pre>(<b style="color:blue">defrecord</b> Faculty [name]
  IPayee
  (parking [person months]
    (if (= name "Albert Einstein")
      0
      (* months (/ 2000.0 12))))
  (tuition [person credits]
    (if (= name "Richard Feynman")
      0
      (* 1.0 credits))))
</code></pre>

# Example:

```clojure
(defn report [person months credit]
  (println (:name person) 
           "needs to pay:"
           (+ (parking person months)
              (tuition person credits))))
```

---

Records act just like hashmaps:

```
(let [person (Student. "Jack")]
  (assoc person :name "Jim"
                :grade "A+"))
```

# Extending existing types

[!](highlight)

## Adhoc patching up existing classes

# Compare to Java

`defprotocol` = Interfaces

`deftype` = Classes with private members

`defrecord` = Classes

---

`extend-type`, `extend-protocol` have no equals in Java.

# Extend

What is a _type_?

> A type is a Java class or a previously defined Clojure type by `deftype` or
> `defrecord`.

[!](***)

Given a type `T`, we can make it implement one or more protocols with
`extend-type`.

```clojure
(extend-type T
    <protocol>
    (<method> [...] (...body...))
    (<method> [...] (...body...))
    ...

    <protocol>
    ...)
```

# Example

Can a string be a payee?  Sure.

```{clojure sm}
(extend-type java.lang.String
  IPayee
  (parking [s months] (* months (Float/parseFloat s)))
  (credits [s credits] (* credits (Float/parseFloat s))))
```

[!](***)

Wow, we can do some crazy stuff:

```clojure
(parking "3.14" 4)
(tuition "6.2" 40)
```

# Reify

[!](highlight)

_re·i·fy_ <br>
/ˈrēəˌfī/

> verb <br>
> make (something abstract) more concrete or real. <br>
> _"these instincts are, in humans, reified as verbal constructs"_

# Example

```clojure
(reify
  IPayee
  (parking [x months] ...)
  (tuition [x credits] ...))
```

# Summary

[!](highlight)

- Polymorphism is a fundamental tool in organizing code.

- Multimethod is a lightweight language feature to implement polymorphism.

- Protocol is a more object-oriented feature of the language to organize
  (unimplemented) functions into interfaces.

- There are several ways providing implementations:

    > 1. Define a type or record from scratch to implement the protocol.
    > 2. Extend an existing type with additional methods to implement the
    protocol.
    > 3. Creating an object that implements the protocol using `reify`.




