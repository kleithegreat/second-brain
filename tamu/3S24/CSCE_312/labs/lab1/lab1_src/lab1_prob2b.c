int main() {
    struct employee1{ 
        int id; 
        char name[50];
    }; 

    struct employee2{ 
        int id; 
        char name[52]; 
    };

    printf("Size of employee1: %d\n", sizeof(struct employee1));
    printf("Size of employee2: %d\n", sizeof(struct employee2));
}