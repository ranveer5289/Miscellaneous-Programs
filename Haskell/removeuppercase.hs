removeuppercase :: [Char] -> [Char]
removeuppercase xs = [x | x <- xs, x `elem` ['A'..'Z']]
