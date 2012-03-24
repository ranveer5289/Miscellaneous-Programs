readInt :: String -> Int
readInt = read

main = do
    x <- fmap readInt getLine --stmt 1
    let y () = x + 3
    print (y ())
    x <- fmap readInt getLine --stmt 2
    print (y ())

