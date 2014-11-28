#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
int main()
{
  int a[10] = { 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 };
  std::sort( a, &a[10], [](int x, int y){ return x < y; } );
  for(int i=0; i<10; i++) { printf("%i ", a[i]); }
  printf("\n");
  return 0;
}

//g++ Lambda2.cpp -std=c++11 && ./a.out 
