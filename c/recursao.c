#include<stdlib.h>
#include<stdio.h>

int fib_recursivo(int z){
    if(z == 1 || z == 2)
        return 1;
    return fib_recursivo(z-1) + fib_recursivo(z-2);
}

int main (int argc, char *argv[]){
    int resul = fib_recursivo(atoi(argv[1]));
    printf("%d", resul);
}
