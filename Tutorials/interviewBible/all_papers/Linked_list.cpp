/*
  Name: Linked List Program[ Cover Boosk]
  Copyright: Interview bibal
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
struct node{
    int val;
    node * next;
};

/* getting a new node */
node * getNewNode(int val)
{
    node * n = (node *) malloc(sizeof(node));
    if (!n)
    {  printf("Not able to alocate memory\n");
      return NULL;
    }    
    n->next= NULL;    
    n->val = val;
    return n;
}    

/*******************************************************************************
* Problem 1: Create an list from an Arry and dispaly it
* Input:
* Output:
* Algorithms:
*******************************************************************************/
node * arary2List(int a[],int n)
{
    
    node *head=NULL;
    node *temp=NULL ;
    if( n >1 )
      {
          node *nw = getNewNode(a[0]);
          head =nw;
          temp = nw;
      }    
    for (int i=1;i<n;i++)
    {
        node *nw = getNewNode(a[i]);
        temp->next =nw;
        temp= nw;
    }    
    return head;
}    

/* Diaply List */
void displayList(node * head)
{
    node *temp = head;
    if (!head)
      printf("Ooops.. List is empty");
    while(temp)
    {
        printf("%d--",temp->val);
        temp=temp->next;
    }
    printf("\n");    
}    
/*******************************************************************************
* Problem 2: Insert and Deletion of a node in a list
* Input:
* Output:
* Algorithms:
*******************************************************************************/
/*Insertion In fromt */
node * addFront(node *head,int i)
{ 
    node *nw =getNewNode(i);
    nw->next =head;
    head = nw;
    return head; //  required
}

/*delete from Fromt */
node * delFront(node *h)
{
    if (!h)
      return NULL ;
    node *temp =h->next;
    free(h);
    h = temp;
    return temp;
}    

// Return void as head is not modified .
node * addLast(node *head,int i) // Not that h is a local varibale and it's increment doent effect head in caller
{   node *h =head;
    node * nw = getNewNode(i);
    if (!h)
      return nw;
    while(h->next !=NULL)
    { h = h->next;
    }
    h->next =nw;
    return head;    
}    

/* delete Last */
node * delLast(node *head)
{   
    node *h =head;
    if (!h) // no nodes
      return NULL;
    if (h->next==NULL) //One node
    { 
        free(h);
        return NULL;
    }
    while(h->next->next != NULL)
    {
        h = h->next;
    }        
    free(h->next);
    h->next= NULL;
    return head;    
}      
/*******************************************************************************
* Problem 3: Search in a list
* Input:
* Output:
* Algorithms:
*******************************************************************************/
void serachList(node *head,int i)
{
    while(head)
    {
        if(head->val==i){printf("%d Found\n",i);return;}
        head=head->next;
    }
    printf("%d Not Found\n",i);    
}    

/*******************************************************************************
* Problem 4: Copy a List
* Input:
* Output:
* Algorithms:
*******************************************************************************/
node * copyList(node *h)
{
    node *newh=NULL;
    node *end= NULL;
    if (!h)
       return NULL;
    // First Node setting head..
    node *nw = getNewNode(h->val);
    newh= end= nw;
    h= h->next;
    
    while(h)
    {
        node *nw = getNewNode(h->val);
        end->next =nw;end=nw;
        h= h->next;
    } 
    return newh;   
}     

/*******************************************************************************
* Problem 5: Delete a list
* Input:
* Output:
* Algorithms:
*******************************************************************************/
node * delList(node *h)
{
    if (!h)
       return NULL;
    delList(h->next);
    free(h);
    return NULL;
}    


/*******************************************************************************
* Problem 6: Sorted Insert in a linked list
* Input:
* Output:
* Algorithms:
*******************************************************************************/
node * shortedInsert(node *h,int i)
{
    node *nw =getNewNode(i);
    if (!h)
      return nw;
    //case 1: Least
    if( i <h->val)
    {
        nw->next=h;
        return nw;//Head Changes.
    }
    //case 2: In middle.
    node *temp1=h;
    node *temp2=h->next;
    while(temp2)
    {
        if(temp2->val >i)
        {
            temp1->next=nw;
            nw->next=temp2;
            return h;
        }
        temp1=temp2;
        temp2= temp2->next;
    }
    //Case 3: at end, for largest number
    temp1->next =nw;
    return h;        
        
}

/*******************************************************************************
* Problem 7: print Reverse a Linked list Recusrivly
* Input:
* Output:
* Algorithms:Revrese via recusion:
* - In Stack, link is not broken , unless we do it...
*******************************************************************************/
void reverseprint(node *h)
{
    if (!h)
      return;
    reverseprint(h->next);
    printf("%d<-",h->val);
}

    
/*******************************************************************************
* Problem 8: Reverse a Linked list Recusrivly
* Input:
* Output:
* Algorithms:Revrese via recusion:
* - In Stack, link is not broken , unless we do it...
*******************************************************************************/

node * reverse1(node *h)
{
    if (h->next==NULL)
      return h;
    node *ret =reverse1(h->next);
    h->next->next=h;
    h->next=NULL;
    return ret;
}
/*******************************************************************************
* Problem 9: Reverse a Linked list iteratively
* Input:
* Output:
* Algorithms:Revrese via Interation:
* Break list in two parts
* Until Second part is empty
* Delete the front of first part and add to the front of firat part
*******************************************************************************/

node * reverse2(node *h)
{
    if (!h)
    return NULL;
    //Breaking down two list
    node *temp1=h;
    node *temp2=h->next;
    temp1->next=NULL;
    
    while(temp2)
    {   node *temp3 =temp2->next; 
        temp2->next =temp1;
        temp1 = temp2;
        temp2= temp3;
    }
    return temp1;    
        
        
}        
/*******************************************************************************
* Problem 10: Revrese a Double Linked List
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 10: Find length of a linked list
* Input:
* Output:
* Algorithms:
*******************************************************************************/
int getLength(node *h)
{
    int i;
    for (i=0;h;h=h->next,i++);
    return i;
}

/*******************************************************************************
* Problem 11: Get MIdddle of a linked list uisng fast pointer and 
            find length even or ODD
* Input:
* Output:
* Algorithms:
*******************************************************************************/
void getMiddle1(node *h)
{
    if(!h) return ;
    node *fast =h;
    node *slow =h;
    while(fast->next && fast->next->next)
    {
     slow = slow->next; fast =fast->next->next;
    }
    
    if (fast->next== NULL)
      printf("\nODD Length_List");
    else
      { printf( "\nEVEN LENTH List");
        slow  = slow->next;
      }        
    printf("\nMiddle: %d\n",slow->val);
}  

/*******************************************************************************
* Problem 11A: Get Middle of a Linked-list using %
* Input:
* Output:
* Algorithms:
*******************************************************************************/
void getMiddle2(node *h)
{
    if(!h) return ;
    int i=0;
    node *slow =h;
    while(h)
    {   
        i++;  h =h->next;
        if( i%2 ==0) { slow = slow->next;} 
    } 
    printf("Middle: %d\n",slow->val);   
}  

/*******************************************************************************
* Problem 11B: Get 1/3 or 1/4 From Lisnked list
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 12: Return N-th node from last
* Input:
* Output:
* Algorithms:
*******************************************************************************/
void lastNth(node *h,int k)
{
    node *temp1= h;
    node *temp2 =h;
    for (int i =0;i<k;i++,temp1=temp1->next);
    while(temp1)
    {
        temp1 = temp1->next;
        temp2 = temp2->next;
    }
    printf("\nlast %d-th Node is : %d",k,temp2->val);
    
}    
/*******************************************************************************
* Problem 13: Comare two list Recursively
* Input:
* Output:
* Algorithms:
*******************************************************************************/
int listcmp(node *h1,node *h2)
{
    if( h1==NULL && h2==NULL)
      return true;
    else if (h1!=NULL && h2!=NULL && h1->val == h2->val)
     return listcmp(h1->next,h2->next);
    else
      return false;
}    
/*******************************************************************************
* Problem 14: Remove Duplicate from a list
* Input:
* Output:
* Algorithms:
*******************************************************************************/
void remDuplicates(node *h)
{
    if (h == NULL || h->next==NULL) //Zero or One node
      return;
    
    while(h->next !=NULL)
    {
        if( h->val == h->next->val)
        { node *track= h->next->next;
          free(h->next);
          h->next=track;
        }
        else
          h = h->next; 
    }    
}    
/*******************************************************************************
* Problem 15: Merge two sorted list, remove duplicate while merging
* Input:
* Output:
* Algorithms:
*******************************************************************************/
node * mergeList(node *h1, node *h2)
{
    if(h1==NULL)
      return h2;
    if (h2==NULL)
      return h1;
    if(h1->val < h2->val)
     {
         h1->next=mergeList(h1->next,h2);
         return h1;
     }
     else if (h2->val <h1->val)
     {
         h2->next=mergeList(h1,h2->next);
         return h2;
     }
     else //both are same
     {
         h1->next= mergeList(h1->next,h2->next);
         free(h2);
         return h1;
     }            
}    

/*******************************************************************************
* Problem 16: Swap an alternative node in a list
* Input:
* Output:
* Algorithms:
*******************************************************************************/
node * swapAlt(node* h)
{
    if ( h==NULL || h->next ==NULL)
      return h;
    node * temp= h->next->next;
    h->next->next=h;
    h =h->next;
    h->next->next=swapAlt(temp);
    return h;
}    

/*******************************************************************************
* Problem 17: Add two large interger in a list
* Input:
* Output:
* Algorithms:
*******************************************************************************/

node * addnum(node *h1,node *h2)
{
    h1 = reverse1(h1);
    h2 = reverse2(h2);
    
    node *nh=NULL;
    node *end =NULL;
    int sum=0,carry=0;
    while(h1 && h2)
    {   
        sum = h1->val+h2->val+carry;
        node *nw=getNewNode(sum%10);
        carry =sum/10;
        if(nh ==NULL)
          nh=end=nw;
        else 
        {
            end->next=nw;end=nw;           
        }  
        h1= h1->next;h2=h2->next;          
    }
    //Still some h1 left having 9->9->9->9->9
    while(h1)
    {
        sum = h1->val+carry;
        node *nw=getNewNode(sum%10);
        carry =sum/10;
        if(nh ==NULL)
          nh=end=nw;
        else 
        {
            end->next=nw;end=nw;           
        }  
        h1= h1->next; 
    }       
    
    while(h2)
    {
        sum = h2->val+carry;
        node *nw=getNewNode(sum%10);
        carry =sum/10;
        if(nh ==NULL)
          nh=end=nw;
        else 
        {
            end->next=nw;end=nw;           
        }  
        h2= h2->next; 
    }
    //We still have carry.. 
    if( carry)
    {
        node *nw=getNewNode(carry);
        end->next=nw;end=nw;
    }     
    return reverse1(nh);
}    

/*******************************************************************************
* Problem 18: Checking a list is palindorme or not !
* Input:
* Output:
* Algorithms:
*******************************************************************************/
void isPal1(node *h)
{
 
           
}    

/*******************************************************************************
* Problem 19: Rotate a list by posion k
* Input:
* Output:
* Algorithms:
*******************************************************************************/
node * rotate(node *h, int k)
{   node *temp =h;
    int len =getLength(h);
    //get new tail
    for (int i=0;i<len-k-1;i++,temp=temp->next);
    
    node *temp1= temp->next; //newhead
    temp->next=NULL; //set new tail
    
    temp=temp1;
    while(temp->next!=NULL)
      temp= temp->next;
    temp->next=h;
    
    return temp1;
}    

/*******************************************************************************
* Problem 20: Reverse each K segment of a list
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 21: Find loop in a list Find the Head and Break the Loop.
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 22: Implement generic Linked lIst
* Input:
* Output:
* Algorithms:
Struct Node{
void * data;
int tag;
node * next;
}
*******************************************************************************/
/*******************************************************************************
* Problem 23: Imaplment Binary Serach on a linked List
* Input:
* Output:
* Algorithms:
*******************************************************************************/
/*******************************************************************************
* Problem 24: Perform Bubble Sort in a Linked-List
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 24: Delete Corupted pointer in a linkedlist
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 11A: Swap  any two nodes in a Linked list
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 11A: Implemnet Double linkedlist using single Linkedlist
* Input:
* Output:
* Algorithms:
*******************************************************************************/
/*******************************************************************************
* Problem 11A: Find Intersection point of two Linkedlist in Y fashion.
* Input:
* Output:
* Algorithms:
*******************************************************************************/
/*******************************************************************************
* Problem 11A:  Pleace Odd element firsnt then Even elements
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem 0: Bresk a linkedlist into two part having even and odd elements
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem 11A: Merege two linkedlist Alternatively.
* Input:
* Output:
* Algorithms:
*******************************************************************************/
/*******************************************************************************
* Problem 11A: Traverse a Linkedlist in SQRT(N)
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem 0: Given Two lisnked list find Differences.
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: Remove Duplicated from unsorted linked list
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: Implemnt deep copy of a linked list
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: Return a Node randomly having equla prob, of unknown length
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: Check a Linkedlist is EVEN or ODD length
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: If head of linkedlist pointing to K-th node of linkedlist , how you access
Element before k?
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: Split a Circular linkedlist into two linked list
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: How to get O(1) Access time of a linked list
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: Sort a linkedlit of 0 1 and 2 ?
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: Impelment a LRU Cache ?
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: Find Triplet in a Linkedlist having SUM =S
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: Find Union and Intersection of Two linkedlist
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: Delete a Node having greatre value in Right Side/
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: Delete Alternative node in a linekdlist
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: Move last elemnt in Fromnt of a Lined list
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: Given  a lL having next and random pointer, how to copy it ?
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: Reverse a Linked-list from position m to N
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: Fattren a Multi-level Linkedlist
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: Fartern a List in sorted order
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: Convert a DLL into a BST
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: Count the occurance of a number in a Linkedlist
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 0: Deltee a Node froma LL, when only refe to the node is given
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem: 
* Input:
* Output:
* Algorithms:
*******************************************************************************/



#if UNIT_TEST
int main()
{
    test();
}    
#endif


#if 0
int main()
{
/************ Diver program start here **********/

//TEST : ARRY to LISt
int a[]= {1,2,3,4,6};
node * head =arary2List(a,5);
displayList(head);

//TEST ADD front, Delete Fornt, add last, del last
head = addFront(head,0);
displayList(head);


head = delFront(head);
displayList(head);



head = addLast(head,10);
displayList(head);

head = delLast(head);
displayList(head);

//TEST: Serrch
serachList(head,5);
serachList(head,100);

//TEST: Copy
node *head2 = copyList(head);
displayList(head2);

//TEST: Delete
head2 = delList(head2);
displayList(head2);

//TEST for Shorted Inert.
head =shortedInsert(head,0);
head =shortedInsert(head,7);
head = shortedInsert(head,5);
displayList(head);

//TEST : reverse print
reverseprint(head);

//TEST : reverse
displayList(head);
head = reverse1(head);
displayList(head);
head = reverse2(head);
displayList(head);

//TEST: Lengtg, ger Middle
int b[]= {1,2,3,4,5,6};
head =arary2List(b,6);
printf("Length : %d",getLength(head));
getMiddle1(head);
getMiddle2(head);

lastNth(head,2);

int c1[]={1,2,3,4,5,6};
int c2[]={1,2,3,4,5,6,7};
node * head1 =arary2List(c1,6);
head2 =arary2List(c2,7);
printf("\n\nisSame:%d\n",listcmp(head1,head2));

int c3[]={1,1,2,3,3,3,4,5,6,6,6,6,6,10,10};
head =arary2List(c3,15);
displayList(head);
remDuplicates(head);
displayList(head);


//Test: Merge
int d1[]={10,20,30,40,50,60};
int d2[]={5,15,25,35,100};
head1 =arary2List(d1,6);
head2 =arary2List(d2,5);
head = mergeList(head1,head2);
displayList(head);

//Test: Swap
int x1[]={10,20,30,40,50,60,70};
head =arary2List(x1,7);
displayList(head);
head = swapAlt(head);
displayList(head);

//Test: Add Number
int x2[]={9,9,9};
int x3[]={9,9,9,9,9};
head1 =arary2List(x2,3);
head2 =arary2List(x3,5);
head = addnum(head1,head2);
displayList(head);

head = rotate(head,4);
displayList(head);



printf("\n\n\n\nDone");
getch();
}        

#endif
/*
class List
{
    private:
        node *head;
    public:
        List();
        ~List();
        void printList();
        void convert2List(int *a);
        void insertFront(int x);
        void insertBack(int y);
        
}
    
*/
