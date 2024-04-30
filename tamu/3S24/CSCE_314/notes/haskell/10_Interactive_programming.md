# Interactive Programming
Here we discuss how to write interactive programs in Haskell. Handling interaction in Haskell is dealt with using a range of primitives and derived functions.
## 10.1 The problem
- In the early days of computing, programs were **batch programs** that were run in isolation from users.
- This was done to maximize time spent on actual work.
- We have already went over how Haskell can be used to write batch programs.
- This makes sense, as batch programs are essentially functions that take input and produce output.
- **Pure functions** are ideal for this kind of work, defined as functions that take all their inputs as explicit arguments and produce all their outputs as explicit results.
- However, in the modern world, we need to write **interactive programs** that are run as an ongoing dialogue with the user.
- For example, an interpreter is an interactive program.
- At first sight it may seem impossible to model interactive programs using pure functions, since their very nature requires the **side effects** of taking additional input and producing additional output.
- The solution used in Haskell is based on a new type with some primitive operations.
- The underlying approach doesn't just work for interactions, but for side effects in general.
## 10.2 The solution
- Haskell views interactive programs as a pure function that takes the current **state of the world** as an argument and produces a modified state of the world as a result.
- This modified world reflects the side effects of the program.
- The type `World` represents states of the world, so an interactive program is a function of type `World -> World`.
- We abbreviate this as `IO`, and is defined as:
    ```haskell
    type IO a = World -> World
    ```
- Interactive programs may also return a result in addition to modifying the state of the world.
    - For example, a program that reads a character from the keyboard and returns it.
    - Thus, we generalize the type `IO` to also return a result:
        ```haskell
        type IO a = World -> (a, World)
        ```
- Expressions of type `IO a` are called **actions**.
    - For example, `IO Char` is the type of actions that return a character.
    - `IO ()` is the type of actions that return an empty tuple as a dummy result.
- Expressions of the type `IO ()` can be thought of as purely side effecting actions with no result.
- Aside from returning results, interactive programs also often require argument values.
- We dont need to generalize `IO` to take arguments, as we can use currying to achieve this.
    - For example, an interactive program that takes a character as an argument and returns an integer as a result has type `Char -> IO Int`.
    - This is actually an abbreviation for `Char -> (World -> (Int, World))`.
- We don't need to worry about the details of the `World` type or how `IO` is implemented.
    - We just need to know that `IO` is a type of actions that modify the state of the world and return a result.
    - `IO` is a primitive in Haskell.
## 10.3 Basic actions
- The action `getChar` reads a character from the keyboard, echoes it to the screen, and returns it as a result.
    - It has type `IO Char`.
    - The actual definition is built into GHC.
    - It will wait for a character to be typed when there is no input available.
- The action `putChar c` writes the character `c` to the screen and returns `()`.
    - It has type `Char -> IO ()`.
- The action `return v` returns the value `v` without interacting with the user.
    - It has type `a -> IO a`.
    - This is meant to be a bridge between pure to impure code.
    - However, there is no way going from impure to pure code--once you go impure, you stay impure.
- Impurity does not actually permeate entire programs.
    - The majority of functions do not involve interaction.
    - Interactions are usually handled by a relatively small number of functions on the outermost level.
## 10.4 Sequencing
- A sequence of `IO` actions can be combined in a single action using the `do` keyword, typically done as follows:
    ```haskell
    do v1 <- a1
       v2 <- a2
       ...
       vn <- an
       return (f v1 v2 ... vn)
    ```
- These expressions have a simple meaning:
    - First perform the action `a1` and bind its result to `v1`.
    - Then perform the action `a2` and bind its result to `v2`.
    - Continue in this way until the action `an` is performed and its result is bound to `vn`.
    - Apply the function `f` to combine the results of the actions.
    - Return the result of the combined actions.
- The `do` notation has some idiosyncrasies:
    - Each action must be in the same column, which follows from the layout rule.
    - The expressions `vi <- ai` are called **generators**, similar to list comprehensions.
    - If the result `vi` of an action `ai` is not used, the generator can be abbreviated as `ai`, which has the same meaning as `_ <- ai`.
- For example, the following program reads three characters, discards the second, and returns the first and third as a pair:
    ```haskell
    act :: IO (Char, Char)
    act = do x <- getChar
             getChar
             y <- getChar
             return (x, y)
    ```
    - Forgetting the `return` statement would result in a type error, since it wraps the `(Char, Char)` in an `IO (Char, Char)`.
## 10.5 Derived primitives
- We can define a number of derived action primitives using the three basic actions and sequencing.
- For example, we can define the action `getLine` that reads a line of characters from the keyboard until a newline `\n` is encountered:
    ```haskell
    getLine :: IO String
    getLine = do x <- getChar
                 if x == '\n' then
                    return []
                 else
                    do xs <- getLine
                       return (x:xs)
    ```
    - We use recursion to read the rest of the string after the first character.
- We can also define the action `putStr` and `putStrLn` that write a string to the screen:
    ```haskell
    putStr :: String -> IO ()
    putStr [] = return ()
    putStr (x:xs) = do putChar x
                       putStr xs

    putStrLn :: String -> IO ()
    putStrLn xs = do putStr xs
                     putChar '\n'
    ```
- Using these primitives, we can define a program that prompts the user to enter a string and then echoes the length of the string:
    ```haskell
    strlen :: IO ()
    strlen = do putStr "Enter a string: "
                xs <- getLine
                putStr "The string has "
                putStr (show (length xs))
                putStrLn " characters."
    ```
    ```
    > strlen
    Enter a string: Haskell
    The string has 7 characters.
    ```