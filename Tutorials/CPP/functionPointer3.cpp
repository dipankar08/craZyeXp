//Using Polymorphism and Virtual Functions Instead of Function Pointers (C++)
#include<stdlib.h>
#include<stdio.h>
class Sorter
{
    public:
    virtual int compare (const void *first, const void *second);
};
class AscendSorter : public Sorter
{

    virtual int compare (const void*, const void*)
    {
        int first = *(int*)first_arg;
        int second = *(int*)second_arg;
        if ( first < second )
        {
            return -1;
        }
        else if ( first == second )
        {
            return 0;
        }
        else
        {
            return 1;
        }
    }
};
int main()
{
    int array[10];
    int i;
    Sorter *ss = new AscendSorter();
    /* fill array */
    for ( i = 0; i < 10; ++i )
    {
        array[ i ] = 10 - i;
    }
    qsort( array, 10 , sizeof( int ), ss );
    for ( i = 0; i < 10; ++i )
    {
        printf ( "%d\n" ,array[ i ] );
    }

}
