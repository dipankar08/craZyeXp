#include "common.h"
#include<stdio.h>
int main(){
  int **mat = READ_INT_2DARR(4,4);
  PRINT_INT_2DARR(mat,4,4);
  return 0;
}