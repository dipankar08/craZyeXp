#include<stdio.h>

int buf[2] ={1,2}; /* Defination of Buf */

int main() /* Defination of main() */
{
  printf ("Before swap :%d ,%d\n",buf[0],buf[1]);
  swap(); /* reference to swap */
  printf ("After swap :%d ,%d\n",buf[0],buf[1]);
  return 0;
}
