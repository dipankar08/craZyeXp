/*
  Name: Stack and Queue Program( Book Covered )
  Copyright: Interview Bible
  Author: 
  Date: 07/03/14 22:58
  Description:  All Stack and Queue program in place
  
  Table of Contents:
      1. Convert Arry to list
      2.
      3.
      
*/


#include<stdio.h>
#include<conio.h>

/*******************************************************************************
* Problem :  Herper Struture Queue and Stack
* Input:
* Output:
* Algorithms:
*******************************************************************************/
#define MAX_SIZE 100
class Queue
{
    private:
        void * list[MAX_SIZE];
        int f,r; //font and rere
    public:
        Queue()
        {
            f = -1;
            r = -1;
        }    
        void enq(void * x){
            if (f ==MAX_SIZE)
             {
                 printf("Queue Full");
             }
             else
             {
                 list[++r] = x;
                 if( f == -1) {f++;}
             }
         }
         void * deq()
         {
             if ( f<0){ printf("Queue Empty");}
             
             else if (f == r)
             {
                 void * data= list[f];
                 f = r = -1;
                 return data;
             }    
             else
             { 
                 return list[f++];
             }
         }
         void * gettop()
         {   
              if (f<0){}
             else{ return list[f];}   
         }
         void show()
         {   
             printf("\nDelete <= ");
             for (int i=f;i<=r;i++)
                printf(" | %d ", (int*)list[i]);
             printf("Insert <= ");
             //printf("\n Font:%d,Rare:%d",f,r);
         }
         bool isEmpty()
         {
             return f == -1;
         }                      
};  

class Stack
{
    private:
        void * list[MAX_SIZE];
        int top; //font and rere
    public:
        Stack()
        {
            top = -1;
        }    
        void push(void * x){
            if (top ==MAX_SIZE)
             {
                 printf("Stack Full");
             }
             else
             {
               list[++top]=x;
             }
         }
         void * pop()
         {
             if ( top<0)
             { 
                 printf("Stack Empty");
                 return 0;
            } 
             else
             { 
                 return list[top--];
             }
         }
         void * gettop()
         {   
              if (top<0){}
             else{ return list[top];}   
         }
         void show()
         {   
             printf("\n");
             for (int i=0;i<=top;i++)
                printf("%d,  ",(int *)list[i]);
             printf(" <<<<<<< TOP");
             //printf("\n Font:%d,Rare:%d",f,r);
         }
         bool isEmpty()
         {
             return top == -1;
         }                      
};  
  

/*******************************************************************************
* Problem 1:  Impelment a Stack Class
* Input / Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem 2: Implement a Queue Class 
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 3: Reverse a Stack In-Place 
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Reverse a Stack Out-of place
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Find Minimum elemnt of a Stack in O(1)
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Sort a Stack Inplece With Recustion
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Insert an Element in botton of stack using std. operations
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Implment a Stack uisng Queue
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Implemnet a Queue using Stack
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Implment a 2 Stack in a Array
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Implemnt 3 Stacks in a Array.
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Implement N stack in a Array
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Using  n -stack and m number given <1,2,3..M>. How many permutation can be generated ?
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Implement thread safe version of stack ?
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Traversal a Tree using a Queue.
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Reverse a Queue using another Queue
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Split a Queue into two queue based on even and odd.
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Implement a DeQueue using two Stack ?
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Implemnet a Prority Queue using Matrix PQ[] and uisng two arry ?
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Implement a Qute eto get max in O(1)?
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Solve TOH using stack only.
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Mimic real life multi stack problem.
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Evalute prefix to postfix uisng Stack
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Convert Infix to postfix expression using Stack
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : How to implement Stack using Heap ? 
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : How to implement Queue using Heap?
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : How to use stack for Symbol balanace checking
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Infix evalusion in One pass
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Let's push 1,2,3,4,5,6,7 in the stack in order, find out how many way to do Push /pop operation to get a combinaation like,3,2,5,6,4,1.
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Doubling Array implemnationof stack, size increase in recusive way.
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Find Largest rectrangle histogram on common base line.
* Input / Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : Given a Sequence of Push and POP operation. Check the sequenec is valid or not !
* Input / Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem : 
* Input / Output:
* Algorithms:
*******************************************************************************/






int main()
{
    printf("**************** Problem of Array **************\n\n");
    
    
    
    printf("****************** [ E N D ] *******************\n\n");
    getch();
}    

