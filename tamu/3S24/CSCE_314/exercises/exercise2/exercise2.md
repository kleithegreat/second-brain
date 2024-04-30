# Exercise 2
## Problem 1
```haskell
['H','a','s','k','e','l','l'] :: [Char]
```
Explanation: This is a simple list of char elements.

```haskell
('c','a','t') :: (Char,Char,Char)
```
Explanation: This is a tuple of three char elements. Tuples do not have to be homogeneous in type, so it's necessary to specify the type of each element.

```haskell
[(False,'0'),(True,'1')] :: [(Bool,Char)]
```
Explanation: This is a list of tuples that contain a boolean and a char in that order.

```haskell
([True,False],['1','0']) :: ([Bool],[Char])
```
Explanation: This is a tuple of two lists; the first list is a list of booleans and the second list is a list of chars.

```haskell
[tail, init, reverse] :: [[a] -> [a]]
```
Explanation: This is a list of functions that take a list of any type and return a list of the same type. List elements must have the same type, and since tail, init and reverse all have the same type signature, this list is valid.
## Problem 2
```haskell
second xs = head (tail xs)
second :: [a] -> a
```
Explanation: This function takes a list of any type and returns the second element of that list. Therefore, the type signature is a list of any type to any type.

```haskell
swap (x,y) = (y,x)
swap :: (a,b) -> (b,a)
```
Explanation: This function takes a tuple of two arbitrary elements and returns a tuple of the same elements in reverse order. Therefore the type signature of the function is a tuple of two arbitrary elements to a tuple of two arbitrary elements, but in reverse order.

```haskell
pair x y = (x,y)
pair :: a -> b -> (a,b)
```
Explanation: This type signature says that pair is a function that takes an arbitrary element 'a' and returns another function that takes an arbitrary element 'b' and returns a tuple of 'a' and 'b' in that order. This is a curried function.

```haskell
double x = x*2
double :: Num a => a -> a
```
Explanation: This functions signature says that double is a function that takes a number 'a' of any numeric type and returns a number of the same type. 

```haskell
palindrome xs = reverse xs == xs
palindrome :: Eq a => [a] -> Bool
```
Explanation: This functions type means that it takes an array of elements 'a' where 'a' is any equality type, meaning any elements 'a' can be compared for equality. Using the list of equality types 'a's, the function returns a boolean value.

```haskell
twice f x = f (f x)
twice :: (t -> t) -> t -> t
```
Explanation: From the function definition we can see that it takes a function and an arguemnt and applies the function to the argument twice. Twice first takes a function: that function (the input for twice) is one that takes types t for its input and output. Using that function as an input, twice then returns another function that takes type t for input and output. That function then takes argument x of type t and returns a value of type t. 

```haskell
lessThanHalf x y = x * 2 < y
lessThanHalf :: (Ord a, Num a) => a -> a -> Bool
```
Explanation: From the function definition, lessThanHalf takes two arguments of type a, where a is both ordered and numeric, and returns a boolean value indicating whether the first argument is less than half of the second argument. The type signature means that lessThanHalf first takes an argument 'a' that has to be ordered and numeric, then it returns a function that takes another argument of the same type 'a' and returns a boolean value.