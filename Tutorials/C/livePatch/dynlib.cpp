#include <stdlib.h>
#include <iostream>
#include "dynlib.hpp"

using namespace std;


extern "C" void print()
{
    static unsigned int counter = 0;
    ++counter;

    cout << counter << ": PID " << getpid() << ": In print() " << endl;
}
