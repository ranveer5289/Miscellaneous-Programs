take' n (x:xs)
        | n<=0 = [] 
        | n >=len = x:xs
        | otherwise = x:take' (n-1) xs
        where len = length (x:xs)
