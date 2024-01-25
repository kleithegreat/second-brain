#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

int main() {
    FILE* my_file_pointer;
    if ( (my_file_pointer = fopen("lab1_prob2_out.txt", "w")) == NULL) {
        printf("Error opening the file, so exiting\n");
        exit(1);
    }

    fprintf(my_file_pointer, "int data type is %lu bytes or %lu bits long\n",sizeof(int), sizeof(int)*8);
    fprintf(my_file_pointer, "unsigned int data type is %lu bytes or %lu bits long\n",sizeof(unsigned int), sizeof(unsigned int)*8);
    fprintf(my_file_pointer, "double data type is %lu bytes or %lu bits long\n",sizeof(double), sizeof(double)*8);
    fprintf(my_file_pointer, "long data type is %lu bytes or %lu bits long\n",sizeof(long), sizeof(long)*8);
    fprintf(my_file_pointer, "long long data type is %lu bytes or %lu bits long\n",sizeof(long long), sizeof(long long)*8);
    fprintf(my_file_pointer, "char data type is %lu bytes or %lu bits long\n",sizeof(char), sizeof(char)*8);
    fprintf(my_file_pointer, "float data type is %lu bytes or %lu bits long\n",sizeof(float), sizeof(float)*8);
    fprintf(my_file_pointer, "struct timeval data type is %lu bytes or %lu bits long\n",sizeof(struct timeval), sizeof(struct timeval)*8);
    fprintf(my_file_pointer, "short data type is %lu bytes or %lu bits long\n",sizeof(short), sizeof(short)*8);
    fprintf(my_file_pointer, "FILE* data type is %lu bytes or %lu bits long\n",sizeof(FILE*), sizeof(FILE*)*8);

    return 0;
}
