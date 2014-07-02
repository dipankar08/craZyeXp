#include<iostream>
#include<csignal>
using namespace std;

void sighand(int no)
{
  cout <<" interrupt signal: "<<no<<"received\n";
}
int main()
{
  while(1){
   signal(SIGINT,sighand);
   signal(SIGSEGV,sighand);
   sleep(1);
   raise(SIGINT);
   raise(SIGSEGV);
  }
}
