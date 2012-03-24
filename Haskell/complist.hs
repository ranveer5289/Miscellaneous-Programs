complist xs = take 2 [if x<10 then 1 else 2 | x <- xs ]
{-complist xs = if odd x && x<10
              then "BOOM"
              else if x>10 && odd x
              then "BANG"
              else
              print "nothing"-}
