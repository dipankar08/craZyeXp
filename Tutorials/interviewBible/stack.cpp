/*
  Name: Stack Program
  Copyright: Interview Bible
  Author: 
  Date: 07/03/14 22:58
  Description:  All linkedlist prgram in place
  
  Table of Contents:
      1. Convert Arry to list
      2.
      3.
      
*/

#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

/*******************************************************************************
* Problem :  Herper Struture Queue and Stack
* Input:
* Output:
* Algorithms:
*******************************************************************************/
#define MAX_SIZE 100

class Stack
{
    private:
        int list[MAX_SIZE];
        int top; /* This is the top */
    public:
        Stack()
        {
            top = -1;
        }    
        void push(int x){
            if (top == MAX_SIZE)
             {
                 printf("Stack Full");
             }
             else
             {
               list[++top]=x;
             }
         }
         int pop()
         {
             if ( top < 0)
             { 
                 printf("Stack Empty");
                 return 0;
            } 
             else
             { 
                 return list[top--];
             }
         }
         int gettop()
         {   
              if (top < 0){}
              else{ return list[top];}   
         }
         void show()
         {   
             printf("\n");
             for (int i=0;i<=top;i++)
                printf("%d,  ",list[i]);
             printf(" <<<<<<< TOP");
             
         }
         bool isEmpty()
         {
             return top == -1;
         }                      
};  


/*******************************************************************************
* Problem :  Push at bottom
* Input:
* Output:
* Algorithms: Pop a itme recusrivly until empty push the item in bbottom 
*******************************************************************************/

void pushBottom(Stack * s, int a) 
{
	if(s->isEmpty())
	{
		s->push(a);
		return;
	}
	int x = s->pop();
	pushBottom(s,a);
	s->push(x);
} 

    
/*******************************************************************************
* Problem :  Revresing a stack.
* Input:
* Output:
* Algorithms: Pop a itme, Revrse the stack, push the item in bbottom 
*******************************************************************************/

void reverse(Stack *s)
{
	if(s->isEmpty())
	  return;
	else
	{
		int a =s->pop();
		reverse(s);
		pushBottom(s,a);
	}
}






int main()
{
    printf("\n\n**************** Problems on STACK **************\n\n");
    
    //Stack test
    
    Stack s = Stack();
    s.push(1);
    s.push(2);
    s.push(3);
    
    Stack s1 = s;
    s1.show();
    printf("\nIsEmpty :%d",s.isEmpty());
    
	pushBottom(&s,10);
	s.show();
    
    printf("\nPOP:%d",s.pop());
    printf("\nPOP:%d",s.pop());
    printf("\nPOP:%d",s.pop());
    
	printf("\nIsEmpty:%d",s.isEmpty());


	reverse(&s);
	s.show();
    /*
    Stack s = Stack();
    Stack * s1 = &s;
    s1->push(1);
    s.show();
    */
    printf("\n\n****************** [ E N D ] *******************\n\n");
    getch();
}    

