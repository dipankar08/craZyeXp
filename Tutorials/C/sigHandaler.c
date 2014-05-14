/************************************
This program is a demo of sighandaler in C

Author : DIpankar Dutta

1. What is a signal? Signals are software interrupts.
- A robust program need to handle signals. This is because signals are a way to deliver asynchronous events to the application.
- A user hitting ctrl+c, a process sending a signal to kill another process etc are all such cases where a process needs to do signal handling.

2.Linux Signals

In Linux, every signal has a name that begins with characters SIG. For example :

A SIGINT signal that is generated when a user presses ctrl+c. This is the way to terminate programs from terminal.
A SIGALRM  is generated when the timer set by alarm function goes off.
A SIGABRT signal is generated when a process calls the abort function.

3. When the signal occurs, the process has to tell the kernel what to do with itThe signal can be ignored.
The signal can be caught.
Let the default action apply.

Catching a Signal
================
Two things
a. void <signal handler func name> (int sig)
b  void (*signal(int signo, void (*func )(int)))(int); -> kernel reg
 
**************************************/

#include<stdio.h>
#include<signal.h>
#include<unistd.h>

void sig_handler(int signo)
{
  if (signo == SIGINT) //CTRL+C
    printf("received SIGINT\n");
  else if (signo == SIGUSR1) //kill -USR1 5225
        printf("received SIGUSR1\n");
  else if (signo == SIGKILL) // cant
        printf("received SIGKILL\n");
  else if (signo == SIGSTOP) // cant't
        printf("received SIGSTOP\n");
}

int main(void)
{ 
  // b. registration here
  if (signal(SIGINT, sig_handler) == SIG_ERR)
    printf("\ncan't catch SIGINT\n");
  if (signal(SIGUSR1, sig_handler) == SIG_ERR)
        printf("\ncan't catch SIGUSR1\n");
  if (signal(SIGKILL, sig_handler) == SIG_ERR)
        printf("\ncan't catch SIGKILL\n");
  if (signal(SIGSTOP, sig_handler) == SIG_ERR)
        printf("\ncan't catch SIGSTOP\n");
  // A long long wait so that we can easily issue a signal to this process
  while(1) 
    sleep(1);
  return 0;
}


