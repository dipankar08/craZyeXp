#include "common.h"
#include<stdio.h>
int main(){
    int i;
    float f;
    char c[10];
    
    scanf("%d",&i);
    scanf("%f",&f);
    scanf("%s",c);
    
    printf("We read i= %d ;f= %f ;c= %s;",i,f,c);
    return 0;
}
