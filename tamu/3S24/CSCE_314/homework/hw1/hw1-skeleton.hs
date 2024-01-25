
-- CSCE 314 [Sections 595, 596, 597] Programming Languages, Spring 2024
-- Homework Assignment 1 (Total 140 points)

-- Problem 1 (5 points)
-- This is head comment (single line comment should be preceded by two dashes)
-- Student Name: Kevin Lei
-- UIN: 432009232
-- Resources: (ACKNOWLEDGE ANY HELP RECEIVED HERE)

-- On my honor, as an Aggie, I have neither given nor received any unauthorized
-- aid on any portion of the academic work included in this assignment.

module Main where

import Test.HUnit  -- if this line causes compile error, try the following
                   -- command at the terminal prompt > cabal v1-install HUnit
import System.Exit


-- Example:
-- Write a recursive function mySum that sums all the numbers
-- in a list without using the prelude function sum.
mySum :: [Int] -> Int  -- type signature of mySum. mySum accepts a list of Ints
                       -- as its argument and returns an Int
mySum []     = 0  -- def.1
mySum (x:xs) = x + mySum xs -- def.2

{- Block comment over multiple lines is enclosed within {- and -}
Explanation:
The type of mySum tells us that mySum takes a list of Ints as an argument
and returns an Int that is the sum of all the Ints in the argument list.

Def.1 of mySum is the base case of the recursion, that is,
the argument list is empty, for which case the function value is 
defined as zero (summation identity).

Def.2 is when the argument list contains at least one element, 
namely x, in which case the function is defined as the sum of x 
and the result of the recursive call of mySum applied to the rest of 
the argument list, namely xs.
-}


-- Problem 2 (5+10 = 15 points)
qsort1 :: Ord a => [a] -> [a]
---- Question 2.1 (5 points)
qsort1 (x:xs) = 

---- Question 2.2 (10 points)
{- Write your answer for Question 2.2 within this block comment.

-}


-- Problem 3 (10 points)
lucas :: Int -> Int
lucas = undefined


-- Problem 4 (10 points)
factorial :: Int -> Int
factorial = undefined


-- Problem 5 (5+10+10=25 points)
---- Question 5.1 (5 points)
semifactorial :: Int -> Int
semifactorial = undefined

---- Question 5.2 (10 points)
{- Write your answer for Question 5.2 within this block comment.

-}

---- Question 5.3 (10 points)
myfactorial :: Int -> Int
myfactorial = undefined



-- Problem 6 (10+15+10=35 points)
---- Question 6.1 (10 points)
term :: Num a => Int -> a -> a
term = undefined

---- Question 6.2 (15 points)
polynaive :: Num a => [a] -> Int -> a -> a
polynaive = undefined

---- Question 6.3 (10 points)
{- Write your answer for Question 6.3 within this block comment.

-}



type Set a = [a]

-- Problem 7 (10 points)
isElem :: Eq a => a -> [a] -> Bool
isElem = undefined


-- Problem 8 (10 points)
-- Using isElem (from Problem 7) in the definition is required.
toSet :: Eq a => [a] -> Set a
toSet = undefined


-- Problem 9 (10 points)
-- Using isElem (from Problem 7) in the definition is required.
subset :: Eq a => Set a -> Set a -> Bool
subset = undefined


-- Problem 10 (10 points)
-- Using subset (from Problem 9) in the definition is required.
setEqual :: Eq a => Set a -> Set a -> Bool
setEqual = undefined



myTestList = 
  TestList [

      "qsort1 1" ~: qsort1 [3, 2, 5, 1, 8] ~=? [8,5,3,2,1]
    , "qsort1 2" ~: qsort1 "howdy" ~=? "ywohd"
    , "qsort1 3" ~: qsort1 "Oh, happy day!" ~=? "yypphhdaaO,!  "

    , "lucas 1" ~: lucas 0 ~=? 2
    , "lucas 2" ~: lucas 1 ~=? 1    
    , "lucas 3" ~: lucas 4 ~=? 7
    
    , "factorial 1" ~: factorial 3 ~=? 6
    , "factorial 2" ~: factorial 5 ~=? 120
    , "factorial 3" ~: factorial 10 ~=? 3628800

    , "semifactorial 1" ~: semifactorial 3 ~=? 3
    , "semifactorial 2" ~: semifactorial 5 ~=? 15
    , "semifactorial 3" ~: semifactorial 10 ~=? 3840

    , "myfactorial 1" ~: myfactorial 3 ~=? 6
    , "myfactorial 2" ~: myfactorial 5 ~=? 120
    , "myfactorial 3" ~: myfactorial 10 ~=? 3628800

    , "term 1" ~: term 3 2 ~=? 8
    , "term 2" ~: term 4 5 ~=? 625
    , "term 3" ~: term 10 3 ~=? 59049

    , "polynaive 1" ~: polynaive [2,-1,3,5] 3 2 ~=? 23
    , "polynaive 2" ~: polynaive [1,3,0,7,2] 4 5 ~=? 1037
    , "polynaive 3" ~: polynaive [(1/3),1,-2,0,2,1,(1/2)] 6 3 ~=? 345.5
    , "polynaive 4" ~: polynaive [3,-4,2,7] 3 2 ~=? 19

    , "isElem 1" ~: (isElem 'h' "happy") ~=? True
    , "isElem 2" ~: (isElem 'o' "happy") ~=? False
    , "isElem 3" ~: (isElem 'p' "happy") ~=? True

    , "toSet 1" ~: length (toSet "aardvark") ~=? 5
    , "toSet 2" ~: length (toSet "BartBart") ~=? 4

    , "subset 1" ~: subset [] [1,2] ~=? True
    , "subset 2" ~: subset [1,2] [] ~=? False
    , "subset 3" ~: subset [2,3] [1,2] ~=? False
    , "subset 4" ~: subset [2,3] [3,1,2] ~=? True
    , "subset 5" ~: subset [2,3] [2,1,4] ~=? False

    , "setEqual 1" ~: setEqual "abc" "bca" ~=? True
    , "setEqual 2" ~: setEqual [1,2] [2,1] ~=? True
    , "setEqual 3" ~: setEqual [1,2,3] [1,2,3,4] ~=? False
    , "setEqual 4" ~: setEqual [2,3,1] [1,2,3] ~=? True

    ]

main = do c <- runTestTT myTestList
          putStrLn $ show c
          let errs = errors c
              fails = failures c
          exitWith (codeGet errs fails)
          
codeGet errs fails
 | fails > 0       = ExitFailure 2
 | errs > 0        = ExitFailure 1
 | otherwise       = ExitSuccess

