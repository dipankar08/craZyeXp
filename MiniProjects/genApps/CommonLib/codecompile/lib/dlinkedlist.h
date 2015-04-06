#include<stdio.h>
#include <stdlib.h>
/*Single Linkedlist node*/
typedef struct SNode snode;
struct SNode{
  int val;
  snode *next;
};
snode * getNode( int val){
 snode *nw = (snode* )malloc(sizeof(snode));
  nw->val= val;
  nw->next = NULL;
  return nw;
}
snode *buildLinkedList(int *a,int n){
  snode *s= getNode(a[0]);
  snode *t=s;
  for(int i=1;i<n;i++){
    t->next = getNode(a[i]);
    t=t->next;
  }
  return s;
}
void print(snode *s){
  printf("\nList:");
  while(s!= NULL){
    printf("%d->",s->val);
    s = s->next;
  }
  printf("\n");
}
int test(){
  int a[10]={1,2,3,4,5,6,7,8,9,10};
  snode *s=buildLinkedList(a,10);
  print(s);
}

