#include "common.h"
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
void PRINT_ARR(int *arr,int n){
  for(int i=0;i<n;i++)
    printf("%d ",arr[i]);
  printf("\n");
}
void PRINT_ARR_SUB(int *arr,int ii,int j){
  printf("[");
  for(int i=ii;i<=j;i++)
    printf("%d ",arr[i]);
  printf("]\n");
}
/*Basicllay String to int array */
void READ_ARR(char *a,int **ans,int*ans_len){
  int state =0;
  char *temp =a;
  //Step1: let's comut the number of int.
  int count=0;
  while(*a){
    if(state==0 && IS_NUMARIC(*a)){
      count++;state=1;
    }
    if(!IS_NUMARIC(*a)){state=0;}
    a++;
  }
  //printf("%d",count);
  //Step2: crete a new array
  int *b = (int*)malloc(sizeof(int)*count);
  //step3: Do the looping agian to evalute the integer.
  a = temp;
  state=0;
  int val =0;
  int i=0;
  while(*a){
    if(state==0 && IS_NUMARIC(*a)){
      state=1;
      val = *a-'0';
    }
    else if(state == 1 && IS_NUMARIC(*a)){
      val = val*10+ (*a-'0');
    }    
    else if( state==1 &&!IS_NUMARIC(*a)){
      state=0;
      b[i++]=val;
      val =0;
    }
    else if( state==0 && !IS_NUMARIC(*a)){
      state=0;
    }
    a++;
  }
  //last element..
  if( state==1){
      b[i++]=val;
    }
  //printf("\nString to Int Covestion: ");
  //PRINT_ARR(b,count);
  *ans=b;*ans_len=count;
  
}     
