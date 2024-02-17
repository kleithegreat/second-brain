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
> The upshot is that functors are a type class for types that can be mapped over. The inclusion of `fmap` means we are able to change the values inside the functor without changing the structure of the functor itself.
### Examples
- The type of lists can easily be made an instance of `Functor` by defining `fmap` as `map`.
	```haskell
	instance Functor [] where
		-- fmap :: (a -> b) -> [a] -> [b]
		fmap = map
	```
	- Here the symbol `[]` is used to denote the type of lists, and no type parameter is needed.
	- This is since `[a]` is written more primitively as `[] a`.
- `Maybe` can also be made into a functor.
	```haskell
	instance Functor Maybe where
		-- fmap :: (a -> b) -> Maybe a -> Maybe b
		fmap _ Nothing = Nothing
		fmap g (Just x) = Just (g x)
	```
	- Recall that `Maybe` is defined as `data Maybe a = Nothing | Just a`, and represents values of type `a` that may or may not be present.
	- This means that mapping a function over a failed value should result in a failed value.
	- Mapping a function over a successful value applies the function to the value and wraps the result in `Just`.
	- Examples:
		```haskell
		> fmap (+1) (Just 2)
		Just 3
		> fmap (+1) Nothing
		Nothing
		```
- User define types can also be made into functors.
- For example, consider this binary tree type:
	```haskell
	data Tree a = Leaf a | Node (Tree a) (Tree a) deriving Show
	```
	- We use `deriving Show` to allow the tree to be printed.
	- We can make this type into a functor by defining `fmap` as follows:
		```haskell
		instance Functor Tree where
			-- fmap :: (a -> b) -> Tree a -> Tree b
			fmap g (Leaf x) = Leaf (g x)
			fmap g (Node l r) = Node (fmap g l) (fmap g r)
		```
		- This definition appies the given function to each leaf in the tree.
		- For example:
			```haskell
			> fmap length (Leaf "abc")
			Leaf 3
			> fmap even (Node (Leaf 1) (Leaf 2))
			Node (Leaf False) (Leaf True)
			```
- Functors in general are similar to the examples above.
- We tend to call functors `f`, similar to how we call integers $m$ and $n$ in math.
	- Likewise, `f a` is a functor with elements of type `a`.
	- Therefore, this type is called a **container type**.
- However, not all functors are containers.
	- For example, the `IO` type is a functor, but it is not a container.
	```haskell
	instance Functor IO where
		-- fmap :: (a -> b) -> IO a -> IO b
		fmap g mx = do {x <- mx; return (g x)}
	```
	- This definition applies the given function to the result of the IO action.
- Functors have some key benefits.
	- The `fmap` function can be used to process elements of any functorial structure.
	- We can define generic functions that can be used with any functor.
		- For example, we can generalize our increment function to work with any functor.
		```haskell
		inc :: Functor f => f Int -> f Int
		inc = fmap (+1)
		```
		- This results in the following:
		```haskell
		> inc (Just 1)
		Just 2

		> inc [1,2,3,4,5]
		[2,3,4,5,6]

		> inc (Node (Leaf 1) (Leaf 2))
		Node (Leaf 2) (Leaf 3)
		```
### Functor laws
- In addition to impementing `fmap`, functors also must satisfy two equational laws:
	```haskell
	fmap id = id
	fmap (g . h) = fmap g . fmap h
	```
- The first law states that mapping the identity function over a functor should preserve the functor.
> Note: The two occurances of `id` in the first law are different. The LHS has type `a -> a`, while the RHS has type `f a -> f a`.
- The second law states that mapping a composition of two functions over a functor should be the same as mapping each function separately and then composing the results.
- In order for the compositions to be well typed, the component functions `g` and `h` must have types `b -> c` and `a -> b`, respectively.
- These laws are important to ensure that `fmap` does indeed perform a mapping operation.
	- For example, in lists, they ensure the `fmap` function does not add, remove, or rearrange elements.
	- Without these laws, we could write an `fmap` function that reverses a list, which is not just mapping.
> This concept of being "wrapped in a context" refers to the encapsulation of values within data structures that add additional layers of meaning or behavior, whether it be the possibility of absence, multiplicity of values, or side effects.
## 12.2 Applicatives
- Functors are useful for mapping a function over a structure.
- Suppose we want to generalize this to allow functions with an arbitrary number of arguments to be mapped over a structure.
- More precisely, we want to define a hierarchy of `fmap` functions with the following types:
	```haskell
	fmap0 :: a -> f a
	fmap1 :: (a -> b) -> f a -> f b
	fmap2 :: (a -> b -> c) -> f a -> f b -> f c
	fmap3 :: (a -> b -> c -> d) -> f a -> f b -> f c -> f d
	...
	```
- `fmap1` is just the `fmap` function we have already seen.
- `fmap0` is the degenerate case when the function being mapped has no arguments.
- One approach would be to declare a special version of the functor class for each number of arguments.
	- This would be tedious and would not scale well.
	- It is not clear how many versions we would need.
- Using the idea of curring, we can make a version of `fmap` for functions with any number of arguments.
	```haskell
	pure :: a -> f a
	(<*>) :: f (a -> b) -> f a -> f b
	```
	- This means `pure` converts a value of type `a` into a structure of type `f a`.
	- `<*>` is a generalized form of function application.
		- The argument function, argument value, and result value are all wrapped in the functor.
		- This operator is placed between its arguments and associates to the left.
> The main difference between `fmap` and `<*>` is that the argument function is also wrapped in the same context as the argument value for `<*>`, while it is not for `fmap`.
- A typical use of `pure` and `<*>` has the following form:
	```haskell
	pure g <*> x1 <*> x2 <*> ... <*> xn
	```
	- These applicatives are said to be in **applicative style**.
	- This is due to its similarity to normal function application notation `g x1 x2 ... xn`.
	- The difference is that in applicative style, each argument `xi` is wrapped in a functor, or the type is `f ai` instead of `ai`.
- We can now define the hierarchy of mapping functions:
	```haskell
	fmap0 :: a -> f a
	fmap0 = pure

	fmap1 :: (a -> b) -> f a -> f b
	fmap1 g x = pure g <*> x

	fmap2 :: (a -> b -> c) -> f a -> f b -> f c
	fmap2 g x y = pure g <*> x <*> y

	fmap3 :: (a -> b -> c -> d) -> f a -> f b -> f c -> f d
	fmap3 g x y z = pure g <*> x <*> y <*> z
	...
	```
- The class of functors that support `pure` and `<*>` are called **applicative functors**, or just **applicatives**.
- The built in class declaration is given as follows:
	```haskell
	class Functor f => Applicative f where
		pure :: a -> f a
		(<*>) :: f (a -> b) -> f a -> f b
	```
### Examples
- The `Maybe` type can be made into an applicative.
	```haskell
	instance Applicative Maybe where
		-- pure :: a -> Maybe a
		pure = Just

		-- (<*>) :: Maybe (a -> b) -> Maybe a -> Maybe b
		Nothing <*> _ = Nothing
		(Just g) <*> mx = fmap g mx
	```
	- This means the `pure` function wraps a value in `Just`, which is a successful value.
	- The `<*>` function applies a function that may fail to a value that may fail, producing a result that may fail.
	- For example:
		```haskell
		> pure (+1) <*> Just 1
		Just 2

		> pure (+1) <*> Just 1 <*> Just 2
		Just 3

		> pure (+1) <*> Nothing
		Nothing
		```
	- In the above examples, the applicative style of `Maybe` supports a form of **exceptional** programming.
	- This means we are able to write code that may fail without needing to manage the propagation of failure manually.
- Lists can also be made into applicatives, and are declared in the standard prelude as follows:
	```haskell
	instance Applicative [] where
		-- pure :: a -> [a]
		pure x = [x]

		-- (<*>) :: [a -> b] -> [a] -> [b]
		gs <*> xs = [g x | g <- gs, x <- xs]
	```
	- This means the `pure` function wraps a value in a singleton list.
	- The `<*>` function applies a list of functions to a list of arguments, producing a list of results.
	- For example:
		```haskell
		> pure (+1) <*> [1,2,3]
		[2,3,4]

		> pure (+) <*> [1] <*> [2]
		[3]

		> pure (*) <*> [1,2] <*> [3,4]
		[3,4,6,8]
		```
	- We can think of lists as a generalization of `Maybe` to allow multiple successful values.
		- More precisely, we can think of the empty list as a failed value, and a non-empty list as all the ways a computation can succeed.
		- In the last example, there are two possible values for the first argument and two possible values for the second argument, resulting in four possible results.
	- As an example, consider a function that returns all possible ways of multiplying two lists of integers:
		```haskell
		prods :: [Int] -> [Int] -> [Int]
		prods xs ys = [x*y | x <- xs, y <- ys]
		```
	- Since lists are applicative, we can also give an applicative style definition, which avoids naming intermediate results:
		```haskell
		prods :: [Int] -> [Int] -> [Int]
		prods xs ys = pure (*) <*> xs <*> ys
		```
- The applicative style for lists supports a form of **nondeterministic** programming.
- This means we can apply pure functions to multi-valued arguments without needing to manage the selection of values or propagation of failure manually.
- Finally, we can also make the `IO` type into an applicative functor:
	```haskell
	instance Applicative IO where
		-- pure :: a -> IO a
		pure = return

		-- (<*>) :: IO (a -> b) -> IO a -> IO b
		mg <*> mx = do {g <- mg; x <- mx; return (g x)}
	```
	- Here, `pure` wraps a value in an IO action that returns the value.
	- `<*>` applies an impure function to an impure argument, producing an impure result.
	- We can declare a function that reads characters from the keyboard in applicative style as follows:
		```haskell
		getChars :: Int -> IO String
		getChars 0 = return []
		getChars n = pure (:) <*> getChar <*> getChars (n-1)
		```
		- Note that we would need to name the intermediate results if we used the `do` notation instead of the applicative style.
- The applicative style for `IO` supports a form of **interactive** programming.
- This means we can apply pure functions to impure arguments without needing to manage the sequencing of actions or extraction of results manually.
### Effectful programming
- The original motivation for applicatives was to generalize the idea of mapping to allow functions with multiple arguments.
- This is useful for many cases, but there is also a more abstract view.
- The motif of applicatives is that they deal with programming with **effects**.
- In each case before, the applicative style allowed us to apply pure functions to effectful arguments without needing to manage the effects manually.
- Applicatives also give us the benefit of declaring functions that are generic to any applicative functor.
- For example, the standard library has the following function:
	```haskell
	sequenceA :: Applicative f => [f a] -> f [a]
	sequnceA [] = pure []
	sequenceA (x:xs) = pure (:) <*> x <*> sequenceA xs
	```
	- This function takes a list of applicative actions into a single applicative action that returns a list of results.
	- This is useful for combining multiple effectful actions into a single effectful action.
	- For example, we can now define `getChars` very simply using this:
		```haskell
		getChars :: Int -> IO String
		getChars n = sequenceA (replicate n getChar)
		```
### Applicative laws
- Applicative functors are required to satisfy four equational laws:
	```haskell
	pure id <*> x = x
	pure (g x) = pure g <*> pure x
	x <*> pure y = pure (\g -> g y) <*> x
	x <*> (y <*> z) = (pure (.) <*> x <*> y) <*> z
	```
	- The first law states that `pure` should preserve the identity function.
	- The second law states that `pure` should preserve function application.
	- The third law states that order of evaluating an effectful function on a pure argument should not matter.
	- The fourth law states that `<*>` should be associative modulo the types involved.
- These laws help formalize our intuition on the `pure :: a -> f a` function, meaning it embeds a pure value into the effectful context.
- The laws also ensure every well-typed expression using `pure` and `<*>` can be written in applicative style.
- Reminder: applicative style has the form `pure g <*> x1 <*> x2 ... <*> xn`.
## 12.3 Monads
### Examples
### The state monad
### Relabelling trees
### Generic functions
### Monadic laws