# Exercise 5
## Problem 1
Given the following declaration of Haskell class Functor.

 

class Functor f where
   fmap :: (a -> b) -> f a -> f b

 

What can go in the underlined space below so that the Functor laws are preserved?

 

instance Functor Maybe where
   fmap _ Nothing = Nothing
   fmap f (Just x) = __________

answer: Just (f x)