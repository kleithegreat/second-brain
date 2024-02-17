# Monads and More
Here we increase the generality achievable in Haskell, using functions that are generic over parameterized types like lists, trees, and IO actions. Specifically, we introduce functors, applicatives, and monads, which captures generic notions of mapping, function application, and effectful programming.
## 12.1 Functors
- Functors, applicatives, and monads all share the idea of abstractive out a common programming pattern as a definition.
- Say we have these two simple functions:
	```haskell
	inc :: [Int] -> [Int]
	int [] = []
	int (n:ns) = n+1 : inc ns
	```
	```haskell
	sqr :: [Int] -> [Int]
	sqr [] = []
	sqr (n:ns) = n^2 : sqr ns
	```
- Both of these lists work in this pattern:
	- The empty list is mapped to itself.
	- A non-empty list has some function applied to its head and the result of recursively processing the tail.
- The only difference between these two functions is the operation applied to each integer in the list.
- Abstracting out this pattern gives us the familiar `map` function.
	```haskell
	map :: (a -> b) -> [a] -> [b]
	map f [] = []
	map f (x:xs) = f x : map f xs
	```
- The above two examples can then be expressed as:
	```haskell
	inc = map (+1)
	sqr = map (^2)
	```
- Even more generally, we can map a function over each element of almost any data structure.
	- This goes beyond just lists.
	- We can do this for a wide range of parameterized types.
- The class of types that support this kind of mapping function are called **functors**.
- They are declared as follows in the standard prelude:
	```haskell
	class Functor f where
		fmap :: (a -> b) -> f a -> f b
	```
	- This means that for some parameterized type `f` to be an instance of `Functor`, it needs to support some function `fmap` of the specified type.
	- The gist is that `fmap` takes a function of type `a -> b` and a structure of type `f a` with elements of type `a`.
	- `fmap` then applies the function to each element and results in a structure of type `f b` with elements of type `b`.
- `f` must be a parameterized type, meaning it takes another type as a parameter.
### Examples
### Functor laws
## 12.2 Applicatives
### Examples
### Effectful programming
### Applicative laws
## 12.3 Monads
### Examples
### The state monad
### Relabelling trees
### Generic functions
### Monadic laws