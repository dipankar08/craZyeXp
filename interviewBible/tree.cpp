/*
  Name: Array Program
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



typedef struct node{
    int val;
    struct node * left;
    struct node * right;
}node ;  

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
* Problem :  Basic Tree Algorithms
* Input:
* Output:
* Algorithms:
*******************************************************************************/

node * getNode(int val)
{ 
    node * n =(node *) malloc(sizeof(node));
    n->val =val;
    n->left = NULL;
    n->right = NULL;
    return n;
}

node * sampleTree1()
{
    node *n1,*n2,*n3,*n4,*n5,*n6,*n7;
    n1=getNode(1);
    n2=getNode(2);
    n3=getNode(3);
    n4=getNode(4);
    n5=getNode(5);
    n6=getNode(6);
    n7=getNode(7);
    n1->left=n2;n1->right=n3;
    n2->left=n4;n2->right=n5;
    n3->left=n6;n3->right=n7;
    return n1;
}

// this is BST
node * sampleTree2()
{
    node *n1,*n2,*n3,*n4,*n5,*n6,*n7;
    n1=getNode(50);
    n2=getNode(30);
    n3=getNode(80);
    n4=getNode(20);
    n5=getNode(40);
    n6=getNode(60);
    n7=getNode(90);
    n1->left=n2;n1->right=n3;
    n2->left=n4;n2->right=n5;
    n3->left=n6;n3->right=n7;
    return n1;
}

void inorder(node*r)
{   
    if (r)
    {
        inorder(r->left);
        printf("%d::",r->val);
        inorder(r->right);
    }    
    
}   


int getheight(node *r)
{
    if (!r) return 0;
    else
    {
        return getheight(r->left)>getheight(r->right) ?getheight(r->left)+1: getheight(r->right) +1;
    }    
}         

/*******************************************************************************
* Problem :  label Wise Traversal with Queue.
* Input:
* Output:
* Algorithms:
*******************************************************************************/

void labelTraversal(node *r)
{
    printf("\n");
    Queue q= Queue();
    if (!r)
      return;
    q.enq(r);
    while(! q.isEmpty())
    {
        node *x =(node*)q.deq();
        printf("%d:",x->val);
        if (x->left) q.enq(x->left);
        if (x->right) q.enq(x->right);
    }    
} 


/*******************************************************************************
* Problem :  Prity Print label Wise Traversal with Queue.
* Input:
* Output:
* Algorithms: Not Working.
*******************************************************************************/

void pp(node *r)
{   
    printf("\n");
    Queue q= Queue();
    if (!r)
      return;
    q.enq(r);
    int t =10;q.enq(&t);
    int level =0;
    printf("level:%d\n",level);
    while(! q.isEmpty())
    {   
        void *t =q.deq();
        if( *(int*)t == 10)
        {
            q.enq(&t);
            level++;
            printf("level:%d\n",level);
            continue;
        }    
        node *x =(node*)t;
        printf("%d:",x->val);
        if (x->left) q.enq(x->left);
        if (x->right) q.enq(x->right);
    }    
} 

/*******************************************************************************
* Problem :  ZIG Zag Print : 
* Input: Sample1
* Output: 7-6-5-4-3-2-1
* Algorithms: Using Stack and Queue
*******************************************************************************/
void printZipZagBtmUp(node *r)
{
    Queue q = Queue();
    Stack s =Stack();
    
    q.enq(r);
    
    while(!q.isEmpty())
    {
      node *t = (node*)(q.deq());
      s.push(t);
      if(t->left) q.enq(t->left);
      if (t->right) q.enq(t->right);  
    }
    while(!s.isEmpty())
    {
        printf("%d",((node *)s.pop())->val);
    }       
          
}    


/*******************************************************************************
* Problem :  ZIG Zag Print : 
* Input: Sample1
* Output: 1-3-2-4-5-6-7
* Algorithms: Using Two Stack
*******************************************************************************/

void printZigzagTopDown(node *r)
{
    int Left2Right=1;
    Stack s1 =Stack();
    Stack s2 = Stack();
    s1.push(r);
    
    while(!s1.isEmpty())
    {
        while(!s1.isEmpty())
        {
            node * t= (node*)s1.pop();
            printf("%d",t->val);
            
            if (Left2Right)
            {
                if(t->left) s2.push(t->left);
                if(t->right) s2.push(t->right);
            }
            else
            {
                if(t->right) s2.push(t->right);
                if(t->left) s2.push(t->left);
            }    
        }
        if(!s2.isEmpty())
        {
            Left2Right= ! Left2Right;
            Stack s =s1;s1=s2;s2=s;
        }
    }            
}    

/*******************************************************************************
* Problem :  Lavel having maxuimum Sum
* Input: Sample1
* Output: 1-3-2-4-5-6-7
* Algorithms: Using Two Stack
*******************************************************************************/

void maxsumlevel(node*r)
{
    Queue q =Queue();
    int t =10;
    q.enq(r);
    q.enq(&t); // This is an implementaion of $
    int level =0,cur_sum =0,max_sum =0; 

    while(!q.isEmpty())
    {   
        void * x = q.deq();
        
        if( *(int*)x == 10)
        {
            if (cur_sum >max_sum){ max_sum=cur_sum; cur_sum =0;}
            level++;
            if (*(int *)q.gettop() !=10) // This is important as if there is no entry we shoud not put $
               q.enq(&t);
        }
        else
        {   node *y = (node*)x;
            cur_sum +=y->val;
            if (y->left) q.enq(y->left);
            if(y->right) q.enq(y->right);
        }    
            
    }
    printf("\n Max Sum: %d",max_sum);
}
    

/*******************************************************************************
* Problem :  Print All Root to leaf path
* Input: Sample1
* Output: 
* Algorithms: Using Two Stack
*******************************************************************************/

void printallpath(node *r,int *path,int count)
{
    if (!(r->left) && !(r->right))
    { 
        path[count++] = r->val;
        for (int i=0;i<count;i++){ printf("%d->",path[i]);} printf("\n");
    }
    else
    {
        path[count++] = r->val;
        printallpath(r->left,path,count);
        printallpath(r->right,path,count);
    }        
}    


/*******************************************************************************
* Problem :  Print path having path sum S
* Input: Sample1
* Output: 
* Algorithms: Using Two Stack
*******************************************************************************/

void printallpathSum(node *r,int *path,int count,int S)
{
    if (!(r->left) && !(r->right) && S - r->val == 0)
    { 
        path[count++] = r->val;
        for (int i=0;i<count;i++){ printf("%d->",path[i]);} printf("\n");
    }
    else
    {
        path[count++] = r->val;
        printallpathSum(r->left,path,count,S - r->val);
        printallpathSum(r->right,path,count,S - r->val);
    }        
}    


/*******************************************************************************
* Problem :  Print all Ansistor
* Input: Sample1
* Output: 
* Algorithms: Using Two Stack
*******************************************************************************/

bool printAllAnt(node *r,int k)
{
    if (!r)
      return false;
    if (r->val == k || printAllAnt(r->left,k) || printAllAnt(r->right,k))
    {
        printf("%d-",r->val);
        return true;
    }
    return false;
}    


/*******************************************************************************
* Problem :  LCA of a BST
* Input: 
* Output: 
* Algorithms: Using Two Stack
*******************************************************************************/

void LCAofBST(node *r,int k1,int k2)
{
    if (r)
    {
        if ((k1 < r->val && k2 > r->val) ||
           (k1> r->val && k2 <r->val)|| k1 == r->val || k2 ==r->val)
         {  printf("LCA is %d",r->val);
           return;
         }    
        if (k1 < r->val) LCAofBST(r->left,k1,k2);
        else {
            LCAofBST(r->right,k1,k2);
            }
    }    
}    

/*******************************************************************************
* Problem :  Range Serach in BST
* Input: 
* Output: 
* Algorithms: Using Two Stack
*******************************************************************************/

void findRange(node *r,int k1,int k2)
{
    if (r)
    {
        if (r->val >=k1 && r->val <=k2)
        {
            printf("%d-",r->val);
        } 
        if (r->val >k2)
           findRange(r->left,k1,k2);
        else if (r->val <k1)
           findRange(r->right,k1,k2);
        else
        {
            findRange(r->left,k1,k2);
            findRange(r->right,k1,k2);
        }    
    }    
}
    
/*******************************************************************************
* Problem :  K-th Smallest Element in a Binary tree.(BST)
* Input: 
* Output: 
* Algorithms: Inorder Travresal
*******************************************************************************/

void kthSmallest(node *r, int k)
{
    static int i =0;
    if (r)
    {
        kthSmallest(r->left,k);
        i ++;
        if(i ==k)
         printf("kth Smallest is %d",r->val);
        kthSmallest(r->right,k); 
    }    
}    

/*******************************************************************************
* Problem :  Print all nodes that are at distance k from a leaf node
* Input: 
* Output: 
* Algorithms: Inorder Travresal
*******************************************************************************/
void kdistfromleaf(node *r,int *path,int count,int k)
{
    if (!(r->left) && !(r->right))
    { 
        path[count++] = r->val;
        if (count > k)
          printf("%d-",path[count-1-k]); //count -1 is Zero Distance
         
    }
    else
    {
        path[count++] = r->val;
        kdistfromleaf(r->left,path,count,k);
        kdistfromleaf(r->right,path,count,k);
    }        
}    


/*******************************************************************************
* Problem : Print all nodes that don’t have sibling
* Input: 
* Output: 
* Algorithms: Inorder Travresal
*******************************************************************************/

void nosibling(node *r)
{
    if(r)
    {
        if (r->left ==NULL && r->right!= NULL)
        {
            printf("%d has no sibling.\n",r->right->val);
            nosibling(r->right);
        }
        else if (r->left !=NULL && r->right== NULL)
        {
            printf("%d has no sibling.\n",r->left->val);
            nosibling(r->left);
        }
        else
        {
            nosibling(r->right);nosibling(r->left);
        }        
    }    
}    


/*******************************************************************************
* Problem : Add all greater values to every node in a given BST
* Input: 
* Output: 
* Algorithms: 
*******************************************************************************/

void geaterSum(node *r, int *sum)
{
    if(r)
    {
        geaterSum(r->right,sum);
        r->val=r->val+*sum;
        geaterSum(r->left,sum);
        *sum =*sum+r->val;
    }
    else
    {
        *sum =0;
    }        
}

/*******************************************************************************
* Problem : Sum of All node in that BST ( Recursive)
* Input: 
* Output: 
* Algorithms: 1. Using staic Variable
                2. Uisng Passing pointer varuaibel
*******************************************************************************/

void allSum1(node *r,int *sum)
{
    if (r)
    {
        int sum1 =0;
        int sum2 =0;
        allSum1(r->left,&sum1);
        allSum1(r->right,&sum2);
        *sum = sum1 + sum2 + r->val;
    }
    else
    {
    *sum =0;
    }       
}

int allSum2(node *r)
{
    static int sum =0;
    if(r)
    {
        sum +=r->val;
        allSum2(r->left);
        allSum2(r->right);
    }
    return sum;   
}        


/*******************************************************************************
* Problem : is BST ? We are assing min and max same iteration....
* Input: 
* Output: 
* Algorithms: 
*******************************************************************************/

bool isBST(node *r, int *min,int *max)
{
    if(!r->left &&!r->right)
    {
        *min = r->val;
        *max = r->val;
        return true;
    }
    else
    { 
        int min1,min2,max1,max2,ret1,ret2;
        ret1 = isBST(r->left,&min1,&max1);
        ret2 = isBST(r->right,&min2,&max2);
        
        *min = min1>min2 ? min2 : min1;
        *min = *min > r->val ? r->val : *min;
        
        *max = max1>max2 ? max1 : max2;
        *max = *max > r->val ? *max : r->val;
                
        if (ret1 && ret2 && (r->val > max1 && r->val < min2))
           return true;
        else
           return false;     
    }        
}

/*******************************************************************************
* Problem : Making BST from Array
* Input: 
* Output: 
* Algorithms: 
*******************************************************************************/    
node * arry2bst(int *arr,int start,int end)
{
    if (start > end)
      return NULL;
    if (start==end)
    {
        return getNode(arr[start]);
    }
    else
    {
        int mid = start+(end-start)/2;
        node *nw = getNode(arr[mid]);
        nw->left =arry2bst(arr,start,mid-1);
        nw->right =arry2bst(arr,mid+1,end);
        return nw;        
    }    
}    

/*******************************************************************************
* Problem : Difference between sums of odd level and even level nodes of a Binary Tree
* Input: 
* Output: 
* Algorithms: 
*******************************************************************************/ 
int diff(node *r)
{
    if(r)
    {
        return r->val - (diff(r->left) + diff(r->right));
    }
    else
      return 0;    
}    
/*******************************************************************************
* Problem : Find distance between two given keys of a Binary Tree.
* Input: 
* Output: 
* Algorithms: Dist(n1, n2) = Dist(root, n1) + Dist(root, n2) - 2*Dist(root, lca) 
*******************************************************************************/ 


 

int main()
{
    printf("\n\n**************** Problems on TREE **************\n\n");
    
    //Queue test
    /*
    Queue q = Queue();
    q.enq(1);q.enq(2);q.enq(3);
    q.show();
    printf("\n%d\n",q.isEmpty());
    printf("\n%d\n",q.deq());
    printf("\n%d\n",q.deq());
    printf("\n%d\n",q.deq());
    printf("\n%d\n",q.isEmpty());
    */
    
    node *n1=sampleTree1();
    

    //inorder(n1);
    //printf("%d\n",getheight(n1));
    //labelTraversal(n1);
    //printZipZagBtmUp(n1);
    //intZigzagTopDown(n1);
    //maxsumlevel(n1);
    
    //int t[100];
    //printallpath(n1,t,0);
    
    int t[100];
    //printallpathSum(n1,t,0,7);
    
    //printAllAnt(n1,7);
    
    n1 = sampleTree2();
    //inorder(n1);
    //LCAofBST(n1,20,90);
    //findRange(n1,60,90);
    //kthSmallest(n1,3);
    // kdistfromleaf(n1,t,0,2);
    int sum =0;
    //allSum1(n1,&sum);
    //printf("%d",allSum2(n1));
    //inorder(n1);
    //geaterSum(n1,&sum);
    //inorder(n1);
    //int min,max;
    //printf("is BST :%d , ",isBST(n1,&min,&max));
    //printf("Max: %d;min:%d",max,min);
    
    //int str[]={1,2,3,4,5,6,7};
    //node * n = arry2bst(str,0,6);
    //inorder(n);
    
    printf("DIFF : %d",diff(n1));
    
    printf("\n\n****************** [ E N D ] *******************\n\n");
    getch();
}    

