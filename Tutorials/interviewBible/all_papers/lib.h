/***********************************************
*  Common function used by our lib
*
*************************************************/

#include <string.h>
#include<math.h>

/* config Macro */
#define UNIT_TEST true


/* Helper Macro */

#define MAX(x,y) ((x>y)?(x):(y))
#define MIN(x,y) ((x>y)?(y):(x))

#define SWAP_VALUE(x,y) {int _t=x;y=x;x=_t;}

#define STRLEN(a,i) char *_z=a; for(i=0;*_z;i++,_z++);

#define PRINT_1D_ARRAY(_x,_n)\
	printf("\n["); \
	for (int _i =0;_i<_n;_i++) 	{ \
		printf("%d, ",_x[_i]); \
	}	printf("]\n"); \

#define PRINT_2D_ARRAY(a,m,n) printf("\n\n");\
                              for(int i=0;i<m;i++) \
                               { for (int j=0;j<n;j++) \
							       printf("%-5d ",a[i][j]); \
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


#define CHAR_TO_DIGIT(x) ((x>='0' && x <='9')?(x-'0'):(x-'A'+10))
#define DIGIT_TO_CHAR(x) ((x<=9 && x>=0)?(x+'0'):(x-10 +'A'))


/* Binary Tree related Operation Here */
/*
bt_node * get_bt_node(int i);
void print_inorder(bt_node *r);

#define TREE_NODE bt_node
#define NEW_TREE_NODE(_i)  get_bt_node(int i)
#define PRINT_TREE(r) printf("\n[ ");print_inorder(r); printf(" ]\n");
*/


/* Stack related macro */
