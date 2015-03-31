#include<stdio.h>
void sort(int *ar,int n){
  for(int i=0;i<n;i++){
    for(int j=0;j<n-i;j++){
     if(ar[j]>ar[j+1])
     {
       int tmp=ar[j];
       ar[j]=ar[j+1];
       ar[j+1]=tmp;
     }
    }
  }
}
PRINT(int *arr,int n){
  for(int i=0;i<n;i++)
    printf("%d ",arr[i]);
  printf("\n");
}
     
