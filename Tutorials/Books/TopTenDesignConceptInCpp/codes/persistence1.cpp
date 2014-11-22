// fstream::open / fstream::close
#include <fstream>      // std::fstream
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <string.h>
using namespace std;


class FileIO
{

  private:
    fstream fs;
    char *name;
  public:
    FileIO() {}
    FileIO(const char* path)
    {
      openFile(path);
    }
    int openFile(const char * path)
    {
      name = new char(100);
      memset(name, '0', sizeof(name));
      strcpy(name, path);
      name = (char*)name;
      fs.open (path, std::fstream::in | std::fstream::out| std::fstream::app | std::fstream::binary );
    }
    int printFile()
    {
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
        cout <<"\n Full File:"<<getSize()<<":<";
        for(int i=0; i < contents.size(); i++)
        {
          cout << contents[i];
        };
        cout<<">\n";
      }
    }
    int appendFile(char*data,int len)
    {
      if(fs.is_open())
      {
        fs.seekp(0, std::ios::end);
        fs.write(data,len);
        return 0;
      }
      return -1;
    }
    int readAnywhere( int offset, int len, char *data)
    {
    if(fs.is_open()){
     fs.seekg (offset, ios::beg);
     fs.read (data,len);
     data[len+1]=0;
     return 0;
    }
    return -1;
    }

    int writeAnywhere(int offset,int len,char*data)
    {
     if(fs.is_open()){
      fs.seekp (offset, ios::beg);
      fs.write(data,len);
      fs.seekp (0, ios::beg);
      return 0;
     }
     return -1;
    }
    int getSize()
    {
      int length;
      fs.seekg (0, ios::end);
      length = fs.tellg();
      fs.seekg (0, ios::beg);
      return length;
    }
    int closeFile()
    {

    }
    int clearFile(){
     if( remove( name ) != 0 )
        perror( "\nError deleting file" );
     else
        puts( "\nFile successfully deleted" );
    }

};


int main()
{
  cout<<"hello World"<<endl;
  FileIO f;// = new FileIO();
  f.openFile("a.txt");
  f.appendFile("012345678901234567890",20);
  cout << f.getSize();
  f.printFile();
  f.writeAnywhere(6,3,"ddd");
  //f.printFile();
  cout << f.getSize();
  f.printFile();

  char a[11];
  f.readAnywhere(5,10,a);
  cout<<a;

  f.clearFile();


  return 0;
}
