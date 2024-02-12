# Exercise 4
## Problem 1
The higher-order functions map and filter can work together in many situations. What will be the result of the following expression?  First, try to figure out the answer and confirm that it is correct by evaluating the expression in ghci. Be able to explain.
```haskell
map (+1) (filter even [1,2,3])
```
This expression maps the increment function to the even elements of the list [1,2,3]. The result is [3].
## Problem 2
Express the following expression using list comprehension. Fill in the blanks in the list comprehension below.

Expression: `map f (filter p xs)`

List comprehension: `[ ___ x | x <- ___, ___ x ]`

```haskell
[ f x | x <- xs, p x ]
```

[Hint: Think about how each component of the expression corresponds to that in the expression given in Question 1.]
## Problem 3
What is the evaluation result of the following expression? Be able to explain step-by-step as shown in slides haskell-04-higher #10 and #11.

```haskell
foldr (:) [3,4] [5,6]
```

This expression applies the cons operator to the elements of the list [5,6] from right to left. The result is [5,6,3,4].
## Problem 4
Consider the evaluation of the following expression and suppose you are to explain by showing the step-by-step of the evaluation. Which would be the first step among the choices?

```haskell
foldr div 3 [12,7,11]
```

Given foldr div 3 [12,7,11], the function f is div, the initial value v is 3, and the list is [12,7,11]. The evaluation unfolds like this:

Initial Call: foldr div 3 [12,7,11]
Apply foldr: This translates to 12 div (foldr div 3 [7,11]).
Apply foldr to [7,11]: This becomes 7 div (foldr div 3 [11]).
Apply foldr to [11]: This becomes 11 div (foldr div 3 []).
Base case with []: The foldr div 3 [] is simply 3, as there are no more elements to process, so foldr div 3 [] = 3.
Reconstructing the calls:

The call with [11] evaluates to 11 div 3, which equals 3 because 11 div 3 performs integer division resulting in 3.
The next call up with [7,11] evaluates to 7 div 3, which equals 2 for the same reason.
Finally, the outermost call with [12,7,11] evaluates to 12 div 2, which equals 6.
## Problem 5
Consider the evaluation of the following expression and suppose you are to explain by showing the step-by-step of the evaluation.  Which would be the first step among the choices?

```haskell
foldl div 40 [4,3,2]
```

Given foldl div 40 [4,3,2], the function f is div, the initial value v is 40, and the list is [4,3,2]. The evaluation unfolds like this:

Initial Call: foldl div 40 [4,3,2]
First Step: Apply div to the initial value 40 and the first element 4, resulting in 40 div 4. This equals 10.
Second Step: Take the result of the first step (10) and apply div with the next element 3, resulting in 10 div 3. This equals 3 because 10 div 3 performs integer division, truncating towards zero.
Third Step: Take the result of the second step (3) and apply div with the last element 2, resulting in 3 div 2. This equals 1, as 3 div 2 also performs integer division.
## Problem 6
Given the following definitions, answer the questions below.

```haskell
data Shape = Circle Float | Rect Float Float 

area (Circle r) = pi * r^2
area (Rect x y) = x * y
```

- What is the type of the following expression? `Rect 3.4`
    - Float -> Shape
- What is the type of function area?
    - Shape -> Float
## Problem 7
Given the following definition,

data Shape = Circle Float | Rect Float Float  deriving Show

You are to write function square that has the following type and meaning.  What is the correct definition of square (i.e., what can go in the underlined space)?

-- Given a Float value as a side length, square returns a rectangular shape with all four sides of equal length

square :: Float -> Shape 

square n = ___
## Problem 8
## Problem 9
## Problem 10
## Problem 11
## Problem 12