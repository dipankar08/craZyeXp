#include<stdio.h>
#define MAX_SIZE 100
//define Queue class
class Queue
{
    private:
        int list[MAX_SIZE];
        int f,r; //font and rere
    public:
        Queue() {
            f = -1;
            r = -1;
        }    
        void enq(int x){ //increnment rare 
            if (f ==MAX_SIZE) {
                 printf("Queue Full");
             }
             else {
                 list[++r] = x;
                 if( f == -1) {f++;}
             }
         }
         int deq(){  // increment front
             if ( f<0){ printf("Queue Empty");} // no ele             
             else if (f == r){ //one ele
                 int data= list[f];
                 f = r = -1;
                 return data;
             }    
             else {  // more than one elements
                 return list[f++];
             }
         }
         int peek() {   // get which one to be removed, but not actually removed it..
              if (f<0){}
             else{ return list[f];}   
         }
         void print() {   
             printf("\n<< ------------------<<---------------- <<\n");
             for (int i=f;i<=r;i++)
                printf(" %d ", list[i]);
             printf("\n<< ------------------<<---------------- <<\n");

         }
         bool isEmpty() {
             return f == -1;
         }                      
};  

template <class T>
class TQueue
{
    private:
        T list[MAX_SIZE];
        int f,r; //font and rere
    public:
        TQueue(){
            f = -1;
            r = -1;
        }    
        void enq(T x){ //increnment rare 
            if (f ==MAX_SIZE) {
                 printf("Queue Full");
             }
             else {
                 list[++r] = x;
                 if( f == -1) {f++;}
             }
         }
         T deq(){  // increment front
             if ( f<0){ printf("Queue Empty");} // no ele             
             else if (f == r){ //one ele
                 T data= list[f];
                 f = r = -1;
                 return data;
             }    
             else {  // more than one elements
                 return list[f++];
             }
         }
         T peek() {   // get which one to be removed, but not actually removed it..
              if (f<0){}
             else{ return list[f];}   
         }
         void print() {   
             printf("\n<< ------------------<<---------------- <<\n");
             for (int i=f;i<=r;i++)
                printf(" %d ", list[i]);
             printf("\n<< ------------------<<---------------- <<\n");

         }
         bool isEmpty() {
             return f == -1;
         }                      
};  
