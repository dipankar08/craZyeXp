#include<stdio.h>
#include "common.h"
#include<stdlib.h>
#include "dqueue.h"
typedef struct node node;
struct node{
  int val;
  node *left;
  node *right;
};

node * newNode( int val){
  node *n =(node *)malloc (sizeof(node));
  n->val =val;
  n->left = NULL;
  n->right = NULL;
}
/* sampleTree1:
      1
    2   3
  4  5 6  7
8           9
              10
*/
node * sampleTree1(){
  node *n1 = newNode(1),*n2 = newNode(2),*n3 = newNode(3),*n4 = newNode(4),*n5 = newNode(5),
  *n6 = newNode(6),*n7 = newNode(7), *n8 = newNode(8),*n9 = newNode(9),*n10 = newNode(10);  
  n1->left=n2;n1->right=n3;
  n2->left =n4;n2->right=n5;
  n3->left =n6;n3->right=n7;
  n4->left = n8; n7->right=n9;
  n9->right = n10;
  
  return n1;
}

void inorder(node *r){
  if(!r) return;
  inorder(r->left);
  printf("%d ",r->val);
  inorder(r->right);
}
void preorder(node *r){
  if(!r) return;
  printf("%d ",r->val);
  preorder(r->left);
  preorder(r->right);
}
void postorder(node *r){
  if(!r) return;
  postorder(r->left);
  postorder(r->right);
  printf("%d ",r->val);
}

void levelorder(node *r){
  TQueue <node *> q;
  q.enq(r);
  while(!q.isEmpty()){
    node *temp=q.deq();
    printf("%d ",temp->val);
    if(temp->left) q.enq(temp->left);
    if(temp->right) q.enq(temp->right);
  } 
}
int height(node *r){
  if(!r) return 0;
  return MAX(height(r->left),height(r->right))+1;
}
