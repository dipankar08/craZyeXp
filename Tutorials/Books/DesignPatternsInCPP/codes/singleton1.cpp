/********************************************
* Singleton1.cpp: Singleton Pattern Example ...
* Author :Dipankar Dutta.
* Description /Steps.
* Step 1: Define a Class where constractor is private
* Step 2: Have a getInstace () which return based on
*********************************************/
#include <iostream>
#include<pthread.h>

using namespace std;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
class Singleton
{
private:
    static Singleton *single;
    int id;
    Singleton(int id)
    {
        this->id =id;
    }
public:
    static Singleton* getInstance();
    void show();
    ~Singleton()
    {
        single = NULL;
        cout <<"Singleton Distroyed .."<<endl;
    }
};
/* These are the static varibale */
Singleton* Singleton::single = NULL;

Singleton* Singleton::getInstance()
{
    if(! single)
    {
        pthread_mutex_lock( &mutex );  // This is thread safe...single as it is a share object,,,
        if(! single)
          single = new Singleton(1);
        pthread_mutex_unlock( &mutex );
    }
    return single;

}

void Singleton::show()
{
    cout << "Id of this object is:"<<id << endl;
}

int main()
{
    //Creting a Singleton in a scope ..
    {
        Singleton *s1 = Singleton::getInstance();
        s1->show();
        delete s1;
    }
    Singleton *s1,*s2;
    s1 = Singleton::getInstance();
    s1->show();
    s2 = Singleton::getInstance();
    s2->show();
    return 0;
}
