//File named "lab5_prob6.c"
#include <stdio.h>
int very_fast_function(int i){
	if ( (i*18 -3) <= 300) return i++;
	else return 0;
}

int main(int argc, char *argv[])
{
	int i;
	i=16;
printf("The function value of  i is %d\n", very_fast_function(i) );
	return 0;
}