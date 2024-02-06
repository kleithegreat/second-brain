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

## 7.4 The foldl function

## 7.5 The composition operator

## 7.6 Binary string transmitter

## 7.7 Voting algorithms
