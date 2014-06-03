#include<stdio.h>
#include<stdlib.h>
#include"lib.h"
#include "menu.h"
#include <string.h>

#include "array.h"
#include "strings.h"
/* Basic marro define Here */
#define WIN_SIZE 80
#define PAGE_SIZE 10

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
  if( p ==NULL || m == NULL)
     return;
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
  (m->hand)();
  printf("\nLike to do more test ?(y/n):");
  scanf("%s",ch); 
  getc(stdin); //read \n
}
while(ch[0] =='y');
}

void display_menu(Menu *m,int page)
{
 char error_status[80]={0};
 while(1)
 {
  system("clear");
  char ch1;
  char ch2;
  int ch;
  PRINT_SEPARATOR('*',WIN_SIZE);
  printf ("Table of Contents for %s \n",m->title) ;
  PRINT_SEPARATOR('*',WIN_SIZE);
  
  PRINT_SEPARATOR('_',WIN_SIZE);
  Menu *c = m->child_head;
  int start= page * PAGE_SIZE + 1;
  int j=1;
  while(j<start)
  {
    c = c->next; j++;
  }
  int i =0;
  while(c!=NULL && i < 10 )
  {
    printf("%5d.    %-20s %-50s\n",j,c->title,c->desc);
    j++; i++;
    c = c->next;
  }
  PRINT_SEPARATOR('_',WIN_SIZE);

  if(*error_status)
  {
   PRINT_SEPARATOR('-',WIN_SIZE);
   printf("ERROR:");
   puts(error_status);
   memset(error_status,0,80);
   PRINT_SEPARATOR('-',WIN_SIZE);
  }
  /* Start reading Input Logic */
  printf("[ <%d - %d>: Select Topics, 0: Exit, u: Up Menu, n: Next, p: Prev ] Your Choice:",start,j-1);
  ch1=getchar();
   ch = 0;
   if((ch1 >= '0' && ch1 <= '9'))
   {  while(ch1 >= '0' && ch1 <= '9')
      {
       ch = ch*10 + (ch1-'0');
       ch1=getchar();
      }
   }
   else
     getc(stdin);// Remove new line
  /* End of reading Input Logic */
  if (ch !=0)
  {
     if(ch >= start && ch <= j-1)
     {
        Menu *sub = getNthChild(m,ch);
        if (sub->c_count >0)
          display_menu(sub,0);
        else if (sub->hand != NULL)
          display_qn(sub);
        else
          strcpy(error_status,"Function not yet implemented");
      }
      else
        strcpy(error_status,"Enter an option within range");
    }
   else if (ch == 0 && ch1 =='\n') /* Press ESC or <0 ENTER> to exist */
   {
     system("clear");
     exit(0);
   }
   else if (ch1 == 72 || ch1 == 'u') /* Up Arrow to go the previous menu */
   { if(m->p != NULL)
       display_menu(m->p,0);
      else
       strcpy(error_status,"This the main menu,Retry");
   }  
   else if( ch1 == 75 || ch1 == 'n')
   {
     if(c != NULL)
       display_menu(m,page+1);
     else
       strcpy(error_status,"No more page .");
   }
   else if( ch1 == 77 || ch1 == 'p')
   {
     if(page > 0)
       display_menu(m,page-1);
     else
       strcpy(error_status,"No previous page .");
   }  
    else
       strcpy(error_status,"Invalid Option Please retry.");
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
REGISTER_MENU(STRING ,-1,"Reverse Word","Revrsing the work in a sentances",test_revWordInSen,0);
REGISTER_MENU(STRING ,-1,"Is a SubSring?","Substring check",test_isSubStr,0) ;
REGISTER_MENU(STRING ,-1,"ROtate inplace","Rotate a string with  place",test_rotateInplace,0 );
REGISTER_MENU(STRING ,-1,"Permutation","Print All permutatuon",test_permute,0);
REGISTER_MENU(STRING ,-1,"Trim a string","Do Left-right trim functon",test_trim,0);
REGISTER_MENU(STRING ,-1,"Repalce by %20","Replace all space by %20",test_replaceby20,0);
REGISTER_MENU(STRING ,-1,"Remove Occ Char","Remove all char if it in second string",test_removeOccInAnother,0);
REGISTER_MENU(STRING ,-1,"Impemt RE","matching a string with a Pattern T having * , ?",test_match,0);
REGISTER_MENU(STRING ,-1,"Encode","Encode a string",test_encode,0);
REGISTER_MENU(STRING ,-1,"Lonest Non-rep substr","Longest Substrring without repetaion",test_printLognonrep,0);
REGISTER_MENU(STRING ,-1,"Interleaved","All Interleabed strung",test_printAllInter,0);
REGISTER_MENU(STRING ,-1,"Remove Adj Rept","Remove Rept",test_remRepetative,-1);
REGISTER_MENU(STRING ,-1,"Remove All White Space","Remove All White Space",test_remWhiteSpace,0);
REGISTER_MENU(STRING ,-1,"aoti","Convert String to signed float",test_my_atoi,-1);
REGISTER_MENU(STRING ,-1,"decode","Decode a String",test_decode,0);


  // Arry 
  REGISTER_MENU(ARRAY ,-1,"inplac Mergee"," Mereg trwo arry inplace",test_InplaceMerge,0);
  REGISTER_MENU(ARRAY ,-1,"Fast Duplicates","Find First duplicate in a sorted arry.",test_getLowerBound,0);  
  REGISTER_MENU(ARRAY ,-1,"StringToIntArray","Convert String to Integer list",test_strTOintList,0);




  REGISTER_MENU(ARRAY ,-1,"inplac Mergee"," Mereg trwo arry inplace",test_InplaceMerge,0);
  REGISTER_MENU(ARRAY ,-1,"Fast Duplicates","Find First duplicate in a sorted arry.",test_getLowerBound,0);
  REGISTER_MENU(ARRAY ,-1,"StringToIntArray","Convert String to Integer list",test_strTOintList,0);
  REGISTER_MENU(ARRAY ,-1,"inplac Mergee"," Mereg trwo arry inplace",test_InplaceMerge,0);
  REGISTER_MENU(ARRAY ,-1,"Fast Duplicates","Find First duplicate in a sorted arry.",test_getLowerBound,0);
  REGISTER_MENU(ARRAY ,-1,"StringToIntArray","Convert String to Integer list",test_strTOintList,0);
  REGISTER_MENU(ARRAY ,-1,"inplac Mergee"," Mereg trwo arry inplace",test_InplaceMerge,0);
  REGISTER_MENU(ARRAY ,-1,"Fast Duplicates","Find First duplicate in a sorted arry.",test_getLowerBound,0);
  REGISTER_MENU(ARRAY ,-1,"StringToIntArray","Convert String to Integer list",test_strTOintList,0);
  REGISTER_MENU(ARRAY ,-1,"inplac Mergee"," Mereg trwo arry inplace",test_InplaceMerge,0);
  REGISTER_MENU(ARRAY ,-1,"Fast Duplicates","Find First duplicate in a sorted arry.",test_getLowerBound,0);
  REGISTER_MENU(ARRAY ,-1,"StringToIntArray","Convert String to Integer list",test_strTOintList,0);
  REGISTER_MENU(ARRAY ,-1,"inplac Mergee"," Mereg trwo arry inplace",test_InplaceMerge,0);
  REGISTER_MENU(ARRAY ,-1,"Fast Duplicates","Find First duplicate in a sorted arry.",test_getLowerBound,0);
  REGISTER_MENU(ARRAY ,-1,"StringToIntArray","Convert String to Integer list",test_strTOintList,0);  
  // Dispaly Menu 
  display_menu(head,0);


  return 0;

}
