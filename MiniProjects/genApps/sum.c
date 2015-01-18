#include "common.h"


#include<stdio.h>
int main(){

    int sum =0;
    for(int i=0;i<10;i++)
    {
        if (i%2 ==0 ) sum+=i;
    }
    printf("Even Sum: %d",sum);

    return 0;
}
