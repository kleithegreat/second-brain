# Exercise 1
## Problem 1
### map
```haskell
ghci> map sum [[1, 2, 3], [4, 5, 6]]
[6,15]
```
The map function takes a function and a list and applies the function to each element in the list, so in this case, map is taking the sum function and summing each list in the list of lists. [1, 2, 3] gets summed to 6 and [4, 5, 6] gets summed to 15, so the result is [6, 15].
```haskell
ghci> map sqrt [4, 9, 16]
[2.0,3.0,4.0]
```
Here, map is working as before, but this time it is taking the square root of each element in the list. 4 gets square rooted to 2, 9 gets square rooted to 3, and 16 gets square rooted to 4, so the result is [2.0, 3.0, 4.0].
### reverse
```haskell
ghci> reverse [1, 2 ,3]
[3, 2, 1]
```
Reverse takes a list and returns the list in reverse order. In this case, [1, 2, 3] gets reversed to [3, 2, 1].
```haskell
ghci> reverse "hello world"
"dlrow olleh"
```
Reverse also works on strings since strings are just lists of characters. "hello world" gets reversed to "dlrow olleh".
### sqrt
```haskell
ghci> sqrt 4
2.0
```
The sqrt function takes a number and returns the square root of that number. 4 gets square rooted to 2.0.
```haskell
ghci> sqrt 16
4.0
```
16 gets square rooted to 4.0.
### head
```haskell
ghci> head [1, 2, 3]
1
```
The head function takes a list and returns the first element in the list. In this case, the first element in [1, 2, 3] is 1, so the result is 1.
```haskell
ghci> head "hello world"
'h'
```
The first element in "hello world" is 'h', so the result is 'h'.
### tail
```haskell
ghci> tail [1, 2, 3]
[2, 3]
```
The tail function takes a list and returns the list without the head, so in this case, the result is [2, 3] since the head is 1. 
```haskell
ghci> tail [1..10]
[2,3,4,5,6,7,8,9,10]
```
The tail of [1..10] is [2..10], since the head is 1.
### !!
```haskell
ghci> [1, 2, 3] !! 0
1
```
The !! function takes a list and an index and returns the element at that index. This is pretty much the same as indexing into an array in other languages. In this case, the element at index 0 in [1, 2, 3] is 1, so the result is 1.
```haskell
ghci> [2..10] !! 5
7
```
The element at index 5 in [2..10] is 7, so the result is 7.
### take
```haskell
ghci> take 5 [5..]
[5,6,7,8,9]
```
The take function takes a number n and a list and returns the first n elements of the list. In this case, the first 5 elements of the infinite list starting from 5 are [5, 6, 7, 8, 9].
```haskell
ghci> take 2 "hello world"
"he"
```
The first two elements of "hello world" are 'h' and 'e', so the result is "he".
### drop
```haskell
ghci> drop 5 [1..10]
[6,7,8,9,10]
```
The drop function takes a number n and a list and returns the list without the first n elements. In this case, the list without the first 5 elements of [1..10] is [6..10].
```haskell
ghci> drop 3 "hello world"
"lo world"
```
"hello world" without the first 3 elements is "lo world".
### ++
```haskell
ghci> [1, 1, 1] ++ [2, 2, 2]
[1,1,1,2,2,2]
```
The ++ function takes two lists and concatenates them. In this case, [1, 1, 1] and [2, 2, 2] get concatenated to [1, 1, 1, 2, 2, 2].
```haskell
ghci> [1..5] ++ [6..10]
[1,2,3,4,5,6,7,8,9,10]
```
[1..5] and [6..10] get concatenated to [1..10].
### length
```haskell
ghci> length [1..10]
10
```
The length function takes a list and returns the number of elements in the list. In this case, there are 10 elements in [1..10].

```haskell
ghci> length "hello world"
11
```
There are 11 characters in "hello world".
### sum
```haskell
ghci> sum [1..10]
55
```
The sum function simply returns the sum of all the elements in a list. In this case, the sum of [1..10] is 55.
```haskell
ghci> sum [1 / (n * n) | n <- [1..1000]]
1.6439345666815615
```
The sum of 1/n^2 for n from 1 to 1000 is 1.6439345666815615.
### product
```haskell
ghci> product [1..10]
3628800
```
The product function returns the product of all the elements in a list. In this case, the product of [1..10] is 3628800.
```haskell
ghci> product [2, 4]
8
```
The product of [2, 4] is 8.
## Problem 2
### 2.1
```haskell
ghci> map length ["Howdy","all"]
[5,3]
```
This code applies the length function to "Howdy" and "all" and returns each length in a list, so the result is [5, 3]. An equivalent way to write this without map is [length "Howdy", length "all"].
### 2.2
```haskell
ghci> map head ["What","a","lovely","day"]
"Wald"
```
This code applies the head function to "What", "a", "lovely", and "day" and returns each head in a list, so the result is "Wald". An equivalent way to write this without map is [head "What", head "a", head "lovely", head "day"].
### 2.3
```haskell
ghci> map sum [[1..10],[1,6,7],[1..100]]
[55,14,5050]
```
This code applies the sum function to [1..10], [1, 6, 7], and [1..100] and returns each sum in a list, so the result is [55, 14, 5050]. An equivalent way to write this without map is [sum [1..10], sum [1, 6, 7], sum [1..100]].
## Problem 3
### First error:
exercise1.hs:1:7: error: lexical error at character 'd'

This is solved by enclosing div with `` instead of ''.
### Second error:
exercise1.hs:4:8: error: parse error on input `xs'

This is solved by making sure `a = 10` has the same indentation as `xs = [1,2,3,4,5]`.
### Third error:
exercise1.hs:1:1: error: Not in scope: data constructor `N'

This is solved by changing `N` to `n`, since function names must start with a lowercase letter.