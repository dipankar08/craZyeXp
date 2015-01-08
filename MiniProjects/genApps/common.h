//common.h: Define all common Macho for data reading

#define PRINT_INT_ARR(_a,_b) printf("[");for(int _i=0; _i<_b; _i ++) { printf("%d ,", _a[_i]);}  printf("]\n");
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
    printf("\ncount_token:%d",count);
}
/*Not working: This function convert a array to float */
float my_atoi(char *b,int start,int end)
{
    int state =1;
    int sign =0;
    float int_sum=0;
    float f_sum =0;
    float mult=1;
    char *a= b+start;
    puts(a);
    while(a!=b+end+1)
    {    
        //validation..
        printf("%c#",*a)  ;
        if (*a !='+' || *a !='-' || *a!='.' || !(*a>'0' && *a<'9')) 
          { a++;continue;}
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
        { int_sum = int_sum*10+ (*a-'0');a++;continue;        
        }
        if (state == 2)
        {   mult =mult/10;
            f_sum = f_sum + (*a-'0')/mult;a++;continue;
        }          
        
    }
    printf("%d",sign*(int_sum+f_sum));
    return sign*(int_sum+f_sum);    
}

