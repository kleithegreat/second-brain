

-- CSCE 314 [Sections 595, 596, 597] Programming Languages Spring 2024
-- Homework Assignment 3 (Total 120 points)
-- Due on Friday, March 1, 2024

-- Problem 1 (5 points)
-- Student Name: Kevin Lei
-- UIN: 432009232
-- course textbook, canvas lectures
-- On my honor, as an Aggie, I have neither given nor received any unauthorized
-- aid on any portion of the academic work included in this assignment.

module Main where

import Test.HUnit
import System.Exit

-- *** Read Chapters 8 and 16 ***

data Tree a b = Leaf a | Branch b (Tree a b) (Tree a b)

---- Tree objects to be used to test your functions in Problems 2 and 3
-- Use tree1 to show the step-by-step of your functions in Problem 3
tree1 :: Tree Int String
tree1 = Branch "*"
            (Branch "+"
               (Branch "*" (Leaf 2) (Leaf 6))
               (Branch "+" (Leaf 3) (Leaf 4)))
            (Branch "*"
               (Branch "+"
                  (Branch "*" (Leaf 8) (Leaf 2))
                  (Leaf 7))
               (Branch "+" (Leaf 5) (Leaf 4)))

-- Another example Tree object
tree2 :: Tree Int String
tree2 = Branch "+"
            (Branch "*" (Leaf 1) (Leaf 2))
            (Leaf 3)

-- Yet another Tree object
tree3 :: Tree Int String
tree3 = Branch "+"
            (Branch "*"
               (Leaf 3)
               (Leaf 4))
            (Branch "+"
               (Branch "*" (Leaf 5) (Leaf 2))
               (Leaf 1))
---------------

-- Problem 2 (20 points)
instance (Show a, Show b) => Show (Tree a b) where
   show a = showTree "" a
      where
         showTree space (Leaf a) = space ++ show a ++ "\n"
         showTree space (Branch b l r) = space ++ show b ++ "\n" ++ showTree (space ++ "\t") l ++ showTree (space ++ "\t") r


-- Problem 3 (15 + 20 = 35 points)
---- Problem 3.1 (5 + 5 + 5 = 15 points)
preorder  :: (a -> c) -> (b -> c) -> Tree a b -> [c]  -- 5 points
preorder f g (Leaf a) = [f a]
preorder f g (Branch b l r) = g b : preorder f g l ++ preorder f g r


inorder   :: (a -> c) -> (b -> c) -> Tree a b -> [c]  -- 5 points
inorder f g (Leaf a) = [f a]
inorder f g (Branch b l r) = inorder f g l ++ [g b] ++ inorder f g r


postorder  :: (a -> c) -> (b -> c) -> Tree a b -> [c]  -- 5 points
postorder f g (Leaf a) = [f a]
postorder f g (Branch b l r) = postorder f g l ++ postorder f g r ++ [g b]


---- Problem 3.2 (10 + 10 = 20 points)
{-- Explain the step-by-step of the following expression (each 10 points).
    Your answer must be in detail step-by-step.

> preorder show id tree1 


> inorder show id tree1


--}
                          

-- Problem 4 (40 points) Chapter 8, Exercise 9 Modified
data Expr = Val Int | Add Expr Expr | Subt Expr Expr | Mult Expr Expr

type Cont = [Op]

data Op = EVALA Expr | ADD Int | EVALS Expr | SUBT Int | EVALM Expr | MULT Int

eval :: Expr -> Cont -> Int
-- Give four definitions for eval.
-- First two definitions,
-- 1) for (Val n) and c as arguments and
-- 2) for (Add x y) and c as arguments
-- are already given in the text Section 8.7, but
-- you need to modify the second definition slightly
-- and give the third and fourth definitions for
-- (Subt x y) and (Mult x y)
eval (Val n) c = exec c n
eval (Add x y) c = eval x (EVALA y : c)
eval (Subt x y) c = eval x (EVALS y : c)
eval (Mult x y) c = eval x (EVALM y : c)


exec :: Cont -> Int -> Int
-- Give seven definitions for exec, one for an empty list and
-- one for each of the six constructors of the data type Op
-- Some of these are already given in the text Section 8.7.
exec [] n = n
exec (EVALA y : c) n = eval y (ADD n : c)
exec (ADD n : c) m = exec c (n+m)
exec (EVALS y : c) n = eval y (SUBT n : c)
exec (SUBT n : c) m = exec c (n-m)
exec (EVALM y : c) n = eval y (MULT n : c)
exec (MULT n : c) m = exec c (n*m)


value :: Expr -> Int
value e = eval e []

-- Following expressions are to test your eval and exec definitions
-- (2 + 3) + 4 = 9
e1 = (Val 3)    -- 3
e2 = (Add (Val 4) (Val 2))  -- 4 + 2 = 6
e3 = (Mult (Val 4) (Val 3))  -- 4 * 3 = 12
e4 = (Add (Subt (Val 5) (Val 3)) (Val 4))  -- (5 - 3) + 4 = 6
e5 = (Mult (Mult (Val 2) (Val 3)) (Val 4))  -- (2 * 3) * 4 = 24
e6 = (Mult (Add (Val 2) (Val 3)) (Val 4))  -- (2 + 3) * 4 = 20
e7 = (Mult (Subt (Val 3) (Val 1)) (Val 4))  -- (3 - 1) * 4 = 8
e8 = (Add (Mult (Val 2) (Val 3)) (Val 4))  -- (2 * 3) + 4 = 10
e9 = (Subt (Mult (Val 2) (Val 3)) (Add (Val 4) (Val 1))) -- (2 * 3) - (4 + 1) = 1
e10 = (Mult (Subt (Val 10) (Val 3)) (Add (Val 4) (Val 5))) -- (10 - 3) * (4 + 5) = 63
e11 = (Add (Mult (Add (Val 2) (Val 3)) (Mult (Val 4) (Val 5))) (Mult (Val 3) (Subt (Val 4) (Val 7)))) -- ((2 + 3) * (4 * 5)) + (3 * (4 - 7)) = 91


-- Problem 5 (20 points)
-- Show the step-by-step of the following application of value.
-- > value e9
{-- Your answer goes here. Your answer must be in detail step-by-step.


--}



myTestList =
  TestList [

    "preorder 1"  ~: (concat (preorder show id tree1)) ~=? "*+*26+34*+*827+54"
  , "inorder 1"   ~: (concat (inorder show id tree1))  ~=? "2*6+3+4*8*2+7*5+4"
  , "postorder 1" ~: (concat (postorder show id tree1)) ~=? "26*34++82*7+54+**"
  , "preorder 2"  ~: (concat (preorder show id tree2)) ~=? "+*123"
  , "inorder 2"   ~: (concat (inorder show id tree2))  ~=? "1*2+3"
  , "postorder 2" ~: (concat (postorder show id tree2))  ~=? "12*3+"
  , "preorder 3"  ~: (concat (preorder show id tree3)) ~=? "+*34+*521"
  , "inorder 3"   ~: (concat (inorder show id tree3))  ~=? "3*4+5*2+1"
  , "postorder 3" ~: (concat (postorder show id tree3))  ~=? "34*52*1++"

  , "value 1"  ~: value e1 ~=? 3
  , "value 2"  ~: value e2 ~=? 6
  , "value 3"  ~: value e3 ~=? 12
  , "value 4"  ~: value e4 ~=? 6
  , "value 5"  ~: value e5 ~=? 24
  , "value 6"  ~: value e6 ~=? 20
  , "value 7"  ~: value e7 ~=? 8
  , "value 8"  ~: value e8 ~=? 10
  , "value 9"  ~: value e9 ~=? 1
  , "value 10" ~: value e10 ~=? 63
  , "value 11" ~: value e11 ~=? 91

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

