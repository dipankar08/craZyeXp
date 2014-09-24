#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

//TODO
class BOARD{
    private:
        int max_x;
        int max_y;
        int ** cod_ptr;
        bool is_opt;
        bool has_circle;
    public:
        BOARD(){}
        void init(int x, int y, int** ptr)
        {
            max_x = x;
            max_y = y;
            cod_ptr = (int**)calloc(max_x, sizeof(int *));
            for(int ii = 0; ii < max_x; ii++) { 
              cod_ptr[ii] = (int*)calloc(max_y, sizeof(int));
            }
            
            for(int i=0; i< max_x;i++)
              for(int j=0; j< max_y;j++)
                cod_ptr[i][j]= (int)(*((ptr+i*max_x) + j));//ptr[i][j];
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
};

char * run(int , int , int ** matrix);

#define MAX_X 50
#define MAX_Y 50

