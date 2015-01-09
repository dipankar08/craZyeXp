#include "common.h"
#include<stdio.h>
int main(){
    int i,n; char s[100]; 
    scanf("%d",&n);
    for(i=0;i<n;i++){
        fgets( s, 100, stdin );
        puts(s);    
    }
    return 0
}
