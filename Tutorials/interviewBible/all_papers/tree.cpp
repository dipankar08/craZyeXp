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

 
/*******************************************************************************
* Problem :[TRAVARSAL] Print Inorder / Pre order and Post ORder in Recustion.
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

void inorder(node*r)
{   
    if (r)
    {
        inorder(r->left);
        printf("%d::",r->val);
        inorder(r->right);
    }    
    
}  

/*******************************************************************************
* Problem : [TRAVARSAL]  Print In/pre/post -order traval without recustion and using stack
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [TRAVARSAL]  Retunr N-th Node in inorder tra versal.
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem :[TRAVARSAL]   Print In/pre/post -order traval without recustion and with out stack - Moris Traveasl.
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 


/*******************************************************************************
* Problem : [TRAVARSAL]  label Wise Traversal with Queue.
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
* Problem :[TRAVARSAL]   Prity Print label Wise Traversal with Queue.
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
* Problem :[TRAVARSAL]  Print perticular level of Tree
* Input:
* Output:
* Algorithms: Not Working.
*******************************************************************************/

/*******************************************************************************
* Problem :[TRAVARSAL]  Print a level having maximum Sum
* Input/ Output:
* Algorithms: Not Working.
*******************************************************************************/

/*******************************************************************************
* Problem :[TRAVARSAL]  Print a level having maximum numebr of node
* Input/ Output:
* Algorithms: 
*******************************************************************************/

/*******************************************************************************
* Problem :  [TRAVARSAL] Print ZigZag botton to up left to right
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
* Problem : [TRAVARSAL] Print Zigzag trversal from top to buttion wil Alternet level order
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
* Problem : [TRAVARSAL]   Print All parts from Root to leaf
* Input / Output: 
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
* Problem : [TRAVARSAL]   Print All node in vertical order.
* Input / Output: 
* Algorithms: Usinng Hash Map.
*******************************************************************************/


/*******************************************************************************
* Problem : [TRAVARSAL]   Print RIght View of a Binary Tree 
* Input / Output: 
Right view of following tree is 1 3 7 8

          1
       /     \
     2        3
   /   \     /  \
  4     5   6    7
                  \
                   8
* Algorithms: Print last node in each level.
*******************************************************************************/

/*******************************************************************************
* Problem : [TRAVARSAL]   PPrint Left View of a Binary Tree
* Input / Output: 
Given a Binary Tree, print left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from left side. Left view of following tree is 12, 10, 25.

          12
       /     \
     10       30
            /    \
          25      40 
* Algorithms: 
The left view contains all nodes that are first nodes in their levels. A simple solution is to do level order traversal and print the first node in every level.
The problem can also be solved using simple recursive traversal .
We can keep track of level of a node by passing a parameter to all recursive calls.
The idea is to keep track of maximum level also. Whenever we see a node whose level is more 
than maximum level so far, we print the node because this is the first node in its level 
(Note that we traverse the left subtree before right subtree). 

*******************************************************************************/



/*******************************************************************************
* Problem : [TRAVARSAL]   Print Trangular covering of a TREE
* Input / Output: 
* Algorithms: Using Two Stack
*******************************************************************************/

/*******************************************************************************
* Problem : [TRAVARSAL]   Print  Level Wise sum of a Tree
* Input / Output: 
* Algorithms: Using Two Stack
*******************************************************************************/
/*******************************************************************************
* Problem : [TRAVARSAL]   Print Vertical sum of Tree
* Input / Output: 
* Algorithms: Using Two Stack
*******************************************************************************/

/*******************************************************************************
* Problem : [TRAVARSAL]   Print all nodes that don’t have sibling
* Input / Output: 
* Algorithms:
This is a typical tree traversal question. We start from root and check if the node
has one child, if yes then print the only child of that node. 
If node has both children, then recur for both the children.
*******************************************************************************/

/*******************************************************************************
* Problem : [Properties] Find the height of a TREE
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 
int getheight(node *r)
{
    if (!r) return 0;
    else
    {
        return getheight(r->left)>getheight(r->right) ?getheight(r->left)+1: getheight(r->right) +1;
    }    
}         


/*******************************************************************************
* Problem : [Properties]  Count Number of Nodes in  a Tree
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [Properties]  Count Number of lefe, interbalnode and Deg 0,1,2 Nodes in a Tree
* Input / Output: 
* Algorithms:  
*******************************************************************************/

/*******************************************************************************
* Problem : [Properties]  Find the Diameter of a TRee
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 
/*******************************************************************************
* Problem : [Properties]  Find the longest/deepest Path of a TRee
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 
/*******************************************************************************
* Problem : [Properties]  Cjeck a Tree is height Balance or Not !
* Input / Output: 
* Algorithms:  
For every node, we need to get the maximum and minimum heights and compare them.
The idea is to traverse the tree and for every node check if it’s balanced. We need
to write a recursive function that returns three things, a boolean value to indicate
the tree is balanced or not, minimum height and maximum height.
To return multiple values, we can either use a structure or pass variables by reference. 
We have passed maxh and minh by reference so that the values can be used in parent calls.

*******************************************************************************/ 
/*******************************************************************************
* Problem : [Properties]  Check a tree is Symetric or not !
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 
/*******************************************************************************
* Problem : [Properties]  Check a Tree is well ordered or Not !
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [Properties]  Sum of All node in that Tree ( Recursive)
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
* Problem : [Properties]  Find the Maximula width of any levle of a TREE
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 


/*******************************************************************************
* Problem : [Properties]  Find the Sum of node in a Tree
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 
/*******************************************************************************
* Problem : [Properties]  Search a number in a TREE not in a BST
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [Properties]  Print Depest Node in a Tree
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [Properties]  Delete  an elemnt in a TREE ?
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 
/*******************************************************************************
* Problem : [Properties]  Find the Maximula width of any levle of a TREE
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 


/*******************************************************************************
* Problem :  [Properties]   Difference between sums of odd level and even level nodes of a Binary Tree
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
* Problem : [Properties]  HHow many Tree possible with n nodes.
* Input / Output: 
*******************************************************************************/ 
/*******************************************************************************
* Problem : [Properties]  How many Binary tree possble with n nodes
* Input / Output: 
* Algorithms:
*******************************************************************************/ 

/*******************************************************************************
* Problem : [Properties]  How many Binary Serach tree possble with n nodes
* Input / Output: 
* Algorithms:
*******************************************************************************/ 

/*******************************************************************************
* Problem : [Properties]  Iterative Method to find Height of Binary Tree
* Input / Output: 
* Algorithms:
Recursive method to find height of Binary Tree is discussed. How to find height without 
recursion? We can use level order traversal to find height without recursion. The idea is to 
traverse level by level. Whenever move down to a level, increment height by 1 (height is 
initialized as 0). Count number of nodes at each level, stop traversing when count of nodes at 
next level is 0. 

*******************************************************************************/ 


/*******************************************************************************
* Problem : [Properties]  
* Input / Output: 
* Algorithms:
*******************************************************************************/ 


/*******************************************************************************
* Problem : [Properties]  
* Input / Output: 
* Algorithms:
*******************************************************************************/ 


/*******************************************************************************
* Problem : [Properties]  
* Input / Output: 
* Algorithms:
*******************************************************************************/ 






/*******************************************************************************
* Problem : [Print_With_Cond]  Lavel having maxuimum Sum
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
* Problem : [Print_With_Cond]  Print path having path sum S
* Input / Output: 
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
* Problem : [Print_With_Cond]  Print path having path sum S strily from root to left, having -ve, +ve nodes
* Input / Output: 
* Algorithms: Using Two Stack
*******************************************************************************/

/*******************************************************************************
* Problem : [Print_With_Cond]  Print path having path sum S strily from root to left, having only +ve nodes in a BST
* Input / Output: 
* Algorithms: Using Two Stack
*******************************************************************************/

/*******************************************************************************
* Problem : [Print_With_Cond]  Find depth of the deepest odd level leaf node
* Input / Output: 
For example, consider the following tree. The deepest odd level node is the node with value 9
and depth of this node is 5.

       1
     /   \
    2     3
  /      /  \  
 4      5    6
        \     \
         7     8
        /       \
       9         10
                 /
                11
* Algorithms: 

The idea is to recursively traverse the given binary tree and while traversing, maintain a 
variable “level” which will store the current node’s level in the tree. If current node is 
leaf then check “level” is odd or not. If level is odd then return it. If current node is not 
leaf, then recursively find maximum depth in left and right subtrees, and return maximum of 
the two depths.

*******************************************************************************/

/*******************************************************************************
* Problem :  [Print_With_Cond] Check if all leaves are at same level
* Input / Output: 
      12
        /    \
      5       7       
    /          \ 
   3            1
  Leaves are at same level

          12
        /    \
      5       7       
    /          
   3          
   Leaves are Not at same level
* Algorithms: 
The idea is to first find level of the leftmost leaf and store it in a variable leafLevel. 
Then compare level of all other leaves with leafLevel, if same, return true, else return false. 
We traverse the given Binary Tree in Preorder fashion. An argument leaflevel is passed to all 
calls. The value of leafLevel is initialized as 0 to indicate that the first leaf is not yet 
seen yet. The value is updated when we find first leaf. Level of subsequent leaves (in 
preorder) is compared with leafLevel.
*******************************************************************************/

/*******************************************************************************
* Problem : [Print_With_Cond]  Deepest left leaf node in a binary tree
* Input / Output: 
he deepest left leaf node is the node with value 9.

       1
     /   \
    2     3
  /      /  \  
 4      5    6
        \     \
         7     8
        /       \
       9         10
       
* Algorithms:
The idea is to recursively traverse the given binary tree and while traversing, 
maintain “level” which will store the current node’s level in the tree. If current node 
is left leaf, then check if its level is more than the level of deepest left leaf seen so far. 
If level is more then update the result. If current node is not leaf, then recursively find 
maximum depth in left and right subtrees, and return maximum of the two depths.

*******************************************************************************/
/*******************************************************************************
* Problem : [Print_With_Cond] Find next right node of a given key
* Input / Output: 
Output for 2 is 6, output for 4 is 5. Output for 10, 6 and 5 is NULL
                 10
               /      \
	      	2         6
           /   \         \ 
	 	8      4          5
* Algorithms:
The idea is to do level order traversal of given Binary Tree.
When we find the given key, we just check if the next node in level order traversal is of 
same level, if yes, we return the next node, otherwise return NULL.

*******************************************************************************/
/*******************************************************************************
* Problem : [Print_With_Cond] Sum of all the numbers that are formed from root to leaf paths
* Input / Output: 
                                         6
                                      /      \
                                    3          5
                                  /   \          \
                                 2     5          4  
                                      /   \
                                     7     4
  There are 4 leaves, hence 4 root to leaf paths:
   Path                    Number
  6->3->2                   632
  6->3->5->7               6357
  6->3->5->4               6354
  6->5>4                    654   
Answer = 632 + 6357 + 6354 + 654 = 13997 

* Algorithms:
The idea is to do a preorder traversal of the tree. 
In the preorder traversal, keep track of the value calculated till the current node, 
let this value be val . For every node, we update the val as val*10 plus node’s data.

*******************************************************************************/
/*******************************************************************************
* Problem : [Print_With_Cond]  Difference between sums of odd level and even level nodes of a Binary Tree
* Input / Output: 
      5
    /   \
   2     6
 /  \     \  
1    4     8
    /     / \ 
   3     7   9  
 in the following tree, sum of nodes at odd level is (5 + 1 + 4 + 8) which is 18.
  And sum of nodes at even level is (2 + 6 + 3 + 7 + 9) which is 27. 
  The output for following tree should be 18 – 27 which is -9.
 
* Algorithms:
A straightforward method is to use level order traversal . In the traversal, check level of current node, if it is odd, increment odd sum by data of current node, otherwise increment even sum. Finally return difference between odd sum and even sum.
The problem can also be solved using simple recursive traversal . We can recursively calculate the required difference as, value of root’s data subtracted by the difference for subtree under left child and the difference for subtree under right child. Following is C implementation of this approach.

*******************************************************************************/
/*******************************************************************************
* Problem : [Print_With_Cond] 
* Input / Output: 
* Algorithms:
*******************************************************************************/
/*******************************************************************************
* Problem : [Print_With_Cond] 
* Input / Output: 
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem : [Node Properties] Print all Ansistor
* Input / Output: 
* Algorithms: 
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
* Problem : [Node Properties] Print ancestors of a given binary tree node without recursion
* Input / Output: 
* Algorithms: 
For example, consider the following Binary Tree

            1
        /       \
       2         3
     /   \     /   \
    4     5    6    7 
   /       \       /
  8         9     10  
Following are different input keys and their ancestors in the above tree

Input Key    List of Ancestors 
-------------------------
 1            
 2            1
 3            1
 4            2 1
 5            2 1
 6            3 1
 7            3 1
 8            4 2 1
 9            5 2 1
10            7 3 1

It is clear that we need to use a stack based iterative traversal of the Binary Tree. The 
idea is to have all ancestors in stack when we reach the node with given key. 
Once we reach the key, all we have to do is, print contents of stack. How to get all ancestors
in stack when we reach the given node? We can traverse all nodes in Postorder way. 
If we take a closer look at the recursive postorder traversal, we can easily observe that, 
when recursive function is called for a node, the recursion call stack contains ancestors of the node. 
So idea is do iterative Postorder traversal and stop the traversal when we reach the desired node.


*******************************************************************************/

/*******************************************************************************
* Problem : [Node Properties]  LCA of a BST
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
* Problem : [Node Properties]  Find LCA of a Binary Tree but not an BST
* Input: 
* Output: 
* Algorithms: 
We have discussed an efficient solution to find LCA in Binary Search Tree . In Binary Search 
Tree, using BST properties, we can find LCA in O(h) time where h is height of tree. Such an
implementation is not possible in Binary Tree as keys Binary Tree nodes don’t follow any order. Following are different approaches to find LCA in Binary Tree.

Method 1 (By Storing root to n1 and root to n2 paths): 

Following is simple O(n) algorithm to find LCA of n1 and n2. 
1) Find path from root to n1 and store it in a vector or array. 
2) Find path from root to n2 and store it in another vector or array. 
3) Traverse both paths till the values in arrays are same. Return the common element just before the mismatch.

Method 2 (Using Single Traversal) 
The method 1 finds LCA in O(n) time, but requires three tree traversals plus extra spaces for
path arrays. If we assume that the keys n1 and n2 are present in Binary Tree, we can find LCA
using single traversal of Binary Tree and without extra storage for path arrays. 
The idea is to traverse the tree starting from root. If any of the given keys (n1 and n2) 
matches with root, then root is LCA (assuming that both keys are present). If root doesn’t 
match with any of the keys, we recur for left and right subtree. The node which has one key 
present in its left subtree and the other key present in right subtree is the LCA. If both 
keys lie in left subtree, then left subtree has LCA also, otherwise LCA lies in right subtree.

*******************************************************************************/

/*******************************************************************************
* Problem : [Node Properties]  Print all nodes that are at distance k from a leaf node
Here the meaning of distance is different from general sense. Here k distance from a leaf
means k levels higher than a leaf node. For example if k is more than height of Binary Tree,
then nothing should be printed. Expected time complexity is O(n) where n is the number nodes in the given Binary Tree.

* Input: 
* Output: 
* Algorithms: 
The idea is to traverse the tree. Keep storing all ancestors till we hit a leaf node. 
When we reach a leaf node, we print the ancestor at distance k. We also need to keep 
track of nodes that are already printed as output. For that we use a boolean array visited[].

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
* Problem : [Node Properties]  Print all nodes that are at distance k from a any node up
 or down. Given a binary tree, a target node in the binary tree, and an integer value k,
 print all the nodes that are at distance k from the given target node. 
 No parent pointers are available.
 
* Input: 
* Output: 
* Algorithms:
Just traverse subtrees rooted with the target node and decrement k in recursive call. 
 When the k becomes 0, print the node currently being traversed (See this for more details). Here we call the function as printkdistanceNodeDown() .
 
How to find nodes of second type? For the output nodes not lying in the subtree with the target node as the root, we must go through all ancestors. For every ancestor, we find its distance from target node, let the distance be d, now we go to other subtree (if target was found in left subtree, then we go to right subtree and vice versa) of the ancestor and find all nodes at k-d distance from the ancestor.

*******************************************************************************/

/*******************************************************************************
* Problem : [Node Properties]  Find distance between two given keys of a Binary Tree
* Input: 
* Output: 
* Algorithms: 
 Distance between two nodes is the minimum number of edges to be traversed to reach one node from other.
 Dist(n1, n2) = Dist(root, n1) + Dist(root, n2) - 2*Dist(root, lca) 
'n1' and 'n2' are the two given keys
'root' is root of given Binary Tree.
'lca' is lowest common ancestor of n1 and n2
Dist(n1, n2) is the distance between n1 and n2.

*******************************************************************************/


/*******************************************************************************
* Problem : [Node Properties]  Print all nodes that don’t have sibling
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
* Problem : [BST] Making BST from Array
* Input / Output: 
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
* Problem : [BST] is BST ? We are assing min and max same iteration....
* Input / Output: 
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
* Problem : [BST] Insert a Node in BST, as leaf, internal node , Check duplicates also.
* Input / Output: 
* Algorithms: Using Two Stack
*******************************************************************************/


/*******************************************************************************
* Problem : [BST] Serach in BST
* Input / Output: 
* Algorithms: Using Two Stack
*******************************************************************************/
/*******************************************************************************
* Problem : [BST] Serach in BST with less comparsim 
* Input / Output: 
* Algorithms: Using Two Stack
*******************************************************************************/
/*******************************************************************************
* Problem : [BST] Range Serach in BST
* Input / Output: 
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
* Problem :[BST]  K-th Smallest Element in a Binary tree.(BST)
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
* Problem : [BST] Add all greater values to every node in a given BST
* Input / Output: 
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
* Problem : [BST] Find the minimum and Maximum of a BST 
* Input / Output: 
* Algorithms: 
*******************************************************************************/



/*******************************************************************************
* Problem : [BST] Find the In/Pre Successor of a BST
* Input / Output: 
* Algorithms: 
*******************************************************************************/


/*******************************************************************************
* Problem : [BST] Find the In/Pre Predicessor of a BST
* Input / Output: 
* Algorithms: 
*******************************************************************************/
/*******************************************************************************
* Problem : [BST] Find floor of node (Next smaller)
* Input / Output: 
* Algorithms: 
*******************************************************************************/

/*******************************************************************************
* Problem : [BST] Find the Next Bigger (next Big) of a Node 
* Input / Output: 
* Algorithms: 
*******************************************************************************/

/*******************************************************************************
* Problem : [BST] Count the number of BST for key <1...k>
* Input / Output: 
* Algorithms: 
*******************************************************************************/

/*******************************************************************************
* Problem : [BST] Find the two key haveing sum S in a BST
* Input / Output: 
* Algorithms: 
*******************************************************************************/

/*******************************************************************************
* Problem : [BST] Find medium of a BST
* Input / Output: 
* Algorithms: 
*******************************************************************************/

/*******************************************************************************
* Problem : [BST] Find Siblink of a BST
* Input / Output: 
* Algorithms: 
*******************************************************************************/

/*******************************************************************************
* Problem : [BST] How to merge n number of BST into a single one.?
* Input / Output: 
* Algorithms: 
*******************************************************************************/

/*******************************************************************************
* Problem :[Modify] Create a Duplicate Node of BST as a left child of it. 
* Input / Output:  <1> --<2> ---<3> => 1--<2>----<2>---<3>---<3>
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [Modify] Delete a Tree
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 


/*******************************************************************************
* Problem : [Modify] Convert an Tree into a Mirror Tree
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [Modify] Copy a Tree
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [Modify] Convert an Tree into N _lisnted from button up.
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 


/*******************************************************************************
* Problem : [Modify] Convert an Tree into double linkedist
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 


/*******************************************************************************
* Problem : [Modify] Convert an Double Linekedy list into a Tree
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [Modify] Convert an Tree into Min Heap and Vice Versa.
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 
/*******************************************************************************
* Problem : [Modify] Is it possble to onvert a min-hepa to max hep in O(n)
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 
/*******************************************************************************
* Problem : [Modify]  Constract Tree from Iordera nd Pre-order travalsal.
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [Modify]  Constract a Tree from Inorder and Levle Order Travarsal.
* Input / Output: 
* Algorithms:  
in[] = {4, 8, 10, 12, 14, 20, 22}; 
level[] = {20, 8, 22, 4, 12, 10, 14};

In a Levelorder sequence, the first element is the root of the tree.
So we know ’20' is root for given sequences.
By searching ’20' in Inorder sequence, we can find out all elements on left side of
‘20’ are in left subtree and elements on right are in right subtree. So we know below
 structure now.

             20
           /    \
          /      \ 
 {4,8,10,12,14}  {22}   
Let us call {4,8,10,12,14} as left subarray in Inorder traversal and {22} as right subarray in Inorder traversal. 
*******************************************************************************/ 

/*******************************************************************************
* Problem : [Modify] Print Postorder traversal from given Inorder and Preorder traversals
* Input / Output: 
* Algorithms:  
A naive method is to first construct the tree, then use simple recursive method to print postorder traversal of the constructed tree.

We can print postorder traversal without constructing the tree . The idea is, root is always
the first item in preorder traversal and it must be the last item in postorder traversal. 
We first recursively print left subtree, then recursively print right subtree. Finally, print 
root. To find boundaries of left and right subtrees in pre[] and in[], we search root in in[], 
all elements before root in in[] are elements of left subtree and all elements after root are 
elements of right subtree. In pre[], all elements after index of root in in[] are elements of 
right subtree. And elements before index (including the element at index and excluding the first
element) are elements of left subtree

*******************************************************************************/ 


/*******************************************************************************
* Problem : [Modify] Constact a Heap from Only Inoredr travalsal.
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 


/*******************************************************************************
* Problem : [Modify] Add all greater values to every node in a given BST
* Input / Output: 
 			 50
           /      \
         30        70
        /   \      /  \
      20    40    60   80 

The above tree should be modified to following 

              260
           /      \
         330        150
        /   \       /  \
      350   300    210   80
      
* Algorithms:  
The idea is to use following BST property. If we do reverse Inorder traversal of BST, 
we get all nodes in decreasing order. We do reverse Inorder traversal and keep track of the
 sum of all nodes visited so far, we add this sum to every node.

*******************************************************************************/ 


/*******************************************************************************
* Problem : [Modify]  Remove all nodes which don’t lie in any path with sum>= k
Given a binary tree, a complete path is defined as a path from root to a leaf. The sum of all
nodes on that path is defined as the sum of that path. Given a number K, you have to remove
(prune the tree) all nodes which don’t lie in any path with sum>=k.

* Input / Output: 
Consider the following Binary Tree
          1 
      /      \
     2        3
   /   \     /  \
  4     5   6    7
 / \    /       /
8   9  12      10
   / \           \
  13  14         11
      / 
     15 

For input k = 20, the tree should be changed to following
(Nodes with values 6 and 8 are deleted)
          1 
      /      \
     2        3
   /   \        \
  4     5        7
   \    /       /
    9  12      10
   / \           \
  13  14         11
      / 
     15 

For input k = 45, the tree should be changed to following.
      1 
    / 
   2   
  / 
 4  
  \   
   9    
    \   
     14 
     /
    15 

* Algorithms:
The idea is to traverse the tree and delete nodes in bottom up manner. While traversing the
tree, recursively calculate the sum of nodes from root to leaf node of each path. For each 
visited node, checks the total calculated sum against given sum “k”. If sum is less than k, 
then free(delete) that node (leaf node) and return the sum back to the previous node. Since 
the path is from root to leaf and nodes are deleted in bottom up manner, a node is deleted 
only when all of its descendants are deleted. Therefore, when a node is deleted, 
it must be a leaf in the current Binary Tree.
  
*******************************************************************************/ 
/*******************************************************************************
* Problem : [Modify]  Extract Leaves of a Binary Tree in a Doubly Linked List
* Input / Output: 
Let the following be input binary tree
        1
     /     \
    2       3
   / \       \
  4   5       6
 / \         / \
7   8       9   10


Output:
Doubly Linked List
785910

Modified Tree:
        1
     /     \
    2       3
   /         \
  4           6
* Algorithms:  
We need to traverse all leaves and connect them by changing their left and right pointers.
We also need to remove them from Binary Tree by changing left or right pointers in parent 
nodes. There can be many ways to solve this. In the following implementation, we add leaves
at the beginning of current linked list and update head of the list using pointer to head 
pointer. Since we insert at the beginning, we need to process leaves in reverse order. 
For reverse order, we first traverse the right subtree then the left subtree. 
We use return values to update left or right pointers in parent nodes.

*******************************************************************************/ 
/*******************************************************************************
* Problem : [Modify]  Construct Complete Binary Tree from its Linked List Representation
* Input / Output: 
If root node is stored at index i, its left, and right children are stored at indices 2*i+1, 2*i+2 respectively. 

* Algorithms:  
We know head of linked list is always is root of the tree. 
We take the first node as root and we also know that the next two nodes are left and right 
children of root. So we know partial Binary Tree. The idea is to do Level order traversal of 
the partially built Binary Tree using queue and traverse the linked list at the same time. 
At every step, we take the parent node from queue, make next two nodes of linked list as 
children of the parent node, and enqueue the next two nodes to queue.

1. Create an empty queue. 
2. Make the first node of the list as root, and enqueue it to the queue. 
3. Until we reach the end of the list, do the following. 
……… a. Dequeue one node from the queue. This is the current parent. 
……… b. Traverse two nodes in the list, add them as children of the current parent. 
……… c. Enqueue the two nodes into the queue.
*******************************************************************************/ 
/*******************************************************************************
* Problem : [Modify] Remove BST keys outside the given range
* Input / Output: 
Given a Binary Search Tree (BST) and a range [min, max], remove all keys which are outside the
given range. The modified tree should also be BST. 
* Algorithms:

1) Node’s key is outside the given range. This case has two sub-cases. 
……. a) Node’s key is smaller than the min value. 
……. b) Node’s key is greater that the max value. 
2) Node’s key is in range.

We don’t need to do anything for case 2. In case 1, we need to remove the node and change root
of sub-tree rooted with this node.The idea is to fix the tree in Postorder fashion. When we 
visit a node, we make sure that its left and right sub-trees are already fixed. 
In case 1.a), we simply remove root and return right sub-tree as new root. 
In case 1.b), we remove root and return left sub-tree as new root.
  
*******************************************************************************/ 
/*******************************************************************************
* Problem : [Modify] Convert a given Binary Tree to Doubly Linked List
* Input / Output: 
* Algorithms:  
1. If left subtree exists, process the left subtree 
….. 1.a) Recursively convert the left subtree to DLL. 
….. 1.b) Then find inorder predecessor of root in left subtree (inorder predecessor is rightmost node in left subtree). 
….. 1.c) Make inorder predecessor as previous of root and root as next of inorder predecessor. 
2. If right subtree exists, process the right subtree (Below 3 steps are similar to left subtree). 
….. 2.a) Recursively convert the right subtree to DLL. 
….. 2.b) Then find inorder successor of root in right subtree (inorder successor is leftmost node in right subtree). 
….. 2.c) Make inorder successor as next of root and root as previous of inorder successor. 
3. Find the leftmost node and return it (the leftmost node is always head of converted DLL).

Another simple and efficient solution is discussed. The solution discussed here has two simple steps.

1) Fix Left Pointers : In this step, we change left pointers to point to previous nodes in DLL. 
The idea is simple, we do inorder traversal of tree. In inorder traversal, we keep track of 
previous visited node and change left pointer to the previous node. 

2) Fix Right Pointers : The above is intuitive and simple. How to change right pointers to 
point to next node in DLL? The idea is to use left pointers fixed in step 1. We start from the 
rightmost node in Binary Tree (BT). The rightmost node is the last node in DLL. 
Since left pointers are changed to point to previous node in DLL, we can linearly traverse 
the complete DLL using these pointers. The traversal would be from last to first node. While 
traversing the DLL, we keep track of the previously visited node and change the right pointer 
to the previous node.

*******************************************************************************/ 
/*******************************************************************************
* Problem : [Modify]  Create tree a lost like : 
* Input / Output: 
a ---> b
b ---> c
b ---> d
a ---> e 
 to 
-->a
   |-->b
   |   |-->c
   |   |-->d
   |-->e

a ---> b
a ---> g
b ---> c
c ---> d
d ---> e
c ---> f
z ---> y
y ---> x
x ---> w
The output would be following forest.

-->a
   |-->b
   |   |-->c
   |   |   |-->d
   |   |   |   |-->e
   |   |   |-->f
   |-->g

-->z
   |-->y
   |   |-->x
   |   |   |-->w
   
* Algorithms:  
The idea is to maintain two arrays, one array for tree nodes and other for trees themselves 
(we call this array forest). An element of the node array contains the TreeNode object that 
corresponds to respective character. An element of the forest array contains Tree object that 
corresponds to respective root of tree.

It should be obvious that the crucial part is creating the forest here, once it is created, 
printing it out in required format is straightforward. To create the forest, following procedure 
is used -

Do following for each input link,
1. If start of link is not present in node array
     Create TreeNode objects for start character
     Add entries of start in both arrays. 
2. If end of link is not present in node array
     Create TreeNode objects for start character
     Add entry of end in node array.
3. If end of link is present in node array.
     If end of link is present in forest array, then remove it
     from there.
4. Add an edge (in tree) between start and end nodes of link.

*******************************************************************************/ 
/*******************************************************************************
* Problem : [Modify] 
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 
/*******************************************************************************
* Problem : [Modify] 
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 
/*******************************************************************************
* Problem : [Modify] 
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 
/*******************************************************************************
* Problem : [Modify] 
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [ Comparism ] Given Two tree T1 and T2. Find they are Same or Not ?
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [ Comparism ] Given Two tree T1 and T2. Find they are Structurly same or not ?(Isomomic )
* Input / Output: 
Two trees are called isomorphic if one of them can be obtained from other by a series of flips,
i.e. by swapping left and right children of a number of nodes. 
Any number of nodes at any level can have their children swapped. Two empty trees are 
isomorphic.

* Algorithms:  
Let the current internal nodes of two trees being traversed be n1 and n2 respectively. There 
are following two conditions for subtrees rooted with n1 and n2 to be isomorphic. 
1) Data of n1 and n2 is same. 
2) One of the following two is true for children of n1 and n2 
…… a) Left child of n1 is isomorphic to left child of n2 and right child of n1 is isomorphic to right child of n2. 
…… b) Left child of n1 is isomorphic to right child of n2 and right child of n1 is isomorphic to left child of n2.

*******************************************************************************/ 
/*******************************************************************************
* Problem : [ Comparism ] Given Two tree T1 and T2. Find they are semi-isomophic or not !
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [ Comparism ] Given Two tree T1 and T2. Find they are Quasi-isomorphic or not!
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [ Comparism ] Given Two tree T1 and T2. Find they are Mirror of each other ?
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [ Comparism ] Given Two tree T1 and T2. Find T1 is a Subtree of T2 or Not !
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [ Comparism ] Given Two tree T1 and T2. Largest common subtree of T1 and T2
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 



/*******************************************************************************
* Problem : [ Comparism ] Check for Identical BSTs without building the trees
* Input / Output: 
* Algorithms:  For example, the input arrays are {2, 4, 3, 1} and {2, 1, 4, 3} will construct the same tree

According to BST property, elements of left subtree must be smaller and elements of right 
subtree must be greater than root.Two arrays represent sane BST if for every element x, 
the elements in left and right subtrees of x appear after it in both arrays. 
And same is true for roots of left and right subtrees. 
The idea is to check of if next smaller and greater elements are same in both arrays. 
Same properties are recursively checked for left and right subtrees. The idea looks simple, 
but implementation requires checking all conditions for all elements. 
*******************************************************************************/ 

/*******************************************************************************
* Problem : [ Comparism ] 
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 
/*******************************************************************************
* Problem : [ Comparism ] 
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 
/*******************************************************************************
* Problem : [ Comparism ] 
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [ Comparism ] Find largest BST in a Tree ?
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [ Comparism ] Given Two tree T1 and T2. Find Union and Intersection. Do it if the tree is BST
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [ General Tree ] Reprsent a Genral Tree
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [ General Tree ] TRavese a General Tree
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [ General Tree ] Count the nodes in a General Tree
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 
/*******************************************************************************
* Problem : [ General Tree ] Count the sibling of a nodes in a General Tree
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 
/*******************************************************************************
* Problem : [ General Tree ] Count the number of child of a  nodes in a General Tree
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [ General Tree ] Find Sum of all ement in a Genrak tree
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : [ General Tree ] We have an array P[1..n] where p[i] indiacte parent if i-th node, Find the height of that tree
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 


/*******************************************************************************
* Problem : [ General Tree ] IMplement Interval serach Tree
* Input / Output: 
* Algorithms:  
Consider a situation where we have a set of intervals and we need following operations to be implemented efficiently. 
1) Add an interval 
2) Remove an interval 
3) Given an interval x, find if x overlaps with any of the existing intervals.

Interval Tree: The idea is to augment a self-balancing Binary Search Tree (BST) like Red Black Tree , AVL Tree , etc to maintain set of intervals so that all operations can be done in O(Logn) time.
Every node of Interval Tree stores following information. 
a) i : An interval which is represented as a pair [low, high] 
b) max : Maximum high value in subtree rooted with this node.

The main operation is to search for an overlapping interval. Following is algorithm for searching an overlapping interval x in an Interval tree rooted with root .

Interval overlappingIntervalSearch(root, x)
1) If x overlaps with root's interval, return the root's interval.

2) If left child of root is not empty and the max  in left child 
is greater than x's low value, recur for left child

3) Else recur for right child.
*******************************************************************************/ 


/*******************************************************************************
* Problem : [ General Tree ] Splay Treee:  Impove seraching in BST
* Input / Output: 
* Algorithms:  
The worst case time complexity of Binary Search Tree (BST) operations like search, delete, 
insert is O(n). The worst case occurs when the tree is skewed. We can get the worst case time
complexity as O(Logn) with AVL and Red-Black Trees.

Can we do better than AVL or Red-Black trees in practical situations? 
Like AVL and Red-Black Trees, Splay tree is also self-balancing BST . The main idea of splay 
tree is to bring the recently accessed item to root of the tree, this makes the recently 
searched item to be accessible in O(1) time if accessed again. The idea is to use locality of 
reference (In a typical application, 80% of the access are to 20% of the items). Imagine a 
situation where we have millions or billions of keys and only few of them are accessed 
frequently, which is very likely in many practical applications.

All splay tree operations run in O(log n) time on average, where n is the number of entries in 
the tree. Any single operation can take Theta(n) time in the worst case.

Search Operation 
The search operation in Splay tree does the standard BST search, in addition to search, 
it also splays (move a node to the root). If the search is successful, then the node that is 
found is splayed and becomes the new root. Else the last node accessed prior to reaching the 
NULL is splayed and becomes the new root.

*******************************************************************************/ 
/*******************************************************************************
* Problem : [ General Tree ] B-Tree : B-Tree is a self-balancing search tree.
* Input / Output: 
* Algorithms:  
To understand use of B-Trees, we must think of huge amount of data that cannot fit in main 
memory. When the number of keys is high, the data is read from disk in the form of blocks. 
Disk access time is very high compared to main memory access time. The main idea of using 
B-Trees is to reduce the number of disk accesses. Most of the tree operations (search, insert, 
delete, max, min, ..etc ) require O(h) disk accesses where h is height of the tree. 
B-tree is a fat tree. Height of B-Trees is kept low by putting maximum possible keys in a 
B-Tree node. Generally, a B-Tree node size is kept equal to the disk block size. Since h is 
low for B-Tree, total disk accesses for most of the operations are reduced significantly 
compared to balanced Binary Search Trees like AVL Tree, Red Black Tree, ..etc.

Properties of B-Tree 
1) All leaves are at same level. 
2) A B-Tree is defined by the term minimum degree ‘t’. The value of t depends upon disk block size. 
3) Every node except root must contain at least t-1 keys. Root may contain minimum 1 key. 
4) All nodes (including root) may contain at most 2t – 1 keys. 
5) Number of children of a node is equal to the number of keys in it plus 1. 
6) All keys of a node are sorted in increasing order. The child between two keys k1 and k2 contains all keys in range from k1 and k2. 
7) B-Tree grows and shrinks from root which is unlike Binary Search Tree. Binary Search Trees grow downward and also shrink from downward. 
8) Like other balanced Binary Search Trees, time complexity to search, insert and delete is O(Logn).

Search is similar to search in Binary Search Tree. Let the key to be searched be k. We start 
from root and recursively traverse down. For every visited non-leaf node, if the node has key, 
we simply return the node. Otherwise we recur down to the appropriate child (The child which 
is just before the first greater key) of the node. If we reach a leaf node and don’t find k in 
the leaf node, we return NULL.

*******************************************************************************/ 
/*******************************************************************************
* Problem : [ General Tree ] Trie : Longest Prefix Matching. 
Given a dictionary of words and an input string, find the longest prefix of the string which is also a word in dictionary.

* Input / Output:
Let the dictionary contains the following words:
{are, area, base, cat, cater, children, basement}

Below are some input/output examples:
--------------------------------------
Input String            Output
--------------------------------------
caterer                 cater
basemexy                base
child 

* Algorithms:
We build a Trie of all dictionary words. Once the Trie is built, traverse through it using 
characters of input string. If prefix matches a dictionary word, store current length and look
for a longer match. Finally, return the longest match. 
  
*******************************************************************************/ 
/*******************************************************************************
* Problem : [ General Tree ]
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 
/*******************************************************************************
* Problem : [ General Tree ]
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 
/*******************************************************************************
* Problem : [ General Tree ]
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 

/*******************************************************************************
* Problem : 
* Input / Output: 
* Algorithms:  
*******************************************************************************/ 


/***********************  Start of Driver Program at Here *********************/
#if UNIT_TEST
int main()
{
    test();
}    
#endif


