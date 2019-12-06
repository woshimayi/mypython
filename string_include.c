#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char * string = {#include "string.txt"};
	printf("string = %s\n", string);
	return 0;
}


