#include<fstream>
#include<iostream>

using namespace std;
class Box{
 int i,j;
 public:
  void set(int i,int j){this->i = i; this->j = j;}
  void show() { cout <<"Box i,j: <"<<i<<" , "<<j<<"> \n";}
};

int main()
{
/* Test Simple input and output */
ofstream fout;
fout.open("test_file.txt");
fout << "hello dipankar"<<endl;
fout.close();

ifstream fin;
fin.open("test_file.txt");
char data[100];

fin >> data;cout <<data; // Space terminated.
fin >> data;cout <<data;
fin.seekg(0);
fin.getline(data,100); cout <<data;
fin.close();

fstream file;
file.open("test_file.txt",ios::in | ios::out | ios::trunc);
/* Objects save restore */
  Box b[10];
  for (int i=0;i<10;i++)
   { b[i].set(i,i);b[i].show();}

  for (int i=0;i<10;i++)
   file.write((char*)( &b[i]),sizeof(b[i]));


  for(int i =0;i<10;i++)
   { file.read((char*)( &b[i] ), sizeof(b[i]));
     b[i].show();
   }
 
}
