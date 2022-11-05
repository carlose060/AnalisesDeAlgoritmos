import System.Environment

fibC :: Integer -> Integer -> Integer -> Integer
fibC 2 _ t = t
fibC z x y = fibC (z-1) y (x+y)
 
getIntArg :: IO  Integer
getIntArg = fmap (read . head) getArgs

main =  do
    n <- getIntArg
    print(fibC n 1 1)