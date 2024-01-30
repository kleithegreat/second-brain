# List Comprehensions
List comprehensions allow many functions on lists to be defined simply.
## 5.1 Basic concepts
- Set comprehensions are widely used in math.
    - Example: $\{x^2 | x \in \{1...5\}\}$ produces $\{1, 4, 9, 16, 25\}$.
    - This means all numbers $x^2$ such that $x$ is an element of the set $\{1...5\}$.
- **List comprehensions** are the Haskell analog of set comprehensions.
    - Example: `[x^2 | x <- [1..5]]` produces `[1, 4, 9, 16, 25]`.
    - The `|` symbol is read as *such that*.
    - `<-` is read as *is drawn from*.
    - The expression `x <- [1..5]` is called a **generator**.
- List comprehensions can also have multiple generators.
    - Multiple generators must be separated by commas.
    - Example: All possible parings of numbers from two lists can be given by `[(x, y) | x <- [1, 2, 3], y <- [4, 5]]`, producing `[(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]`.
    - Changing the order of the generators will change the order of the results, but results will be the same.
    - Example: `[(x, y) | y <- [4, 5], x <- [1, 2, 3]]` produces `[(1, 4), (2, 4), (3, 4), (1, 5), (2, 5), (3, 5)]`.
    - This can be thought of where the first generator is the outer loop and the last generator is the inner loop (later generators are more deeply nested).
- Later generators can have variables depending on earlier generators.
    - Example: `[(x, y) | x <- [1..3], y <- [x..3]]` produces `[(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]`.
    - This can be thought of as using a loop index from an outer loop in the bounds of an inner loop.
- A practical example is the function `concat`, which concatenates lists.
    ```haskell
    concat :: [[a]] -> [a]
    concat xss = [x | xs <- xss, x <- xs]
    ```
- The wildcard pattern `_` can be used in generators in cases where we don't care about some value.
    - For example, say we want to define a function `firsts` that takes a list of pairs and returns a list of the first component of each pair.
    - We can use the wildcard pattern to ignore the second component of each pair.
    ```haskell
    firsts :: [(a, b)] -> [a]
    firsts ps = [x | (x, _) <- ps]
    ```
- The library function `length` also uses the wildcard pattern.
    ```haskell
    length :: [a] -> Int
    length xs = sum [1 | _ <- xs]
    ```
    - Here `_ <- xs` means that we don't care what the elements of `xs` are, we just want to count them.
## 5.2 Guards
- List comprehensions can be used in logical expressions called **guards**.
    - Guards filter the values produced by earlier generators.
    - If the guard is `True`, the value is retained, otherwise it is discarded.
- Example: `[x | x <- [1..10], even x]` produces `[2, 4, 6, 8, 10]`.
- More interestingly, we can write a function that maps a positive integer to its list of factors.
    ```haskell
    factors :: Int -> [Int]
    factors n = [x | x <- [1..n], n `mod` x == 0]
    ```
- Using the `factors` function, we can define a function that determines whether a number is prime.
    ```haskell
    prime :: Int -> Bool
    prime n = factors n == [1, n]
    ```
    - If `n` is prime, then `factors n` must return `[1, n]`.
- Using the `prime` function, we can define a function that returns a list of all prime numbers up to a given limit.
    ```haskell
    primes :: Int -> [Int]
    primes n = [x | x <- [2..n], prime x]
    ```
- The upshot is that guards can be used to define functions that search for values with certain properties, and guard conditions can contain many nested conditions.
## 5.3 The zip function
- The library function `zip` takes two lists and returns a list of corresponding pairs.
    - Example:
    ```haskell
    > zip ['a', 'b', 'c'] [1, 2, 3, 4]
    [('a', 1), ('b', 2), ('c', 3)]
    ```
- `zip` is useful for list comprehensions that combine two lists.
    - Say we want to write a function that returns a list of all pairs of adjacent elements from a list.
    - We can use `zip` to do this.
    ```haskell
    pairs :: [a] -> [(a, a)]
    pairs xs = zip xs (tail xs)
    ```
    - This works because:
        - `tail` returns a list of all elements of a list except the first.
        - `zip` will stop when the shorter list is exhausted.
        - We don't want to zip the last element of the list with anything, so `tail` is perfectly suited for this.
    ```haskell
    > pairs [1, 2, 3, 4]
    [(1, 2), (2, 3), (3, 4)]
    ```

## 5.4 String comprehensions
- Strings are not a primitive type in Haskell.
    - Rather they are just lists of characters.
    - Example: `"abc" :: String` is just abbreviated syntax for `['a', 'b', 'c'] :: [Char]`.
- Since strings are functionally lists, polymorphic functions on lists also work on strings.
    - Functions like indexing `!!`, concatenation `++`, length `length`, `take`, `drop`, etc. all work on strings.
- For this same reason, list comprehensions can also be used on strings.
    - Function that returns the number of lower case letters in a string:
    ```haskell
    lowers :: String -> Int
    lowers xs = length [x | x <- xs, x >= 'a' && x <= 'z']
    ```
    - Function that returns the number of occurrences of a given character in a string:
    ```haskell
    count :: Char -> String -> Int
    count x xs = length [x' | x' <- xs, x == x']
    ```