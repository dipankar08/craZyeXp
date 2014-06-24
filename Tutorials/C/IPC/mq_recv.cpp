/* Message Receiver */
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <iostream>
#include <string.h>
#include <stdlib.h>
using namespace std;

#define MAXSIZE     128

struct MSG
{
    long    mtype;
    char    mtext[MAXSIZE];
};

int main()
{
    int msqid;
    int msgflg = IPC_CREAT | 0666;
    int count = 0;
    /* Getting message Queue */
    key_t  key = 1234;
    if ((msqid = msgget(key, msgflg )) < 0)   //Get the message queue ID for the given key
    {
      cout <<"Eroor while getting Quie ID"<<endl;
    }
    while(1){
      cout << "Getting messages "<<count<<endl;count ++;
      /* getting Message */
      MSG  rcvbuffer;
      if (msgrcv(msqid, &rcvbuffer, MAXSIZE, 1, 0) < 0)
      { cout <<"ERROR"<<endl;
      }
      else
      {
        cout <<"Message is "<< rcvbuffer.mtext<<endl;
      }
    sleep(1);
  }
}

// SEE the message by ipcs -q
//  RUn : g++ mq_recv.cpp -lpthread && ./a.out
