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


safehead :: [a] -> Maybe a
safehead xs = if null xs then Nothing else Just (head xs)

safehead' :: [a] -> Maybe a
safehead' xs | null xs = Nothing 
             | otherwise = Just $ head xs