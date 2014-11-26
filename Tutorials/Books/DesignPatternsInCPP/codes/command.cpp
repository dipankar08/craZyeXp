/********************************************
* Singleton1.cpp: Command Pattern
* Author :Dipankar Dutta.
* Description /Steps.
*
* Step1: We have 3 things here: Command Reciver and Invoker.
* Icommand have a receiver(Basicay a handaler ) and a execuet()
* Crete comand basciccaly Implement this execute.
* A Concrete recivber implement action() what to do.
* InVoker basically has a comamnd , we can set /unset the comamnd and invoke it ..
*
* For each command we have Implement conand and Reciver only
*
* *********************************************/
#include <iostream>
#include <cstdarg>

//1. Define a Receiver and Command here .....................
class IReceiver
{
public:
    virtual void Action(int n,...) =0; //Actions take variable length argumnets
};
class ICommand
{
public:
    IReceiver * _r; // We define it here as a comand must have a reciver..
    ICommand(IReceiver * r){
        _r =r;
    }
    virtual void Execute() = 0;
};

//2. Implement your Command and receiver here < No Peremeters>......................
class Command: public ICommand{
private:
    char* param;

public:
    void setParam(char *p){param= p;}
    char * getParam(){return param;}
    Command(IReceiver * r):ICommand(r){
        //do nothing..
    }
    void Execute(){
     _r->Action(0); // Not passing any data
    }
};

class Receiver:public IReceiver
{
public:
    void Action(int n,...)
    {
        std::cout << "Command received" << std::endl;
    }
};


//2.A Implement Another Command <Parameters>..............................
class AddCommand: public ICommand{
private:
    int a,b;
public:
    void setParam(int a,int b){this->a=a,this->b=b;}
    AddCommand(IReceiver * r):ICommand(r){
        //do nothing..
    }
    void Execute(){
        _r->Action(2, a,b);
    }
};

class AddReceiver:public IReceiver
{
public:
    void Action(int n, ...)
    {   int sum =0;
        va_list arguments;                     // A place to store the list of arguments
        va_start ( arguments, n );
        for ( int x = 0; x < n; x++ )        // Loop until all numbers are added
            sum += va_arg ( arguments, int ); // Adds the next value in argument list to sum.
        va_end ( arguments );

        std::cout << "Adding two number:"<<sum << std::endl;
    }
};

// 3. We have a Invoker Which basically set and Rest all these command ..
class Invoker{
    ICommand *m_command;
public:
    Invoker(ICommand *cmd = 0) : m_command(cmd){
    }
    void SetCommand(ICommand *cmd){
        m_command = cmd;
    }
    void Invoke(){
        if (0 != m_command){
            m_command->Execute();
        }
    }
};
/////////////////////////////////////////////////////////////////////////
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    IReceiver *r = new Receiver();
    ICommand *cmd = new Command(r);
    Invoker i;
    i.SetCommand(cmd);
    AddCommand * add =  new AddCommand(new AddReceiver());
    add->setParam(1,2);
    i.SetCommand(add);
    i.Invoke();
    return 0;
}
