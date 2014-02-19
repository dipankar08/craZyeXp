#include<stdio.h>
#define INFO(msg) \
    printf("info: %s:%d: ", __FILE__, __LINE__); \
    printf("%s\n", msg);
int main(){
printf("HelloWorld\n");
INFO("dipankar");
return 0;
}
