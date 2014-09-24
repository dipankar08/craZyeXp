
#include "DrawBlock.h"
#include <cstdlib> 


char* run(int x, int y, int ** matrix){

  BOARD *b = new BOARD();
   b->init(x,y,(int**)matrix);
   b->print();
   return (char*) "Abc";
}    

int main ( int argc, char *argv[] )
{
    cout<<"hello test:\n"<<argc;

   // Initilize the arry.. 
   int matrix[MAX_X][MAX_Y];
   // Constract Matrix 
   for(int i=0;i<  MAX_X;i++)
     for(int j=0;j< MAX_Y;j++)
       matrix[i][j]=0;
#if 0       
   int codlist[]=   {1019, 1069, 1119, 1169, 1219, 1269, 1319, 1369, 1419, 1469, 1519, 1569, 1619, 1670, 1720, 1770, 1820, 1821, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889, 1890, 1841, 1791, 1792, 1742, 1693, 1643, 1644, 1594, 1544, 1494, 1444, 1394, 1344, 1294, 1244, 1194, 1144, 1094, 1044, 1043, 992, 942, 941, 890, 839, 789, 788, 738, 737, 736, 686, 685, 684, 634, 633, 632, 631, 630, 629, 628, 627, 626, 625, 624, 673, 723, 773, 823, 873, 923, 973, 1023, 1073, 1123, 1173, 1223, 1222, 1221, 1220, 1219, 1218, 1217, 1216, 1215, 1214, 1213, 1212, 1211, 1210, 1209};
#endif
int len = argc -1;
int *codlist =(int*) calloc(sizeof(int), (argc-1));

for(int i=1;i<argc;i++)
   codlist[i-1]= atoi(argv[i]);

for(int i=0;i<len;i++)
   printf("%d--",codlist[i]);

   for(int i=0;i< len ;i++)
       matrix[codlist[i]%MAX_X][codlist[i]/MAX_X]=1;
   
   /* crete a board and access it */   
   BOARD *b = new BOARD();
   b->init(MAX_X,MAX_Y,(int**)matrix);
   b->print();   
    return 0;
}

