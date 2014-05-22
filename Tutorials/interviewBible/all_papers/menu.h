

#define MAX_MENU 10000
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
 void (*hand)();              /* call back */
 Menu *next ;                /* next shibling */
 struct Menu *child_head;    /* Child head */
 Menu *child_tail;           /* ppinter to last child */
 int c_count;                /* child count */
 struct Menu *p;             /* Link to the parent pointer */
 int tags;                   /* tagging for serach */

};



Menu * getMenuItem(int id,char *title,char *desc,void (*hand)());
void addMenuItem(Menu *m,Menu *p);
Menu* getNthChild(Menu *m, int n);
Menu *getMenuByID( int id);



#define REGISTER_MENU(_pid,_id,_title,_desc,_hand,_tags) do{\
Menu *_t = getMenuItem(_id,_title,_desc,_hand); \
if (_t != NULL) \
 { Menu *_pm = getMenuByID(_pid);\
   addMenuItem(_t,_pm); \
 } \
else \
  printf("Error: menu can't getting added ");\
}while(0);

