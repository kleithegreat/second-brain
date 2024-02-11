# Higher-order Functions
Higher-order functions allow for common programming patterns to be encapsulated as functions.
## 7.1 Basic concepts
- As seen before, functions with multiple arguments are typically defined as curried functions.
- This uses the fact that functions can return functions as results.
- It is also permissible to define functions that take functions as arguments.
- For example, the following are equivalent:
```haskell
add :: Int -> Int -> Int
add x y = x + y

add :: Int -> (Int -> Int)
add = \x -> (\y -> x + y)
```
- We can also define functions that take functions as arguments.
- Suppose for example we want to define a function that applies a function twice to its argument.
```haskell
twice :: (a -> a) -> a -> a
twice f x = f (f x)
```
- Because this function is curried, it can be partially applied to create new useful functions.
- Formally, functions that take other functions as arguments or return functions as results are called **higher-order functions**.
> In practice, higher-order functions mostly just refer to functions that take functions as arguments, since currying implies that functions can return functions as results.
- Higher-order functions can be used to define domain-specific languages within Haskell.
## 7.2 Processing lists
- The standard prelude defines many higher-order functions that are useful for processing lists.
- For example, the `map` function applies a function to every element of a list. 
    - It is defined as:
    ```haskell
    map :: (a -> b) -> [a] -> [b]
    map f xs = [f x | x <- xs]
    ```
    - This means that `map f xs` returns the list of all values `f x` for `x` in `xs`.
    - Note that `map` is polymorphic, so it can be applied to lists of any type.
    - Moreover, `map` can be applied to itself to process lists of lists.
        - For example, `map (map (+1)) [[1,2,3],[4,5]]` returns `[[2,3,4],[5,6]]`.
    - `map` can also be defined using recursion:
    ```haskell
    map :: (a -> b) -> [a] -> [b]
    map f [] = []
    map f (x:xs) = f x : map f xs
    ```
    - This definition means that map will apply `f` to the head of the list and then recursively apply `f` to the tail of the list.
    - This definition is preferable to the list comprehension definition since we can prove properties using induction.
- The `filter` function selects elements from a list that satisfy a predicate.
    - A predicate is just like a mathematical predicate, a function that returns a boolean value.
    - It can be defined using a list comprehension:
    ```haskell
    filter :: (a -> Bool) -> [a] -> [a]
    filter p xs = [x | x <- xs, p x]
    ```
    - This means that `filter p xs` returns the list of all values `x` in `xs` such that `p x` is true.
        - For example, `filter even [1..10]` returns `[2,4,6,8,10]`.
    - Just like map, `filter` is polymorphic and can be applied to lists of any type.
    - `filter` can also be defined using recursion for inductive reasoning:
    ```haskell
    filter :: (a -> Bool) -> [a] -> [a]
    filter p [] = []
    filter p (x:xs) | p x = x : filter p xs
                    | otherwise = filter p xs
    ```
    - This definition means that `filter` will keep every element `x` in the list if `p x` is true and then recursively apply `filter` to the tail of the list.
## 7.3 The foldr function
- Many functions that process lists follow a simple pattern:
    ```haskell
    f [] = v
    f (x:xs) = x # f xs
    ```
    - This mean the function maps the empty list to some value `v`.
    - The function applies some operator `#` to the head of the list.
    - The function then recursively applies itself to the tail of the list.
- Some common examples of this pattern are:
    - Summing a list of numbers.
    - Computing the product of a list of numbers.
    - Logical OR on a list of boolean values.
- The higher order library function `foldr` (abbreviates *fold right*) captures this pattern.
    - The following are equivalent:
    ```haskell
    sum :: Num a => [a] -> a
    sum [] = 0
    sum (x:xs) = x + sum xs

    sum :: Num a => [a] -> a
    sum = foldr (+) 0
    ```
    ```haskell
    product :: Num a => [a] -> a
    product [] = 1
    product (x:xs) = x * product xs
    
    product :: Num a => [a] -> a
    product = foldr (*) 1
    ```
    ```haskell
    or :: [Bool] -> Bool
    or [] = False
    or (x:xs) = x || or xs

    or :: [Bool] -> Bool
    or = foldr (||) False
    ```
- The `foldr` function can be defined as follows using recursion:
```haskell
foldr :: (a -> b -> b) -> b -> [a] -> b
foldr f v [] = v
foldr f v (x:xs) = f x (foldr f v xs)
```
- This definition means that `foldr` replaces the empty list with `v`.
- Any non-empty list is replaced by the operator `f` applied to the head of the list and the result of recursively applying `foldr` to the tail of the list.
- The name *fold right* reflects the fact that the operator is assumed to associate to the right.
- Generally, the behavior of `foldr` can be summarized as:
```haskell
foldr (#) v [x0,x1,...,xn] = x0 # (x1 # (... (xn # v) ...))
```
## 7.4 The foldl function
- Recursive functions also exist for operators that associate to the left.
- For example, we can defined `sum` using an auxiliary function `sum'` that takes an extra argument `v` that accumulates the sum:
```haskell
sum :: Num a => [a] -> a
sum = sum' 0
    where
        sum' v [] = v
        sum' v (x:xs) = sum' (v + x) xs
```
- To generalize, many functions on lists can be defined using this pattern of recursion:
```haskell
f v [] = v
f v (x:xs) = f (v # x) xs
```
- This means the function maps the empty list to the **accumulator** value `v`.
- Any non-empty list is replaced by the operator `#` applied to the accumulator and the head of the list.
- The function then recursively applies itself to the tail of the list.
- The higher order library function `foldl` (abbreviates *fold left*) captures this pattern.
    - The following are equivalent:
    ```haskell
    sum :: Num a => [a] -> a
    sum = foldl (+) 0
    ```
    ```haskell
    product :: Num a => [a] -> a
    product = foldl (*) 1
    ```
    ```haskell
    or :: [Bool] -> Bool
    or = foldl (||) False
    ```
- The `foldl` function can be defined as follows using recursion:
```haskell
foldl :: (a -> b -> a) -> a -> [b] -> a
foldl f v [] = v
foldl f v (x:xs) = foldl f (f v x) xs
```
- In practice, it is best to think of the behavior of `foldl` in a non-recursive manner.
## 7.5 The composition operator
- The composition operator `.` returns the composition of two functions as a single function.
- It is defined as:
```haskell
(.) :: (b -> c) -> (a -> b) -> (a -> c)
f . g = \x -> f (g x)
```
- This means that `f . g` (read as `f` *composed with* `g`) is the function that takes an argument x, applies `g` to `x`, and then applies `f` to the result.
- Composition can be used to reduce parentheses in expressions.
- For example, the following are equivalent:
```haskell
odd :: Int -> Bool
odd n = not (even n)

odd :: Int -> Bool
odd = not . even
```
```haskell
twice :: (a -> a) -> a -> a
twice f x = f (f x)

twice :: (a -> a) -> a -> a
twice f = f . f
```
```haskell
sumsqreven :: [Int] -> Int
sumsqreven ns = sum (map (^2) (filter even ns))

sumsqreven :: [Int] -> Int
sumsqreven = sum . map (^2) . filter even
```
- This last definition exploits the fact that `.` is associative.
- This means that `f . (g . h)` is the same as `(f . g) . h` for any functions `f`, `g`, and `h` of the appropriate types.
- Composition also has an identity, given by the identity function `id`:
```haskell
id :: a -> a
id \x -> x
```
- This means that `id` simply returns the argument it is given.
- This is useful when reasoning about programs.
- This can also give a suitable starting point for a chain of compositions.
- For example, the composition of a list of functions can be defined as:
```haskell
compose :: [a -> a] -> (a -> a)
compose = foldr (.) id
```