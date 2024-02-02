# Introduction
## 1.1 Functions
- A *function* is a mapping that takes one or more arguments and produces a single result.
- Functions in Haskell are defined using an equation with the following:
    - A name for the function
    - Names for each of the arguments
    - A body that specifies how the result can be computed in terms of the arguments
- *Example:* `double x = x + x`
    - The name of the function is `double`
    - The argument is `x`
    - The body is `x + x`
- When a function is applied, it can result in either a plain value or more commonly, an expression containing other functions.
- *Example:* `double 3` results in `3 + 3` which is another expression, which finally results in `6`.
- *Example:* `double (double 2)` results in `double (2 + 2)` which is another expression, which finally results in `8`.
## 1.2 Functional Programming
- Functional programming is a style of programming where the basic method of computation is the application of functions to arguments.
- A functional programming language is one that supports and encourages the functional paradigm.
### Example: Imperative vs. Functional Sum
Imperatively, summing the first n integers would look something like this, using a loop:
```java
int sum = 0;
for (int i = 1; i <= n; i++) {
    sum += i;
}
```
Here, the basic method of computation is *changing stored values*.

Functionally, summing the first n integers would look something like this:
```haskell
sum [1..n]
```
In Haskell, `sum` and `[..]` are both functions. 
The `..` function takes two arguments, a starting value and an ending value, and returns a list of all the values in between.
The `sum` function takes a list of numbers and returns the sum of those numbers.
The basic method of computation is *applying functions to arguments*.
## 1.3 Features of Haskell
- **Concise programs** - Haskell programs are typically much shorter than their counterparts in other languages.
- **Powerful type system** - Haskell allows for a large class of errors to be caught at compile time and supports very general forms of polymorphism and overloading.
- **List comprehensions** - A concise way to create new lists by filtering and transforming existing lists.
- **Recursive functions** - Imperative style loops are replaced by recursive functions which are often more concise and elegant, especially when *pattern matching* and *guards* are used.
- **Higher-order functions** - Functions can take other functions as arguments and return functions as results.
- **Effectful functions** - Although Haskell is a pure functional language, it allows for functions that have side effects such as input/output, using *monads* and *applicatives*.
- **Generic functions** - skull emoji
- **Lazy evaluation** - Computations are not performed until their results are needed, resulting in more efficient programs.
- **Equational reasoning** - what even is this
## 1.4 Historical Background
skipping lmao
## 1.5 A Taste of Haskell
A few examples to elucidate the feel of Haskell.
### Summing numbers
The sum function from earlier can be defined using only two lines of code:
```haskell
sum [] = 0
sum (n:ns) = n + sum ns
```
The line is the base case of the function, which is the case where the list is empty.
The second line is the recursive case of the function, which states any non-empty list made of a first element `n` and a rest of the list `ns` is the sum of `n` and the sum of `ns`.
Thus, `sum [1, 2, 3]` evaluates to the following:
```
1 + sum [2, 3]
1 + (2 + sum [3])
1 + (2 + (3 + sum []))
1 + (2 + (3 + 0))
6
```
The sum function has the type signature:
```haskell
sum :: Num a => [a] -> a
```
The above type signature can be broken down into:
- `sum` is the name of the function
- `::` is read as "has type"
- `Num a =>` is a class constraint. `Num` is a type class, and `a` is a type variable. 
    - This constraint states that `a` must be a member of the `Num` type class. 
    - Haskell has many types of numbers like floats and integers
    - This can be read as "for all types `a` that are members of the `Num` type class"
- `[a] -> a` is the actual type signature of the function. 
    - `[a]` is a list of elements of type `a`
    - The signature indicates that the function takes a list of elements of type `a` and returns a single element of type `a`

Type signatures allow for the compiler to catch errors before the program is run.
Every time a function is called, a check is made if the arguments provided match the type signature of the function.
### Sorting values
Suppose we define the following function:
```haskell
qsort [] = []
qsort (x:xs) = qsort smaller ++ [x] ++ qsort larger
               where
                    smaller = [a | a <- xs, a <= x]
                    larger = [b | b <- xs, b > x]
```
- `++` is a function that appends two lists together.
- `where` is a keyword that introduces a local definition.
    - We defined `smaller` as all elements `a` in `xs` such that `a <= x`.
    - We defined `larger` as all elements `b` in `xs` such that `b > x`.

Our `qsort` function is a recursive implementation of quicksort.
For each recursive call, we take the first element of the list and partition the rest of the list into two lists, one containing all elements smaller than the first element and one containing all elements larger than the first element.

`qsort` is more general than exepected, as it can sort any list of elements that can be compared using the `<=` and `>` operators.
It has the following type signature:
```haskell
qsort :: Ord a => [a] -> [a]
```
This type signature can be interpreted as "for all types `a` that are members of the `Ord` type class, `qsort` takes a list of elements of type `a` and returns a list of elements of type `a`".
### Sequencing actions
Consider a function `seqn` that takes a list of IO actions (like reading or writing characters), performs each action sequentially, and returns a list of the resulting values.
```haskell
seqn [] = return []
seqn (act:acts) = do x <- act
                     xs <- seqn acts
                     return (x:xs)
```
The first line states that the empty list of actions results in the empty list.
Otherwise, we perform the first action, bind the result to `x`, perform the rest of the actions, bind the result to `xs`, and return the list `x:xs`. The final list is the result of performing all the actions in sequence.

For example, `seqn [getChar, getChar, getChar]` would result in the following:
```
> seqn [getChar, getChar, getChar]
abc"abc"
```
The interesting part of this function is its type. One possible type inferred from this is:
```haskell
seqn :: [IO a] -> IO [a]
```
This type states that `seqn` maps a list of IO actions that produce results of some type `a` to a single IO action that produces a list of results of type `a`.
> This definition makes clear that this function is not a pure function, as it performs IO actions. However, this function is not specific to just IO, but can be used for anything impure involving side effects, such as changing stored values, fail to succeed, write to a log file, etc.
```haskell
seqn :: Monad m => [m a] -> m [a]
```
This means for any monadic type `m` and any type `a`, `seqn` maps a list of actions of type `m a` to a single action that returns a list of results of type `a`.
> Monads get much more complex, but the basic idea is that they are a way to encapsulate computations that have side effects.