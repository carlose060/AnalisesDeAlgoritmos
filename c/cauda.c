#include<stdlib.h>


int fib_cauda(int z, int a, int b){
    if(z <= 2)
        return b;
    return fib_cauda(z-1, b, a + b);
}

int main (int argc, char *argv[]){
    int _ = fib_cauda(atoi(argv[1]),1,1);
}