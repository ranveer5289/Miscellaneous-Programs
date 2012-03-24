readInt :: String -> Int
readInt = read

main = do
    x   <- fmap readInt getLine
    let y = (x + 3)
    print y
    x <- fmap readInt getLine
    print (x+3)
