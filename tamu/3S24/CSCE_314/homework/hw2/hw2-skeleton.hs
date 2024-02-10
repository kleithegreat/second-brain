
-- CSCE 314 [Sections  595, 596, 597] Programming Languages Spring 2024
-- Hyunyoung Lee
-- Homework Assignment 2 (Total 100 points) Due on Friday, 2/16/24 at 11:59 p.m.

-- Problem 1 (5 points)
-- Student Name: Kevin Lei
-- UIN: 432009232
-- Resources: Course textbook, canvas lectures

-- On my honor, as an Aggie, I have neither given nor received any unauthorized
-- aid on any portion of the academic work included in this assignment.

module Main where

import Test.HUnit
import System.Exit
import Data.List
import Data.Char

-- *** Read textbook Chapters 5, 6, and 7 ***

-- Problem 2 (Chapter 5, Exercise 9 (modified)) (10+5=15 points)
scalarproduct :: [Int] -> [Int] -> Int  -- This function takes two lists of Int types and returns a single Int type
---- Question 2.1 (10 points)
scalarproduct xs ys = sum (map (\(x, y) -> x * y) (zip xs ys))  -- This function works by zipping the two lists together and then mapping a lambda function that multiplies the two numbers in each tuple. After that, simply just sum the list of products to get the final result.

---- Question 2.2 (5 points)
{- Write your answer for Question 2.2 within this block comment.
When scalarproduct [3, 2, 4] [5..] is called, the result is 55.
The function evaluates like this:
  scalarproduct [3, 2, 4] [5..]
= sum (map (\(x, y) -> x * y) (zip [3, 2, 4] [5..]))             -- replace xs and ys with [3, 2, 4] and [5..] for clarity
= sum (map (\(x, y) -> x * y) [(3, 5), (2, 6), (4, 7)])          -- zip the two lists together, resulting in a list of tuples
= sum [15, 12, 28]                                               -- map a lambda function that multiplies the two numbers in each tuple
= 55                                                             -- sum the list of products to get the final result
-}



-- Problem 3 (Chapter 6, Exercise 7) (10 points)
merge :: Ord a => [a] -> [a] -> [a]  -- This function takes two lists of ordered type "a" and returns a single list of ordered type "a"
merge [] ys = ys  -- one base case where the left argument is the empty list, in this case return the other argument since there is nothing to merge.
merge xs [] = xs  -- other base case where the right argument is the empty list. same logic as above.
merge xs ys | head xs <= head ys = head xs : merge (tail xs) ys  -- recursive definition: in the case that the least value of xs is less than or equal to the least value of ys, then the least value of xs is the least value of the arguments, so we append it to the merged list and call merge again with the tail of xs and the same ys.
            | otherwise = head ys : merge xs (tail ys) -- otherwise, the least value of ys is the least value of the arguments, so we append it to the merged list and call merge again with the same xs and the tail of ys.



-- Problem 4 (Chapter 6, Exercise 8) (5+10=15 points)
---- Question 4.1 (5 points)
halve :: [a] -> ([a], [a])
halve xs = (lm, ao)
            where
              lm = head xs
              ao = 



---- Question 4.2 (10 points)
msort :: Ord a => [a] -> [a]
msort = undefined



-- Problem 5 (10+10+15=35 points)
---- Question 5.1 (10 points) 
mergeBy :: (a -> a -> Bool) -> [a] -> [a] -> [a]
mergeBy = undefined

---- Question 5.2 (10 points) 
msortBy :: (a -> a -> Bool) -> [a] -> [a]
msortBy = undefined

---- Question 5.3 (15 points)
{- Write your answer for Question 5.3 within this block comment.

-}



-- Problem 6 (Chapter 7, Exercise 9) (10+10=20 points)
---- Question 6.1 (10 points)
altMap :: (a -> b) -> (a -> b) -> [a] -> [b]
altMap = undefined

---- Question 6.2 (10 points)
{- Write your answer for Question 6.2 within this block comment.

-}




    
myTestList =
  TestList [
      "scalarproduct 1" ~: scalarproduct [4,5,6] [1,2,3] ~=? 32
    , "scalarproduct 2" ~: scalarproduct [2,3] [1,-1] ~=? -1
    , "scalarproduct 3" ~: scalarproduct [1..10] [1..5] ~=? 55
    , "scalarproduct 4" ~: scalarproduct [3,2,4] [5..] ~=? 55

    ,"merge 1" ~: merge "EGG" "ABCDEFGH" ~=? "ABCDEEFGGGH" 
    , "merge 2" ~: merge "Hello" "e" ~=? "Heello"
    , "merge 3" ~: merge [1,3,5,7,9] [2,4,6] ~=? [1,2,3,4,5,6,7,9]

    , "halve 1" ~: halve "" ~=? ("","")
    , "halve 2" ~: halve "halves" ~=? ("hal","ves")
    , "halve 3" ~: halve "halve" ~=? ("ha","lve")

    , "msort 1" ~: msort "Howdy all!" ~=? " !Hadllowy"
    , "msort 2" ~: msort "" ~=? ""
    , "msort 3" ~: msort "Mississippi" ~=? "Miiiippssss"
    , "msort 4" ~: msort [3,2,1,5,4] ~=? [1,2,3,4,5]

    , "mergeBy 1" ~: mergeBy (>) "FED" "GBA" ~=? "GFEDBA"
    , "mergeBy 2" ~: mergeBy (<) "Howdy" "Maui" ~=? "HMaouiwdy"
    , "mergeBy 3" ~: mergeBy (>) [5,1] [6,4,3] ~=? [6,5,4,3,1]
      
    , "msortBy 1" ~: msortBy (<) "gig 'em" ~=? " 'eggim" 
    , "msortBy 2" ~: msortBy (>) "Jack be nimble" ~=? "nmlkieecbbaJ  "
    , "msortBy 3" ~: msortBy (<) "" ~=? ""
    , "msortBy 4" ~: msortBy (>) [3,2,1,5,4] ~=? [5,4,3,2,1]

    , "altMap 1" ~: altMap (* 10) (* 100) [1,2,3,4,5] ~=? [10,200,30,400,50]
    , "altMap 2" ~: and (altMap even odd [1..10]) ~=? False
    , "altMap 3" ~: altMap toLower toUpper "Haskell IS fun!" ~=? "hAsKeLl iS FuN!"
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
