//CSCE 312: Lab-1 Problem-5 framework
// This is version-2; bugfix for timediff
/* ***   README   **** */
/*This file is a framework: i.e. there is no actual code whose execution time will be
  measured. You need to populate the appropriate functions with the code that you wrote
  for the previous problems in order to get useful data.

  Turning in this file without your code will result in zero points being awarded for this problem.

  run this file as: gcc FileName.c -o ExecutableName -lrt

*/




#include <stdio.h>
#include <time.h>

// Macro definitions to ensure portablity between both sun.cs and linux.cs

#if defined(sun)
#define CLOCKNAME CLOCK_HIGHRES

#else
#define CLOCKNAME CLOCK_PROCESS_CPUTIME_ID
#endif

unsigned int input = 0;
unsigned int output = 0;

void control_action(){
    //   7  6  5   4   3   2  1  0
    //  CM BP KIC DOS DLC DC ER DSBF

    //   2   1   0
    //   BA	DLA	BELL

    if (((input & 1<<1) == 1<<1) && (!(input & 1<<2) || !(input & 1))) output |= 1;
    if ((input & 1<<3) && (!(input & 1<<5) ||(input & 1<<4))) output |= 1<<1;
    if ((input & 1<<6) && (input & 1<<7)) output |= 1<<2;
}


void read_inputs_from_ip_if(){
	printf("input signal: ");
	scanf("%d", &input);
}

void write_output_to_op_if(){
    printf("BELL: %d, DLA: %d, BA: %d\n", output & 1, (output & 1<<1) >> 1, (output & 1<<2) >> 2);
}


/* ---     You should not have to modify anything below this line ---------*/

/*timespec diff from
http://www.guyrutenberg.com/2007/09/22/profiling-code-using-clock_gettime/
*/
struct timespec diff(struct timespec start, struct timespec end)
{
    struct timespec temp;
    //the if condition handles time stamp end being smaller than than
    //time stamp start which could lead to negative time.

    if ((end.tv_nsec-start.tv_nsec)<0) {
        temp.tv_sec = end.tv_sec-start.tv_sec-1;
        temp.tv_nsec = 1000000000+end.tv_nsec-start.tv_nsec;
    } else {
        temp.tv_sec = end.tv_sec-start.tv_sec;
        temp.tv_nsec = end.tv_nsec-start.tv_nsec;
    }
    return temp;
}

int main(int argc, char *argv[])
{
    unsigned int cpu_mhz;
    unsigned long long int begin_time, end_time;
    struct timespec timeDiff,timeres;
    struct timespec time1, time2, calibrationTime;

    clock_gettime(CLOCKNAME, &time1);
    clock_gettime(CLOCKNAME, &time2);
    calibrationTime = diff(time1,time2); //calibration for overhead of the function calls
    clock_getres(CLOCKNAME, &timeres);  // get the clock resolution data

    read_inputs_from_ip_if(); // get the sensor inputs

    clock_gettime(CLOCKNAME, &time1); // get current time
    control_action();                 // process the sensors
    clock_gettime(CLOCKNAME, &time2);   // get current time

    write_output_to_op_if();    // output the values of the actuators

    timeDiff = diff(time1,time2); // compute the time difference

    printf("Timer Resolution = %u nanoseconds \n ",timeres.tv_nsec);
    printf("Calibrartion time = %u seconds and %u nanoseconds \n ", calibrationTime.tv_sec, calibrationTime.tv_nsec);
    printf("The measured code took %u seconds and ", timeDiff.tv_sec - calibrationTime.tv_sec);
    printf(" %u nano seconds to run \n", timeDiff.tv_nsec - calibrationTime.tv_nsec);

    return 0;
}
