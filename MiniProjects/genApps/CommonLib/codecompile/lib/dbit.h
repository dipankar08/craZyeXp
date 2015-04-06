#include<stdio.h>
void show_bit(int n){
  for(int i=0;i<8*sizeof(n);i++){
    if(i%8==0) printf(" ");
    printf("%d",(n>>(31-i)&1));    
  }
  printf("\n");
}
//masks
int LeftMaskKOne(int k){
  //printf("Step1: (1<<(32-k): ");show_bit((1<<(32-k)));
  //printf("Step2: (1<<(32-k) -1 : ");show_bit((1<<(32-k))-1);
  return ~((1<<(32-k))-1);
}
int RightMaskKOne(int k){
  return ((1<<(k))-1);
}
int MaskInMiddle(int i,int j){
  return 0 | LeftMaskKOne(i) | RightMaskKOne(j);
}
int MaskNotInMiddle(int i,int j){
  return ~( 0 | LeftMaskKOne(i) | RightMaskKOne(j));
}
