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
	//This read the current state of the available sensors

	printf("input signal: ");
	scanf("%d", &input);
}

void write_output_to_op_if(){

    //This display/print the state of the 3 actuators (DLA/BELL/BA)
    printf("output signal: %d\n", output);
}


//The code segment which implements the decision logic
void control_action(){

    /*
       The code given here sounds the bell when driver is on seat
       AND hasn't closed the doors. (Requirement-2)
       Replace this code segment with your own code to do problems 3 and 4.
    */

    //   7  6  5   4   3   2  1  0
    //  CM BP KIC DOS DLC DC ER DSBF

    //   2   1   0
    //   BA	DLA	BELL

    //    if (engine_running && !doors_closed) bell = 1;

    //    extract the relevant bits using the mask [00000110] and compare with condition [00000010]
    //    if we need to change the last bit to 1, we use bitwise OR
    //    if we need to change the last bit to 0, we use bitwise AND
    //    if (input & [00000110] == [00000010]) output = output | [001]

    if (input & 0x02 == 0x02 && (input & 0x04 == 0x00 || input & 0x01 == 0x00)) output = output | 0x01;
    if (input & 0x08 == 0x08 && (input & 0x20 == 0x00 || input & 0x10 == 0x10)) output = output | 0x02;
    if (input & 0x40 == 0x40 && input & 0x80 == 0x80) output = output | 0x04;
}

/* ---     You should not have to modify anything below this line ---------*/

int main(int argc, char *argv[])
{

    // code segment 1 starts here
    /*
        The main control loop which keeps the system alive and responsive for ever,
        until the system is powered off 
    */
    for (; ; )
    {
        input  = 0;
        output = 0;
        read_inputs_from_ip_if();
        control_action();
        write_output_to_op_if();
    }
    
    // code segment 1 ends here

    // code segment 2 starts here 
    /*
        - 8 test cases for Problem 4.
    */
    
    /*
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
    */

    // code segment 2 ends here

    return 0;
}
