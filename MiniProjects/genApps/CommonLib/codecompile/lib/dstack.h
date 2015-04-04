#include<stdio.h>
#define MAX_SIZE 100
//define stack class
class Stack{
    private:
        int list[MAX_SIZE];
        int top; //font and rere
    public:
        Stack() {
            top = -1;
        }    
        void push(int x){
            if (top ==MAX_SIZE) {
                 printf("Stack Full");
             }
             else{
               list[++top]=x;
             }
         }
         int pop() {
             if ( top<0) { 
                 printf("Stack Empty");
                 return 0;
            } 
             else{ 
                 return list[top--];
             }
         }
         int peek() {
             if ( top<0) { 
                 printf("Stack Empty");
                 return 0;
            } 
             else{ 
                 return list[top]; // get the top elements..
             }
         }
         int gettop(){   
              if (top<0){}
             else{ return list[top];}   
         }
         void print() {   
             printf("\n---------------------------------\n");
             printf("TOP -> ");
             for (int i=0;i<=top;i++)
                printf("%d ",list[i]);
             printf("\n---------------------------------\n");
             
         }
         bool isEmpty(){
             return top == -1;
         }                      
}; 
template <class T>
class TStack{
    private:
        T list[MAX_SIZE];
        int top; //font and rere
    public:
        TStack() {
            top = -1;
        }    
        void push(T x){
            if (top ==MAX_SIZE) {
                 printf("Stack Full");
             }
             else{
               list[++top]=x;
             }
         }
         T pop() {
             if ( top < 0) { 
                 printf("Stack Empty");
                 return 0;
            } 
             else{ 
                 return list[top--];
             }
         }
         int peek() {
             if ( top<0) { 
                 printf("Stack Empty");
                 return 0;
            } 
             else{ 
                 return list[top]; // get the top elements..
             }
         }
         T gettop(){   
              if (top<0){}
             else{ return list[top];}   
         }
         void print() {   
             printf("\n---------------------------------\n");
             printf("TOP -> ");
             for (int i=0;i<=top;i++)
                printf("%d ",list[i]);
             printf("\n---------------------------------\n");
             
         }
         bool isEmpty(){
             return top == -1;
         }                      
}; 