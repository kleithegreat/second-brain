# Exercise 3
## Problem 1
The min function accepts two values of an instance type of Ord and returns the smaller of the two.  Here we want to define it using if conditional expressions.  Complete the definition of the min function by filling in the blanks with the answer chosen from the following eight choices (with correct spelling and correct capitalization; each blank holds only one choice; one choice can be used more than once).

Choices: `min`, `if`, `then`, `else`, `otherwise`, `=`, `x`, `y`
```haskell
min x y __ __ x <= y __ y __ x
```

```haskell
min x y = if x <= y then x else y
```
## Problem 2
The min function accepts two values of an instance type of Ord and returns the smaller of the two.  Here we want to define it using guarded expressions (guards).  Complete the definition of the min function by filling in the blanks with the answer chosen from the following eight choices (with correct spelling and correct capitalization; each blank holds only one choice; one choice can be used more than once).

Choices: `min`, `if`, `then`, `else`, `otherwise`, `=`, `x`, `y`
```haskell
min x y | x <= y __ x 
        | __ __ y
```
    
```haskell
min x y | x <= y = x
        | otherwise = y
```
## Problem 3
What is the type of the min function?
```haskell
min :: Ord p => p -> p -> p
```
## Problem 4
Study the definitions for take in the haskell-03-functions lecture slides #3 and #5. And then, complete the definition of take below so that it uses only one argument pattern   n  xs   with three guards, where the first guard checks if n is less than or equal to zero (the first base case), the second guard uses the Prelude function null to check whether the list argument xs is empty (the second base case), and the third guard is for all other cases (using otherwise) where the recursion occurs.  Assume the three guards below are aligned.  Choose your answers from the following nine choices (with correct spelling and correct capitalization; each blank holds only one choice; one choice can be used more than once).

Choices: `head`, `tail`, `take`, `null`, `[]`, `otherwise`, `n`, `(n-1)`, `xs`
```haskell
take n xs | __ <= 0 = __
          | __ xs = __
          | __ = __ xs : __ (n-1) (__ xs)
```

```haskell
take n xs | n <= 0 = []
          | null xs = []
          | otherwise = head xs : take (n-1) (tail xs)
```
## Problem 5
What is the evaluation result of the following expression (list comprehension)?

`[(x,y) | x <- [1,2,3], y <- [4,5]]`

[(1,4),(1,5),(2,4),(2,5),(3,4),(3,5)]
## Problem 6
What is the evaluation result of the following expression (list comprehension)?

`[(x,y) | x <- [4,5], y <- [1,2,3]]`

[(4,1),(4,2),(4,3),(5,1),(5,2),(5,3)]
## Problem 7
What is the evaluation result of the following expression (list comprehension)?  The answer is a number between 0 and 100.  Be able to explain.

`sum [ y | x <- [4,5], y <- [1,2,3], even (x*y) && odd x]`

This takes the sum of a list comprehension with a guard at the end. The list comprehension can be read as all ys such that when we take every combination of x and y where x can be 4 or 5 and y can be 1, 2, or 3, x times y is even and x is odd. Since the only odd value of x is 5, we can just ignore 4. 1 * 5 = 5 is odd, 2 * 5 = 10 is even, 3 * 5 = 15 is odd. Thus the only element in the list is 2 since that is the only y that satisfies the guard, and the sum of the list is 2.