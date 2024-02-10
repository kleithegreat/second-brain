# Defining Functions
Haskell has a range of mechanisms for defining functions.
## 4.1 New from Old
- New functions can be defined by combining existing functions.
    - Example:
        ```haskell
        even :: Integral a => a -> Bool
        even n = n `mod` 2 == 0
        ```
## 4.2 Conditional Expressions
- You can choose between possible results using **conditional expressions**.
    - Example:
        ```haskell
        abs :: Int -> Int
        abs n = if n >= 0 then n else -n
        ```
- Conditional expressions can be nested.
    - Example:
        ```haskell
        signum :: Int -> Int
        signum n = if n < 0 then -1 else
                   if n == 0 then 0 else 1
        ```
- In Haskell, conditional expressions must have an `else` branch.
    - This avoids the **dangling else** problem.
## 4.3 Guarded Equations
- A **guarded equation** is a sequence of logical expressions called **guards** to choose between possible results of the same type.
    - If the first guard is `True`, the first result is chosen.
    - If the first guard is false and second guard is `True`, the second result is chosen, and so on.
    - Example:
        ```haskell
        abs n | n >= 0    = n
              | otherwise = -n
        ```
- The symbol `|` is read as "such that".
- The symbol `otherwise` is defined in the standard prelude by `otherwise = True`.
- Definitions with multiple guards are often easier to read than the equivalent conditional expression.
## 4.4 Pattern Matching
- Many functions have a simple and intuitive definition using **pattern matching**.
- Pattern matching is where a sequence of syntactic expressions called **patterns** are used to choose between possible results of the same type.
    - If the first pattern matches the value, the first result is chosen.
    - If the first pattern fails to match the value, the second pattern is tried, and so on.
    - Example:
        ```haskell
        not :: Bool -> Bool
        not False = True
        not True  = False
        ```
- Pattern matching also works for functions of multiple arguments.
    - Example:
        ```haskell
        (&&) :: Bool -> Bool -> Bool
        True  && True  = True
        True  && False = False
        False && True  = False
        False && False = False
        ```
    - This definition can be simplified by combining the last three equations into one.
        ```haskell
        (&&) :: Bool -> Bool -> Bool
        True  && b = b
        _ && _ = False
        ```
- The **wildcard pattern** `_` can be used to match any argument value.
- Also, Haskell does not permit using the same name for more than one argument in a single function.
### Tuple Patterns
- A tuple of patterns is itself a pattern.
- It is matched when there is a tuple of the same arity and corresponding components have the same patterns.
- Example:
    ```haskell
    fst :: (a, b) -> a
    fst (x, _) = x
    ```
### List Patterns
- A list of patterns is also a pattern.
- Matched when the list has the same length and elements all match the corresponding elements in order.
- Example: say the function `test` determines whether a list starts with `a` and has three elements.
    ```haskell
    test :: [Char] -> Bool
    test ['a', _, _] = True
    test _           = False
    ```
- Lists can also be constructed one element at a time from the empty list.
- The `:` operator *cons* constructs a new list by prepending a new element to the start of an existing list.
- For example, the list `[1, 2, 3]` can be constructed as follows:
    ```haskell
    1 : (2 : (3 : []))
    ```
- To save on parentheses, the `:` operator associates to the right.
    ```haskell
    1 : 2 : 3 : []
    ```
- In addition to lists, the cons operator can also be used to construct patterns.
- Example:
    ```haskell
    head :: [a] -> a
    head (x : _) = x
    ```
- Note that in this case, the cons operator must be parenthesized since function application has a higher priority.
## 4.5 Lambda Expressions
- These are one alternative to defining functions using equations.
- A lambda expression is comprised of a pattern for each of the arguments as well as a body that uses these arguments.
- However, there is no name for these functions.
- For example, the lambda expression `\ x -> x + x` doubles its argument.
- The symbol `\` represents the Greek letter lambda.
- Despite being nameless, lambda functions can be used like any other function.
    - Example:
        ```haskell
        > (\ x -> x + x) 2
        4
        ```
- Lambda expressions can be used for formalizing the meaning of curried function definitions.
    - Example: The following are equivalent.
        ```haskell
        add :: Int -> Int -> Int
        add x y = x + y

        add :: Int -> (Int -> Int)
        add = \ x -> (\ y -> x + y)
        ```
- Additionally, lambda expressions are useful for defining functions that return functions as results.
    - Example: 
        ```haskell
        const :: a -> b -> a
        const x _ = x

        const :: a -> (b -> a)
        const x = \ _ -> x
        ```
- Lambda expressions can also be used to avoid naming functions that are only referenced once.
    - Example: This function returns a list of `n` odd numbers.
        ```haskell
        odds :: Int -> [Int]
        odds n = map f [0..n-1]
                 where
                   f x = x * 2 + 1

        odds :: Int -> [Int]
        odds n = map (\ x -> x * 2 + 1) [0..n-1]
        ```
## 4.6 Operator Sections
- Functions like `+` are called **operators** since they are written between two arguments.
- Any function can be made into an operator by enclosing its name in backticks.
- Also, any operator can be made into a curried function by enclosing it in parentheses.
    - Example:
        ```haskell
        > 1 + 2
        3
        > (+) 1 2
        3
        > mod 10 3
        1
        > 10 `mod` 3
        1
        ```
- Generally, if `#` is an operator, then the expressions `(#)`, `(x #)` and `(# y)` for arguments `x` and `y` are called **sections**.
- Formally, the following are equivalent.
    ```haskell
    (#) = \x -> (\y -> x # y)
    (x #) = \y -> x # y
    (# y) = \x -> x # y
    ```
- Sections are useful for constructing functions that are partially applied.
- The following are some common examples.
    ```haskell
    (+) -- the addition function \x -> (\y -> x + y)
    (1+) -- the successor function \x -> 1 + x
    (1/) -- the reciprocation function \x -> 1 / x
    (*2) -- the doubling function \x -> 2 * x
    (/2) -- the halving function \x -> x / 2
    ```
- Sections are also necessary for stating types of operators, since operators themselves are not valid expressions in Haskell.
- Sections are necessary when using them as arguments to higher-order functions.
    - Example: The sum function as a fold.
        ```haskell
        sum :: [Int] -> Int
        sum = foldr (+) 0
        ```