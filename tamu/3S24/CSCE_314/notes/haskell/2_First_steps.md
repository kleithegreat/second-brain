# First steps
## 2.1 Glasgow Haskell Compiler
- This is the state of the art open source compiler for Haskell.
- It comes with a batch compiler GHC and an interactive interpreter GHCi.
## 2.2 Installing and starting
lmao
## 2.3 Standard prelude
- The *standard prelude* defines a large number of built-in functions.
    - For example, it provides the numeric functions `+` and `*`
    - It also provides functions for manipulating lists.
        - `head` returns the first element of a list.
        - `tail` returns the list without its first element.
        - arrays are indexed by the following syntax:
            ```haskell
            [1,2,3] !! 0 -- returns 1
            [1,2,3] !! 1 -- returns 2
            [1,2,3] !! 2 -- returns 3
            ```
        - `take n xs` returns the first `n` elements of `xs`.
            ```haskell
            take 2 [1,2,3] -- returns [1,2]
            ```
        - `drop n xs` returns the list `xs` without its first `n` elements.
            ```haskell
            drop 2 [1,2,3] -- returns [3]
            ```
        - `length xs` returns the length of `xs`.
            ```haskell
            length [1,2,3] -- returns 3
            ```
        - `sum xs` returns the sum of the elements of `xs`.
            ```haskell
            sum [1,2,3] -- returns 6
            ```
        - `product xs` returns the product of the elements of `xs`.
            ```haskell
            product [1,2,3] -- returns 6
            ```
        - `++` concatenates two lists.
            ```haskell
            [1,2] ++ [3,4] -- returns [1,2,3,4]
            ```
        - `reverse xs` reverses the order of the elements of `xs`.
            ```haskell
            reverse [1,2,3] -- returns [3,2,1]
            ```
## 2.4 Function application
- Order of evaluation is implied using spacing.
- Multiplication is denoted explicitly using `*`.
- For example, $f(a, b) + cd$ is written as `f a b + c * d`.
> Function application has the highest level of precedence for order of operations.
List of equivalent expressions:
- $f(x)$ in haskell is `f x`
- $f(x, y)$ in haskell is `f x y`
- $f(g(x))$ in haskell is `f (g x)`
- $f(x, g(y))$ in haskell is `f x (g y)`
- $f(x) g(y)$ in haskell is `f x * g y`
> In the case $f(g(x))$, the parentheses are required in `f (g x)` because otherwise it would be interpreted as $f(g, x)$.
## 2.5 Haskell scripts
Haskell scripts are a sequence of definitions and typically use the `.hs` extension.
### My first script
- Its useful have one window for editing and another for running GHCi.
- GHCi requires the `:reload` command when the script is modified.
### The layout rule
- Function scope/level is determined by indentation.
- The layout rule is that the declarations in a block must begin in the same column.
- For example, `a` and `d` are in the same block, but `b` and `c` are in a different block.
    ```haskell
    a = b + c
        where
            b = 1
            c = 2
    d = a * 2
    ```
- Grouping can also be made explicit using braces and semicolons:
    ```haskell
    a = b + c 
        where 
            {b = 1;
            c = 2};
    d = a * 2
    ```
- Braces and semicolons can also make one liners:
    ```haskell
    a = b + c where {b = 1; c = 2}; d = a * 2
    ```
### Tabs
- Tabs tend to create problems in Haskell. 
- It is recommended to use spaces instead.
- Haskell assumes that a tab is 8 spaces wide.
### Comments
Single line comments:
```haskell
a = b + c -- this is a comment
```
Multi line comments:
```haskell
{-
This is a comment
spanning multiple lines
-}
```