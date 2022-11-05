#include<stdlib.h>


int fib_loop(int z){
    int i, x = 1, y = 1;

    if(z == 1 || z == 2)
        return 1;
    for(i=0;i < (z-2);i++){
        y += x;
        x = y-x;
    }
    return y;
}

int main (int argc, char *argv[]){
    int _ = fib_loop(atoi(argv[1]));
}