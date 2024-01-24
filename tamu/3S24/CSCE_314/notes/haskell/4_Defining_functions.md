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
- You can choose bewteen possible results using **conditional expressions**.
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

### Tuple Patterns

### List Patterns

## 4.5 Lambda Expressions

## 4.6 Operator Sections