safetail :: [a] -> [a]
safetail xs = if null xs then [] else tail xs

safetail' ::[a] -> [a]
safetail' xs | null xs = []
             | otherwise = tail xs

safetail'' ::[a] -> [a]
safetail'' [] = []
safetail'' xs = tail xs

fuckkoreans [] = [[]]
fuckkoreans (x:xs) = fuckkoreans xs ++ [x:s | s <- fuckkoreans xs]
