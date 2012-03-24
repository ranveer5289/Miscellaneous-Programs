maximum' [] = error "no max for empty list"
maximum' [x] = x
maximum' (x:xs) = max x (maximum' xs)
