#!/bin/bash

# DIR PATHs
PyCauda=./tempos/python/Cauda
PyRecursivo=./tempos/python/Recursivo
PyFor=./tempos/python/For

cCauda=./tempos/c/Cauda
cRecursivo=./tempos/c/Recursivo
cFor=./tempos/c/For

haskellCauda=./tempos/haskell/Cauda
haskellRecursivo=./tempos/haskell/Recursivo

# Criando as pastas de times
{ mkdir -p $PyCauda ; }
{ mkdir -p $PyRecursivo  ; }
{ mkdir -p $PyFor ; }

{ mkdir -p $cCauda ; }
{ mkdir -p $cFor ; }
{ mkdir -p $cRecursivo ; }

{ mkdir -p $haskellCauda ; }
{ mkdir -p $haskellRecursivo ; }

# Compilando os arquivos .c
{ gcc ./c/cauda.c -o ./c/cauda ; }
{ gcc ./c/for.c -o ./c/loop ; }
{ gcc ./c/recursao.c -o ./c/recursao ; }


# Compilando os arquivo .hs
{ ghc -o ./haskell/hscauda ./haskell/cauda.hs ; }
{ ghc -o ./haskell/hsrecursao ./haskell/cauda.hs}


for i in {10..990..10}
do
 { time python3 ./python/cauda.py $i ; } 2> $PyCauda/$i.txt
 { time python3 ./python/for.py $i ; } 2> $PyFor/$i.txt

 { time ./c/cauda $i ; } 2> $cCauda/$i.txt
 { time ./c/loop $i ; } 2> $cFor/$i.txt

 { time ./haskell/hscauda $i ; } 2> $haskellCauda/$i.txt
done


for i in {10..50..10}
do
 { time python3 ./python/recursao.py $i ; } 2> $PyRecursivo/$i.txt
 { time ./c/recursao $i ; } 2> $cRecursivo/$i.txt

 { time ./haskell/hsrecursao $i ; } 2> $haskellRecursivo/$i.txt
done



