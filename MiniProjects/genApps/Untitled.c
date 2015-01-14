#include "common.h"
#include<stdio.h>
int fact(int);

int main(){
printf("%d",fact(10));
}int fact(int i){
    if(i==0) return 1;
    else return i*fact(i-1);
}