/*
  Name: Dynamic Prgramming Program
  Copyright: Interview Bible
  Author: 
  Date: 07/03/14 22:58
  Description:  All linkedlist prgram in place
  
  Table of Contents:
      1. Convert Arry to list
      2.
      3.
      
*/


#include<stdio.h>
#include<conio.h>

#define MAX 9999

/*******************************************************************************
* Problem : Fibonacci Series
* Input:
* Output:
* Algorithms: f(i) = f(i-1) + f(i-2)
*******************************************************************************/
int fib(int n)
{
	int cache[MAX] = {0};
	cache[0]=0;
	cache[1] =1;
	for (int i =2;i<=n;i++)
	  cache[i]= cache[i-1]+cache[i-2];
	return cache[n];	
}


/*******************************************************************************
* Problem : 
* Input:
* Output:
* Algorithms:
*******************************************************************************/






int main()
{
    printf("**************** Problem of Array **************\n\n");
    
    printf("\n fib(10): %d",fib(5);
    printf("\n fib(10): %d",fib(10));
    printf("\n fib(10): %d",fib(15));
    printf("\n fib(10): %d",fib(150));
    
    
    printf("****************** [ E N D ] *******************\n\n");
    getch();
}    

