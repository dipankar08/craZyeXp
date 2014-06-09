/*
  Name: BackTracking Algorithms
  Copyright: Interview Bible
  Author: 
  Date: 07/03/14 22:58
  Description:  All linkedlist prgram in place
  
  Table of Contents:
      1. 
      2.
      3.
      
*/


#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include "lib.h"

/*******************************************************************************
* Problem :  Generate Binary of n-length.
* Input:
* Output:
* Algorithms:
*******************************************************************************/

void printAllBinOfLengthN(int i,int n, char *a)
{
    if (i ==n)
      {
          a[i]='\0';
          printf("%s\n",a);
          return;
      }
      a[i]='0';
      printAllBinOfLengthN(i+1,n,a);
      a[i]='1';
      printAllBinOfLengthN(i+1,n,a);
}

void printAllBinWrapper(int n)
{
    char *a =(char *) malloc(sizeof(char)*n);
    printAllBinOfLengthN(0,n,a);
    
}    

/*******************************************************************************
* Problem :  Generate All K -Radix number of length n
* Input:
* Output:
* Algorithms:
*******************************************************************************/
void genKradix(int i,int n, char *a,int k)
{
    if (i ==n)
      {
          a[i]='\0';
          printf("%s\n",a);
          return;
      }
      for(int j=0;j<k;j++)
      { 
          a[i]='0'+j;
          genKradix(i+1,n,a,k);
      }    
}

void genKradixWrapper(int n,int k)
{
    char *a =(char *) malloc(sizeof(char)*n+1);
    genKradix(0,n,a,k);
    
}  

/*******************************************************************************
* Problem 3 : Permutation of all String
* Input:
* Output:
* Algorithms:
*******************************************************************************/
//TBD


/*******************************************************************************
* Problem 4 :  Knight Move : A Knight is place is a board and can move as per Chase
Find that if it is possible to move all the direction from any starting position 
given.
* Input: Start with location (x,y) in chess board n x n.
* Output:
* Algorithms:
    i. Kight can move ({2,1),(-2,1)....}
*******************************************************************************/

bool isvalidMove(int i,int j,int n)
{
    return (i>=0 && j>=0 && i<n && j<n);
}    

void KnightMoveUtil(int x,int y,int n,int** space,int map[8][2],int count)
{
    printf("\n(%d,%d )=>%d",x,y,count);
    space[x][y]=1;//Block
    count =count +1;
    // See it cover all the Move or not
    if (count == n*n)
      printf("We Complete All move");
    //Try to move all 8 location
    for (int i=0;i<7;i++)
    {
        if( isvalidMove(x+map[i][0],y+map[i][1],n) && space[x+map[i][0]][y+map[i][1]]==0)
        {
            KnightMoveUtil(x+map[i][0],y+map[i][1],n,space,map,count);
        }    
    }
    //Release
    space[x][y]=0;
    count =count -1;    
}    

void isMovePossibleWrapper(int x, int y, int n)
{
    int **space;
    space = (int **)malloc(n * sizeof *space);
    for (int i=0; i<n; i++)
      {
        space[i] = (int *)malloc(n * sizeof *space[i]);
      }
    // initilize the board
    for (int i=0;i<n;i++)
       for (int j=0;j<n;j++)
           space[i][j]=0;
    int move[8][2]={ {2,1},{2,-1},{1,2},{1,-2},{-2,-1},{-2,1},{-1,-2},{-1,2}};
    // Call the function.
    KnightMoveUtil(x, y, n , space, move,0);
             
}    


/*******************************************************************************
* Problem 5: [ RAT MoVE ]
  Print all possible paths from top left to bottom right of a mXn matrix
             Where you can go from L2R and T2B
* Input:
* Output:
* Algorithms:
*******************************************************************************/

void printAllMoveUtil(int x, int y,int m,int n, int** maze,int* ans,int count)
{   
    if (x ==m-1 && y == n-1)
    {   ans[count++] =maze[x][y];
        for (int i=0;i<count;i++)
           printf("%d->",ans[i]);
           printf("\n");
        return;
    }
    int t = maze[x][y];
    ans[count] = maze[x][y];
    //block the maze          
    maze[x][y]= -1;
    
    if(x+1<n && y<m && maze[x+1][y] != -1)
    {
        
        printAllMoveUtil(x+1,y,m,n,maze,ans,count+1);
    }   
    if(x<n && y+1<m && maze[x][y+1] != -1)
    {
        
        printAllMoveUtil(x,y+1,m,n,maze,ans,count+1);
    }  
    //restore
    maze[x][y]= t;
     
}    

void printAllMoveUtilWrapper(int m,int n)
{
    int **maze;
    maze =(int **)malloc(m*sizeof(*maze));
    for(int i=0;i<m;i++)
    maze[i] =(int *) malloc(n*sizeof(*maze[i]));
    
    for (int i=0;i<m;i++)
      for(int j=0;j<n;j++)
         maze[i][j]=i*m+j;
    int *ans = (int *) malloc((m+n)*sizeof(int));
    printAllMoveUtil(0,0,m,n,maze,ans,0);
    
}    

/*******************************************************************************
* Problem 5A. :  Rat Move if there is a Zero from (0,0) to (n,n) in a boolen Matrix
* Input:
* Output:
* Algorithms:
*******************************************************************************/

bool checkUtil(int x, int y, int m , int n)
{
    return x>=0 && y >=0 && x<m && y<n;
}
void printAllRatMoveUtil(int x,int y, int space[4][4],int m,int n,int *ans, int count)
{
    if (x == m-1 && y == n-1)
    {
        ans[count++]= x*m +y;
        for (int i=0;i<count;i++) printf("%d->",ans[i]);
        printf("\n");
        return;
    }
    space[x][y] = 1;
    ans[count] = x*m +y;
    
    if( checkUtil(x,y+1,m,n) && space[x][y+1] == 0)
    {
        printAllRatMoveUtil(x,y+1,space, m,n,ans,count+1);
    }       
    if( checkUtil(x,y-1,m,n) && space[x][y-1] == 0)
    {
        printAllRatMoveUtil(x,y-1,space, m,n,ans,count+1);
    } 
    if( checkUtil(x+1,y,m,n) && space[x+1][y] == 0)
    {
        printAllRatMoveUtil(x+1,y,space, m,n,ans,count+1);
    } 
    if( checkUtil(x-1,y,m,n) && space[x-1][y] == 0)
    {
        printAllRatMoveUtil(x-1,y,space, m,n,ans,count+1);
    } 
    space[x][y] = 0;
}    

void printAllRatMoveWrapper(int space[4][4])
{
 int ans[16]={0};
  printAllRatMoveUtil(0,0,space,4,4,ans,0);
}    


/*******************************************************************************
* Problem 6 :  (N Queen Problem)
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem 7:  (Subset Sum)
* Input:
* Output:
* Algorithms:
*******************************************************************************/
void sumOfSubsetUtil(int *set,int n,int k,int *ans,int upto)
{   
    /* it reach the end point-- return --*/
    if ( n+1 == upto )
       return;
    /* Huryee ! We get all the sum */
    if ( k == 0)
    {
        for (int i=0;i<upto;i++)
        {
            if ( ans[i] == 1 ) { printf("%d + ",set[i]);}
        }
        printf("\n");  
        return;  
    }   
    /* We are picking up upto-th data */
    if( k - set[upto] >=0 )
    {
        ans[upto] = 1;
        sumOfSubsetUtil(set, n, k - set[upto], ans, upto+1);
        ans[upto] = 0;
    } 
    /* We are not pecking up */
    ans[upto] = 0;
    sumOfSubsetUtil(set, n, k , ans, upto+1);      
     
}

void sumOfSubsetWrapper(int *set,int n,int k)
{
    int ans[n];
    for (int i=0;i<n;i++) ans[i]=0;
    sumOfSubsetUtil(set,n,k,ans,0);
    
}    


/*******************************************************************************
* Problem 8 :  (m Coloring Problem)
* Input: N*N Verices and 1..m color
* Output:
* Algorithms:
    - Default Algo. try 1..m  for all N Vetices ->O(M^n);
    - Color Vrtices one by one with color 1..m without breaking the rule.
*******************************************************************************/





/*******************************************************************************
* Problem 9:  (Hamiltonian Cycle)
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 10:  [SODUKU SOLVER ]
* Input:
* Output:
* Algorithms:
*******************************************************************************/
void next_loc(int m[9][9],int x, int y, int *a,int *b)
{
	if ( x== 8  && y == 8 ) 
	{
		*a=10; return;
	}
	else if (y ==8 && x <8)
	{
		x++; y = 0;
	}
	else
	{
		y++;
	}
	for(int i =x;i<9;i++)
	 for (int j=y;j<9;j++)
	   if(!m[i][j])
	   {
	   	*a =i;*b=j;
	   	return;
	   }
	*a=10;
	return;
}


void sodukuSolver( int in[9][9],int x,int y)
{	
    /* No more Location */
	if(x==10) return;
	for (int k=1;k<10;k++)
	{
		printf("\nTrying <%d,%d> to %d ",x,y,k);
		in[x][y] = k;
		
		/* Test colition either row or column */
		for (int i=0;i<9;i++)
		{
		  if (in[i][y] == k && i != x)
		    goto NEXT;
		  if(in[x][i] == k && i != y)
		    goto NEXT;
	   }
	    /*test colition in Box */
	    for (int i= 3*(x/3);i<3*(x/3)+1 ;i++)
	      for (int j= 3*(y/3);j<3*(y/3)+1 ;j++)
	        if (in[i][j] == k && i != x && j !=y )
	          goto NEXT;
	    /* At thsi point All test succedd: Find Next point*/
	    int a,b;
	    next_loc(in,x,  y, &a, &b);
	    if (a ==10) return;
	    sodukuSolver(in,a,b);
NEXT:	    
    1+1;
	}
	/* no one solve this, Please back track */
	in[x][y] = 0;
	
}

void test_sodukuSolver()
{
	int in[9][9]={
	{1,2,3,7,9,0,0,0,0} ,
	{0,0,0,0,0,0,0,0,0} ,
	{0,0,0,0,0,0,0,0,0} ,
	{0,0,0,0,0,0,0,0,0} ,
	{0,0,0,0,0,0,0,0,0} ,
	{0,0,0,0,0,0,0,0,0} ,
	{0,0,0,0,0,0,0,0,0} ,
	{0,0,0,0,0,0,0,0,0} ,
	{0,0,0,0,0,0,0,0,0} ,
	};
	
	int a,b;
	next_loc(in,0,  -1, &a, &b);
	if (a == 10) return;
	sodukuSolver(in,a,b);
	PRINT_2D_ARRAY(in,9,9);
}









/*******************************************************************************
* Problem 11 :  Generate all (n+m) length String having n A and m B.
* Input:
* Output:
* Algorithms:
*******************************************************************************/
void genAllAnBUnit(int hasA,int hasB,int maxA,int maxB,char *ans, int count)
{
    if (count == maxA+maxB)
    {
        ans[count] = '\0';
        printf("%s\n",ans);
        return;
    }
    if ( hasA < maxA)
    {
        ans[count] = 'A';
        genAllAnBUnit(hasA+1,hasB,maxA,maxB,ans, count+1);
    }   
    if ( hasB < maxB)
    {
        ans[count] = 'B';
        genAllAnBUnit(hasA,hasB+1,maxA,maxB,ans, count+1);
    }   
}    
void genAllAnBwrapper(int maxA,int maxB)
{
    char ans[maxA + maxB +1];
    genAllAnBUnit(0,0,maxA,maxB,ans,0);
}
    



/*******************************************************************************
* Problem 12:  Genarte All balance Parenthesis
* Input:
* Output:
* Algorithms:
*******************************************************************************/
void genAllBalParenUtil(int hasopen,int hasclose,char *ans,int count,int n)
{   
    /* We already have 2*n Symbol */
    if (count == 2*n )
    {
        ans[count] = '\0';
        printf("%s\n",ans);
        return;
    }    
    /* Add a close break now..*/
    if(hasopen > hasclose)
    {
        ans[count] = ')';
        genAllBalParenUtil(hasopen, hasclose+1, ans, count+1, n);
    }
    /* We stilll can add a open breakts */
    if(hasopen < n )
    {
        ans[count] = '(';
        genAllBalParenUtil(hasopen+1, hasclose, ans, count+1, n);
    }       
}

void genAllBalParen(int n)
{
    char ans[2*n+1];
    genAllBalParenUtil(0, 0, ans, 0, n);
}    


/*******************************************************************************
* Problem 13:  FAct Using Tail recursion
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 14:  TAG oF WAR [DEvide a set into two equal part havng minimum sun diff
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem 15:  Cryptograpic puzzle.
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 16:  All Possible sting of length K with N charcter
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 17:  Print Conbunation of r element from N items.
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 18:  A number is a palindoem or not by recussion.
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/****************** Drive Program ********************************/

/***********************  Start of Driver Program at Here *********************/
#if UNIT_TEST
int main()
{
    test();
}    
#endif

/*
int main()
{
    printf("************ [ Problem of Backtrace ] ***********\n\n");
    //printAllBinWrapper(5);
    //genKradixWrapper(2,3);
    //isMovePossibleWrapper(0,0,8);
    //printAllMoveUtilWrapper(3,3);
    //genAllBalParen(3);
    //genAllAnBwrapper(2,2);
    //int a[] ={1,1,2,4,6,8};
    //sumOfSubsetWrapper(a,6,8);
    int maze[4][4] ={
        {0,0,0,0},
        {1,1,1,0},
        {1,1,1,0},
        {1,1,1,0}
        };
    printAllRatMoveWrapper(maze);    
    
    
    printf("****************** [ E N D ] *******************\n\n");
    getch();
}    
*/

