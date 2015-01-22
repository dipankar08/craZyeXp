#include "common.h"


#include<stdio.h>
int main(){
  int n;
  int *a =READ_INT_ARR(&n);
  PRINT_INT_ARR(a,n); 
  return 0;
}