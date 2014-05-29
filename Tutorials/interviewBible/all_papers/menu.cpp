#include<stdio.h>
#include<stdlib.h>
#include"lib.h"
#include "menu.h"
#include <string.h>

#include "array.h"
#include "strings.h"
/* Basic marro define Here */
#define WIN_SIZE 80


void scan_int_array(char *str, int *beg, int * len)
{
int count =0;
char *a= str;
int state =0;

while(*a!=NULL)
{
 if( state ==0 && IS_DIGIT(*a) )
   {count ++;state =1;}
 if( state ==1 && !IS_DIGIT(*a))
  { state =0;
  }
  a++;
}
*len=count;
beg = (int *) malloc((count*sizeof(int)));
int index=0;
a=str;state =0;
int data=0;
while(*a!=NULL)
{
 if( state ==0 && IS_DIGIT(*a) )
   { state =1;
     data = *a-'0';
   }
 if (state ==1 && IS_DIGIT(*a) )
 { data =data *10 + (*a-'0');
 }
 if( state ==1 && !IS_DIGIT(*a))
  { state =0;
    beg[index++] = data;
  }
  a++;
}
if( state ==1)
  { state =0;
    beg[index++] = data;
  }
}


Menu * getMenuItem(int id,char *title,char *desc,void (*hand)())
{
  if (id != -1 && mmg->bitmap[id] != 0)
   { printf("Error: Key Exist ");
     return NULL;
   }
  if (id == -1) //AUTO GENERATE ID
  { id = ++(mmg->menu_count);
  }
  Menu * m = (Menu *) malloc(sizeof(Menu));
  m->id =id;
  strcpy(m->title,title);
  strcpy(m->desc,desc);
  m->hand = hand;
  m->next = NULL;
  m->child_head = NULL;
  m->child_tail = NULL;
  m->p = NULL;
  m->c_count = 0;
  m->tags = 0;
  mmg->bitmap[id] = m;
  mmg->menu_count = id;
  return m; 
}

void addMenuItem(Menu *m,Menu *p)
{
  if(p->c_count == 0)
  {
  
    p->child_head = m;
    p->child_tail = m;
  }
  else
  {
    p->child_tail->next =m;
    p->child_tail =m;
  }
  p->c_count ++;
  m->p =p;
}


Menu* getNthChild(Menu *m, int n)
{
  if(n > m->c_count  )
    return NULL;
  Menu *c = m->child_head;
  for (int i=1;i<n;i++)
    c = c->next;
  return c;
}

Menu *getMenuByID( int id)
{
 return mmg->bitmap[id];
}

void display_qn( Menu *m)
{
printf ("\n\n");
PRINT_SEPARATOR('_',WIN_SIZE);
printf("Question: %s ?\n",m->desc);
PRINT_SEPARATOR('_',WIN_SIZE);
int i =1;
char ch[10];
do
{
  printf("TEST #%d: \n",i++);
  CLEAR_STDIN;
  (m->hand)();
  printf("Like to do more test ?(y/n):");
  CLEAR_STDIN;
  scanf("%s",ch); 
}
while(ch[0] =='y');
}

void display_menu(Menu *m)
{
 char error_status[80]={0};
 while(1)
 {
  system("clear");
  int ch;
  PRINT_SEPARATOR('*',WIN_SIZE);
  printf ("Table of Contents for %s \n",m->title) ;
  PRINT_SEPARATOR('*',WIN_SIZE);
  
  PRINT_SEPARATOR('-',WIN_SIZE);
  Menu *c = m->child_head;
  int i=1;
  while(c!=NULL)
  {
    printf("%5d.    %-20s %-50s\n",i,c->title,c->desc);
    i++;
    c = c->next;
  }
  PRINT_SEPARATOR('-',WIN_SIZE);
  if(*error_status)
  {
   PRINT_SEPARATOR('-',WIN_SIZE);
   printf("ERROR:");
   puts(error_status);
   memset(error_status,0,80);
   PRINT_SEPARATOR('-',WIN_SIZE);
  }
  printf("[ <%d - %d> : Select Topics, 0 : Exit,   9 : Previous Menu ] Your Choice:",1,m->c_count);
  //CLEAR_STDIN;
  scanf("%d",&ch);
  CLEAR_STDIN;
  
  if (ch == 0)
   {
     system("clear");
     exit(0);
   }
    else if (ch ==9)
    { if(m->p != NULL)
       display_menu(m->p);
      else
       strcpy(error_status,"Error: This the main menu,Retry");
     }  
  
    else if(ch <= m->c_count)
    { 
    Menu *sub = getNthChild(m,ch);
    if (sub->c_count >0)
      display_menu(sub);
    else if (sub->hand != NULL)
      display_qn(sub);
    else
     strcpy(error_status,"Error: Function not yet implemented");
    }
    else
       strcpy(error_status,"Error: Invalid Option Please retry.");
 }
}


/* Initilization menu */
Menu * initMenu()
{
  mmg = (struct MenuMaster *) malloc(sizeof(MenuMaster));
  memset(mmg, 0, sizeof(MenuMaster)) ;
  
  char a[]= "Main Menu";
  Menu *head = getMenuItem(0,a,"Welcome to main List",NULL);
  mmg->menu =head;
  return head;
}

/*sample */

int fact(int i)
{
 if (i<=0)
   return 1;
 else
  return i *fact(i-1);
}
void test_fact()
{
  int i;
  printf("Enter a number: ");
  scanf("%d",&i);
  printf("Fact of %d is %d.\n",i,fact(i));
}


//end of sample
int main()
{
  Menu *head;
  head = initMenu();

  REGISTER_MENU(HEADMENU,ARRAY,"Array","Arrry related topics",NULL,0);
  REGISTER_MENU(HEADMENU,STRING,"String","String related topics",NULL,0);
  REGISTER_MENU(HEADMENU,LINKEDLIST,"LinkedList","Linkedlist related topics",NULL,0);
  REGISTER_MENU(HEADMENU,STACKQUEUE,"Stack & Queue","Stack and Queue related topics",NULL,0);
  REGISTER_MENU(HEADMENU,TREE,"Tree","Tree related topics",NULL,0);
  REGISTER_MENU(HEADMENU,GRAPH,"Graph","Graph related topics",NULL,0);
  REGISTER_MENU(HEADMENU,BIT,"Bit","Bit manupulation related topics",NULL,0);
  REGISTER_MENU(HEADMENU,ALGORITHM,"ALGORITHM","Bit manupulation related topics",NULL,0);

  REGISTER_MENU(ALGORITHM,RECUSTION,"Recustion ","Recurtion manupulation related",NULL,0);
  REGISTER_MENU(ALGORITHM,GREADY,"Gready tech","Gready tech related topics",NULL,0);
  REGISTER_MENU(ALGORITHM,DP,"Dynamic programming","Dynamic p related topics",NULL,0);
  REGISTER_MENU(ALGORITHM,BACKTRACKING,"Backtracking","Backtracking related topics",NULL,0);
  REGISTER_MENU(ALGORITHM,DEVIDE_N_CON,"Devide and Conquire","D&C related topics",NULL,0);

  //register_string();

  REGISTER_MENU(RECUSTION,-1,"Fact","Find Fact of an integer",test_fact,0);

  //String
  REGISTER_MENU(STRING ,-1,"Reverse inplace","reverse a String Inplace",test_reverse,0);
  
  // Arry 
  REGISTER_MENU(ARRAY ,-1,"inplac Mergee"," Mereg trwo arry inplace",test_InplaceMerge,0);
  REGISTER_MENU(ARRAY ,-1,"Fast Duplicates","Find First duplicate in a sorted arry.",test_getLowerBound,0);  
  REGISTER_MENU(ARRAY ,-1,"StringToIntArray","Convert String to Integer list",test_strTOintList,0);
  
  // Dispaly Menu 
  display_menu(head);


  return 0;

}
