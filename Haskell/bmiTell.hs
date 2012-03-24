bmiTell :: (RealFloat a) => a -> String
bmiTell bmi 
        | bmi <= 18.5 = "underweight" 
        | bmi <=25.0  = "normal" 
        | bmi <=30.0  = "fat" 
        | otherwise   = "exit"

   
