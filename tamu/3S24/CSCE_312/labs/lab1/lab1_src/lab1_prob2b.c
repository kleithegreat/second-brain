#include <stdio.h>

int main() {
    struct employee1{ 
        int id; 
        char name[50];
    }; 

    struct employee2{ 
        int id; 
        char name[52]; 
    };

    printf("Size of struct employee1 (bits): %d\n", sizeof(struct employee1)*8);
    printf("Size of struct employee1 (bytes): %d\n", sizeof(struct employee1));
    printf("Size of struct employee2 (bits): %d\n", sizeof(struct employee2)*8);
    printf("Size of struct employee2 (bytes): %d\n", sizeof(struct employee2));

    printf("Size of int (bits): %d\n", sizeof(int)*8);
    printf("Size of char (bits): %d\n", sizeof(char)*8);
    printf("Size of char[50] (bits): %d\n", sizeof(char[50])*8);
    printf("Size of char[52] (bits): %d\n", sizeof(char[52])*8);
    
    return 0;
}
