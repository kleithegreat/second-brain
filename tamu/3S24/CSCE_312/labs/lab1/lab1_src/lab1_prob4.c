// CSCE312: Lab-1 Problem-4 framework

/* ***   README   **** */

/*
   This example program sounds the bell when driver is on seat
   AND haven't closed the doors. Use the general framework and the function
   shells, replace the code inside  the control_action() function with your
   own code to do problem 4.

Note: This code is designed to run in an infinite loop to mimic a real control system.
If you prefer to read the inputs from a file, modify the code appropriately to terminate the
loop when all the inputs have been processed.

Turning in this file without your code will result in zero points being awarded for this problem.

run this file as : gcc -std=c99 filename.c -o executableName

*/


#include <stdio.h> //This is useful to do i/o to test the code

unsigned int input = 0;
unsigned int output = 0;

void read_inputs_from_ip_if(){
	printf("input signal: ");
	scanf("%d", &input);
}

void write_output_to_op_if(){
    printf("BELL: %d, DLA: %d, BA: %d\n", output & 1, (output & 1<<1) >> 1, (output & 1<<2) >> 2);
}

void control_action(){
    //   7  6  5   4   3   2  1  0
    //  CM BP KIC DOS DLC DC ER DSBF

    //   2   1   0
    //   BA	DLA	BELL

    if (((input & 1<<1) == 1<<1) && (!(input & 1<<2) || !(input & 1))) output |= 1;
    if ((input & 1<<3) && (!(input & 1<<5) ||(input & 1<<4))) output |= 1<<1;
    if ((input & 1<<6) && (input & 1<<7)) output |= 1<<2;
}

/* ---     You should not have to modify anything below this line ---------*/

int main(int argc, char *argv[])
{

    // code segment 1 starts here
    /*
        The main control loop which keeps the system alive and responsive for ever,
        until the system is powered off 
    */
   /*
    for (; ; )
    {
        input  = 0;
        output = 0;
        read_inputs_from_ip_if();
        control_action();
        write_output_to_op_if();
    } */
    
    // code segment 1 ends here

    // code segment 2 starts here 
    /*
        - 8 test cases for Problem 4.
    */
    
    
    int inputs[] = {0, 163, 245, 42, 126, 171, 255, 98};
    for (int i = 0; i < 8; i++) {
        int bell = 0;
        int dla  = 0;
        int ba   = 0;
        input    = inputs[i];
        output   = 0;

        control_action();

        if (output & 1)
            bell = 1;
        if (output & 2)
	        dla = 1;
        if (output & 4)
            ba = 1;

        printf("Case %d:  %d %d %d \n", i, bell, dla, ba);
    }
    

    // code segment 2 ends here

    return 0;
}
