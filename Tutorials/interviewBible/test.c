#include<stdio.h>
#define MIN(a,b) ((a>b)?b:a)
#define ARRAY_LEN(arr) (sizeof(arr)/sizeof(arr[0]))

int smallestSubArrywithMoreSum(int a[],int n, int x)
{
	int win_left=0;
	int win_right=0;
	int win_sum =a[0];
	int min_length = n;
	
    while(win_right < n-1)
    {
    	/* Expanding windows right side */
    	while(win_sum <x )
    	{
    		win_right ++;
    		win_sum += a[win_right];
    	}
    
    	/* Srinking windows from left */
    	while(win_sum  >= x)
    	{
    		win_sum -= a[win_left];
    		win_left ++;
    		
    		if(win_sum  > x)
    		min_length =MIN( min_length, win_right-win_left +1);      		
    	}
    	
   	
    }
    printf("Min length is %d",min_length);
	return 0;
}

int main()
{
	int arr1[] = {1, 4, 45, 6, 10, 19};
	smallestSubArrywithMoreSum(arr1,ARRAY_LEN(arr1),51);
}

