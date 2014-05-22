/***********************************************
*  Common function used by our lib
*
*************************************************/


#define MAX(i,j) ( (i > j) ? i:j)
#define MIN(i,j) ( (i<j) ? i:j)
#define STRLEN(a,i) char *_z=a; for(i=0;*_z;i++,_z++);

#define PRINT_1D_ARRAY(a,n) for(int i=0;i<n;i++) printf("%d,"a[i]);
#define PRINT_2D_ARRAY(a,m,n) printf("\n\n");\
                              for(int i=0;i<m;i++) \
                               { for (int j=0;j<n;j++) \
							       printf("%d ",a[i][j]); \
							      printf("\n"); \
							    }

#define SET_2D_ARRAY_ZERO(a,m,n) for (int i=0;i<m;i++) for (int j=0;j<n;j++) a[i][j] = 0;							
							    
#define PRINT_SEPARATOR(type,len) \
printf("\n");\
for (int i=0;i<len;i++) \
  printf("%c",type); \
printf("\n");

#define PRINT_ARRY_WITH_INDEX(arr,n) \
PRINT_SEPARATOR('-',n*5);\
for(int i =0 ;i<n;i++) \
 printf("%5d",i);\
PRINT_SEPARATOR('-',n*5);\
for(int i =0 ;i<n;i++) \
 printf("%5d",arr[i]); \
PRINT_SEPARATOR('-',n*5);\


