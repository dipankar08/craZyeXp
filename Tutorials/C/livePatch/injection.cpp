// injection.cpp

#include <stdlib.h>

extern "C" void print();

extern "C" void injection()
{
    print(); // do the original job, call the function print()
	system("date"); // do some additional job
}
