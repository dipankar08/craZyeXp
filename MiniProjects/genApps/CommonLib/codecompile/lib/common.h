//common.h: Define all common Macho for data reading
#include<stdio.h>
#include<stdlib.h>
#define bool int

#define MIN(i,j) ((i>j)?(j):(i))
#define MAX(i,j) ((i>j)?(i):(j))
#define ABS(i) (i>0)?i:-i


#define IS_NUMARIC(i) (i>='0' && i<='9')

#define PRINT_BOOL(i) (i != 0)?printf("True"):printf("False");
#define PRINT_INT_ARR(_a,_b) printf("[");for(int _i=0; _i<_b; _i ++) { printf("%d ,", _a[_i]);}  printf("]\n");
#define PRINT_FLOAT_ARR(_a,_b) printf("[");for(int _i=0; _i<_b; _i ++) { printf("%f ,", _a[_i]);}  printf("]\n");
#define PRINT_CHAR_ARR(_a,_b) printf("[");for(int _i=0; _i<_b; _i ++) { printf("%c ,", _a[_i]);}  printf("]\n");
#define PRINT_STR_ARR(_a,_b) printf("[");for(int _i=0; _i<_b; _i ++) { printf("%s ,", _a[_i]);}  printf("]\n");

#define PRINT_INT_2DARR(_a,_b,_c) for(int _i=0; _i<_b; _i ++) {for(int _j=0; _j<_c; _j ++) printf("%-4d ", _a[_i][_j]);  printf("\n");}
#define PRINT_FLOAT_2DARR(_a,_b,_c) for(int _i=0; _i<_b; _i ++) {for(int _j=0; _j<_c; _j ++) printf("%-4.2f ", _a[_i][_j]);  printf("\n");}
#define PRINT_CHAR_2DARR(_a,_b,_c) for(int _i=0; _i<_b; _i ++) {for(int _j=0; _j<_c; _j ++) printf("%-2c ", _a[_i][_j]);  printf("\n");}
#define PRINT_STR_2DARR(_a,_b,_c) for(int _i=0; _i<_b; _i ++) {for(int _j=0; _j<_c; _j ++) printf("%-4s ", _a[_i][_j]);  printf("\n");}

#define IS_WHITE_CHAR(x) ((x)==' '||(x)=='\t' || (x)=='\n')

/* This function count the token separated by space */
int count_token(char *a)
{
    int count =0;
    int state = 0; //Outside word.
    char*temp = a;
    while(*temp){
        if(state == 1 && IS_WHITE_CHAR(*temp)){
            count++; //getting space
            state = 0;        
        }
        if(state == 0 && !IS_WHITE_CHAR(*temp)){
            state = 1 ;// inside word
        }
        temp++;           
    }
    if(state==1){count++;}
    //printf("\ncount_token:%d",count);
    return count;
}
/*working: This function convert a array to float */
float my_atoi(char *b,int start,int end)
{
    int state =1;
    int sign =1;
    float int_sum=0;
    float f_sum =0;
    float mult=1;
    char *a = b+start;
    while(a!=b+end+1)
    {    
        //validation..
        if (!(*a =='+' || *a =='-' || *a =='.' || (*a>='0' && *a<='9'))) 
        {  // invalid symbol..
           a++;continue;
        }
        else if ( *a =='+')
        {
            sign = 1;a++;continue;
        }
        else if (*a =='-')
        { sign = -1;a++;continue;
        }
        else if(*a=='.')
        {
            state = 2, a++; continue; //Mode to float State
        }          
        if( state == 1)
        { 
          int_sum = int_sum*10+ (*a-'0');a++;continue;        
        }
        if (state == 2)
        {   
          mult =mult/10;
          f_sum = f_sum + (*a-'0')*mult;a++;continue;
        }          
        
    }
    return sign*(int_sum+f_sum);    
}
/* read  User Input Arry 
Uses:
  int n;
  int *a =READ_INT_ARR(&n);
  PRINT_INT_ARR(a,n);  
*****************************/
int * READ_INT_ARR(int *_n){
    char s[100];
    fgets(s, sizeof(s), stdin);
    int n = count_token(s);
    int *a=(int *)malloc(n*sizeof(int));
    int count =0;
    int state = 0; //Outside word.
    char*temp = s;
    int sloc=0,eloc=0;
    int i=0;
    while(*temp){
        if(state == 1 && IS_WHITE_CHAR(*temp)){
            a[count]=my_atoi(s,sloc,i-1);        
            count++; //getting space
            state = 0;
                            
        }
        if(state == 0 && !IS_WHITE_CHAR(*temp)){
            state = 1 ;// inside word
            sloc=i;        
        }
        temp++;
        i++;               
    }
    if(state==1){a[count]=my_atoi(s,sloc,i-1); count++;}   
    *_n=n;
    return a;
}
float * READ_FLOAT_ARR(int *_n){
    char s[100];
    fgets(s, sizeof(s), stdin);
    int n = count_token(s);
    float *a=(float *)malloc(n*sizeof(float));
    int count =0;
    int state = 0; //Outside word.
    char*temp = s;
    int sloc=0,eloc=0;
    int i=0;
    while(*temp){
        if(state == 1 && IS_WHITE_CHAR(*temp)){
            a[count]=my_atoi(s,sloc,i-1);        
            count++; //getting space
            state = 0;
                            
        }
        if(state == 0 && !IS_WHITE_CHAR(*temp)){
            state = 1 ;// inside word
            sloc=i;        
        }
        temp++;
        i++;               
    }
    if(state==1){a[count]=my_atoi(s,sloc,i-1); count++;}   
    *_n=n;
    return a;
}
/* Not able to compile in cpp
int ** READ_INT_2DARR(int rows,int cols){
  int **array;
  int i,j;
  array = malloc(rows * sizeof(int *));
  for (i = 0; i < rows; i++)
    array[i] = malloc(cols * sizeof(int));

  // Some testing
  for (i = 0; i < rows; i++) {
    for (j = 0; j < cols; j++)
      array[i][j] = 0; // or whatever you want
  }

  for (i = 0; i < rows; i++) {
    for (j = 0; j < cols; j++)
      scanf("%d", &array[i][j]);
  }
  return array;
}
*/
