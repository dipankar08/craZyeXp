#include "common.h"
#include<stdio.h>
#include<stdlib.h>

#define IS_WHITE_CHAR(x) ((x)==' '||(x)=='\t' || (x)=='\n')

/* This function convert a array to float */
float my_atoi(char *b,int start,int end)
{
    int state =1;
    int sign =0;
    float int_sum=0;
    float f_sum =0;
    float mult=1;
    char *a= b+start;
    puts(a);
    while(a!=b+end+1)
    {    
        //validation..
        printf("%c#",*a)  ;
        if (*a !='+' || *a !='-' || *a!='.' || !(*a>'0' && *a<'9')) 
          { a++;continue;}
        else if ( *a =='+')
        {
            sign = 1;a++;continue;
        }
        else if (*a =='-')
        { sign = -1;a++;continue;
        }
        else if(*a=='.')
        {
            state = 2, a++; continue; //Mode to float State
        }          
        if( state == 1)
        { int_sum = int_sum*10+ (*a-'0');a++;continue;        
        }
        if (state == 2)
        {   mult =mult/10;
            f_sum = f_sum + (*a-'0')/mult;a++;continue;
        }          
        
    }
    printf("%d",sign*(int_sum+f_sum));
    return sign*(int_sum+f_sum);    
}


int main(){
    int i;
    int *a;
    
    char _t[1000];
    gets(_t);
    
    puts(_t);

    printf("--->%f", my_atoi("12345",2,4));
    return 0;
    
}