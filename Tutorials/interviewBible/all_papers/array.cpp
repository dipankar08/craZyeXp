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

#define PRINT(A,B) for(int z=0; z<B; z++) printf("%d,",A[z]);printf("\n");
#include <algorithm>
#include "lib.h"
#define Int(a)( a-'0')

/*******************************************************************************
* Problem : buble Sort
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/* Check the Adjucent and place the big value at a[n-1], a[n-2]...*/
void bubbleSort(int a[],int n)
{
	int swap =1;
	/* Optimizsed by swap: if any swap is tehre please do the next pass
	* In Every pass it will fix a[n-1] , a[n-2] and so on...*/
	for (int i=0;i<n && swap;i++)  
	{   swap =0;
		for (int j=0;j<n-i-1;j++) 
		{
			if (a[j]>a[j+1])
			{
				//swap a[j] and a[j+1]
				int temp = a[j]; a[j] = a[j+1]; a[j+1] = temp;
				swap = 1;
			}
		}
	}
}

/*******************************************************************************
* Problem : Selection Sort
* Input:
* Output:
* Algorithms:
1. Find the mimimu value in the list
2. Wap with current one.
3. repect the process of next..
*******************************************************************************/

void selectionSort(int a[], int n)
{
	for (int i=0;i<n;i++)
	{
		int min = i;
		for (int j=i+1; j<n;j++)
		{
			if (a[j] < a[min])
			{
				min =j;
			}
		}
		//We get the min here..now swap with i <--> min
		int temp =a[min]; a[min] =a[i];a[i]=temp;
		
	}
}

/*******************************************************************************
* Problem : Insertion Sort
* Input:
* Output:
* Algorithms:
1. See the input as a string.
2. a[0] is sorted and we get a[1] from stream
3. Get the poper location to insert it, 
*******************************************************************************/

void insertionSort(int a[],int n)
{
	//a[0] is sorted. start from 1
	for (int i=1;i<n;i++)
	{
	   int j = i;
	   int v = a[i] ; //We need this backup as in below for loop  it would be replaced.
	   while((j-1) >=0 && a[j-1] > v )
	   {
	   	a[j] =a[j-1]; //Shifting right
	   	j--;
	   }
	   //In thsi point we get the place j where to insert the new value.
	   a[j] = v;
	}
}

/*******************************************************************************
* Problem : Merge Sort
* Input:
* Output:
* Algorithms:
*******************************************************************************/
void merge(int a[],int temp[], int left, int mid, int right)
{
	int left_end =mid;
	int left_start =left;
	int right_start =mid+1;
	int right_end = right;
	
	int temp_start = left;
	
	while(left_start<=left_end && right_start <= right_end)
	{
		if(a[left_start] <= a[right_start])
		{
			temp[temp_start++]=a[left_start++];
		}
		else
		{
			temp[temp_start++] = a[right_start++];
		}
	}
	/* If Left Side still have some item*/
	while(left_start<=left_end)
	{
		temp[temp_start++]=a[left_start++];
	}
	/*if right half still have some item*/
	while(right_start<=right_end)
	{
		temp[temp_start++]=a[right_start++];
	}
	
	//Copy Back from temp to a
	for (int i = left; i<=right; i++)
	{
		a[i]=temp[i];
	}
	
}

void mergeSort(int a[],int temp[],int left,int right)
{
	int mid;
	if (left<right)
	{
		mid = left+(right-left)/2;
		mergeSort(a,temp,left,mid);
		mergeSort(a,temp,mid+1,right); // Mid+1 is the strt of second arry..
		merge(a,temp,left,mid,right);
		
	}
}

/*******************************************************************************
* Problem :  Merge two Array
* Input:
* Output:
* Algorithms:
*******************************************************************************/
/* A has enough Space to add element of B */
void InPlaceMerge(int a[],int b[], int a_len,int b_len)
{
	int a_start =0;
	int a_end = a_len -1;
	int b_start =0;
	int b_end =b_len-1;
	
	int new_end = a_len + b_len -1;
	
	while(a_end >=0 && b_end >=0 && new_end >=0)
	{
		if (a[a_end] >= b[b_end])
		{
			a[new_end--] = a[a_end--];	
		}
		else
		{
			a[new_end--] = b[b_end--];
		}
			
	}
	while(a_end >=0 && new_end>=0)
	{
		a[new_end--]= a[a_end--];	
	}
	
	while(b_end >=0 && new_end >=0)
	{
		a[new_end--]= b[b_end--];	
	}
	
	
}

void test_InplaceMerge()
{
  int x[10]={10,20,30,40,50,0,0,0,0,0};
  int y[5] ={1,2,15,25,100};
  InPlaceMerge(x,y,5,5);
  PRINT(x,10);
}
/*******************************************************************************
* Problem : Quick Sort
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem :  Couting Sort
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem : Radix Sort
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem : Linear Serach
* Input:
* Output:
* Algorithms:
*******************************************************************************/
int linearSerach(int a[],int n,int x)
{
	for (int i=0;i<n;i++)
	{
		if(a[i] ==x)
		{
			printf(" %d is found in location %d\n",x,i);
			return i;
		}
		
	}
	printf(" %d is not found",x);
	return -1;
}

/*******************************************************************************
* Problem :  Binary Serach
* Input:
* Output:
* Algorithms:
*******************************************************************************/
int binSearch(int a[],int left,int right,int x)
{
	if (left >right)
	{
		printf("not found\n");
		return -1;
	}
	int mid =left + (right -left)/2;// Avoid Ovrflow here
	if (a[mid]== x)
	{
		printf("Found %d in location %d",x,mid);
		return mid;
	}
	else if (a[mid]>x)
	{
		return binSearch(a,left,mid-1,x);	
	}
	else if (a[mid] < x)
	{
		return binSearch(a,mid+1,right,x);	
	}
	
}


/*******************************************************************************
* Problem 1 : Given Two arry Permutation or not
* Input:
* Output:
* Algorithms: 
SOL1: Sort n Match
SOl2 : BitMap and Hash
SOl3: S=S' and M = m'
*******************************************************************************/

/*******************************************************************************
* Problem 2: Sort array having 0/1/2 
* Input:
* Output:
* Algorithms:
Sol1: 3 pointer Partiton Technique.
Sol2 : ounting Sort
*******************************************************************************/


/*******************************************************************************
* Problem 4: Find Min/Max Element. NIL
* Input:
* Output:
* Algorithms:
Sol1 : Traverse The array and make make comparisn  O(2*(n-1))
Sol2 : Traverse the Arry with else part either max or min O(n-2)
sol3 : Traverse the Array by jump of two O(3n-2)
Sol4 : Devide and Conqure Approach (O(lonn)
*******************************************************************************/

/*******************************************************************************
* Problem 5: Merge Two Arry Inplecae
* Input:
* Output:
* Algorithms:
Sol 1: Merge from Back side with Comarisn.
*******************************************************************************/

/*******************************************************************************
* Problem 6: A[i] = Multiplication of Other Element. 
* Input:
* Output:
* Algorithms:
Sol 1: A[i] Replace by Cumalative Multi from Left and Agin A[i] *= Cumalative multiplication from Right
*******************************************************************************/

/*******************************************************************************
* Problem 7: K-th Max elemnt of an Arry. 
* Input:
* Output:
* Algorithms:
Sol1: Sort and return O(nlogn )
Sol2 : Use Partition of Quick Sort O(nlog n)
*******************************************************************************/

/*******************************************************************************
* Problem 8 : get All Unique elemnts of an Arry 
* Input:
* Output:
* Algorithms:
Sol1 : Use Hash Map/ Bit map to cont.
Sol2 : Sort the Arry and Check for neighbours.
sol3 : Make BST having a counter field.
*******************************************************************************/

/*******************************************************************************
* Problem 9: Two Set are Dis-joint or Not ! 
* Input:
* Output:
* Algorithms:
Sol1 :
A) Sort the larger array O(mlogm)
B) Make a Binary serch for all elemnet in second arry . O(n*logm) ==> (n+m)logm
*******************************************************************************/

/*******************************************************************************
* Problem 10 : Find an Elemnet having A[i]= i 
* Input:
* Output:
* Algorithms:
Sol1 : 
A) Apply One Way Binary sercah 
if (A[mid] > mid ) Serach on Left
if (A[mid] <mid) Search on Right
*******************************************************************************/

/*******************************************************************************
* Problem 11/12: Maximim Sum SubArray  
* Input:
* Output:
* Algorithms:

Sol1: 
1. Linear Scan by keeping Max_sum_so_far Techniqie.
2. Using D&C Algoritthms O(nlogn)
a) Find Mid 
b)maxSum=Max ( Sum(leftside) or Sum(rightSide) or Sum in Cross )
*******************************************************************************/

/*******************************************************************************
* Problem 13 : Sort a Marix 
* Input:
* Output:
* Algorithms: N/A
*******************************************************************************/

/*******************************************************************************
* Problem 14: Search a Sorted Matrix[n][n]
* Input:
* Output:
* Algorithms:
Sol1 : Search ecah row using binary serach - O(n *long)
Sol 2: Use diagonally Step-wise serach Technique.
a) Start form upper right corner <i,j> =<0,n-1>
b) if ( mat[i][j] == K) return 
b) if (mat[i][j] >K i++ or J++;
*******************************************************************************/

/*******************************************************************************
* Problem 15: Sort An Zig Zag Like Arrar like [ 10,20,30,40,30,20,10,15,25,15,10] 
* Input:
* Output:
* Algorithms:
Sol 1: 
a) Find the local maxima,
b) find the local mimal
c) Reverse [loca_min: lcal_max]
d) Apply Inplce merge sort.( That can use swaping)
*******************************************************************************/

/*******************************************************************************
* Problem 16/167: An Arrry is Rotated and Find the Rotate Point. 
* Input:
* Output:
* Algorithms:
Sol1 : Use Binary Serach  : Check Mid with it's Adjacent
a) if (Mid <high && A[mid] > A[mid+1]) return mid+1
b) if( mid >low  && a[mid]<A[mid -1] return mid
c) Make One Side recustion call
*******************************************************************************/

/*******************************************************************************
* Problem 18 / 161: Find K-th Samllest element in two Sorted Arry. 
* Input:
* Output:
* Algorithms: N/A
Sol1 : Merge Both and Find K-th Samllest O(m+n)
Sol2 : Use Two pointer technique to simulate merge but actully not merge , O(k), Itarate uptotimes
Sol 3: Tricky Approcah O(lg n+ lg m)
a) Find Middle Element Ai and Bj => if Bj<=Ai<Bj+1 then Ai is (i+j+1)th smallest element
b) Our Target to find out i and j such that i+j = k-1, then Ai will be (i+j+1)= (k)th Smallest ement.
c) Recustion Call
*******************************************************************************/

/*******************************************************************************
* Problem 19: We have 2*n+1 elemnt having one distinct and others are in pair . find distinct 
* Input:
* Output:
* Algorithms:
1. Sort and Check neighber O(nlogn +n)
2. Use XOR operation O(n)
*******************************************************************************/

/*******************************************************************************
* Problem 20: We have 2*n+2 Element having two distinct elemt.  
* Input:
* Output:
* Algorithms:
Sol 1: Sorting Appoch,
sol 2: XOR Approach.
a) find res = XOR of all Ement = A XOR B
b) Find a Mask to having max Bit set to identfy A or B
c) res2 = Xor again with all elemnt which satisfy mask => Will return one elemnet
d Other Elemt is res ^ res2
*******************************************************************************/

/*******************************************************************************
* Problem 20A: Given an Arry of length n-1 one item is missing find that.
* Input:
* Output:
* Algorithms:
Sol 1: Sum Aproach (n*(n-1)/ -Sum
sol 2: XOR Approach.

*******************************************************************************/

/*******************************************************************************
* problem 21 : Repeted.
* Problem 22:  Rearrage <a0b1c2 -> abc012>
* Input:
* Output:
* Algorithms: N/A
Sol1:  The Represtation is Nothing But Raw-major to conlum major represtion
a) Make a 2D A[n][2] and read in colum major order.
b) Dont Actlly map the arry - but simulated the formula

Sol2 : Devide conquire and SWAP.
EX: A1B2C3D4 
=> A1B2 + C3D4 (Swap 1,b and 3,d)
=> AB12 + CD34 ( Now SWAP 12-CD)
=> ABCD1234
*******************************************************************************/

/*******************************************************************************
* Problem 23/164: Print Spiralorder of a Matrix. 
* Input:
* Output:
* Algorithms:
Sol1 : Using Iterative Version
While(1)
{ print TOP_ROW; print_RIGHT_COl ; print BTM_ROW;print LEFT_COL;
  adjust i--,j--,z--,y--; 
  if (i>j) || Ix>y) break;
}

Sol2: use Recustive Vesrion.
*******************************************************************************/

/*******************************************************************************
* Problem 24: Count path from <0,0> to <n,n> 
* Input:
* Output:
* Algorithms: Dynamic Progrmmaing
*******************************************************************************/

/*******************************************************************************
* Problem 25 : Remove Duplicates in a Sorted Arry. 
* Input:
* Output:
* Algorithms:
Sol 1: Scan from left to right and Keeptrace, fill_up_to_this Pointers
if A[fill_up_to_this]!= A[i] => A[++fill_up_to_this]= A[i++]; else i++;
*******************************************************************************/

/*******************************************************************************
* Problem 26: Set a Row to ZERO if any elemt is ZERO 
* Input:
* Output:
* Algorithms:
Sol1 : 
a) Make ROW_IS_ZERO[1:n]=1 and COL_IS_ZERO[1:n] =1;
b) Travser the Arry and put 0 in above arry if row/col contains ZERO.
c) SCAN the array and populate raw as zero if ROW_IS_ZERO
*******************************************************************************/

/*******************************************************************************
* Problem 27: Find ALl pairs having sum X 
* Input:
* Output:
* Algorithms:
sol1 : TWO LLOP method.O(n2)
sol2 : Use Hash/BIT MAP 
a) hash all elemnt O(n)
b) for all elemnt serach X-A[i] into hash. O(n)
Sol3 :
*******************************************************************************/

/*******************************************************************************
* Problem 28/29 : Maxisum sum SubMatrix 
* Input:
* Output:
* Algorithms: N/A
*******************************************************************************/

/*******************************************************************************
* Problem 30: Maximum repetaive Elements 
* Input:
* Output:
* Algorithms:
Sol1: TWO LOOP O(n2)
sol2 : Use hash and find maximum hash colision., keep trace counter,and max_colision_so_far variable O(N)
sol3 Trick techniwq in O(N) and O(1) Space: 
Assumtion : Element are belongs to 0-->K-1 and K<n.
a) Rise the value a[i] = a[i] + a[ a[i] %k ] +: each occurace rise k
b) Find Max vlaue of A[i] and return i
c) Reset Array by A[i] =A[i] %K
*******************************************************************************/

/*******************************************************************************
* Problem 31: Search in a Rotated Array 
* Input:
* Output:
* Algorithms: N/A
*******************************************************************************/

/*******************************************************************************
* Problem 32: We have Big 2 D array a[10^9][10^9] . Store and serach efficiently. 
* Input:
* Output:
* Algorithms: N/A using hashing.
*******************************************************************************/

/*******************************************************************************
* Problem 33: Rotate an Arry by 90 degree 
* Input:
* Output:
* Algorithms: <i,j> = (j,N-i+1)
*******************************************************************************/

/*******************************************************************************
* Problem 34: Traspose an Matrix Recustivly. 
* Input:
* Output:
* Algorithms: Recustion
a) Swap First raw with First Col.
b) Tsans post Arry start with <1,1>
*******************************************************************************/

/*******************************************************************************
<35/36 are repeted>
* Problem 37: Maxmin length substring equal 0 and 1
* Input:
* Output:
* Algorithms: N/A
sol1 : Two loop Approach o(n2)
sol 2: tricky.
a) Replace all Zero by -1
b) Find cumalative sum form left to right and keep trace Max_so_far_length and store with C[i]
c) find Max value of i such that C[i] is Zero => (0..i) is the Ans
d) if C[j] -C[i] = 0 then <i..j> is ans. get the max (c and d)
*******************************************************************************/

/*******************************************************************************
* Problem 38: Find Two number having less differnec. 
* Input:
* Output:
* Algorithms: N/A
Sol1 : Two loops.
Sol2 : Sort and find the diff or consicutive elemnts.
Sol3: Efficient and tricky
*******************************************************************************/

/*******************************************************************************
* Problem 39 : A pair waise sum given find indivisual elemnst. 
* Input:
* Output:
* Algorithms: n/A
*******************************************************************************/

/*******************************************************************************
* Problem 40 : Given An Arry, where A[i] = count of less number in Right Hand Side. Fins Actual Arry 
* Input:
* Output:
* Algorithms: N/A
*******************************************************************************/

/*******************************************************************************
* Problem  41:  Given Sorted Mat[n][n] bollena matrix. Find raw having mazimum zero.
* Input:
* Output:
* Algorithms:
Sol1 : Count in each row - O(n2)
Sol2 : Effient and tricky.
a) Start with top right corner
b) if a[i][i] ==0 i ++; else j ++
*******************************************************************************/

/*******************************************************************************
* prob 42 -repeted.
* prob 43 -repeted.
* Problem 44: Flip the Array over diaginal
* Input:
* Output:
* Algorithms:
for i = 0..n
for j = 0 to n-i-1 :
  A[i][j] = A[n-1-i][n-1-j
*******************************************************************************/

/*******************************************************************************
* Problem 45: Find The Arry haing Maximum Products SubArray. 
* Input:
* Output:
* Algorithms:
sol1: Two Array.
Sol 2: Tricky and Effecinet

a) if Even number of Negative , return all multiplications.
b) if odd number of -ve, the split of over each -ve and calculate products.
b) Max_product can't lies between two -ve elemts.

*******************************************************************************/

/*******************************************************************************
* Problem 46 : Find All Sbset having sum =S ( 2^n subset) 
* Input:
* Output:
* Algorithms: N/A
Sol 1: generate all 2^n subset and check if sum =S
sol 2:  Devide and Conquire
a) Deive
Step 3: Dynamic Programming count All subset.
A[1..n]
Count(i,S)= Count(i-1,S) + Count(i-1,S-A[i])

*******************************************************************************/

/*******************************************************************************
* Problem 47: In an Arry 1..N one number if mssing find it ? 
* Input:
* Output:
* Algorithms:
Missig Number n*(n-1)/2 -SUM
*******************************************************************************/

/*******************************************************************************
* Problem 48 :  In an arry 1..N One is missuing and Another is Duplocate find Both ?
* Input:
* Output:
* Algorithms:
Say Missing number is X and Dupliacte is Y
SUM[i] = n*(n-1)/2 -X +Y ------------ eqn(1)
ProDuct = n! /X *Y  ------------------eqn(2)
Solve these above two equations.
*******************************************************************************/

/*******************************************************************************
* Problem 49 : Improve Bubble Sort 
* Input:
* Output:
* Algorithms:
1. Keep trak a swap flag to get best case o(n)
2. Do Paralel bubble sort to get Worst case O(n2/2)
*******************************************************************************/

/*******************************************************************************
* Problem 50 : how to Sort item when the item are in Strems data 
* Input:
* Output:
* Algorithms: Insertion Sort /Heap Sort.
*******************************************************************************/

/*******************************************************************************
* Problem 51: Imporove Quick Soert 
* Input:
* Output:
* Algorithms: Randamize Quick Sort
*******************************************************************************/

/*******************************************************************************
* Problem  52 :  Sort 900 MB data suing 100MB RAM
* Input:
* Output:
* Algorithms:
a) Devide 900Mb into 9 chanks 100 MB, put info buffer, and Sort it and  put into disk .
b) Load 10MB from each chank (Sort it), hence total 90MB for input
c) Remanining 10Mb memory for oupyt buffer.
d) Do 9 way merge and when it is merge put back to buffer,
*******************************************************************************/

/*******************************************************************************
* Problem 53: Find  Dupliactes in an Array  
* Input:
* Output:
* Algorithms:
Sol 1: Two loop Technique. O(n^2)
Sol 2: Sort the array and check Adj o(nlogn +n)
Sol 3: Use Bit map and chek collision.
Sol 4: Tricky And Efficient o(n)
a) Scan from left to right 
b) for each a[i] make a[a[i] as Negative.
c) Scan Again and if a[i] is negeative say i is duplicates. 
 
*******************************************************************************/

/*******************************************************************************
* Problem 54: FInd an element Repeat Maximum 
* Input:
* Output:
* Algorithms: 
Sol1: make counter fro each elemnt and store it and return element having max count O(n) with O(K) Space
sol2: Two loop O(n2)
sol3: Sort it and check for adjacent elemnt O(nlogn +n)
Sol4 : Use BST having a counters O(nlogn)
Sol5. Use Hash Table and count Hash collision. O(n)
sol 6. -Ve technique will Not work.
*******************************************************************************/

/*******************************************************************************
* Problem 55: Sort 1 to N^2  / 1 to N3..
* Input:
* Output:
* Algorithms:
Sol1 : A[]={1 to n^2}
a) Substact 1 from each {0 to N^2 -1}
b) Any elemnt in this range have 2 digit of base N. Example N= 5 then:
 {0,..24} 21 Can be represted as (4*5^1 + 1*5^0) =(41) base 5
c) thus all digit are of length 2 of base N, Use Radix sort to Sort
d) for N^3 case, all digit are 3 length of base N
*******************************************************************************/

/*******************************************************************************
* Problem 56: Given two arry A and B find a and b such that a+b = K
* Input:
* Output:
* Algorithms:
Sol1 : 
a) Sort A and for each element in B do a binary serach for K-b[i] => O(mlogm)+n*logm
Sol2: put all ement of A in hash and fro each element in B do a lookup for k-b[i]
*******************************************************************************/

/*******************************************************************************
* Problem 57 :Duplicates
* problem 58: A[1..n] haveelemnt inplace . Sort it. 
* Input:
* Output:
* Algorithms:
Sol 1: Do insertion sort, there will be no swap forelements.
Sol 2: Useway merge sort.
Sol 3: Use Heap sort. Put fisrtelemnt in Heap and then sort it. Then delete elemnt and continue..
*******************************************************************************/

/*******************************************************************************
* Problem 59/67 : How to mergeshorted List. 
* Input:
* Output:
* Algorithmss: 
- We have Total Element = N and N/K each.
sol 1: Merge in lenear fasion .
(N/K+N/K) +N/K) + N/K )....
sol2 : Use turnament Merge
( (A+B) +( C+D))  + ( (E+E )+ (G+H) ))

Sol 3: Use Heap.
a) Create amin heap of size k.
b) Extarct each elemnt from each list and put it dr.
c) Delete min and put int outout buffer
*******************************************************************************/

/*******************************************************************************
* Problem 60 : n Nut and N-bold problem
* Input:
* Output:
* Algorithms: Devide and conqure.
*******************************************************************************/

/*******************************************************************************
* Problem 61 : Sort 1 billon image pixel. 
* Input:
* Output:
* Algorithms:  Pixel value in {0..254} use counting sort
*******************************************************************************/

/*******************************************************************************
* Problem 62: Sort 1 bilion telephone number 
* Input:
* Output:
* Algorithms: 10-Digit telephoen number so use radix sort
*******************************************************************************/

/*******************************************************************************
* Problem 63/66:  A file contains bilion of number , find max 10.
* Input:
* Output:
* Algorithms:
Sol 1: 
a) Devide Hole list with 1000 No. Make Max heap of each
b) take top 10 from each and make heap to all
c) Take top 10 from Amx heap

Sol 2:
a) Deivide the number like 1000,990,990,990...
b) Make heap first chank, take top 10 and push it to next chank. and so on.

Sol 3:
1. Have a min -heap of length 10. insert 10 number .
2. Delete top (min andinsert next number and so on..
3. At last the heap contains a max 10 numbr.
4

*******************************************************************************/

/*******************************************************************************
* Problem 64 : Duplicates
* Porblem 65: Find First Element which duplicates. 
* Input:
* Output:
* Algorithms:
Sol 1:  Two llop techniw O(n2)
sol 2: Sortning Technic will not work
Sol 3: Hash: hash each elemnt and Note< count, first ocuurence>, After hash serach on hash table.
*******************************************************************************/
int getLowerBound(int a[],int key,int l,int r)
{         
  int mid;
  if (l<=r)
  {      
    mid = l + (r-l)/2;
    if(a[mid] == key && ( mid == l || a[mid] > a[mid-1]))
      return mid;
    if (a[mid] != key && ( mid == l))
      return -1;
    
    if (a[mid] >= key)
       return getLowerBound(a,key,l,mid-1);
    if (a[mid] <= key)
       return getLowerBound(a,key,mid+1,r);
  } 
    
}   

void test_getLowerBound()
{
  int arr[]={1,1,1,1,3,4,5,5,5,5,5,6,6,6,6};
  PRINT_ARRY_WITH_INDEX(arr,15);

  int key = 3;
  printf ("First loc of arr of %d is %d\n",key,getLowerBound(arr,key,0,14));
}

/*******************************************************************************
* Problem : 66/67 Duplocates
*problem 68:. Given Two arry A[] and B[], find Nlargest pair (a,b)
* Input:
* Output:
* Algorithms: N/A
Sol 1:
a) Hapify both arry A and B => O(m+n)
b) Keep Deleting the largest pair  O(logn +logm) *N

Sol 2: Find all pair and make max n pair.
Sol 3: Sort both Arry and Take max n-pair Just like mereg technque.

*******************************************************************************/

/*******************************************************************************
* Problem 69 : Find Medium for a Strema of Integer. 
* Input:
* Output:
* Algorithms: 
Sol 1:  Use Max nd Min heap-- See Tree
*******************************************************************************/

/*******************************************************************************
* Problem 70 : Printelemnt followed by medium in Sorted order. 
* Input:
* Output:
* Algorithms:
Sol 1:
a) Find medium , say m.
b)Find k-th largest elemnt in Set A[m:hight} => use Quick sort pertition.=> say postion k
c) Sort A[m:k]
d) Print
*******************************************************************************/

/*******************************************************************************
*problem 71 invalid.
* Problem 3/72 : Find 2 elemnt Sum to X. a+b = X 
* Input:
* Output:
* Algorithms:
Sol 1: Use loop O(n2)
Sol 2: use hash table. Put all elemnt in hash and serach hash by X-A[i] in H
Sol1 : Sort Array and use beg and End pointer Approcah O(nlog n)+O(n)
*******************************************************************************/

/*******************************************************************************
* Problem 73: Given an Arry A [] find x+y+z=0; 
* Input:
* Output:
* Algorithms:
Sol1 : # nested Loop.
Sol2: use hash . stote all pair sum.
This menas x+y = -z.
This for each elemt A[i] in A call prevrios function for x+y =-A[i]  O(n)*O(n)
*******************************************************************************/

/*******************************************************************************
* Problem 74  : Given an Arry A[] find x+y+z+w = X 
* Input:
* Output:
* Algorithms:
Sol1 : use 4 Nested foor loop => O(n4)
Sol2 : use 2 nested for loop and Run Algorith [==>  <==] ==> O(n2 *n)
for (int i=0;i<n;i++)
{
  for (int j=i;j<n;j++)
    //algo here A[p]+A[q] = X-A[i]-A[j]
}
Sol 3: Tricky and Efficient
a) Create an Aux Arry for pair sum. => O(n2)
b) Sort the AUX arry =>(n2logn2)
c) Fid two elemnt in AUX sunch that sum =X O(N2)
Complexity : O(n2 log(n2))

*******************************************************************************/

/*******************************************************************************
* Problem 75 : Given an Arry having x, y,z such that x^2+y^2 = Z^2. 
* Input:
* Output:
* Algorithms:
Sol1 : 
a) COnvert the Arrry A[i] = A[i]^2.
b) Apply Algo from X+Y =Z
*******************************************************************************/

/*******************************************************************************
* Problem 76: Given An Arry find sum of two elemnt closed to ZERO. 
* Input:
* Output:
* Algorithms:
Sol 1: Two llop method.
Sol2 :  Tricky but efficient
a) Sort the arry.
b) if All elemnt are +ve, take minmum two elemnt
c)if all ele are -ve , take sum of max two elemnts.
d) Take two piinter i and j in middile but -ve and +ve side.
and Expand both ends untile gwe get the ->0
-5 -4 -3 -2 0 6 9 19
 <========  ========>
 
*******************************************************************************/

/*******************************************************************************
* Problem 77 : Given An Arry find x+y+z =M 
* Input:
* Output:
* Algorithms:
Sol 1: 3 loop =>o3)
sol 2: One loop and run X+Y=S Algo O(n2)
sol3 : Trciky but efficients
a) Hash M -A[i] in H()
b) Apply X+Y=S algo checking if sum is in hash.

*******************************************************************************/

/*******************************************************************************
* Problem 78 : Array of unknown length, but Increaing and then decrsijng fashine. Implemnt serach algo. 
* Input:
* Output:
* Algorithms: N/A
*******************************************************************************/

/*******************************************************************************
* Problem  79:  We have an Annty [111111111111111..0000000000...] Find where 0 Starts? 
* Input:
* Output:
* Algorithms:
Sol1: Use 2^n technique. and when found apply binary serach
*******************************************************************************/

/*******************************************************************************
80,81 Dupliactes
* Problem 82 : Find fiest and last occurance of Dupliactes=> 1[2222]456789
* Input:
* Output:
* Algorithms:
Algo 1:
=> Use modified binary serach 
First: if(mid==low && a[mid ==data) or (a[mid]==data && a[mid-1] < data) return MID.

last occuraces =
if (mid==high && a[mid ]== data ) or (a[mid]==data and a[mid+1] >data) return mid

*******************************************************************************/

/*******************************************************************************
* Problem 83- > 94 : Find Second Smallest number 
*******************************************************************************/

/*******************************************************************************
* Problem 84: Find Majority Elemnt ( Which Occume more than N/2 Times.) 
* Input: 
* Output:
* Algorithms:
Sol 1: Two llops.
Sol 2: BST with counters
Sol 3: Sorting and Find Mah
Sol 4: Fine the midium (if it occue more than n/2 , midium is an candicate.
a) Find Mididum of an Arry O(n)
b) Test the Medium if it ocuure more than n/2 time. O(n)
Sol5 : Efficient and Tricky: Voting techniqu.
a)  candiacte = a[0]
b) for (int i=1 to n)
{  if (a[i] == canicate, count ++ ;else count --
   if count ==0 {candidate =a[i]; coint =1 }
}
*******************************************************************************/

/*******************************************************************************
* Problem 85: Given 2n Elements: n elements are same and otehr are all diff. Find maj 
* Input:
* Output:
* Algorithms:
Sol1: As n are same, the Maximum distance of similar elemnt is two, in worst case.
Thus folowing two pass in that arry;
a) Check two adjacent elemnet if same then it's the Majority. for relative distnace 0
b) check A[i] wth A[i+1] for all i for relative distance 1
Sol 2:
a) Sort the Arary
In that cast it n-chank might be at beg or at end or in middle. So possiblity test is:
a[0] ==a[1] or a[m]==a[m+1] or a[n-1]==a[n-1]

*******************************************************************************/

/*******************************************************************************
* Problem 86/87/88: Duplicate
* Prolem 89: Separte Evne and odd number
* Input:
* Output:
* Algorithms:
Sol 1: Parition using Quick Sort
x=1, y =n
while(x<y)
{ while a[x] is odd x++
  while a[y[ is evne y--
  swap(a[x] anda[y]) x++,y--
}s

*******************************************************************************/

/*******************************************************************************
* Problem 90 :  Find the max diff between any two elemnt in an unsorted Array
* Input:
* Output:
* Algorithms:
Sol1 : find max and Min elemnt and FInd the diff.O(n)
Sol2   Sort it and Find A[n]-A[1]
sol3 : use D&C Rule
a) Get Mid
b) Find Max diff in Left side, Right side and in Cross. N/A
*******************************************************************************/

/*******************************************************************************
* Problem 91: Given an Arry A[1..n] Find all pair (a,b) such that a*b =K 
* Input:
* Output:
* Algorithms:
Sol 1: two loop Approach
sol1: 
a) Hash all the elemnt
b) Do a serach for K/A[i]

*******************************************************************************/

/*******************************************************************************
* Problem 92 :  Find K-th largest Elemt and also with subsequent query
* Input:
* Output:
* Algorithms:
1. Hre Sort is menaing ful as Sort thake O(nlogn)
if tehre are n query then the Complexity with n call is O(logn)
*******************************************************************************/

/*******************************************************************************
* Problem 93 : Largest and Smallest / Duplicates
* Problem 94:  Second Largest
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 83/94 : Find Second Smallest number 
* Input:
* Output:
* Algorithms:
Sol1: 
a) Find Fisrt Minnimum ,O(n)
b) Do a second scan by removing First Elemt. O(n)
Sol2: use PQ.
a) make a Min heap O(n)
b) Delete Root and Heradp O(logn)
c) return TOP
Sol3. Use Turnament method.
*******************************************************************************/

/*******************************************************************************
* Problem  95: Find Kth smallest Elemnt. 
* Input:
* Output:
* Algorithms:
Sol1 : Do K-scan Techniue. , Find smallest, second smallest and so on.. O(n*k)
Sol2: Sort and return Kth Elemnt O(nlogn)+O(1)
Sol 3: Make BST and return k-th elemnt in order traversal.
Sol 4: 
a) Make min Heap tree of K-node O(k)
b) Delete and Insert (n-k) Nodes. O(n-k)logK
c) return Top O(1)
Sol5. Partition techique using Quick Sort
*******************************************************************************/

/*******************************************************************************
* Problem 96:  Find the Medium of two Sorted Arry A[1.n] and B[1.B] 
* Input:
* Output:
* Algorithms:
Sol1 : Merge the list and return M[m+n /2] => O(n+m) +O(1)

Sol 2: Use Binary serach Method. O(logn) + O(logm)
a) Find MediumA and MeiumB
b) if ma ==mb return (ma+mb)/2
c) if ma < mb return FindMidium(ma,n ,0,mb)
d) if ma > mb return FidnMin(0,ma,mb,m)

*******************************************************************************/

/*******************************************************************************
* Problem 97: Find K-th smallest in two sorted list
* Input:
* Output:
* Algorithms: Duplicates.
*******************************************************************************/

/*******************************************************************************
* Problem 98: Find all K-th sorted array. 
* Input:
* Output:
* Algorithms:
Sol 1: Sort and a[1:k] => O(nlogn) +O(k)
Sol 2: 
a) Make a Heap of sizeO(k)
a) Delete and insert O(n-k)*logK
c) return all elemnt in Heap O(k)
sol 3: 
a) Find -kth elemt using partiton => O(n)
b) All left of pivot is less.
c) Sortelemnt in left O(klogk)
d) Print allelemnt O(k)

*******************************************************************************/

/*******************************************************************************
* Problem 99/100: Find K- nearest elemnt from medium .
* Input:
* Output:
* Algorithms:
Sol 1:
b) Sort the arry and find the midium => O(nlogn) +O(1)
c) find k-th nearest algorithms by folowing O(k)
i,j =mid
while(count < K)
{
  if (a[i] >a[j] {print a[j], j++;count ++;
  if(a[i] <a[j]) {i++; ,...}
}
*******************************************************************************/

/*******************************************************************************
* Problem 101 :  Find all semmteric pair from a set of tuple. 
* Input:
* Output:
* Algorithms:
Sol1 :  
a) Scan the tuple and hash in opposite direction h[b] =a;
b) while checkin in hash also check (a.b) and(b,a). 
Sol 2: 
a) Make a mtrix from the elemnt 
b) Now cehck if Aij == Aji


*******************************************************************************/

/*******************************************************************************
* Problem 102 :duplicate/ Given M set of interger list , having n integer each, find repeatve elemtest.
* Input:
* Output:
* Algorithms:
Sol 1: Solution Multiple dimemnation hash.
*******************************************************************************/

/*******************************************************************************
* Problem 103:  Given an file having all distinct line except two line are same. Find the same line.
* Input:
* Output:
* Algorithms:
sol1 : Hash the line and Check for colision -colision line are duplictes.
sol 2: XOR It 3 Times. We will getXOR of all distict the elemnts. -- WILL NOT Work.
*******************************************************************************/

/*******************************************************************************
* Problem 104 : How to avoid Overflow in Mid calculation 
* Input:
* Output:
* Algorithms:
m = l+(h-l)/2
*******************************************************************************/

/*******************************************************************************
* Problem 105 : Find the Squire root effiecly. 
* Input:
* Output:
* Algorithms:
Sol1 : Biuild an arry A[i] = i^2
Sol 3: Given a X , find the loction by doing Binary serach o(nlogn) and return i
O(log2^16)
*******************************************************************************/

/*******************************************************************************
* Problem 106: Search for fist ocuurance of an elemnt in a sorted arry which is larger tahn
* Input:
* Output:
* Algorithms: N/A
Sol1: 
a) Lookup forusing binary serach - say r
b) return a[r+1]
*******************************************************************************/

/*******************************************************************************
* Problem 107 /108/109./110 --122 :  From AFI will not be coded/
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 123: Given K, find k-th largest number in a sorted Matrix 
* Input:
* Output:
* Algorithms:
a) Start from bottom right corner and it;s the largest.
b) Move Up and left size but comparism upto K.
*******************************************************************************/

/*******************************************************************************
* Problem 124: Revrse an Arry in O(N) 
* Input:
* Output:
* Algorithms:
sol1 : Iteratibe
Sol 2: Recussive
*******************************************************************************/

/*******************************************************************************
problem 125: roatted search
* Problem 126 : Rotate an Arry bytimes.
* Input:
* Output:
* Algorithms:
Sol1 : Swap last-first elemt/shift  with n time. O(n*k)
void leftRotate(int arr[], int d, int n)
{
  int i;
  for (i = 0; i < d; i++)
    leftRotatebyOne(arr, n);
}
Sol 2: Juggling Algorithhms Move by gcd(n,k)
*Function to left rotate arr[] of siz n by d
void leftRotate(int arr[], int d, int n)
{
  int i, j, k, temp;
  for (i = 0; i < gcd(d, n); i++)
  {
    // move i-th values of blocks 
    temp = arr[i];
    j = i;
    while(1)
    {
      k = j + d;
      if (k >= n)
        k = k - n;
      if (k == i)
        break;
      arr[j] = arr[k];
      j = k;
    }
    arr[j] = temp;
  }
}
 
sol 3: Reversal Algothims 
void leftRotate(int arr[], int d, int n)
{
  rvereseArray(arr, 0, d-1);
  rvereseArray(arr, d, n-1);
  rvereseArray(arr, 0, n-1);
}

Sol 4: Block Swap Algo
Initialize A = arr[0..d-1] and B = arr[d..n-1]
1) Do following until size of A is equal to size of B

  a)  If A is shorter, divide B into Bl and Br such that Br is of same 
       length as A. Swap A and Br to change ABlBr into BrBlA. Now A
       is at its final place, so recur on pieces of B.  

   b)  If A is longer, divide A into Al and Ar such that Al is of same 
       length as B Swap Al and B to change AlArB into BArAl. Now B
       is at its final place, so recur on pieces of A.

2)  Finally when A and B are of equal size, block swap them.
*******************************************************************************/

/*******************************************************************************
* Problem 127: Leader of an Arry : A[i] > A[j] for all j > i
* Input:
* Output:
* Algorithms:
sol1 : two _loop in O(n^2)
Sol 2: Scan from right and keep track the max value. O(n)
*******************************************************************************/

/*******************************************************************************
* Problem 129 : Union and Intersecion of Two Arry 
* Input:
* Output:
* Algorithms:
Sol1: use hashing
sol2 : Sort them and Keep track on Merge procedure
*******************************************************************************/

/*******************************************************************************
* Problem 130 : Floot and cilleing of X in A[] 
                floor[x] => A[i] just less than X
                cill[x] => A[i[ just greater than X
* Input:
* Output:
* Algorithms: N/A
Sol 1: Learing sercah O(n)
Sol 2: Sort and do a binary search

*******************************************************************************/

/*******************************************************************************
* Problem 131 :Find the minimu of unsorted arry, sorting of which, whole arry got sorted. 
* Input: 10,12,20,30,40,32,31,35,50,60
                    <=============>
* Output:
* Algorithms: N/A
Sol 1. 
a) From left to right, keep trace max_num_so_far, and stop if toggle occure -> T1
b) from right to left , keep tracjk min_sum_so_far, and 

*******************************************************************************/ 

/*******************************************************************************
* Problem 132: Find Equibilium index of an arry , It is a point i such that Left hand sum = Right hand sum 
* Input:
* Output:
* Algorithms: 
Sol1 : two Loop Techniq. Devide into two part, find sum and chek if they are equal or not
SOl2: Tricky but efficient
a) Find sum S -O(n)
b) Find cumalitive sum from left until it is S/2
*******************************************************************************/

/*******************************************************************************
* Problem 133: Which Sort required minimum sswap ?
* Input:
* Output:
* Algorithms:
a) Bubble -> (n-1) +(n-2) +.. 1
b) Insertion : n Swap but require shift.
c) Selection : N swap but N^2 Comparism
*******************************************************************************/

/*******************************************************************************
* Problem 134: Check if the ement of an Arry are consicutive or not 
* Input: 1,4,3,2,5 -> YES>
* Output:
* Algorithms:
Sol 1: Sort and check fro consicutive -O(nlon)+O(n)
sol 2: Use Bit Map and Check Bit map all 1 are in consicutive position.
Sol 3: Tricky but efficient
a) Find Min and Max of that Arry O(n)
b) Find Max-min +1 =n && The function has no duplicates,

*******************************************************************************/

/*******************************************************************************
* Problem 135:  Find samllest missing number in the arry, which is sorted.
* Input: 0,1,2,6,9 --> Ans : 3
* Output:
* Algorithms:
1) Do a leniear serach .O(n) and Checfor consicutive-ness
2) Do a Binary serach.
a) if A[mid] > mid , then serach Left or search right
*******************************************************************************/

/*******************************************************************************
* Problem 136: Find max j-i such that A[j] >A[i] 
* Input:
* Output:
* Algorithms:
Sol1 : Use two loop approach and See max difference between big and small ement -O(n2)
Sol 2: Tricky but efficient.
a) N/A
*******************************************************************************/

/*******************************************************************************
* Problem 137: 
* problem 138: Find/count Distinct sub-sequence in S for T 
* Input: S = abcabcabc  T = abc
* Output:
* Algorithms:
This is a Dynamic programming Problem
f(i,j)= count of sub sequence of T[0:i] in S[0:j]
f(i,j = f(i-1,j) <<<<<<<<<, Serach T[0:i-1] in S[1,j]
+ f(i-1,j-1) <<<<<<<<<< Serach T[0,i-1] in S[O,j-1] if T[i] == S[j]
*******************************************************************************/

/*******************************************************************************
* Problem 139: Checa String if interleaved of other rwo string.
* Input: S1 = abc and S2 = def ; T= abdefc is a interleaved
* Output:
* Algorithms: 
f(k,i,j) is true if T[0:k] is interleaved of S[0:i] and S[0:j]
f(k,i,j) = f(k-1,i-1 ) <<<<<<<<<<<< if T[k] = S1[i]
          OR f(k-1,j,j-1) <<<<<<<<<<, if T[k] = S2[j]
          
*******************************************************************************/

/*******************************************************************************
* Problem 140 : Get All IP Address. 
* Input: 10 10 10 10 -> 10.10.10.10 or 101.0.10.10 or ...
* Output:
* Algorithms:
get_all_ip(A[],int start,int end, int remain)
{ if remain ==1
     if int(a[start:end]) <256 , print Solutions; else rerturn
   else
   For All possible a[strt], a[strt:s+1] a[start:start+2] and if they less than 255,
       call get_all_ip(stat +i,remain -1)
}
*******************************************************************************/

void getAllIP(char *a, int rem, int *sol)
{
   //base case
   if (rem ==4)
  {
    if (*a=='\0')
      printf("%d.%d.%d.%d\n",sol[0],sol[1],sol[2],sol[3]);
    return;
  }
   int sum =0;
   while(*a)
   { if ((sum * 10 + (*a-'0'))<= 255)
     {  sum = sum * 10 + (*a-'0');
        a++;
        sol[rem]=sum;
        getAllIP(a,rem +1,sol);
     }   
     else 
     {   
        break;
     }
   }         
}     
#if 0
int main()
{   
char a[]="555555";
int sol[4]; 
getAllIP(a,0,sol); 
}   
#endif

/*******************************************************************************
* Problem 141 : Print Power set of the Arry  [1,2,3]
* Input:
* Output:
* Algorithms:
a) P(S) ={{}} # Start with Empty Set
b) Take one elemnt one by one from the array
c) Taking = P(S) =+ {{}} +{1} => {1} => P(S) =[ {], {1} ]
d) Taking 2 in account P(S) += P(S) * {2} = [{},{1} ,{2},{1,2} ] 
e) so on...
that is P(S) =P(S) + P(S) *{i}
*******************************************************************************/



/*******************************************************************************
* Problem 142 : Print All permuation in Sorted Order => [2,1,3] =>123,132,213,231,312,321 
* Input:
* Output:
* Algorithms:
a) Find the Start ( Minimum Permutation) that is lowest permutation by sort => 123.
b) Find Next permuation by next algotuhim.
*******************************************************************************/

/*******************************************************************************
* Problem 143: Print Next permuation in same number
* Input: DCFEBA
* Output: DEABCF
* Algorithms:
a) Start with previous Permuation :                                                  D C F E B A 
b) Scan from Right , find right most chrater which is smaller than previous(basically next from left) chrater.      ==> Here is C , is the right most chater which is less than F.
c) Find the Cilling of X : Find Just greater chrater on right of C : here min(F,E) = E
d) Swap C and E : >>> D E F C B A
e) Sort after E : D E <A B C F > ==> D E A B C F
*******************************************************************************/
#if 0

#endif
void nextHigh(char *a,int n)
{
  //get the pivit X
  int x,h;
  x=h =-1;
  for (int i =n-2;i>=0;i--)
    if (Int(a[i]) < Int(a[i+1]))
      { x = i; break;}
  if( x == -1)
  { printf(" No higher"); return;}

  // Find Just Greater tha 4.
  for (int i = x+1;i<=n;i++)
  {
   if (a[i] > a[x]) 
   {     
    if( h == -1) h = i;
    else if (a[h] > a[i]) h = i;
   }    
  }
 if( h== -1) 
  { printf(" No higher"); return; }

 // Swap Just Greater with X.
 char temp = a[x]; a[x]=a[h];a[h]=temp;
    
 //sort the a[h+1:]  
   std::sort(a+x+1,a+n); 
    
 printf("%s\n",a);
}  
#if 0
int main()
{
char a[]="12341";//"12345678498765321";
 nextHigh(a,5);
}
#endif
 
/*******************************************************************************
* Problem 144 : Given an Arry , find how many trangle can be formed. 
* Input: { 4,6,3,7 } =>[ {3,4,6},{4,6,7},{3,6,7} ]
* Output:
* Algorithms:
Sol 1: Run 3 nested Loop O(n^3)
Sol 2: Rule is if sum of two more than other number
a) Sort the Arry non-creating order.
b) trabgle count = 0, i =0, j =1
c) Scan from arry find the right most such that A[k] > ( A[i] + A[j] ), thus all k+1 to n will satisfy this rule.
  thus count = n-k+1
d) incremnt value of j : j++ and Do again
>>> Impormnt , w can find the vaue of from the k, getting from step (c)
e) when j reahes the end ;incement the value of i ; i++;
*******************************************************************************/

/*******************************************************************************
* Problem 145 : How to sort Nearly sorted Arry Efficytly : Dupliacte 
* Input:
* Output:
* Algorithms:
Sol 1: Using insertion sort => O(n*k)
for (i=1li<size;i++)
{
 key = A[i];
 j =i-1;
 While( j>= && A[j] > key)
 { A[j+1] = A[j] ; 
    j--;
 }
 A[j+1] =key 
}
Sol 2: Useing heap sort O(k) + O(n-k)*logk
a) We have arry a[0-----------k-------------------n]
b) Make a heap a[0<============>k] O(k)
for the last (n-k) do
c1) remove top and put it last
c2) Insert the next elemnt 
*******************************************************************************/


/*******************************************************************************
* problem 146 : Find maximum circular Sum 
* Input:
* Output:
* Algorithms: 
Modified Kadanes' Algorithms:
a) K= Apply Kadane's Algo
b) Find Full Sum S= sum(A[i])
c) Invert the full Appyu A[i] = -A[i]
d) Run Kadane's Algo again : K2
e) Ans = max (K1,K2+S)

Sol 2: Rotate N time and Apply Kadane algo n times -O(n2)
*******************************************************************************/

/*******************************************************************************
* Problem 147: Find Uniqe raw in a Matrix 
* Input:
* Output:
* Algorithms:
Sol 1: For each row , check with all otehr raw (O(n2*m)
sol2 : Find decimal of each row and Do a Hash lookup -
a) R= A[i]*10^i
b) Use hash lookup for unity.

Sol 3: USE Ties to do a insert a Raw ad loopup / Bollean tree. O(n*m)
*******************************************************************************/

/*******************************************************************************
* Problem 148: generate Random suffle of an array 
* Input:
* Output:
* Algorithms:
Sol 1: Copy the Array by Randomly select any elemnt. besicaly It require a bit map to check dupliactes.
Sol2: Tricky but efficient== O(n)
a) Selct an randon elemnt from A[1..n] and swap with A[n]
b) Do the same for A[1..n-1] 
*******************************************************************************/

/*******************************************************************************
* Problem 149 :  Given a list of tupule, find logesnt length of Chain pair.(a,b) <(c,d) iff a<b && c<d
* Input:
* Output:
* Algorithms:
Sol 1: Use two loop methids
Sol 2: Tricky and Efficient
a) Sort the tuples based on first index O(nlogn)
b) Find LIS on second elemnts/
*******************************************************************************/

/*******************************************************************************
* Problem 150 : replace every elemnt by next height number in right -- Duplicate
* problem 151:  Find a pair of Given difference |A[i] -A[j] | = M 
* Input:
* Output:
* Algorithms:
Sol1: Two loop / For each pair do the tet. O(n2)
Sol 2: Sort the list and Do the Binary serach for M-A[i] or M+A[i]
Sol 3: Tricky but efficient.VVI
a) Sort the arry
b) initilliaze i =0 and j =1
if A[j]-A[i] <n then do j++
if A[j] -A[i] >n then do i++
*******************************************************************************/

/*******************************************************************************
* Problem 152: Find all sorted sunsequence of length 3 
* Input:
* Output:
* Algorithms: Duplicates.

*******************************************************************************/

/*******************************************************************************
* Problem 153:  A party has N people, Only One persion is known by all. But she doesnt know anyone. Find Her?
* Input:
* Output:
* Algorithms: 
SOl1 : Make a Graph NC2 Haveing an edge if A knows B A-->B ,and Find the Sink
Sol2 : use Recustion , when A say B is celibrity , then we know A is not, remove A from that SET and Do the recusion Talk with Other 
T(n) = T(n-1)+1

Sol 3: Use Stack.
a) Push all Celebrity in Stack
b) Pop Two persion: A and B; Ask (A knows B)? 
c) Push one and Discart Another
d) Repeat Step b/c until one elemnt in Stack
*******************************************************************************/

/*******************************************************************************
* Problem 154: Find a Sub Arry of given Sum= N(VVi) 
* Input:
* Output:
* Algorithms:
Sol1 : Consider all sub arry and find Sum and return Max . O(n3)
Sol2 : Optimize the Efficiency , why keeping track the previous calculation O(n2), Here sum calculation is not done all the time/
Sol 3: Tricky But effficients
a) Scan from left to right and keep track the sum so far(cumative sum)

for (int i=0;i<n;i++)
{
  while(sur_sum >M && start <i-1)
  { cur_sum = cursum- A[start]; start ++;}
  if(cur_sum == m) ==> print
  cur_sum += A[i]
}
*******************************************************************************/

/*******************************************************************************
* Problem 154: Find Maximum Sub Ary Sum
* Input:
* Output:
* Algorithms:
Sol1 : Consider all sub arry and find Sum and return Max . O(n3)
Sol2 : Optimize the Efficiency , why keeping track the previous calculation O(n2), Here sum calculation is not done all the time/
Sol 3: Tricky But effficients
a) Scan from left to right and keep track the Max_Sum_so_far and cur_sum_upto

for (int i=0;i<n;i++)
{
  cur_sum_upto += A[i]
  if (cur_sum_upto > Max_Sum_so_far) { Max_Sum_so_far =cur_sum_upto}
  if cur_sum_upto ==0
  { Start =i;
  }
}
*******************************************************************************/



/*******************************************************************************
* Problem: Smallest subarray with sum greater than a given value
* Input:
* Output:
* Algorithms: Windows technique
*******************************************************************************/

int smallLengthMaxGrtArry(int *a,int len,int k)
{
	
   int win_left =0;
   int win_right =0;
   int sum = 0;
   int min_length = len+1,reg_left =0,reg_right=0;
   while(win_right < len)
   {   
   
       /* Streaching windows to right side */
   	   while(sum <= k && win_right < len)
   	   {
   	   	sum += a[win_right];
   	   	win_right ++;
   	   }
       /* Now shinking the windows from left and update minimum length */
   	   while(sum > k && win_left < len  )
   	   {
   	   	  if (min_length > win_right - win_left)
   	   	  {
   	   	  	min_length = win_right - win_left;
   	   	  	reg_left =win_left;reg_right= win_right-1;
   	   	  }
   	   	  sum -= a[win_left];
   	   	  win_left ++;
   	   }     	   
   }
   printf("Ans: %d",min_length);
   PRINT_1D_ARRAY_SEGMENT(a,reg_left,reg_right);
}

void test_smallLengthMaxGrtArry()
{
	int a[6] = {1, 4, 45, 6, 0, 19};
	smallLengthMaxGrtArry(a,6,51);
}


/*******************************************************************************
* Problem 155: A arry first increaing and then Decreaing, Find the Max Elemnts 
* Input:
* Output:
* Algorithms:
1) Linera serach : see pair to pair.
2) Binary serach
 if A[m] >A[m+1] || A[m] <A[m-1] return; 
*******************************************************************************/
/*******************************************************************************
* Problem 157: Find Minimum distance between two numbr ? 
* Input:
* Output:
* Algorithms:
Sol1 :two loop approach.
a) for(int i=0;i<n;i++)
   for(int j=i;j<n;j++)
     if A[i]==x && A[j] = Y or A[j]=X && A[i] =Y and i-j > max_diff => upadte max_diff
     
     
Sol 2: Trickt and Effie=cinet
a) Traverse left to right if any one foind(x or y) save the index.aldo keep tarce the elemnts
b) Now start again from dr, if found save the position and chec the diff, if now ocuue is not same oas prevois occure

i=0
while(A[i]not X or Y)
i++
=> Keep pre = x or y and pre_loc as i
for (; i<n;i++)
 if (A[i] is X or Y)
  if A[i] not as prv and i -prev_loc <min) ==> Update A[i] and Min diff.
  Now save this prev and prev_loc 
*******************************************************************************/

/*******************************************************************************
* Problem 156: An arry is a subset of another arry or not ? 
* Input:
* Output:
* Algorithms:
Sol1; Use Bit map
Sol2 : Sort and Check.
Sol 3: Two loop
*******************************************************************************/



/*******************************************************************************
* Problem 158: Maximum of all sub arry of size K ? 
* Input:
* Output:
* Algorithms:
Sol 1: Use Two loop techniw.
Find all Arry of Size k.
for ( int i=0;i< N-K;i++)
  j= i+k
  // find sumA[i:j] and ceck for max sum
  
Sol 2: Optimize  Sol1 : by keep trace prevois  sum , So re sum calculation is not requied.
Sol 3: Windows Techniqie. Think We have a K length windows passing the array.
     <======>
1,2,3[ 4,5,6]  ,8,9,0
     <======>
A) Keep the sumin the windos.
b) while moving new sum = Win_sum = winsum+A[++j] -A[--i]'
c) Keep checking minimum.
*******************************************************************************/

/*******************************************************************************
* Problem 159:  Rpale Next greater elemnt for all elemnt in that Arry.
* Input: 4,5,2,25 => 5, -1,25,-1
* Output:
* Algorithms:
Sol 1: Use toop loops.
Sol 2: Right to Left scan will NOT WORK.
Sol 3L use Stack. N/A
a) Push the first Elemnt
b) pick rest of the elemnt and do.
c) mark the current elemt as next
d) Pop the elemnt and comare with next
1) If next > pop => Good print
2. if next < pop => keep poping until you get an elemt smaller than next=> Not foudn push back
*******************************************************************************/

/*******************************************************************************
* Problem 160:  Fina Max Arithmetic progressing
* Input:
* Output:
* Algorithms:N/A
*******************************************************************************/

/*******************************************************************************
* Problem 161: Print a Sequence of gray code 
* Input:
* Output: 
* Algorithms: N/A
1. Start with all 0 <0 0 0 0>
2. find First left as 0 and make it 1 <0 0 0 1>
3. if it is not zero,find the Zero befoe it and make it 1 and : 0010
*******************************************************************************/
/*******************************************************************************
* Problem 162: Find Intersection of two sorted arry 
* Input:
* Output:
* Algorithms:
Sol1 : Two lop
Sol2: Sort one and do a Binarty serach for another
Sol3: Hash/Bit map collision.
Sol4: Sort and simulate merge sort
*******************************************************************************/

/*******************************************************************************
* Problem 163: Find an elemt in sorted rotateed arry 
* Input:
* Output:
* Algorithms:
1.linear srach (n)
2. Find Pivot and so Both way Binary sercah
3. One way binary serach.
*******************************************************************************/
#if 0
int rotate_serach(int a[],int n,int key)
{
	int l=0;
	int r =n-1;
	int m;
	while(l<r)
	{
		m =l+(r-l)/2;
		if (a[m] ==key)
		  printf("find key at %d loaction",m);
		if(a[l]<=a[m]) //left is sorted.
		{
			if (a[l] <=key && key < a[m]) //kry is 
			{
				r = m-1;
			}
			else
			{
				l=m+1;
			}
		}
		else
		{
			//right sorted.
			if( a[m] <= key && key <= a[h])
			{
				l =m+1;
			}
			else
			{
				r=m-1;
			}
		}
	}
	
}
#endif
/*******************************************************************************
* Problem 165: Find elemnt wich occue N/2, N/3 and N/K times. 
* Input:
* Output:
* Algorithms:
Sol 1:
for N/2 use two counter technique
Sol2 : Sort and only 3 Comrarinsm <0,1> or <n/2,n/2-1) or <n-2,n-1>
for N/3 use Two counter varaible
For N/k use k counter, or a list of K candidates.
*******************************************************************************/

/*******************************************************************************
* Problem 166: Find K-th larest elemt in 2D arry
* Input:
* Output:
* Algorithms: Duplicates
*******************************************************************************/

/*******************************************************************************
* Problem 167: Find max (j-i) when A[i]-A[j] is Zero ? 
* Input:
* Output:
* Algorithms:
Sol1 : Brought fouce pproach
Sol 2: N/A
*******************************************************************************/
/*******************************************************************************
* Problem 168: Implemnt Bucket fill Algorithms 
* Input:
* Output:
* Algorithms:
a) bktfill(image,newcolr,x,y)
{
   old = image[x][y]
   if old= nw;
     return
    else
    imahe [x][y] = new_color.
    All 9 side if iamge[x+1]][y+1] is old color. call this func..
*******************************************************************************/

/*******************************************************************************
* Problem 170: Imaplemht Set havig: Insert/Remove/Get random  
* Input:
* Output:
* Algorithms:
DS: Arry/Linkedlist + Hash table/
Insert => Check hash and insert in both
Delete => Check hash and delete from both
Serach => hash
get Random : random Index in arry.
*******************************************************************************/

/*******************************************************************************
* Problem 171: Count all posible way to group(len 2 or 3) whose sum is multiple of 3 
* Input:
* Output:
* Algorithms:
a) map all rement to 3 buckets or Remender 0,1,2
c) find out the combination of group of two or three ement from these buckets.
*******************************************************************************/

/*******************************************************************************
* problem 172: Duplicates
* Problem 173 : Rearrange a[i] to a[a[i] 
* Input:
* Output:
* Algorithms: N/A
a) rise A[i]: A[i]+= A[a[i] %i]*n
b) Arr[i] =arr[i]/n
*******************************************************************************/

/*******************************************************************************
* Problem 174: All distict pair having diff k {<a,b> sunch that |a-b| =k}
* Input:
* Output:
* Algorithms:
Sol1 : two loop fins all pair.
Sol 2: sort arry and do a binry srcag for a[i]+k and a[i] -K
Sol 3: Use hashing.
*******************************************************************************/


/*******************************************************************************
* Problem 175: have two arry X and Y, find x, y such that X^y >y^x 
* Input:
* Output:
* Algorithms:
sol 1: two llop.
Sol2: Tricky but efficinet
idea: y>x =>x^y >y^x
a) sort Y
b) for each x in X,find inx in Y shuch that Y[idx]>y
c) count+ = Y[idx-M]

*******************************************************************************/

/*******************************************************************************
* Problem 176: Move All zero at end. 
* Input:
* Output:
* Algorithms:
Sol 1: Loop count all Zero and move Non-zero i  left.
Sol 2: partiion swap techque.
*******************************************************************************/

/*******************************************************************************
* Problem 177 : Stable Marrge problem 
* Input:
* Output:
* Algorithms:
a) amke all mena nd wopmen free
whiel(Atleast one mem m left)
{
  >> w is his choice.
  >> if (w is not engaed ) <m,w>
  >> if w is engaed . break up . <m,w> anothet men free
}
*******************************************************************************/

/*******************************************************************************
* Problem 177 : Duplicate 
* Problem 178 : Increaing sequnece of llength 3 max product 
* Input:
* Output:
* Algorithms:
a. find Largest smallest elemnt in left LSL[i]
b) find largest greter elemnt in Right LGR[i]
c) ans = max(LSL[i]*A[i] *LGR[i])
*******************************************************************************/

/*******************************************************************************
* Problem 179 : Find Next Greatest Elemnt in Right: Largest Greater Right 
* Input:
* Output:
* Algorithms:
Sol 1: Use Two loop method.
Sol2: Tricky but effiect.
a) Scan from right to left, while scanning keep track max_elemnt fo_far and keep replacing these elemnts.

*******************************************************************************/
/*******************************************************************************
* Problem 180 : Largest smallest element in left 
* Input:
* Output:
* Algorithms:
a) Make BST, taking input one by one, and while doing find the Inorder sucessor fot it.
*******************************************************************************/

/*******************************************************************************
* Problem 181 : find whne f(i) >0 for first time. 
* Input:
* Output:
* Algorithms:
f() is an infinie=te sequences.
use juming by poer of two
if foudd , do the binary serach over [n/2,n] range
*******************************************************************************/

/*******************************************************************************
* Problem 182 : umber Apper more than N/K times. 
* Input:
* Output:
* Algorithms:
Sol1 : two looping techniw O(n2)
Sol 2: Shot and do a leaniear serach O(nlogn +n)
Sol 3: Tricky aand efficient  O(n *k )
iDEA : There can be maximum k-1 elemnts
a) create elemnt [1:k-1] <<<<<<<< O(k)
b) Select Candidate Iterate over list and if a[i] not in element[], insert that item with cout =1
   if no space , decremnt the counter of all, <<< O(K)
c) Test the cndiacte again . O(n*k)
*******************************************************************************/

/*******************************************************************************
* Problem 183 : Find Local Pick Elemnts 
* Input:
* Output:
* Algorithms:
It just to find loacl pick by a Binry serach.

we have l, m,h:
if m==0 && a[m] >=a[mid+1) OR
if m ==n-1 && a[m] <=A[mid-1] OR
a[m-1] <=a[m]<=a[m+1-
return m

We have brank to only one directuuon. why ?

*******************************************************************************/

/*******************************************************************************
* Problem 184 : Sort Elemnt by frequuency  
* Input:
* Output:
* Algorithms:
Sol1 : Short the elemne
Scan from left to right and maintain a counter.( this ia baslaiil a hash)
Print the ouput by counter map

sol2: BST and 2D index arry.
a) form a BST of input arry , Node has a counter.
b) Make a 2d index arry on counter and a ponter to node.
c) sort the index arry.
d) print data from bst as pointed by index arry.
*******************************************************************************/


/*******************************************************************************
* Problem 185: place +ve and -ve number Alternatovly 
* Input:
* Output:
* Algorithms:
a) use partion techniw, make all +ve the all -ve,
b) Now palce pointer at first -ve and first +ve and keep swaping
*******************************************************************************/


/*******************************************************************************
* Problem 186: Stock But Shell To max profit 
* Input:
* Output:
* Algorithms:
Sol:
While(end of list)
{
>> Find local minima to buy : while(p[i+1<p[i]) --< buy this point when break
>> Find local maxima to shell : while(p[i+1] >p[i] ) <<<< sell this point when while vreat
buy_sell_count ++;
}
*******************************************************************************/

/*******************************************************************************
* Problem 187: Find Max[Aj-Ai] where j> i 
* Input:
* Output:
* Algorithms:
Sol1 : two lloop.
Sol2 : Tricky and Efficient
>>>>>>.. keep track max_diff_so_far
min_ele =a[0]
max_so_far =a[1]-a[0]
for (i = 1 to n)
{  if a[i]-min el) >max_dif_so_far, then updtae;
   if a[i]<min_ele , then update min_ele
}
*******************************************************************************/

/*******************************************************************************
* Problem 188 : Merge Overlap Interval 
* Input:
* Output:
* Algorithms:
a) Sort the interval on start time
b) Stack() and push the fiest interval
c) for next interval<a,b> :
  if top is indipent of <a,b> Push
  else: mare <a,b> with top and push
*******************************************************************************/

/*******************************************************************************
* Problem  189 : Print Matrix Diagonaly
* Input:
* Output:
* Algorithms: N/A
*******************************************************************************/


/*******************************************************************************
* Problem  190 : Maximum sum such that no two elements are adjacent
* Input:
* Output:
* Algorithms: 
int FindMaxSum(int arr[], int n)
{
  int incl = arr[0];
  int excl = 0;
  int excl_new;
  int i;
 
  for (i = 1; i < n; i++)
  {
     // current max excluding i 
     excl_new = (incl > excl)? incl: excl;
 
     /* current max including i 
     incl = excl + arr[i];
     excl = excl_new;
  }
 
   /* return max of incl and excl 
   return ((incl > excl)? incl : excl);
}
*******************************************************************************/



/*******************************************************************************
* Problem  191: Leader of an Arry : Write a program to print all the LEADERS in the array.
 An element is leader if it is greater than all the elements to its right side.
  And the rightmost element is always a leader. For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.
* Input:
* Output:
* Algorithms: 
/*Function to print leaders in an array 
void printLeaders(int arr[], int size)
{
  int max_from_right =  arr[size-1];
  int i;
 
  /* Rightmost element is always leader 
  printf("%d ", max_from_right);
     
  for(i = size-2; i >= 0; i--)
  {
    if(max_from_right < arr[i])
    {
       printf("%d ", arr[i]);
       max_from_right = arr[i];
    }
  }    
}
*******************************************************************************/

/*******************************************************************************
* Problem  : Maximum size square sub-matrix with all 1s
* Input:
* Output:
* Algorithms: 
1) Construct a sum matrix S[R][C] for the given M[R][C].
     a)	Copy first row and first columns as it is from M[][] to S[][]
     b)	For other entries, use following expressions to construct S[][]
         If M[i][j] is 1 then
            S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
         Else /*If M[i][j] is 0
            S[i][j] = 0
2) Find the maximum entry in S[R][C]
3) Using the value and coordinates of maximum entry in S[i], print 
   sub-matrix of M[][]
*******************************************************************************/

/*******************************************************************************
* Problem  : Find the smallest and second smallest element in an array in same go
* Input:
* Output:
* Algorithms: 
1) Initialize both first and second smallest as INT_MAX
   first = second = INT_MAX
2) Loop through all the elements.
   a) If the current element is smaller than first, then update first 
       and second. 
   b) Else if the current element is smaller than second then update 
    second
*******************************************************************************/

/*******************************************************************************
* Problem  : Find whether an array is subset of another array
* Input:
* Output:
* Algorithms: 
1. Method 1 (Simple) 
Use two loops: The outer loop picks all the elements of arr2[] one by one. 
The inner loop linearly searches for the element picked by outer loop.
If all elements are found then return 1, else return 0.
Method 2 (Use Sorting and Binary Search)

1) Sort arr1[] O(mLogm)
2) For each element of arr2[], do binary search for it in sorted arr1[].
         a) If the element is not found then return 0.
3) If all elements are present then return 1.

Method 3 (Use Sorting and Merging ) 
1) Sort both arrays: arr1[] and arr2[] O(mLogm + nLogn) 
2) Use Merge type of process to see if all elements of sorted arr2[] are present in sorted arr1[].

Method 4 (Use Hashing) 
1) Create a Hash Table for all the elements of arr1[]. 
2) Traverse arr2[] and search for each element of arr2[] in the Hash Table. If element is not found then return 0. 
3) If all elements are found then return 1.

*******************************************************************************/


/*******************************************************************************
* Problem  : Median in a stream of integers (running integers)
* Input:
* Output:
* Algorithms:
Sol1 : Method 1: Insertion Sort: If we can sort the data as it appears, we can easily locate median element.
 Insertion Sort is one such online algorithm that sorts the data appeared so far.
 Sol 2:  Balace BST
 At every node of BST, maintain number of elements in the subtree rooted at that node.
  We can use a node as root of simple binary tree, whose left child is self balancing BST with elements less than root
   and a right child is self balancing BST with elements greater than root.
    The root element always holds effective median .
    
Sol 3: S
we can use a max heap on left side to represent elements that are less than effective median ,
and a min heap on right side to represent elements that are greater than effective median .

*******************************************************************************/


/*******************************************************************************
* Problem  : Maximum Length Bitonic Subarray
* Input:
* Output:
* Algorithms:
Let us consider the array {12, 4, 78, 90, 45, 23} to understand the soultion. 
1) Construct an auxiliary array inc[] from left to right such that inc[i] contains length of the nondecreaing subarray ending at arr[i]. 
For for A[] = {12, 4, 78, 90, 45, 23}, inc[] is {1, 1, 2, 3, 1, 1}

2) Construct another array dec[] from right to left such that dec[i] contains length of nonincreasing subarray starting at arr[i]. 
For A[] = {12, 4, 78, 90, 45, 23}, dec[] is {2, 1, 1, 3, 2, 1}.

3) Once we have the inc[] and dec[] arrays, all we need to do is find the maximum value of (inc[i] + dec[i] – 1). 
For {12, 4, 78, 90, 45, 23}, the max value of (inc[i] + dec[i] – 1) is 5 for i = 3.
*******************************************************************************/

/*******************************************************************************
* Problem  : Convert String to input array
* Input:
* Output:
* Algorithms:N/A
*******************************************************************************/
int * strTOintList(char *s,int *len)
{
  int state = 0, i, count;
  char *a=s;

  for (count=0;*a != '\0';a++)
  { if (IS_DIGIT(*a) && state == 0)
      { state = 1;count++;
      }
    if (!IS_DIGIT(*a) && state == 1)
     { state =0;
     }
  }

  *len = count;
  int *out =(int *) malloc(sizeof(int) * count);
  int sum=0;
  for (a=s,count= 0;*a != '\0';a++)
  { if (IS_DIGIT(*a) && state == 0)
      { state = 1;
        sum = CHAR_TO_DIGIT(*a);
      }
    else if (IS_DIGIT(*a) && state == 1)
    {
      sum = sum*10 + CHAR_TO_DIGIT(*a);
    }
    else if (!IS_DIGIT(*a) && state == 1)
     { state =0;
       out[count++] =sum;
       sum =0;
     }
  }
  if(state == 1)
    out[count] =sum;
  return out;
}

void test_strTOintList()
{
  char str[100];
  printf("Enter the String :");
  scanf("%[^\n]s",str);

  int n;
  int *a = strTOintList(str,&n);
  PRINT_ARRY_WITH_INDEX(a,n);
}
 
/*******************************************************************************
* Problem  : [Partition technique 1] Given an arry of intergers , given an index i, re-arrange all elemnt 
less than A[i], in left,then all elemt equlal to A[i], then all greater elemnets
* Input:
* Output:
* Algorithms:N/A
*******************************************************************************/

void partition(int x[],int len,int pivot)
{

	int left=0,right =len-1;
	while(left<right)
	{
		while(x[left] <= pivot)
		  left ++;
		while(x[right] > pivot)
		  right --;
		  
		SWAP_VALUE(x[left],x[right]);
		left++;right --;
	}
	PRINT_1D_ARRAY(x,len);

}

void test_partition()
{
	int x[]={2,3,4,2,2,10,2,4,5};
	partition(x,9,2);
	
}

/*******************************************************************************
* Problem  : [Partition technique 2] Given an arry of intergers , given an index i, re-arrange all elemnt 
less than A[i], in left,then all elemt equlal to A[i], then all greater elemnets
* Input:
* Output:
* Algorithms:N/A
*******************************************************************************/

void partition20(int x[],int len,int pivot)
{

	int left=0,right =len-1;
	while(left<right)
	{
		while(x[left] <= pivot)
		  left ++;
		while(x[right] > pivot)
		  right --;
		  
		SWAP_VALUE(x[left],x[right]);
		left++;right --;
	}
	PRINT_1D_ARRAY(x,len);

}

void test_partition20()
{
	int x[]={2,3,4,2,2,10,2,4,5};
	partition(x,9,2);
	
}

/*******************************************************************************
* Problem  : 
* Input:
* Output:
* Algorithms:N/A
*******************************************************************************/
/*******************************************************************************
* Problem  : 
* Input:
* Output:
* Algorithms:N/A
*******************************************************************************/
/*******************************************************************************
* Problem  : 
* Input:
* Output:
* Algorithms:N/A
*******************************************************************************/
/*******************************************************************************
* Problem  : 
* Input:
* Output:
* Algorithms:N/A
*******************************************************************************/
/*******************************************************************************
* Problem  : 
* Input:
* Output:
* Algorithms:N/A
*******************************************************************************/
/*******************************************************************************
* Problem  : 
* Input:
* Output:
* Algorithms:N/A
*******************************************************************************/





/***********************  Start of Driver Program at Here *********************/
#if UNIT_TEST
int main()
{
    test();
}    
#endif

