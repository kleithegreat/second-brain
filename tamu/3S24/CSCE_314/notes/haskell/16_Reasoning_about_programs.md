# Reasoning About Programs
Equational reasoning can be used to prove properties of programs. 
## 16.1 Equational reasoning
- The algebraic axioms allow us to use more efficient implementations of functions without changing the meaning of the program.
- For example, $x(y+z)$ is the same as $xy+xz$, but the number of operations is different.
## 16.2 Reasoning about Haskell
- The same style of reasoning can be applied to Haskell programs.
- We would use the mathematical equality operator instead of the Haskell equality operator.
> We want to use math as a language to reason about Haskell, not use Haskell as a language to reason within itself (which would be circular).
- Not only can we use mathematical axioms, but we can also use equations in user-defined functions.
- For example, consider the following function:
    ```haskell
    double :: Int -> Int
    double x = x + x
    ```
- The equation `double x = x + x` is both the **definition** of the function as well as being a **property** that can be used to reason about the function.
    - This implies that `double x` can be freely replaced by `x + x` in any context.
    - `x + x` can be replaced by `double x` in any context.
- Function definition can be **applied** from left to right or **unapplied** from right to left.
- We must be cognizant when reasoning with functions with multiple equations.
    - For example, consider a function that decides if an integer is zero:
        ```haskell
        isZero :: Int -> Bool
        isZero 0 = True
        isZero n = False
        ```
    - The first equation `isZero 0 = True` can be freely applied bidirectionally.
    - The second equation `isZero n = False` can be applied bidierectionally only given that the first equation does not apply.
- Generally, we cannot view equations of a function with multiple equations as logical properties in isolation of each other.
- The order of pattern matching is important.
- Thus it is preferable to define functions such that the order of equations does not matter.
    - For example, consider the earlier `isZero` function:
        ```haskell
        isZero 0 = True
        isZero n | n /= 0 = False
        ```
    - The second equation can now be freely applied bidierectionally due to the guard.
- Patterns that do no rely on the order of equations are called **non-overlapping**.
- Using non-overlapping patterns whenever possible is a good practice.
## 16.3 Simple examples
- Let's use the `reverse` function to demonstrate equational reasoning.
    ```haskell
    reverse :: [a] -> [a]
    reverse [] = []
    reverse (x:xs) = reverse xs ++ [x]
    ```
- Using this function definition we can show that `reverse` has no effect on singleton lists.
    ```haskell
      reverse [x]  
    = reverse (x:[])  -- list notation
    = reverse [] ++ [x]  -- applying reverse
    = [] ++ [x]  -- applying reverse
    = [x]  -- applying ++
    ```
- Thus, we can freely replace `reverse [x]` with `[x]` in any context, which is more efficient than evaluating `reverse [x]`.
- Equational reasoning is often combined with some form of case analysis.
    - For example, consider the logical negation function:
        ```haskell
        not :: Bool -> Bool
        not True = False
        not False = True
        ```
    - The property that `not` is its own inverse can be proven by case analysis:
        ```haskell 
          not (not False)
        = not True
        = False
        ```
## 16.4 Induction on numbers

## 16.5 Induction on lists

## 16.6 Making append vanish

## 16.7 Compiler correctness
