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
    - The second equation `isZero n = False` can be applied bidirectionally only given that the first equation does not apply.
- Generally, we cannot view equations of a function with multiple equations as logical properties in isolation of each other.
- The order of pattern matching is important.
- Thus it is preferable to define functions such that the order of equations does not matter.
    - For example, consider the earlier `isZero` function:
        ```haskell
        isZero 0 = True
        isZero n | n /= 0 = False
        ```
    - The second equation can now be freely applied bidirectionally due to the guard.
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
- Reasoning on recursive equations often use **induction**
- Since many functions in Haskell are recursive induction can be used
- The simplest example is the definition of the natural numbers:
    ```haskell
    data Nat = Zero | Succ Nat
    ```
    - `data Nat` declares a new type `Nat` with two constructors `Zero` and `Succ`.
    - `Succ Nat` is a recursive constructor that takes a `Nat` type as an argument, representing the successor of a natural number.
- Suppose we want to prove some property $p$ holds for all (finite natural numbers)
> In this example we will only consider the finite natural numbers, meaning we start with zero and apply `Succ` a finite number of times.
- The principle of induction states that it is sufficient for us to prove that $p$ is true for the base case (zero) and is preserved by `Succ` (the **inductive case**).
    - More formally: The inductive case requires that the property $p$ holds for any natural number, called the **induction hypothesis**.
    - This works because we defined the natural numbers as a base case and a recursive case.
    - You can think of this as a domino effect, if we can prove that the first domino falls, and that if any domino falls, the next one will fall, then all the dominos will fall.
## 16.5 Induction on lists
- Induction works naturally on recursion, and since lists can be built from the empty list using the cons operator, induction also works nicely on lists.
- The induction principle for lists states that we must show that $p$ holds for the empty list as well as any list `xs`.
	- If we can show this, then $p$ holds for `x:xs` for any element `x`.
- For example, we can show the function `reverse` is its own inverse.
	- This means we want to show `reverse (reverse xs) = xs` using induction.
	- The base case is easy:
        ```haskell
          reverse (reverse [])
        = reverse []
        = []
        ```
    - Using the assumption `reverse (reverse xs) = xs` we can show that `reverse (reverse (x:xs)) = x:xs`:
        ```haskell
          reverse (reverse (x:xs))
        = reverse (reverse xs ++ [x])
        -- applying the inner reverse
        = reverse [x] ++ reverse (reverse xs)
        -- distributivity
        = [x] ++ reverse (reverse xs)
        -- singleton list
        = [x] ++ xs
        -- induction hypothesis
        = x:xs  -- applying ++
        ```
    - This used two properties of `reverse`:
        1. Reverse of singleton list is itself: `reverse [x] = [x]`
        2. Reverse distributes over append, except the order is then reversed: `reverse (xs ++ [x]) = reverse [x] ++ reverse xs`
            - Technically we say here that the distribution is *contravariant*.
## 16.6 Making append vanish
- Many recursive functions use the append operator `++`.
- However, the append operator is not very efficient.
- Induction can be used to eliminate some uses of `++`.
- As a motivating example, consider the following definition of `reverse`:
    ```haskell
    reverse :: [a] -> [a]
    reverse [] = []
    reverse (x:xs) = reverse xs ++ [x]
    ```
    - The append operation `xs ++ ys` is $O(n)$ where $n$ is the length of `xs`, since we must traverse `xs` to append `ys`.
    - For a list of length $n$, the append operation is called $n$ times, so the total time complexity is $O(n^2)$.
- Quadratic time is bad, so we want to eliminate the append operator.
- Induction can help us eliminate the append operator in the definition of `reverse`.
- The trick here is to use a *more general* function, combining the behavior of `reverse` and `++`.
- We want to define a recursive function `reverse'` that *satisfies* the following:
    ```haskell
    reverse' xs ys = reverse xs ++ ys
    ```
    - When we say satisfies, we mean that `reverse'` should behave like `reverse` and `++` combined, not that the function is defined exactly like this.
    - This means applying `reverse'` to two lists `xs` and `ys` is the same as appending `ys` to the reverse of `xs`.
- If we can define such a function `reverse'`, then we can define `reverse` in terms of `reverse'`, which hopefully will be more efficient.
- Rather than starting with the definition, we have a desired behavior for `reverse'`, so we can use this as a driving force to construct the definition itself.
    - This is perfect for induction.
    - The base case gives us the following: `reverse' [] ys = ys`
    - The inductive case will give us a definition for `reverse' (x:xs) ys`
Base case:
```haskell
  reverse' [] ys
= reverse [] ++ ys  -- specification of reverse'
= [] ++ ys  -- applying reverse
= ys  -- applying ++
```
Inductive case:
```haskell
  reverse' (x:xs) ys
= reverse (x:xs) ++ ys  -- specification of reverse'
= (reverse xs ++ [x]) ++ ys  -- applying reverse
= reverse xs ++ ([x] ++ ys)  -- associativity of ++
= reverse' xs ([x] ++ ys)  -- specification of reverse'
= reverse' xs (x:ys)  -- applying ++
```
- From this proof we can define `reverse'` as follows:
    ```haskell
    reverse' :: [a] -> [a] -> [a]
    reverse' [] ys = ys
    reverse' (x:xs) ys = reverse' xs (x:ys)
    ```
- Now, `reverse'` neither references the original function `reverse` nor the append operator `++`.
- Finally, we can define `reverse` in terms of `reverse'`:
    ```haskell
    reverse :: [a] -> [a]
    reverse xs = reverse' xs []
    ```
- In this definition, the list is reversed by accumulating the reverse in a second (empty) list.
- The new definition of `reverse` takes linear time with respect to the length of the list.
## 16.7 Compiler correctness
