#include <iostream>
#include <vector>
using namespace std;
#define printVec(v) cout <<"\nVector ("<<v.size()<<")::"; for (int i=0;i<v.size();i++)  cout << v[i]<<" ";
vector<string> getAllStr(int len,int s_ch,int e_ch)
{
  vector<string> all ;
  vector<string> now ; 
  for (int i =s_ch; i<=e_ch;i++)
    now.push_back(string(1,char(i)));
  all.insert(all.end(), now.begin(), now.end());
  
  for (int ii =1;ii<len;ii++)
  { 
    vector<string> temp ;
    for (int j =0; j<now.size();j++)
        for (int i =s_ch; i<=e_ch;i++)
          temp.push_back(now[j]+string(1,char(i)));
    //printVec(temp);
    all.insert(all.end(), temp.begin(), temp.end());
    now =temp;
    temp.clear();
  }
  //all.insert(all.end(), now.begin(), now.end());
  // printVec(all);
  cout<<"size"<<all.size();
}


int main()
{
   cout << "Hello World";
   getAllStr(8,'a','z');
   return 0;
}
