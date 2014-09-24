#include<iostream.h>
#include<conio.h>
#include<stdio.h>
using namespace std;

#define MAX_X 50
#define MAX_Y 50

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
int main()
{
    cout<<"hello test\n";

   // Initilize the arry.. 
   int matrix[MAX_X][MAX_Y];
   // Constract Matrix 
   for(int i=0;i<  MAX_X;i++)
     for(int j=0;j< MAX_Y;j++)
       matrix[i][j]=0;
       
   int codlist[]=   {1019, 1069, 1119, 1169, 1219, 1269, 1319, 1369, 1419, 1469, 1519, 1569, 1619, 1670, 1720, 1770, 1820, 1821, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889, 1890, 1841, 1791, 1792, 1742, 1693, 1643, 1644, 1594, 1544, 1494, 1444, 1394, 1344, 1294, 1244, 1194, 1144, 1094, 1044, 1043, 992, 942, 941, 890, 839, 789, 788, 738, 737, 736, 686, 685, 684, 634, 633, 632, 631, 630, 629, 628, 627, 626, 625, 624, 673, 723, 773, 823, 873, 923, 973, 1023, 1073, 1123, 1173, 1223, 1222, 1221, 1220, 1219, 1218, 1217, 1216, 1215, 1214, 1213, 1212, 1211, 1210, 1209};
   for(int i=0;i< sizeof(codlist)/sizeof(codlist[0]) ;i++)
       matrix[codlist[i]%MAX_X][codlist[i]/MAX_X]=1;
   
   /* crete a board and access it */   
   BOARD *b = new BOARD();
   b->init(MAX_X,MAX_Y,(int**)matrix);
   b->print();   
   


    getch();
    return 0;
}
