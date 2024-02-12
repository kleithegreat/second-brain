# Declaring Types and Classes
This chapter covers mechanisms for declaring new types and classes in Haskell.
## 8.1 Type declarations
- The simplest way of declaring a new type is introducing a new name for an existing type.
- For example, the following declaration introduces the type `String` as a synonym for the type `[Char]`.
  ```haskell
  type String = [Char]
  ```
- The name of a new type must start with a capital letter.
- Type declarations can be nested, as in one type can be defined in terms of another type.
- For example, if we are defining a number of functions that transform coordinate positions, we can declare a position as a pair of integers.
    ```haskell
    type Pos = (Int, Int)
    type Trans = Pos -> Pos
    ```
- Type declarations cannot be recursive however.
- For example, the following declaration is not allowed.
  ```haskell
  type Tree = (Int, [Tree])
  ```
- When required, recursive types can be defined using the more powerful `data` declaration.
- Type declarations can also be parameterized.
- Say we want to define a number of functions that manipulate pairs of values of the same type.
- We can define a type `Pair` that is parameterized by a type `a`.
  ```haskell
  type Pair a = (a, a)
  ```
- Type declarations with more than one parameter are also allowed.
- For example, we can define a type of lookup tables that map keys of one type to values of another type.
  ```haskell
  type Assoc k v = [(k, v)]
  ```
- Using this we can define a function that returns the first value that is associated with a given key in a lookup table.
  ```haskell
  find :: Eq k => k -> Assoc k v -> v
  find k t = head [v | (k', v) <- t, k == k']
  ```
## 8.2 Data declarations
- A completely new type, rather than a synonym for an existing type, can be defined using a `data` declaration.
- For example, the standard prelude defines a new type `Bool` with the following declaration.
  ```haskell
  data Bool = False | True
  ```
  - This means that the type `Bool` has two values, `False` and `True`.
- In these declarations, the `|` symbol is read as "or".
- The new values of a type are called its **constructors**.
    - The names of new constructors must start with a capital letter.
    - The same constructor name can be used in different types.
- The names given to new types and constructors have no inherent meaning to the Haskell compiler.
- For example, the definition of the type `Bool` could have been written as follows.
  ```haskell
  data B = F | T
  ```
- The names `Bool`, `False`, and `True` are predefined in Haskell, so the first definition has more meaning to a human reader.
- Values of new types can be used in the same ways as values of built-in types.
    - Most importantly, they can be used as arguments to functions and as results of functions.
    - Say we have this declaration:
        ```haskell
        data Move = North | South | East | West
        ```
    - We can define a function that moves in a direction.
        ```haskell
        move :: Move -> Pos -> Pos
        move North (x, y) = (x, y + 1)
        move South (x, y) = (x, y - 1)
        move East (x, y) = (x + 1, y)
        move West (x, y) = (x - 1, y)
        ```
- Constructors can also have arguments.
- For example, a type consisting of circles with a given radius and rectangles with given sides can be defined as follows.
  ```haskell
  data Shape = Circle Float | Rect Float Float
  ```
    - This means the type `Shape` has values of the form `Circle r` and `Rect x y`, where `r`, `x`, and `y` are of type `Float`.
    - These constructors can be used to define functions on shapes, like:
        ```haskell
        square :: Float -> Shape
        square n = Rect n n
        ```
        ```haskell
        area :: Shape -> Float
        area (Circle r) = pi * r^2
        area (Rect x y) = x * y
        ```
    - Due to the use of arguments, the constructors `Circle` and `Rect` are actually **contructor functions** that produce values of the type `Shape` from arguments of the `Float` type
        ```haskell
        Circle :: Float -> Shape
        Rect :: Float -> Float -> Shape
        ```
- The difference between normal functions and constructor functions is that the latter have no defining equations.
- See the following examples:
    - `negate 1.0` can be simplified to `-1.0`
    - However, `Circle 1.0` cannot be simplified to anything, since there are no defining equations.
- One can think of a constructor function as a functional analog of the imperative struct.
- Data declarations can also be parameterized.
- For example, the standard prelude includes the following type definition:
    ```haskell
    data Maybe a = Nothing | Just a
    ```
    - This means a value of type `Maybe a` is either `Nothing` or `Just x`, where `x` is of type `a`.
    - Values of the types `Maybe a` can be used to represent values of type `a` may fail to exist.
- We can use the `Maybe` type to define safe versions of functions like `div` and `head`.
    ```haskell
    safediv :: Int -> Int -> Maybe Int
    safediv _ 0 = Nothing
    safediv m n = Just (m `div` n)
    ```
    ```haskell
    safehead :: [a] -> Maybe a
    safehead [] = Nothing
    safehead xs = Just (head xs)
    ```
## 8.3 Newtype declarations
- A `newtype` declaration is a way of defining a new type that has only one constructor and only one argument.
- For example, a type of natural numbers can be defined as follows.
  ```haskell
  newtype Nat = N Int
  ```
  - This means a single constructor `N` that takes an `Int` as an argument.
  - Here it is up to the programmer to ensure that the argument of the constructor `N` is always a non-negative integer.
- This begs the question of why we would use `newtype` instead of `data` or `type`.
    ```haskell
    type Nat = Int
    data Nat = N Int
    ```
- Using `newtype` instead of `type` means that the new type is *not* just a synonym for an existing type.
- Using `newtype` instead of `data` is beneficial since it does not incur the overhead of an extra constructor at runtime.
> The upshot is that `newtype` helps improve safety without affecting performance.
## 8.4 Recursive types
- New types using `data` and `newtype` can be recursive.
- A recursive definition of the natural numbers was given in a previous section:
    ```haskell
    data Nat = Zero | Succ Nat
    ```
    - This means a value of type `Nat` is either `Zero` or `Succ n`, for some `n` of type `Nat`.
    - Here, values of type `Nat` are represented with `Zero` and a chain of successor applications.
- We can define conversion functions between `Nat` and `Int` as follows.
    ```haskell
    nat2int :: Nat -> Int
    nat2int Zero = 0
    nat2int (Succ n) = 1 + nat2int n
    ```
    ```haskell
    int2nat :: Int -> Nat
    int2nat 0 = Zero
    int2nat n = Succ (int2nat (n - 1))
    ```
## 8.5 Class and instance declarations
