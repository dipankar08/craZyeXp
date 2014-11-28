#include <stdio.h>
void my_int_func(int x)
{
    printf( "%d\n", x );
}


int main()
{   
   /* defie a function pointer: foo is a pointer to a function takes an integer and retrun void  */
    void (*foo)(int);
    /* assigning a function pointer */
    foo = &my_int_func;

    /* call my_int_func (note that you do not need to write (*foo)(2) ) */
    foo( 2 );
    /* but if you want to, you may */
    (*foo)( 2 );

    return 0;
}

// g++ functionPointer.cpp -std=c++11 && ./a.out 
