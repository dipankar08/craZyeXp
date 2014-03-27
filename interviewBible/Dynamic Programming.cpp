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
* Problem : Ugly Number
* Input:
* Output:
* Algorithms: U[i] =min{ 2*U[x],3*U[y],5*U[z] } whre x, y z are the correct pointer to 2,3,5, multiplier
*******************************************************************************/
#define MIN(x,y) ((x<y)? x : y)


int ugly(int n)
{
	int U[MAX]={0};
	int x,y,z;
	x=y=z=1; 
	U[1]=1; /* We will not use 0th Index. */
	
	for (int i=2;i<=n;i++)
	{
		U[i] = MIN(2*U[x],MIN(3*U[y],5*U[z]));
		
		if (U[i]== 2* U[x]) x++;
		if(U[i] == 3* U[y]) y++;
		if(U[i] == 5* U[z]) z++;
	}
	return U[n];

}

/*******************************************************************************
* Problem : Find the count of  N-digit Lucky Number, doesnt conayin 13
* Input:
* Output:
* Algorithms: f(i) = f(i-1)*10 - f(i-2)
*******************************************************************************/

int luckyCount(int n)
{
	long long f[MAX]={0};
	
	f[1] = 9; // Donest include ZERo
	f[2] = 100 -10 -1; // Doesnt include 0-9 and 13
	
	for (int i=3;i<=n;i++)
	{
		f[i] = f[i-1] * 10 - f[i-2];
	} 
	return f[n];
}

/*******************************************************************************
* Problem :  Count N-digt , K based Valid Number donesnt have TWO consicutive Zero
* Input:
* Output:
* Algorithms: 
Z(1) = 1; NZ(1) = k-1;
Z(2) = k-1 ; NZ(2) = k*(k-1)-1;
Z(i) = NZ(i-1)*1
NZ(i) = (k-1)* { Z[i-1] + NZ(i-1) }

*******************************************************************************/

int validNumber(int n, int k)
{
	long Z[MAX] = {0};
	long NZ[MAX] = {0};
	
	Z[1]=1;  NZ[1]= k-1;
	Z[2]= k-1; NZ[2]= (k-1)*(k-1);
	for (int i=3;i<=n;i++)
	{
		Z[i] = NZ[i-1];
		NZ[i]= (k-1)*(Z[i-1] + NZ[i-1]);
	}
    return Z[n]+NZ[n];

}

/*******************************************************************************
* Problem : 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem : 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

int main()
{
    printf("**************** Problem of Array **************\n\n");
    
    printf("\n fib(5): %d",fib(5));
    printf("\n fib(10): %d",fib(10));
    printf("\n fib(15): %d",fib(15));
    printf("\n fib(150): %d",fib(150));
    
    printf("\n\n ugly(5): %d",ugly(5));
    printf("\n ugly(10): %d",ugly(10));
    printf("\n ugly(15): %d",ugly(15));
    printf("\n ugly(150): %d",ugly(150));

    printf("\n\n luckyCount(3): %d",luckyCount(3));
    printf("\n luckyCount(10): %d",luckyCount(10));
    printf("\n luckyCount(15): %d",luckyCount(15));
    printf("\n luckyCount(150): %d",luckyCount(150));
    
    
    printf("\n\n validNumber(2,10): %d",validNumber(2,10));
    printf("\n validNumber(10): %d",validNumber(10,4));
    printf("\n validNumber(15): %d",validNumber(15,4));
    printf("\n validNumber(150): %d",validNumber(150,4));
    
    
    
    
    
    
    
    
    
    printf("\n\n****************** [ E N D ] *******************\n\n");
    getch();
}    

