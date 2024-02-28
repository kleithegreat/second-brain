

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
instance (Show a, Show b) => Show (Tree a b) where  -- We want to make Tree an instance of Show, and the elements of the tree must also be instances of Show.
   show a = showTree "" a  -- Here we define the show function for Tree objects, which uses a helper function showTree which is defined below.
      where  -- Here we want to define the helper function showTree which takes a string and a Tree object and returns a string. The string should just be the level of indentation, and then we need to consider the two constructors of the Tree data type: Leaf and Branch. The reason we need to use a helper function is because we need to keep track of the level of indentation as we traverse the tree.
         showTree space (Leaf a) = space ++ show a ++ "\n"  -- If we call showTree with a Leaf object, we return the given amount of indentation and then the string representation of the Leaf object, which is just calling the show function on the data in the Leaf object. After that we add a newline character.
         showTree space (Branch b l r) = space ++ show b ++ "\n" ++ showTree (space ++ "\t") l ++ showTree (space ++ "\t") r  -- In the case of a Branch object, we return the given amount of indentation and then the string representation of the data in the Branch, then a newline character. Then we call showTree on the left and right children of the Branch object, but we add one more tab of indentation to the space string. This is because we want to indent the children of the Branch object one more level than the Branch object itself.


-- Problem 3 (15 + 20 = 35 points)
---- Problem 3.1 (5 + 5 + 5 = 15 points)
preorder  :: (a -> c) -> (b -> c) -> Tree a b -> [c]  -- 5 points
-- This function takes two functions that both map to some type c, and a Tree object that can contain up to two different types of data (hence the two functions before). This function then returns a list of type c.
-- The returned list should just be the appropriate function applied to the data in the Tree object in a preorder traversal. 
preorder f g (Leaf a) = [f a]  -- In the case that we reach a leaf, we return a list containing the result of applying the first function to the data in the leaf, since the first function takes 'a' as an argument.
preorder f g (Branch b l r) = g b : preorder f g l ++ preorder f g r  -- In the case that we reach a branch, the preorder traversal is to first visit the root, then the left child, then the right child. Thus, we apply the function 'g' to the data of type 'b' in the branch node, then recursively call preorder on the left branch, then the right branch. This all gets concatenated together into one list.


inorder   :: (a -> c) -> (b -> c) -> Tree a b -> [c]  -- 5 points
-- This function has the same type signature as the previous function, and the same explanation applies.
-- The returned list should just be the appropriate function applied to the data in the Tree object in an inorder traversal.
inorder f g (Leaf a) = [f a]  -- This is the same as the base case for preorder, and the explanation is the same as before.
inorder f g (Branch b l r) = inorder f g l ++ [g b] ++ inorder f g r  -- Almost the same as the recursive case for preorder, but inorder goes in the order of left child, root, right child. Thus, we recursively call inorder on the left child, then apply the function 'g' to the data of type 'b' in the branch node, then recursively call inorder on the right child. This all gets concatenated together in that order into one list.


postorder  :: (a -> c) -> (b -> c) -> Tree a b -> [c]  -- 5 points
-- This function has the same type signature as the previous two functions, and the same explanation applies.
-- The returned list should just be the appropriate function applied to the data in the Tree object in a postorder traversal.
postorder f g (Leaf a) = [f a]  -- This is the same as the base case for preorder and inorder, and the explanation is the same as before.
postorder f g (Branch b l r) = postorder f g l ++ postorder f g r ++ [g b]  -- Almost the same as the recursive case for the last two functions, but postorder goes in the order of left child, right child, root. Thus, we recursively call postorder on the left child, then recursively call postorder on the right child, then apply the function 'g' to the data of type 'b' in the branch node. This all gets concatenated together in that order into one list.


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

eval :: Expr -> Cont -> Int  -- This function takes an Expr object and a control stack and returns an Int.
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

