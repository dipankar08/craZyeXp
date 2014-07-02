#include <dlfcn.h>
#include <stdio.h> /*for printf() */
#include <stdlib.h> /* for exit() */

int main()
{
   void *handle;
   void (*patch) (void);
   char *error;
   while(1)
   {   
   /* dynamically load the shared lib that contains somefunc() */
   handle = dlopen("./mylib.so", RTLD_LAZY);
   if (!handle) {
   fprintf(stderr, "%s\n", dlerror());
   exit(1);
   }
   /* get a pointer to the somefunc() function we just loaded */
   patch = dlsym(handle, "patch");
   if ((error = dlerror()) != NULL) {
      fprintf(stderr, "%s\n", error);
      exit(1);
   }
   /* Now we can call somefunc() just like any other function */
   patch();
 
   /* unload the shared library */
   if (dlclose(handle) < 0) {
      fprintf(stderr, "%s\n", dlerror());
      exit(1);
   }
   sleep(2);
  }
   return 0;
}

