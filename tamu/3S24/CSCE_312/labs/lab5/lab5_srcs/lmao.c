#include <stdio.h>

int main() {
    int j,k;

    for (int i=4; i <=10; i++) {
        j = i*2;
        k = j-4;
    }

    printf("j = %d, k = %d\n", j, k);  // j = 20, k = 16

    return 0;
}