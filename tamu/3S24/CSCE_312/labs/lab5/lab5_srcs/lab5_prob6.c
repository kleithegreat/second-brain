//File named "lab5_prob6.c"
#include <stdio.h>

int very_fast_function(int i) {
    int result;
    __asm__ (
        "movl %1, %%eax;"      // move i into %eax
        "imull $18, %%eax;"    // multiply %eax by 18 (i.e. i * 18)
        "subl $3, %%eax;"      // subtract 3 from %eax (i.e. i * 18 - 3)
        "cmpl $300, %%eax;"    // compare %eax with 300
        "jle .increment;" 	   // if %eax <= 300, jump to .increment
        "movl $0, %%eax;"      // else, set %eax to 0
        "jmp .done;"           // jump to .done
        ".increment:"          // label for the increment
        "incl %1;" 		       // increment i
        "movl %1, %%eax;" 	   // move i into %eax
        ".done:" 			   // label for the end
        "movl %%eax, %0;" 	   // move %eax into result
        : "=r" (result)        // output gets assigned to result variable declared above
        : "r" (i) 			   // input to out assembly code
        : "%eax"               // tell gcc that %eax is the clobered register
    );
    return result;
}

int main(int argc, char *argv[]) {
    int i;
    i = 16;
    printf("The function value of i is %d\n", very_fast_function(i));
    return 0;
}
