#include<stdio.h>
#include "common.h"
#include<stdlib.h>
#include "dqueue.h"
#include <fstream>
#include <iostream>
#include <deque>
#include <iomanip>
#include <sstream>
#include <string>
#include <math.h>
using namespace std;

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


node * sampleTree2(){
  node *n1 = newNode(1),*n2 = newNode(2),*n3 = newNode(3),*n4 = newNode(4),*n5 = newNode(5),
  *n6 = newNode(6),*n7 = newNode(7), *n8 = newNode(8),*n9 = newNode(9),*n10 = newNode(10),*n11 = newNode(11),*n12 = newNode(12),*n13 = newNode(13),*n14 = newNode(14),*n15 = newNode(15),*n16 = newNode(16);
  n1->left=n2;n1->right=n3;
  n2->left =n4;n2->right=n5;
  n3->left =n6;n3->right=n7;
  n4->left = n8; n4->right=n9;
n5->left = n10; n5->right=n11;
n6->left = n12; n6->right=n13;
n7->left = n14; n7->right=n15;
  

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

/*************************
Function prity print 
*************************/
// Find the maximum height of the binary tree
int maxHeight(node *p) {
  if (!p) return 0;
  int leftHeight = maxHeight(p->left);
  int rightHeight = maxHeight(p->right);
  return (leftHeight > rightHeight) ? leftHeight + 1: rightHeight + 1;
}

// Convert an integer value to string
string intToString(int val) {
  ostringstream ss;
  ss << val;
  return ss.str();
}

// Print the arm branches (eg, /    \ ) on a line
void printBranches(int branchLen, int nodeSpaceLen, int startLen, int nodesInThisLevel, const deque<node*>& nodesQueue, ostream& out) {
  deque<node*>::const_iterator iter = nodesQueue.begin();
  for (int i = 0; i < nodesInThisLevel / 2; i++) {  
    out << ((i == 0) ? setw(startLen-1) : setw(nodeSpaceLen-2)) << "" << ((*iter++) ? "/" : " ");
    out << setw(2*branchLen+2) << "" << ((*iter++) ? "\\" : " ");
  }
  out << endl;
}

// Print the branches and node (eg, ___10___ )
void printNodes(int branchLen, int nodeSpaceLen, int startLen, int nodesInThisLevel, const deque<node*>& nodesQueue, ostream& out) {
  deque<node*>::const_iterator iter = nodesQueue.begin();
  for (int i = 0; i < nodesInThisLevel; i++, iter++) {
    out << ((i == 0) ? setw(startLen) : setw(nodeSpaceLen)) << "" << ((*iter && (*iter)->left) ? setfill('_') : setfill(' '));
    out << setw(branchLen+2) << ((*iter) ? intToString((*iter)->val) : "");
    out << ((*iter && (*iter)->right) ? setfill('_') : setfill(' ')) << setw(branchLen) << "" << setfill(' ');
  }
  out << endl;
}

// Print the leaves only (just for the bottom row)
void printLeaves(int indentSpace, int level, int nodesInThisLevel, const deque<node*>& nodesQueue, ostream& out) {
  deque<node*>::const_iterator iter = nodesQueue.begin();
  for (int i = 0; i < nodesInThisLevel; i++, iter++) {
    out << ((i == 0) ? setw(indentSpace+2) : setw(2*level+2)) << ((*iter) ? intToString((*iter)->val) : "");
  }
  out << endl;
}

// Pretty formatting of a binary tree to the output stream
// @ param
// level  Control how wide you want the tree to sparse (eg, level 1 has the minimum space between nodes, while level 2 has a larger space between nodes)
// indentSpace  Change this to add some indent space to the left (eg, indentSpace of 0 means the lowest level of the left node will stick to the left margin)
void printPretty(node *root, int level, int indentSpace, ostream& out) {
  int h = maxHeight(root);
  int nodesInThisLevel = 1;

  int branchLen = 2*((int)pow(2.0,h)-1) - (3-level)*(int)pow(2.0,h-1);  // eq of the length of branch for each node of each level
  int nodeSpaceLen = 2 + (level+1)*(int)pow(2.0,h);  // distance between left neighbor node's right arm and right neighbor node's left arm
  int startLen = branchLen + (3-level) + indentSpace;  // starting space to the first node to print of each level (for the left most node of each level only)
    
  deque<node*> nodesQueue;
  nodesQueue.push_back(root);
  for (int r = 1; r < h; r++) {
    printBranches(branchLen, nodeSpaceLen, startLen, nodesInThisLevel, nodesQueue, out);
    branchLen = branchLen/2 - 1;
    nodeSpaceLen = nodeSpaceLen/2 + 1;
    startLen = branchLen + (3-level) + indentSpace;
    printNodes(branchLen, nodeSpaceLen, startLen, nodesInThisLevel, nodesQueue, out);

    for (int i = 0; i < nodesInThisLevel; i++) {
      node *currNode = nodesQueue.front();
      nodesQueue.pop_front();
      if (currNode) {
        nodesQueue.push_back(currNode->left);
        nodesQueue.push_back(currNode->right);
      } else {
        nodesQueue.push_back(NULL);
        nodesQueue.push_back(NULL);
      }
    }
    nodesInThisLevel *= 2;
  }
  printBranches(branchLen, nodeSpaceLen, startLen, nodesInThisLevel, nodesQueue, out);
  printLeaves(indentSpace, level, nodesInThisLevel, nodesQueue, out);
}

void pprint(node *r){
  //cout << "Tree pretty print with level=1 and indentSpace=0\n\n";
   cout<<"\nPritty print of a Tree:\n"
  // Output to console
  printPretty(r, 1, 0, cout);
}
