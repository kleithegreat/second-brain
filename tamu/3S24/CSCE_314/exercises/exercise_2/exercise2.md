# Problem 1
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

# Problem 2
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
Explanation: 

```haskell
double x = x*2
double :: Num a => a -> a
```
Explanation: 

```haskell
palindrome xs = reverse xs == xs
palindrome :: Eq a => [a] -> Bool
```
Explanation: 

```haskell
twice f x = f (f x)
twice :: (t -> t) -> t -> t
```
Explanation:

```haskell
lessThanHalf x y = x * 2 < y
lessThanHalf :: (Ord a, Num a) => a -> a -> Bool
```
Explanation: 