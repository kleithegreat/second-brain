# Lazy Evaluation
- Haskell is a **lazy** language, meaning that expressions are not evaluated until their results are needed.
- Useful for infinite structures and modular programming.
## 15.1 Introduction
- Since Haskell is all about the application of pure functions, changing the order of evaluation does not change the meaning of a program.
- This is not the case for imperative languages.
- This can be taken advantage of to improve efficiency.
## 15.2 Evaluation Strategies
- A **reducible expression** or **redex** is an expression that can be reduced to a value.
- For example, `1 + 2` is a redex that can be reduced to `3`.
- When there are multiple redexes in an expression, we can have different evaluation strategies.
- **Innermost evaluation** reduces the innermost redex first, in the sense that it contains no other redexes.
    - This ensures that arguments are always fully evaluated before being passed to a function.
    - Arguments are passed by **value**.
- **Outermost evaluation** reduces the outermost redex first, in the sense that it is contained in no other redex.
    - This ensures that functions are always fully applied before being evaluated.
    - Arguments are passed by **name**.
- Many built-in functions require their arguments to be fully evaluated before they can be applied.
    - For example, `*` and `+` require their arguments to be fully evaluated.
    - Functions like this are called **strict**.
### Lambda expressions
- Lets define a curried version of `mult` that takes arguments one by one and uses a lambda expression to make currying explicit.
    ```haskell
    mult :: Int -> Int -> Int
    mult x = \y -> x * y
    ```
- Using innermost evaluation, we have this example:
    ```haskell
    mult (1+2) (2+3)
    = mult 3 (2+3)
    = (\y -> 3 * y) (2+3)
    = (\y -> 3 * y) 5
    = 3 * 5
    = 15
    ```
- In this example, the arguments are taken one at a time instead of all at once, which is usual for curried functions.
- This is because with innermost evaluation, we evaluate the expressions with no redexes first.
> Note: In Haskell, selection of redexes within the bodies lambda expressions is prohibited. This is due to the rationale that functions are "black boxes", and the only operation that can be performed on a function is applying it to an argument.
- Innermost and outermost evaluation (not within lambda expressions) are called **call-by-value** and **call-by-name** respectively.
## 15.3 Termination
- Say we define the following function:
    ```haskell
    inf :: Int
    inf = 1 + inf
    ```
- This function will never terminate, because it will keep evaluating `inf` forever.
- Say we have the expression `fst (0, inf)`.
    - `fst` selects the first element of a tuple.
    - Using call by value, the expression will not terminate since it will try to evaluate `inf` first.
    - However, using call by name, the expression will terminate and return `0`, since `inf` is never evaluated.
- **If theres any evaluation sequence that terminates, then call by name will terminate.**
- Call by name is preferable to call by value since it ensures termination more often.
## 15.4 Number of Reductions
- Say we have the following:
    ```haskell
    square :: Int -> Int
    square n = n * n
    ```
- Using call by value, the expression `square (1+2)` will be reduced as follows:
    ```haskell
      square (1+2)
    = square 3
    = 3 * 3
    = 9
    ```
- However, call by name will require one more reduction:
    ```haskell
      square (1+2)
    = (1+2) * (1+2)
    = 3 * (1+2)
    = 3 * 3
    = 9
    ```
- Sometimes call by name will result in more reductions than call by value, especially when there are multiple occurrences of the same argument.
- **Call by value evaluates each argument at most once, while call by name may evaluate an argument many times.**
- Good thing is this problem can be solved using pointers to indicate sharing of arguments.
- Lazy evaluation combines call by name with sharing of arguments.
## 15.5 Infinite Structures
- Lazy evaluation allows for programming with infinite structures, which may seem impossible at first.
- Suppose we try `head [1..]`.
    - `head` selects the first element of a list.
    - `[1..]` is an infinite list of all natural numbers.
    - Using call by value, this expression will not terminate since it will try to evaluate `[1..]` first.
    - However, using call by name, the expression will terminate and return `1`, since `[1..]` is never evaluated.
- Under lazy evaluation, seemingly infinite lists are only **potentially infinite**, evaluated as much as needed.
    - This applies to not just lists, but all data structures.
    - Another popular structure is the binary tree.
## 15.6 Modular Programming
- Lazy evaluation allows us to separate **control** from **data**.
    - For example, we can produce a list of three ones by selecting the first three elements (control) of an infinite list of ones (data).
- However, nontermination can still occur if the control is not strict enough.
    - For example, `filter (<= 5) [1..]` will not terminate since it keeps testing the next element of the list.
    - However, `takeWhile (<= 5) [1..]` will terminate since it stops testing once the condition is false.
### Sieve of Eratosthenes
- The **Sieve of Eratosthenes** is an algorithm for generating an infinite list of prime numbers.
- It follows these steps:
    1. Write down the list of all natural numbers greater than 1.
    2. Mark the first number $p$ in the list as prime.
    3. Delete all multiples of $p$ from the list.
    4. Repeat from step 2.
- The first and third steps require potentially infinite work.
- The following is the Haskell implementation of the Sieve of Eratosthenes:
    ```haskell
    primes :: [Int]
    primes = sieve [2..]

    sieve :: [Int] -> [Int]
    sieve (p:xs) = p : sieve [x | x <- xs, x `mod` p /= 0]
    ```
- Lazy evaluation allows us to write the algorithm as if it were a finite list.
## 15.7 Strict Application
- Haskell also provides a **strict** version of function application.
- Strict application is denoted by `$!`.
- For example, `f $! x` is the same as `f x`, except `x` is evaluated before being passed to `f`.