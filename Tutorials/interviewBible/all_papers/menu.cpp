#include<stdio.h>
#include<stdlib.h>
#include"lib.h"
#include <string.h>
/* Basic marro define Here */
#define WIN_SIZE 80

/* Macro for Menu */
#define HEADMENU 0
#define ARRAY 1
#define STRING 2
#define LINKEDLIST 3
#define STACKQUEUE 4
#define TREE 5
#define GRAPH 6
#define BIT 7
#define ALGORITHM 8
#define RECUSTION 9
#define GREADY 10
#define DP 11
#define BACKTRACKING 12
#define DEVIDE_N_CON 13

/* Scan sfacific */
#define IS_DIGIT(x) (x>='0' && x<='9')

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

#define MAX_MENU 10000
struct MenuMaster
{
 struct Menu *menu;
 struct Menu* bitmap[MAX_MENU];
 int menu_count;
}MenuMaster;
struct MenuMaster * mmg ; /* Global Menu master */

struct Menu
{
 int id;                     /*Unique ID */
 char title[80];               /* 2 word title */
 char desc[80];                /* small desc */
 int (*hand)();              /* call back */
 Menu *next ;                /* next shibling */
 struct Menu *child_head;    /* Child head */
 Menu *child_tail;           /* ppinter to last child */
 int c_count;                /* child count */
 struct Menu *p;             /* Link to the parent pointer */
 int tags;                   /* tagging for serach */

};

Menu * getMenuItem(int id,char *title,char *desc,int (*hand)())
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

#define REGISTER_MENU(_pid,_id,_title,_desc,_hand,_tags) do{\
Menu *_t = getMenuItem(_id,_title,_desc,_hand); \
if (_t != NULL) \
 { Menu *_pm = getMenuByID(_pid);\
   addMenuItem(_t,_pm); \
 } \
else \
  printf("Error: menu can't getting added ");\
}while(0);


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
void display_menu(Menu *m)
{
  system("clear");
  int ch;
  PRINT_SEPARATOR('*',WIN_SIZE);
  printf ("Table of Contents for %s ",m->title) ;
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
  while(1)
  {
    printf("\n Enter your choice:\n   Press  <%d  to %d> to select topics. \n   Press 0 to exit or \n   Press 9 to go previous menu\n Your Choice: ",1,m->c_count);
    fflush(stdin);
    scanf("%d",&ch);
    printf("\r\r\r");
    fflush(stdin);
    if (ch == 0)
      exit(0);
  
    else if (ch ==9)
    { if(m->p != NULL)
       display_menu(m->p);
      else
       printf("Error: This the main menu,Retry");
     }  
  
    else if(ch <= m->c_count)
    { 
    Menu *sub = getNthChild(m,ch);
    if (sub->c_count >0)
      display_menu(sub);
    else if (sub->hand != NULL)
      (sub->hand)();
    else
     printf("Error: Function not yet implemented.");
    }
    else
       printf("Error: Invalid Option Please retry:");
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

int hello()
{
printf("hello");
}
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

  REGISTER_MENU(ARRAY,-1,"Print hello World"," Arrry related topics",hello,0);


display_menu(head);


return 0;

}
