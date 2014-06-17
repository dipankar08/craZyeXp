#include<iostream>
#include<pthread.h>
using namespace std;

/* This is a Share Buffer 
 We should use Lock to access these shareed varaible*/
#define B_SIZE 10
#define COMSUME_TIME 1
#define PROD_TIME 10
int buff[B_SIZE+1];
int cur_index = -1;


/* Global thread lock and Conditinal Lock*/
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t sig_consumer= PTHREAD_COND_INITIALIZER;
pthread_cond_t sig_producer= PTHREAD_COND_INITIALIZER;


/* Produces thread handaling Code */
void * producer(void * dummy)
{
  cout <<"Prod: Started.."<<endl;
  int item= 0;
  while(1)
  {   
    
    /* if no space in buff , Produce Wait */
    pthread_mutex_lock(&lock);
    if(cur_index == B_SIZE) 
        pthread_cond_wait(&sig_producer, &lock);
    pthread_mutex_unlock(&lock);
    /* Produce An Item and place it to buffer */
     item ++;
     sleep(PROD_TIME);
     cout <<"prod: Generate "<<item<<endl;
     
     /* Place the item in the buff */
     pthread_mutex_lock(&lock);
     cur_index++;
     buff[cur_index]=item;        
     pthread_mutex_unlock(&lock);
     /* Now Signal comsuper ..*/
     pthread_cond_signal(&sig_consumer);

  }
}

/* Consumer thread */
void * consumer(void * dummy)
{
  cout <<"Con: Started.."<<endl;
  while(1)
  {
     
     /* If No item Single Producer to Prouce Item and wait.. */
     pthread_mutex_lock(&lock);
     if(cur_index < 0)
       { 
          pthread_cond_signal(&sig_producer);
          pthread_cond_wait(&sig_consumer, &lock);
       }
     pthread_mutex_unlock(&lock);

     /* Now get the Item from buffer */
     pthread_mutex_lock(&lock);
     int item = buff[cur_index];cur_index--;
    /* Single Comsumer if it create some space */
     pthread_cond_signal(&sig_producer);
     pthread_mutex_unlock(&lock);

     /* Consume the item */
     sleep(COMSUME_TIME);
     cout <<"con: Consume "<<item<<endl;

  }
}

/* Start Main Program */
int main()
{
  pthread_t t[2];
  int ret;
  
  /* Inililize shared data and lock */
  pthread_mutex_init(&lock,NULL);

  /* Create consumer & producer threads. */
  if ((ret= pthread_create(&t[0], NULL, consumer, NULL)))
    cout<< "Error creating the consumer thread..\n"<<endl;

  if ((ret= pthread_create(&t[1], NULL, producer, NULL)))
    cout << "Error creating the producer thread..\n"<<endl;

  /* Wait for consumer/producer to exit. */
  for (int i= 0; i < 2; i ++)
    pthread_join(t[i], NULL);  
  
  cout <<"Main() : Exit "<<endl;
  pthread_exit(NULL);

}

//g++ thread2.cpp -lpthread && ./a.out  
