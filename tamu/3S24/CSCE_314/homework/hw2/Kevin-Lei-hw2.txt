
-- CSCE 314 [Sections  595, 596, 597] Programming Languages Spring 2024
-- Hyunyoung Lee
-- Homework Assignment 2 (Total 100 points) Due on Friday, 2/16/24 at 11:59 p.m.

-- Problem 1 (5 points)
-- Student Name: Kevin Lei
-- UIN: 432009232
-- Resources: Course textbook, canvas lectures, haskell standard prelude website

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
halve :: [a] -> ([a], [a])  -- This function takes a list of any type "a" and returns a tuple of two lists of type "a"
halve xs = splitAt (length xs `div` 2) xs -- Halve should pass the argument to splitAt and its length in half as the other argument, which returns the desired tuple


---- Question 4.2 (10 points)
msort :: Ord a => [a] -> [a]  -- This functions takes a list of an ordered type "a" and returns a list of type "a"
msort [] = []  -- base case: empty list sorted is the empty list
msort [a] = [a]  -- base case: singleton list sorted is just itself
msort xs = merge lm ao  -- recursive case: merge two sorted lists, where each list is a sorted half of the list to be sorted
          where  -- we want to define our halves here
            (pog, gers) = halve xs  -- use pattern matching to assign names to each half
            lm = msort pog  -- recursively call msort on this half to sort it before merging
            ao = msort gers  -- without loss of generality, same applies here



-- Problem 5 (10+10+15=35 points)
---- Question 5.1 (10 points) 
mergeBy :: (a -> a -> Bool) -> [a] -> [a] -> [a]  -- this function takes three things: 1. another function that takes two values of type "a" and returns their type, 2. a list of type "a", 3. another list of type "a". this function returns a list of type "a"
mergeBy f [] ys = ys  -- base case: any list merged with the empty list is itself
mergeBy f xs [] = xs  -- base case: any list merged with the empty list is itself
mergeBy f xs ys | f (head xs) (head ys) = head xs : mergeBy f (tail xs) ys  -- use the given function to determine which element goes first: if the function returns true, the head of xs goes first, and then recursively call mergeBy on the rest of the lists without the head of xs
                | otherwise = head ys : mergeBy f xs (tail ys)  -- if the function returns false, the head of ys comes first, and recursively call mergeBy on the rest of the list without the head of ys

---- Question 5.2 (10 points) 
msortBy :: (a -> a -> Bool) -> [a] -> [a]  -- this function takes the same kind of comparison function as the one taken by mergeBy and a list of any type "a"
msortBy f [] = []  -- base case: like the prior msort function, the empty list sorted is just the empty list
msortBy f [a] = [a] -- base case: the sorted singleton list is just itself
msortBy f xs = mergeBy f lm ao  -- the sorted list is given by merging two smaller sorted lists, and we want to use the same comparison function in mergeBy as it is given to msortBy
              where  -- define our two halves
                (pog, gers) = halve xs  -- pattern match the resuls of halve
                lm = msortBy f pog  -- recursively call msortBy to sort this half of the list
                ao = msortBy f gers  -- same thing as above

---- Question 5.3 (15 points)
{- Write your answer for Question 5.3 within this block comment.
when we call msortBy (>) [3,2,1,5,4], it gives halve [3,2,1,5,4] which yields (pog, gers) = ([3,2], [1,5,4]).
In our first recursive call we have msortBy (>) [3,2]
Halve [3,2] results in ([3], [2]).
We then call msortBy (>) [3] which returns [3] since a singleton list is already sorted.
THen, msortBy (>) [2] returns [2] for the same reason.
MergeBy (>) [3] [2] is called, and since 3 > 2, 3 is placed before 2, resulting in [3,2].
Now this half is sorted and we move on to the next recursive call, whcih is msortBy (>) [1,5,4]
Splitting this into halves gives us ([1], [5,4]).
Then msortBy is called on [1] and [5,4].
The first recursive call returns [1] since it is a singleton list.
Then [5, 4] is split into halves, resulting in ([5], [4]), and msoryBy is called on each of these halves.
Both lists are singletons, so nothing happens here.
Now, mergeBy (>) [5] [4] is called, and since 5 > 4, 5 is placed before 4, resulting in [5,4].
Then mergeBy (>) [1] [5,4] is called, and since 5 > 1 and 4 > 1, 5 is placed before 1, and 4 is placed before 1, resulting in [5,4,1].
Now this half is sorted, so we merge the final two halves.
The final sorted list is [5,4,3,2,1].
-}



-- Problem 6 (Chapter 7, Exercise 9) (10+10=20 points)
---- Question 6.1 (10 points)
altMap :: (a -> b) -> (a -> b) -> [a] -> [b]  -- this function takes two functions that map from a to b and a list of as and returns a list of bs
altMap f g [] = []  -- base case: applying this function to the empty list returns just the empty list
altMap f g xs = f (head xs) : altMap g f (tail xs)  -- apply the first function to the head of the given list argument, then apply altMap to the rest of the list recursively except the position of f and g in the arguments is swapped, so the next call will apply g to the head of the remaining list and so on

---- Question 6.2 (10 points)
{- Write your answer for Question 6.2 within this block comment.
  altMap (‘div‘ 2) (*7) [1..9]
= 1 `div` 2 : altMap (*7) (`div` 2) [2..9]
= 0 : 2 * 7 : altMap (`div` 2) (*7) [3..9]
= 0 : 14 : 3 `div` 2 : altMap (*7) (`div` 2) [4..9]
= 0 : 14 : 1 : 4 * 7 : altMap (`div` 2) (*7) [5..9]
= 0 : 14 : 1 : 28 : 5 `div` 2 : altMap (*7) (`div` 2) [6..9]
= 0 : 14 : 1 : 28 : 2 : 6 * 7 : altMap (`div` 2) (*7) [7..9]
= 0 : 14 : 1 : 28 : 2 : 42 : 7 `div` 2 : altMap (*7) (`div` 2) [8..9]
= 0 : 14 : 1 : 28 : 2 : 42 : 3 : 8 * 7 : altMap (`div` 2) (*7) [9]
= 0 : 14 : 1 : 28 : 2 : 42 : 3 : 56 : 9 `div` 2 : altMap (*7) (`div` 2) []
= 0 : 14 : 1 : 28 : 2 : 42 : 3 : 56 : 4 : []
= [0,14,1,28,2,42,3,56,4]
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
