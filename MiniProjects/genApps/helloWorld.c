#include "common.h"
#include <stdlib.h>
int main()
{
    char *x = malloc(100); /* or, in C++, "char *x = new char[100] */
    memset(x,"Hello",1);
    puts(x);
    return 0;
}

