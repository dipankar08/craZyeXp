/***********************************************
*  Common function used by our lib
*
*************************************************/


#define MAX(i,j) ( (i > j) ? i:j)
#define MIN(i,j) ( (i<j) ? i:j)
#define STRLEN(a,i) char *_z=a; for(i=0;*_z;i++,_z++);

#define PRINT_1D_ARRAY(_a,_n)\
 printf("\n["); \
 for(int _i=0;_i<_n;_i++) \
    printf("%d,"_a[_i]); \
 printf("]\n");

#define PRINT_2D_ARRAY(a,m,n) printf("\n\n");\
                              for(int i=0;i<m;i++) \
                               { for (int j=0;j<n;j++) \
							       printf("%d ",a[i][j]); \
							      printf("\n"); \
							    }

#define SET_2D_ARRAY_ZERO(a,m,n) for (int i=0;i<m;i++) for (int j=0;j<n;j++) a[i][j] = 0;							
							    
#define PRINT_SEPARATOR(type,len) \
for (int i=0;i<len;i++) \
  printf("%c",type); \
printf("\n");

#define PRINT_ARRY_WITH_INDEX(arr,n) \
printf("\n"); \
PRINT_SEPARATOR('-',n*5);\
for(int i =0 ;i<n;i++) \
 printf("%5d",i);\
printf("\n");PRINT_SEPARATOR('-',n*5);\
for(int i =0 ;i<n;i++) \
 printf("%5d",arr[i]); \
printf("\n"); PRINT_SEPARATOR('-',n*5);\

#if 0
#define CLEAR_STDIN \
scanf("%*[^\n]")
#endif

#define CLEAR_STDIN do{\
    int _chi; \
    while ((_chi = fgetc(stdin)) != EOF && _chi != '\n') {\
        /* null body */; \
    } \
}while(0);

#define IS_CHAR(a) ((a >='a' && a <='z') || (a >='A' && a <='Z'))
#define IS_DIGIT(a) (a>='0' && a <='9')
#define CHAR_TO_DIGIT(a) (a -'0')
