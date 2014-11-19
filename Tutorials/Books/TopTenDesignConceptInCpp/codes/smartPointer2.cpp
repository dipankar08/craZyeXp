/* Use Smart pointer */
#include<iostream>
#include<stdio.h>
using namespace std;
class Person
{
    int age;
    char* pName;
    public:
        Person(): pName(0),age(0)
        {
        }
        Person(char* pName, int age): pName(pName), age(age)
        {
        }
        ~Person()
        {
        }
        void Display()
        {
            printf("Name = %s Age = %d \n", pName, age);
        }
        void Shout()
        {
            printf("%s :Ooooooooooooooooo\n",pName);
        } 
};


template < typename T > class SP
{
    private:
    T*    pData; // Generic pointer to be stored
    public:
    SP(T* pValue) : pData(pValue)
    {
    }
    ~SP()
    {
        cout<<"Delete Done ";
        delete pData;
    }
    T& operator* ()
    {
        return *pData;
    }
    T* operator-> ()
    {
        return pData;
    }
};


int main()
{

    SP<Person> p(new Person("Scott", 25));
    p->Display();
    {
        SP<Person> q = p;
        q->Display();
        // Destructor of Q will be called here..
    }
    p->Display(); //*** Error in `./a.out': double free or corruption (fasttop): 0x09c62008 ***

    return 0;
}

