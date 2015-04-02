/* dtest is automated testing by dipankar */
#include<stdio.h>
void TEST_INT_TO_INT(int (*f)(int) ){
  printf("\n==========================================");
  printf("\n======= W E L C O M E   D T E S T   ======");
  printf("\n==========================================");
  int tc=0,pass=0,fail=0;
  int in,out;
  scanf("%d",&tc);
    printf("\nTotal test case  : #%d",tc);
  for(int i=0;i<tc;i++){
  printf("\n\nTest Case        : %d",i);
    scanf("%d",&in);
    scanf("%d",&out);
    printf("\nExpected Input   : %d",in);
    printf("\nExpected Output  : %d",out);
    int exp = f(in);
    printf("\nObserved Output  : %d",exp);
    printf("\nStatus: "); 
    if(exp==out){printf("PASS");pass++;}
    else{printf("FAIL");fail++;}
  }
  printf("\n============  R E S U L T  ==============");
  printf("\nPass : %5d            FAIL : %5d    .",pass,fail);
  printf("\n=========================================");
}
void TEST_INTARR_TO_INT(int (*f)(int*,int) ){
  printf("\n==========================================");
  printf("\n======= W E L C O M E   D T E S T   ======");
  printf("\n==========================================");
  int tc=0,pass=0,fail=0;
  int in[100],n,out;
  scanf("%d",&tc);
    printf("\nTotal test case  : #%d",tc);
  for(int i=0;i<tc;i++){
  printf("\n\nTest Case        : %d",i);
    scanf("%d",&n);
    for(int j=0;j<n;j++){
      scanf("%d",&in[j]);
    }
    scanf("%d",&out);
    printf("\nExpected Input   :["); 
    for(int j=0;j<n;j++) printf("%d ",in[j]); printf(" ],%d",n);
    printf("\nExpected Output  : %d",out);
    int exp = f(in,n);
    printf("\nObserved Output  : %d",exp);
    printf("\nStatus: "); 
    if(exp==out){printf("PASS");pass++;}
    else{printf("FAIL");fail++;}
  }
  printf("\n============  R E S U L T  ==============");
  printf("\nPass : %5d            FAIL : %5d    .",pass,fail);
  printf("\n=========================================");
}

/* 
Example
4
1 1 hello how r u
2 2 1 a
3 3 2 1 a
4 5 4 3 2 aaa
*/
void TEST_INTARR_TO_STR(char* (*f)(int*,int) ){
  printf("\n==========================================");
  printf("\n======= W E L C O M E   D T E S T   ======");
  printf("\n==========================================");
  int tc=0,pass=0,fail=0;
  int in[100],n;
  char out[100];
  scanf("%d",&tc);
    printf("\nTotal test case  : #%d",tc);
  for(int i=0;i<tc;i++){
  printf("\n\nTest Case        : %d",i);
    scanf("%d",&n);
    for(int j=0;j<n;j++){
      scanf("%d",&in[j]);
    }
    printf("\nExpected Input   :["); 
    for(int j=0;j<n;j++) printf("%d ",in[j]); printf(" ],%d",n);
    //fgets (out, 100, stdin); // to ignore new line.
    scanf ("%[^\n]%*c", out);
    printf("\nExpected Output  : <%s>",out);
    char* exp = f(in,n);
    printf("\nObserved Output  : <%s>",exp);
    printf("\nStatus: "); 
    if(strcmp(exp,out)==0){printf("PASS");pass++;}
    else{printf("FAIL");fail++;}
  }
  printf("\n============  R E S U L T  ==============");
  printf("\nPass : %5d            FAIL : %5d    .",pass,fail);
  printf("\n=========================================");
}

