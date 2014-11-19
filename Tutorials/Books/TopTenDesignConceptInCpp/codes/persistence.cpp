// fstream::open / fstream::close
#include <fstream>      // std::fstream
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


class FileIO {

 private:
  fstream fs; 
 public:
  FileIO(){}
  FileIO(const char* path){
   fs.open (path, std::fstream::in | std::fstream::out | std::fstream::app );
  }
  int openFile(const char * path){
  fs.open (path, std::fstream::in | std::fstream::out | std::fstream::app );
  }
  int printFile(){
   if(fs.is_open())
   {   
      // get the starting position
      streampos start = fs.tellg();
      // go to the end
      fs.seekg(0, std::ios::end);
      // get the ending position
      streampos end = fs.tellg();

      // go back to the start
      fs.seekg(0, std::ios::beg);

      // create a vector to hold the data that
      // is resized to the total size of the file    
      std::vector<char> contents;
      contents.resize(static_cast<size_t>(end - start));

      // read it in
      fs.read(&contents[0], contents.size());

      // print it out (for clarity)
      cout <<"\n Full File:\n";
      for(int i=0; i < contents.size(); i++){
         cout << i;
      };  
      cout<<"\n File Read Done!!\n";
   }   
  }
  int appendFile(char*data,int len){

  }
  char * readAnyWhere( int offset, int len){

  }
  int writeAnywhere(int offset,int len,char*data){

  }
  int getSize(){
  int length;
  fs.seekg (0, ios::end);
  length = fs.tellg();
  fs.seekg (0, ios::beg);
  return length;
  }
  int closeFile(){

  }

};


int main()
{
  cout<<"hello World"<<endl;
   FileIO f;// = new FileIO();
  f.openFile("a.txt");

  return 0;
}
