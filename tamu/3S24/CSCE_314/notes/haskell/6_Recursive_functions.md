# Recursive Functions
Recursion is the basic mechanism for looping in Haskell. 
## 6.1 Basic concepts
- As seen previously, it is permissible and common for functions to be defined in terms of themselves.
- This is called **recursion**.
- Example: The factorial function can be defined as follows:
    ```haskell
    factorial :: Int -> Int
    factorial 0 = 1
    factorial n = n * factorial (n - 1)
    ```
- The first equation is called the **base case**.
    - It is the simplest case of the function.
    - It is the case where the function does not call itself.
- The second equation is called the **recursive case**.
- Defining functions recursively allow for properties to be proved by induction.
## 6.2 Recursion on lists
- Recursion is commonly used on lists.
- For example, the library function `product` returns the product of a list of numeric types.
    ```haskell
    product :: Num a => [a] -> a
    product [] = 1
    product (n:ns) = n * product ns
    ```
- This is possible because lists are actually constructed one at a time using the `:` operator.
- More examples of recursive functions on lists.
## 6.3 Multiple arguments
- Functions with multiple arguments can also be defined recursively.
- The library function `zip` does exactly this.
    ```haskell
    zip :: [a] -> [b] -> [(a, b)]
    zip [] _ = []
    zip _ [] = []
    zip (x:xs) (y:ys) = (x, y) : zip xs ys
    ```
- Another example is the library function `drop`, which drops a given number of elements from the front of a list.
    ```haskell
    drop :: Int -> [a] -> [a]
    drop 0 xs = xs
    drop _ [] = []
    drop n (_:xs) = drop (n - 1) xs
    ```
## 6.4 Multiple recursion
- **Multiple recursion** is when a function is applied more than once in its definition.
- A Fibonacci function can be defined using double recursion.
    ```haskell
    fib :: Int -> Int
    fib 0 = 0
    fib 1 = 1
    fib n = fib (n - 1) + fib (n - 2)  -- fib applied twice
    ```
- The function `qsort` is another example of multiple recursion.
    ```haskell
    qsort :: Ord a => [a] -> [a]
    qsort [] = []
    qsort (x:xs) = qsort smaller ++ [x] ++ qsort larger
        where
            smaller = [a | a <- xs, a <= x]
            larger = [b | b <- xs, b > x]
    ```
## 6.5 Mutual recursion
- **Mutual recursion** is where two or more functions are defined in terms of each other.
- The library functions `even` and `odd` can be defined with mutual recursion.
    - They are not actually defined this way in the standard prelude.
    ```haskell
    even :: Int -> Bool
    even 0 = True
    even n = odd (n - 1)

    odd :: Int -> Bool
    odd 0 = False
    odd n = even (n - 1)
    ```
## 6.6 Advice on recursion
- Using recursion can be difficult at first.
- The following is a five-step process for writing recursive functions.
- Say we want to define the `product` function.
### Step 1: Define the type
- Thinking about types is helpful for defining functions in general.
- It can be helpful to start with a simple type and then refine or generalize as needed.
    ```haskell
    product :: [Int] -> Int
    ```
### Step 2: Enumerate the cases
- Think of the standard cases to consider.
- For lists, the standard cases are the empty list and the non-empty list.
- For nonnegative integers, the standard cases are zero and positive integers.
- For logical values, the standard cases are `True` and `False`.
- Use this logic for other types.
    ```haskell
    product [] = 
    product (n:ns) = 
    ```
### Step 3: Define the simple cases
- In this example, the simple case is the empty list.
- Simple cases are often the base cases.
    ```haskell
    product [] = 1
    ```
### Step 4: Define the other cases
- It is often helpful to think about what can be used in the function.
    - The function iteself can be used.
    - Argument provided to the function can be used.
    - Standard library functions can be used.
    ```haskell
    product (n:ns) = n * product ns
    ```
### Step 5: Generalize and simplify
- At this point the function should be working and its purpose is clear.
- It is often possible to generalize and simplify the function.
- In this example, the function can be generalized to any numeric type and simplified with the `foldr` function.
    ```haskell
    product :: Num a => [a] -> a
    product = foldr (*) 1
    ```