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

#define PRINT(A,B) for(int z=0; z<B; z++) printf("%d,",A[z]);printf("\n");

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
* Problem : Check Duplicates
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem : Find Maximum Repetative Elements
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem : Find Majority Elements ( Occure > n/2 times)
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem : Find First  repetative elemnt in an Array
* Input:
* Output:
* Algorithms:
*******************************************************************************/





/*******************************************************************************
* Problem : Find a+b = k when a,b =>A
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Find a+b -> 0 when a,b =>A
* Input:
* Output:
* Algorithms:
*******************************************************************************/



/*******************************************************************************
* Problem : find a+b =K if a,b =>A,B
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem : find a+b+c = k whne a,b,c =>A
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem : Find Rotate point K 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem :  Serach in a Rotated array
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem : Find the first occurance of a number
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem : Fina lat occurance of a number
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem : Find local minumum
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem : Sepapre odd/even or 0/1
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem :  Separate 0/1/2/
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem : Find maximim differenec
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Find lastget and smalest number in same scan in O(3n/2)
* Input:
* Output:
* Algorithms:
*******************************************************************************/



/*******************************************************************************
* Problem : Find k-th Smallest number uisng pertination.
* Input:
* Output:
* Algorithms:
*******************************************************************************/



/*******************************************************************************
* Problem : Find medium of two Sorted Array.
* Input:
* Output:
* Algorithms:
*******************************************************************************/



/*******************************************************************************
* Problem : Find k-th Smallest number of two Sorted Array.
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/***********************  Start of Driver Program at Here *********************/

int main()
{
    printf("********** [ Start oF driver Program ] *************\n\n");
    //int a[10]={8,1,2,9,3,7,0,6,4,5};
    int z;
    //bubbleSort(a,10);
    //selectionSort(a,10);
    //insertionSort(a,10);
    //int temp[10];
    //mergeSort(a,temp,0,9);
    
    
    //int x[10]={10,20,30,40,50,0,0,0,0,0};
    //int y[5] ={1,2,15,25,100};
    //InPlaceMerge(x,y,5,5);
	//PRINT(x,10);
	int a[7] ={1,2,3,4,5,6,7};
	binSearch(a,0,6,10) ;
    
    
    
    
    printf("\n\n****************** [ E N D ] *******************\n\n");
   // getch();
}    

