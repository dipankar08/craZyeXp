#include<string.h>
int main(){
  char str[200];
  printf("Enter stirng:\n");
  gets(str);
  puts(str);
  printf("Len: %d\n",strlen(str));
  char *ptr;
  ptr = str;
  int count = 0;
  while(*(ptr)!='\0'){
    if(*(ptr)==' ' ){
       while(*(ptr)== ' ')
         ptr++;
    }
    else{
       while(*(ptr)!= ' ' && *(ptr)!= '\0'  )
         ptr++;
       count++;
    }
  }
  printf("\nDiff: %d\n",ptr-str);
  printf("Number of words %d",count);
}


