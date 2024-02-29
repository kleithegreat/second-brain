-- Question 2
-- a) using a conditional expression
safetail :: [a] -> [a]
safetail xs = if null xs then [] else tail xs

-- b) using guarded equations
safetail' :: [a] -> [a]
safetail' xs | null xs = []
             | otherwise = tail xs

-- c) using pattern matching
safetail'' :: [a] -> [a]
safetail'' [] = []
safetail'' (x:xs) = xs