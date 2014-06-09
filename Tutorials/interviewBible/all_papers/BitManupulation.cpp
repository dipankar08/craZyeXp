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

#define PRINT_BOOL(x) printf("%s",((x)?"True":"False"));


/*******************************************************************************
* Problem :  General function Here
* Input:
* Output:
* Algorithms: Show Bit and byte
*******************************************************************************/

#define AND(A,B) A & B
#define OR(A,B) A | B
#define XOR(A,B) A^B
#define LSHIFT(A,K) A>>K
#define RSHIFT(A,K) A<<K
#define NEG(A) ~A


#define CHECK_KTH_BIT(A,K) ((A>>K)&1 )
#define SET_KTH_BIT(A,K) (A | (1 << K))
#define UNSET_KTH_BIT(A,K) (A & (~(1<<K)))
#define TOGGLE_KTH_BIT(A,K) (A ^ (1<<K))

#define UNSET_RIGHT_MOST_BIT(A) A & (A-1)
#define ISOLATE_RIGHT_MOST_BIT(A) (A & -A)
#define ISOLATE_RIGHT_MOST_ZERO_BIT(A) (~A) & (A+1)

#define CHECK_POWER_OF_TWO(A) (A && !(A & A-1))
#define FIND_MULT_TWO_POWER_K(A,K) (A<<K)
#define FIND_DIV_BY_TWO_POWER_K(A,K) (A>>K)
#define FIND_MOD_BY_TWo_POWER_K(A,K) (A & (K-1))

#define CREATE_MASK_K_RIGHTMOST_ONES(K) ((1 << K) - 1)
#define CREATE_MASK_K_LEFTMOST_ONES(K) ~((1 << (32-K))-1)
#define CREATE_MASK_K1_K2_INBETEEN_ONES(K1,K2)   ((1 << K1) - 1) & (~((1<<K2)-1))                      /* 00001111100000 k1>k2  */


/*******************************************************************************
* Problem :  Show Memory
* Input:
* Output:
* Algorithms: Show Bit and byte
*******************************************************************************/
void show_bit(int x)
{   
	printf("\n");
	for (int i =0; i<sizeof(int)*8; i++)
	{
		if(i%8==0){
			printf(" ");
		}
		printf("%d", x>> (31-i) &1 );
		
	}
	printf("\n");
}



void show_mem(char *x, int len )
{
  for (int i=0;i<len;i++)
  {
  	printf("\n%u : 0x%.2x",x, *x);
  	x++;
  }
  printf("\n\n");
}



/*******************************************************************************
* Problem : 
* Input:
* Output:
* Algorithms: Check the Sign Bit i.e 31th bit's
*******************************************************************************/
bool getSign(int x )
{
	return  x >> (sizeof(int)*8-1) & 1;  // 1 for negetive and 0 for +ve
}

/*******************************************************************************
* Problem : 
* Input:
* Output:
* Algorithms: Find mask as 0 for +ve and -1 for -ve.
-1 indicate all 1 bit
thie x^0-0 is x
and x^(-1) -(-1) ==Compl(x)+1 = 2's compliment = -x.
*******************************************************************************/
int getAbs(int x)
{
	int mask = - (x >> (sizeof(int)*8 - 1) & 1) ; // 0 for +ve and -1 for -ve
	return x^mask + mask;
}


/*******************************************************************************
* Problem :  test little endiumn
* Input:
* Output:
* Algorithms: 
*******************************************************************************/

void testEndian()
{
	unsigned int i = 1;
	char *c =(char *)&i;
	if(*c)
	  printf("Little");
	else
		printf("BigEndiun");
}

/*******************************************************************************
* Problem :  Reverse Bit
* Input:
* Output:
* Algorithms: 
*******************************************************************************/

int reverse(int n)
{
	int j=0;
	for(int i=0;i<sizeof(int)*8;i++)
	{
		j = j << 1;
		j = j | (n & 1);
		n= n >> 1;
	}
	return j;
}


/*******************************************************************************
* Problem :  Rotate Bit
* Input:
* Output:
* Algorithms: 
*******************************************************************************/

int rotate(int x, int k)
{
  //return (x>>k)|(x<<(32-k)); <<< Will nt work for negetive number
  return ((x >> k))| (x << (32 - k));	
}


/*******************************************************************************
* Problem :   Find out parity of 64-bit long Interger(Odd count =>True or Even count of set bits )?
* Input:
* Output:
* Algorithms:
Interger Width of length n and having K 1's/
Sol1 : iteratvly test each bit =>O(n)
Sol 2: Count and erage each lowest set bit =>O(k)
Sol 3: Lookup table, Create a lookup table which constains parity of any 8-bit integer.
and use that table to calculate 64 bit data =>O(1), Here Lookup tbale size is BIG.
Sol4: Impove Lookup table.
Contscat 4-bit lookup table. 

 
*******************************************************************************/
short parity1(long x)
{
	bool res =0;
	while(x)
	{
		res =res ^ (x &1) ;  // Set each bit
		x >>=1;
	}
	return res;
}
short parity2(long x)
{
	bool res =0;
	while(x)
	{
		res =res ^ 1 ; // Alwas alter 
		x = x &(x-1); //unset lowest set bit
	}
	return res;
}



void test_parity()
{
	PRINT_BOOL(parity2(11));
}

/*******************************************************************************
* Problem :  Find x/y with only add, sub, bit ops.
* Input:
* Output:
* Algorithms: 
Solution : x/y = 0 if y>x;
x/y = 1+ (x-y)/y else

Sol 2: Improve the recusrion Step as find lartst k such that 2^k*y <=x 
then x/y = 2^k +(x-2^k*y)/(y)

Calculating k will take O(n^2) Complexity.

Sol 3: Finding k can be reduce to O(logn ) if if you use binary serach 
*******************************************************************************/
int div(int x,int y)
{
	if(y>x)
	  return 0;
	else
	  return 1 + div(x-y,y);
}
void test_div()
{
	printf ("%d",div(11,8));
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


/*******************************************************************************
* Problem : 
* Input:
* Output:
* Algorithms: 
*******************************************************************************/




int main()
{
    printf("**************** Problem of Array **************\n\n");
    test();
    
#if 0    
    
    printf("\n show_bit(10):"); show_bit(10);
    printf("\n show_bit(21):"); show_bit(21);
    printf("\n show_bit(-10):"); show_bit(-10); /* See two complement is used */
    
    printf("\n show_mem(10):"); int i =10; show_mem((char*)&i,sizeof(int));
    printf("\n show_mem(-10):"); i=-10;show_mem((char*)&i,sizeof(int));
    printf("\n show_mem(10.55):");float j =10.5; show_mem((char *)&j, sizeof(float)); /* See two complement is used */
    
    
    /* All macro Test */
    
    
    printf("\n 10:");show_bit(10);
    printf("\n 20:");show_bit(20);
    
    printf("\nAND:");show_bit(AND(10,20));
    printf("\nOR:");show_bit(OR(10,20));
    printf("\nXOR:");show_bit(XOR(10,20));
    printf("\nLSHIFT:");show_bit(LSHIFT(10,2));
    printf("\nRSHIFT:");show_bit(RSHIFT(10,2));
    printf("\nNEG:");show_bit(NEG(10));
    
    printf("\nCheck 3rd bit: %d",CHECK_KTH_BIT(10,3));
    printf("\nSet 2nd bit:");show_bit(SET_KTH_BIT(10,2));
    printf("\nUnSet 3nd bit:");show_bit(UNSET_KTH_BIT(10,3));
    printf("\nToggle 0nd bit:");show_bit(TOGGLE_KTH_BIT(10,0));
    
    
    printf("\n UNSET_RIGHT_MOST_BIT:");show_bit(UNSET_RIGHT_MOST_BIT(10));
    printf("\n ISOLATE_RIGHT_MOST_BIT:");show_bit(ISOLATE_RIGHT_MOST_BIT(10));
    printf("\n ISOLATE_RIGHT_MOST_ZERO_BIT:");show_bit(ISOLATE_RIGHT_MOST_ZERO_BIT(10));
    
    printf("\n CHECK_POWER_OF_TWO: %d\n",CHECK_POWER_OF_TWO(512));
    printf("\n FIND_MULT_TWO_POWER_K:%d\n",FIND_MULT_TWO_POWER_K(10,4));
    printf("\n FIND_DIV_BY_TWO_POWER_K:%d\n",FIND_DIV_BY_TWO_POWER_K(500,4));
    printf("\n FIND_MOD_BY_TWo_POWER_K:%d\n",FIND_MOD_BY_TWo_POWER_K(500,4));
    
    
    printf("\n CREATE_MASK_K_RIGHTMOST_ONES:");show_bit(CREATE_MASK_K_RIGHTMOST_ONES(8));
    printf("\n CREATE_MASK_K_LEFTMOST_ONES:");show_bit(CREATE_MASK_K_LEFTMOST_ONES(8));
    printf("\n CREATE_MASK_K1_K2_INBETEEN_ONES:");show_bit(CREATE_MASK_K1_K2_INBETEEN_ONES(16,8));
    
    
    printf("\n reverse(110);");show_bit(110);show_bit(reverse(110));
    
    
    printf("\n testEndian():");testEndian();
    
    printf("\n GetSign(10): %d",getSign(10));
    printf("\n GetSign(-10): %d",getSign(-10));
    
    printf("\n getAbs(10): %d",getAbs(10));
    printf("\n getAbs(-10): %d",getAbs(-10));
    
    printf("\n rotate(-511,4):");show_bit(-511);show_bit(rotate(-511,4));
    
    
    

    
    
    printf("\n\n****************** [ E N D ] *******************\n\n");
    getch();
#endif
}    
