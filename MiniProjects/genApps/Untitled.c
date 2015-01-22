#include "common.h"
#include<string.h>
int main(){
char str[200];
printf("Enter stirng:\n");
gets(str);
puts(str);
printf("Len: %d\n",strlen(str));
char *ptr;
ptr = str;
int count=0;
while(*(ptr)!='\0'){
        if(*(ptr)==' ' ){
        while(*(ptr)== ' ')
                ptr++;
        }
        else{
        while(*(ptr)!= ' ')
        ptr++;
        count++;
        }
}
printf("Number of words %d",count);
}


