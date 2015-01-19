#include "common.h"


#include<stdio.h>
int main(){
    int sum=10;
    for(int i=0;i<10;i++)
    if(i%2==1){
        sum = sum+i;
    }
    printf("%d",sum);
}