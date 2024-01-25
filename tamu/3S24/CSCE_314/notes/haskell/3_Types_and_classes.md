# Types and Classes
Types and classes are two of the most important concepts in Haskell.

## 3.1 Basic Concepts
- A **type** is a collection of related values.
    - Example: `Bool` is a type that contains the values `True` and `False`.
    - Example: `Bool -> Bool` contains all functions that take a `Bool` as an argument and return a `Bool`.
- We use the notation `v::T` to denote that `v` has type `T`.
    - Example: `True :: Bool`
    - Example: `not :: Bool -> Bool`
- Unevaluated expressions have a type.
    - Example: `not True :: Bool`
    - Example: `not (not True) :: Bool`
- All expressions *must* have a type
    - This is part of Haskell's strong static type system.
    - All types are calculated at compile time by **type inference**.
    - The compiler will reject programs that have **type errors**.
- Haskell is **type safe**.
    - This means that a program cannot crash due to a type error.
    - This is because all type errors are caught at compile time.

## 3.2 Basic Types
Most common types in Haskell are built-in.
- **Bool** - logical values
    - `True` and `False`
- **Char** - single characters
    - All single characters in the Unicode standard
    - Includes special control characters like `\n` and `\t`
    - Must be surrounded by single quotes
- **String** - strings of characters
    - All sequences of characters
    - Must be surrounded by double quotes
- **Int** - fixed-precision integers
    - GHC has values of Int from $-2^{63}$ to $2^{63}-1$
- **Integer** - arbitrary-precision integers
    - Will use as much memory as necessary to store the value
    - Processing Integer is slower than Int
- **Float** - single-precision floating point numbers
    - The term floating point comes from the fact that the decimal point can "float" to the left or right. In other words, the number of digits after the decimal point depends on the size of the number.
- **Double** - double-precision floating point numbers
    - Double the precision of Float
    - Double the memory usage of Float

A single number can have **more than one** numeric type.
For example, `3` can have type `Int`, `Integer`, `Float`, or `Double`.
## 3.3 List Types
- A **list** is a sequence of elements of the same type.
- We write `[T]` to denote a list of elements of type `T`.
    - Example: `[False, True, False] :: [Bool]`
    - Example: `['a', 'b', 'c', 'd'] :: [Char]`
    - Example: `["one", "two", "three"] :: [String]`
- The **length** of a list is the number of elements.
    - Lists of length zero are called **empty lists**.
    - Lists of size one are called **singleton lists**.
        - Examples: `[False]`, `['a']`, `[[]]`
- Lists can get interesting, like having lists of lists.
    - Example: `[[1,2,3], [4,5], [6]] :: [[Int]]`
- Infinite lists can exist and are often practical due to lazy evaluation.

## 3.4 Tuple Types
- A **tuple** is a finite sequence of **components** of possibly different types.
- Tuples are enclosed by parentheses and separated by commas.
- The number of elements in a tuple is called its **arity**.
    - Tuple of arity 0 is called a **empty tuple**.
    - Tuples of arity 2 are called **pairs**.
    - Tuples of arity 3 are called **triples**.
    - Tuples of arity 1 are *not allowed*, since they conflict with parentheses to make order of operations explicit.
- Tuple types convey information about the arity of the tuple and the types of its components.
    - Example: `(False, True) :: (Bool, Bool)`
    - Example: `('a', False, "hello") :: (Char, Bool, String)`
    - Example: `([1,2], ['a','b','c']) :: ([Int], [Char])`
- Tuples must have finite arity to ensure type inference is decidable.

## 3.5 Function Types
- A **function** is a mapping from one type to another.
- We write `T1 -> T2` for the type of all functions that map arguments of `T1` to results of `T2`.
    - Example: `not :: Bool -> Bool`
    - Example: `even :: Int -> Bool`
- The existence of a function type `T1 -> T2` implies functions that take multiple arguments and return multiple results can exist.
    - This is done by packaging values with lists or tuples.
    - Example:
        ```haskell
        add :: (Int, Int) -> Int
        add (x, y) = x + y
        ```
- Haskell has the convention of preceding function bodies by their type signatures, as shown above.
- Functions do not have to be **total** on their argument type.
    - A function is **total** if it is defined for all values of its argument type.
    - Haskell has no restrictions on the domain of a function.
    - Example: `head :: [a] -> a` is not total because it is not defined for empty lists.

## 3.6 Curried Functions
- Functions with multiple arguments can also be handled by the fact that functions can return other functions as results.
    - Example:
        ```haskell
        add' :: Int -> (Int -> Int)
        add' x y = x + y
        ```
    - This function type takes an argument `Int` and returns a function of type `Int -> Int`.
    - The function definition takes an argument `x` and returns a function that takes an argument `y` and returns the sum of `x` and `y`.
- The above technique is called **currying**.
- Functions that do this are called **curried functions**.
- Curried functions are more flexible than functions that take tuples.
    - This is due to the fact that curried functions can be partially applied.
    - Only giving a function some of its arguments is called **partial application**.
    - For example, the partial application of `add' 1 :: Int -> Int` increments its argument by 1.
- There are two important conventions in Haskell when it comes to curried functions.
    - The arrow associates to the right.
        - This means `Int -> Int -> Int` is equivalent to `Int -> (Int -> Int)`.
    - Function application associates to the left.
        - This means `add' 1 2` is equivalent to `(add' 1) 2`.
- Generally, unless tupling is required, curried functions are preferred in Haskell.
- The meaning of curried function definitions can be formalized using lambda expressions.

## 3.7 Polymorphic Types
- The prelude function `length` can take a list of any type and return an `Int`.
- The length function uses a **type variable** to denote that it can take a list of any type.
- Type variables must begin with a lowercase letter, and typically are simply named `a`, `b`, `c`, etc.
- The type of `length` is `length :: [a] -> Int`.
- A type that contains at least one type variable is called **polymorphic**.

## 3.8 Overloaded Types
- The prelude function `+` calculates the sum of two numeric values.
- This works for two integers, two floats, etc.
- The idea that a single function can be used on multiple types is called **overloading**.
- The types of an overloaded function are defined with a **class constraint**.
    - Example: `(+) :: Num a => a -> a -> a`
    - The `Num a =>` part is the class constraint.
    - This means that `a` must be a member of the `Num` class.

## 3.9 Basic Classes
- A type is a collection of related values
- Building on this, a **class** is a collection of types that support certain overloaded operations called **methods**.
- Haskell has a number of built-in classes.
    - `Eq` - equality types
        - Types whose values can be tested for equality using `==` and `/=`.
        - All the basic types (`Bool`, `Char`, `String`, `Int`, `Integer`, `Float`, `Double`) are members of `Eq`.
        - List and tuple types are also members of `Eq` if their component types are members of `Eq`.
    - `Ord` - ordered types
        - Equality types that are totally (linearly) ordered.
        - Types that are members of `Ord` can be compared using `<`, `<=`, `>`, `>=`, `min`, and `max`.
        - All the basic types (`Bool`, `Char`, `String`, `Int`, `Integer`, `Float`, `Double`) are members of `Ord`.
        - Strings, lists, and tuples are ordered *lexicographically*.
    - `Show` - showable types
        - Types whose values can be converted to strings using `show :: a -> String`.
        - All the basic types (`Bool`, `Char`, `String`, `Int`, `Integer`, `Float`, `Double`) are members of `Show`.
        - List and tuple types are also members of `Show` if their component types are members of `Show`.
    - `Read` - readable types
        - Dual to show, types whose values can be converted from strings using `read :: String -> a`.
    - `Num` - numeric types
        - Values that are numeric and can be processed using `+`, `-`, `*`, `negate`, `abs`, and `signum`.
    - `Integral` - integral types
        - Instances of `Num` that are integers and can be processed using `div` and `mod`.
        - `div` performs integer division and `mod` performs integer modulus.
        - The basic integral types are `Int` and `Integer`.
    - `Fractional` - fractional types
        - Numeric types that support fractional division using `/` and fractional reciprocals using `recip`.