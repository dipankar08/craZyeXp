/*
  Name: Array Program
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
#include "lib.h"

void test(){
}

/*******************************************************************************
* Problem :  How to genarte number in range [a,b] when a binay ramdom number genarator is given ?
* Input:
* Output:
* Algorithms:
1. RandomNo(a,b) = a+ RnadomNo(0,b-a)
2. Find random number (0,t-1) as t <= 2^i
3. Fillup i number of 1 or 0 randomly genarated.
*******************************************************************************/


/*******************************************************************************
* Problem : tere are 500 door in a ofc and initialy closed ,There are 500 persion, 
First person go and open all doors.
second persion close all alternative doors
Thirst persion open evney 3rd alterntave doors
so on.
At processing of 500, tell what is the status of 500 door ?
* Input:
* Output:
* Algorithms:
Indpendent of N , the door k is open iff k is perfact square.
as the  number dividor of perfact square is always odd
*******************************************************************************/




/*******************************************************************************
* Problem:  Find GCD of two number without mult,dev.rem.?
* Input:
* Output:
* Algorithms:
Sol 1: Simple but unefficient.
gcd(x,y) = y if x ==0
gcd(x,y) =  gcd(max(x,y) -min(x,y),min(x,y))

Compelxity O(max(x,y)).

Sol 2:  Some efiicinet techn is dr, which solve O(log x +log y) i.e. Sum of bits in x and y.

*******************************************************************************/


/*******************************************************************************
* Problem: Find the smallest number whose digits multiply to a given number n 
* Input / Output:
Input:  n = 36
Output: p = 49 
// Note that 4*9 = 36 and 49 is the smallest such number
* Algorithms:
Case 1: n < 10 When n is smaller than n, the output is always n+10. 
For example for n = 7, output is 17. For n = 9, output is 19.

Case 2: n >= 10 Find all factors of n which are between 2 and 9 (both inclusive).
The idea is to start searching from 9 so that the number of digits in result are minimized.
For example 9 is preferred over 3*3 and 8 is preferred over 2*4.
Store all found factors in an array. 
The array would contain digits in non-increasing order, so finally print the array in reverse order.
*******************************************************************************/


/*******************************************************************************
* Problem: Write a function that generates one of 3 numbers according to given probabilities 
* Input / Output:
You are given a function rand(a, b) which generates equiprobable random numbers between [a, b] inclusive.
Generate 3 numbers x, y, z with probability P(x), P(y), P(z) such that P(x) + P(y) + P(z) = 1 using the given rand(a,b) function.

The idea is to utilize the equiprobable feature of the rand(a,b) provided.
Let the given probabilities be in percentage form, for example P(x)=40%, P(y)=25%, P(z)=35%..

Following are the detailed steps.
1) Generate a random number (r) between 1 and 100. Since they are equiprobable, the probability of each number appearing is 1/100.
2) Following are some important points to note about generated random number r.
a) r is smaller than or equal to P(x) with probability P(x)/100.
b) r is greater than P(x) and smaller than or equal P(x) + P(y) with P(y)/100.
c) r is greater than P(x) + P(y) and smaller than or equal 100 (or P(x) + P(y) + P(z)) with probability P(z)/100
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

#if UNIT_TEST
int main()
{
    test();
}    
#endif

