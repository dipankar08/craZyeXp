#include<iostream>
#include<pthread.h>
using namespace std;

/* This is a Message Structure */
struct MSG{
	int tid;
	char *info;
        float money;
};

/* Global Shared data and thread lock */
float total_money;
pthread_mutex_t lock;

/* Thread handaling Code */
void * print(void * m)
{
  MSG *msg = ( MSG* ) m;
  /* Now the share and print will be inside lock and unlock */
  pthread_mutex_lock(&lock);
  cout<<"Recined MesageLike ID:"<<msg->tid<<" info: "<<msg->info<<endl;
  total_money += msg->money;
  cout <<" Now Total Price :" <<total_money<<endl;
  pthread_mutex_unlock(&lock);
  sleep(1);
  pthread_exit(NULL);
}

/* Start Main Program */
int main()
{
  pthread_t t[5];
  int ret;
  
  /* Build 5 message */
  MSG m[5];
  for (int i=0;i<5;i++)
  {
    m[i].tid =(i+1);
    m[i].info ="Hello Dipankar";
    m[i].money = 10.0 *(i+1);
  }
  
  /* Inililize shared data and lock */
  total_money =0.0;
  pthread_mutex_init(&lock,NULL);

  cout <<"Main(): Start.."<<endl;
  for (int i=0;i<5;i++)
  {
    /* Creating Thread */ 
    ret = pthread_create(&t[i],NULL,print,(void*)&m[i]);
    if(ret)
    {
      cout << "Not able to create thread"<<ret<<endl;
    }
  }
  /*  Wait for all thread to join first */
  for (int i=0;i<5;i++)
  {
    ret = pthread_join(t[i],NULL);
    if(ret)
    {
      cout <<"Error is Thread Join"<<endl;
    } 
  }
  cout <<"Main() : Exit "<<endl;
  pthread_exit(NULL);

}

//g++ thread1.cpp -lpthread && ./a.out  
