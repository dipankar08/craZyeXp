#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;
/* This is a Board State */
class BOARD{
    private:
        int max_x;
        int max_y;
		int * raw_data;     	/*List of raw data */
		int raw_data_len;		/*length */
        int ** cod_ptr;			/*Define the matrix*/
        bool is_opt;			/* IS OPTIMIZE BOARD */
        bool has_circle;		/* iT HAS A CIRCLE OR NOT */
    public:
        BOARD(){}
        void init(int x, int y, int* ptr, int len)
        {
            max_x = x;
            max_y = y;
			raw_data_len=len;
			raw_data = (int*)calloc(raw_data_len, sizeof(int));
			for(int i=0;i<raw_data_len;i++)
			   raw_data[i] = *(ptr+i);
			
            cod_ptr = (int**)calloc(max_x, sizeof(int *));
            for(int ii = 0; ii < max_x; ii++) { 
              cod_ptr[ii] = (int*)calloc(max_y, sizeof(int));
            }      
			
		 for(int i=0;i< raw_data_len ;i++)
           cod_ptr[raw_data[i]%max_x][raw_data[i]/max_x] = 1;
		   
        }
        void print()
        {
            cout<<"Printing Matrix:\n";
            for(int i=0; i< max_x;i++)
            { for(int j=0; j<max_y;j++)
                { printf("%d ",cod_ptr[i][j]);}     
               printf("\n");  
            }  
        }   

        int getX(){return max_x;}
        int getY(){ return max_y;}
		int getCount(){ return raw_data_len;}
		int * getRawInputSeq() {return raw_data; }		
};

char * run(int , int , int ** matrix);

#define MAX_X 50
#define MAX_Y 50

