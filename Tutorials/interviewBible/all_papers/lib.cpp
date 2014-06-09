/*
  Name: Lib progrma 
  Copyright: Interview Bible
  Author: 
  Date: 07/03/14 22:58
  Description:  All linkedlist prgram in place

      
*/


#include<stdio.h>
#include<malloc.h>
#include "lib.h""

/* Binary Tree related Operation Here */
struct bt_node {
	int val;
	bt_node *left;
	bt_node *right;
};

bt_node * get_bt_node(int i)
{
	bt_node * newnode = (bt_node *)malloc(sizeof(bt_node));
	newnode->val =i;
	newnode->left = NULL;
	newnode->right =NULL;
	return newnode;
	
}

void print_inorder(bt_node *r)
{
	if(r!=NULL)
	{
	   print_inorder(r->left);
	   printf("%d, ",r->val);
	   print_inorder(r->right);
	}
}

/*
 
Easy way to contarct a Tree :

*/
bt_node * makeTreeFromString(char *a)
{
   
}

/* Stack Related Operation */

void test()
{
	
	bt_node *r = get_bt_node(1);
	print_inorder(r);
	
}


#if UNIT_TEST
int main()
{
    test();
}    
#endif
