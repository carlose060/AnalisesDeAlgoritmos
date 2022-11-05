import System.Environment

fib :: Integer -> Integer
fib 2 = 1
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

getIntArg :: IO  Integer
getIntArg = fmap (read . head) getArgs

main =  do
    n <- getIntArg
    print(fib n)

