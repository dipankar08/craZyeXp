#include <stdio.h> /*for printf() */
#include <stdlib.h> /* for exit() */

int main()
{
   void *handle;
   void (*patch) (void);
   char *error;
   while(1)
   {   
     patch(); 
     sleep(2);
  }
   return 0;
}

