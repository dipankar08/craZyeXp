/* Message Sender */
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
      cout << "Genaring messages "<<count<<endl;count ++;
      /* Building Message */
      MSG  sbuf;
      sbuf.mtype = 1;
      strcpy(sbuf.mtext,"Hello World");
      /* Sending messages */
      size_t buflen = strlen(sbuf.mtext) + 1 ;
      if (msgsnd(msqid, &sbuf, buflen, IPC_NOWAIT) < 0){
        cout <<" Not able to send msg \n";
      }
    else
      cout << "Message Sent\n";
    sleep(2);
  }
}

// SEE the message by ipcs -q
//g++ mq_sender.cpp -lpthread && ./a.out
