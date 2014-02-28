/******************************************
Given a list of pattern and a text, find out if that text is meeting any of the pattern
./a.out "p1" "p2" "p3" "this ia a text"

******************************************/

#include <sys/types.h>
#include <regex.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_MATCHES 1 //The maximum number of matches allowed in a single string

struct list{
char *ptn;
struct list *next;
};

int match(regex_t *pexp, char *sz) {
	regmatch_t matches[MAX_MATCHES]; //A list of the matches in the string (a list of 1)
	//Compare the string to the expression
	//regexec() returns 0 on match, otherwise REG_NOMATCH
	if (regexec(pexp, sz, MAX_MATCHES, matches, 0) == 0) {
		//printf("\"%s\" matches characters %d - %d\n", sz, matches[0].rm_so, matches[0].rm_eo);
    return 1;
	} else {
		//printf("\"%s\" does not match\n", sz);
    return 0;
	}
}


 
int main ( int argc, char *argv[] )
{
    struct list *patter_list=NULL;   
    char  *text;
    int i;    
    if ( argc < 3 ) /* argc should be 2 for correct execution */
    {
        /* We print argv[0] assuming it is the program name */
        printf( "usage: %s filename.\n", argv[0] );
        return 0;
    } 
         
    for(i =1;i<argc-1; i++)
      { 
        struct list *new = (struct list*) malloc(sizeof(struct list));
        new->ptn = argv[i];
        new->next= NULL;
        if (patter_list == NULL) // First Node.
         { patter_list= new;
         }
        else 
         {
         new->next = patter_list;
         patter_list = new;
         }         
      }
      text = argv[argc-1];
      printf(" Text: %s \n",text); 
      printf("Patters are : ");
      struct list *temp = patter_list;
      while(temp)
      {
      printf("%s ",temp->ptn);
      temp=temp->next;
      }
      printf("\n");
  
	int rv;
  int flag=0;
	regex_t exp; //Our compiled expression
  // Algorithms : For each patten Find the text and if found say.. "hurrayyyy"
  temp = patter_list;
  while(temp)
  {
    //printf("%s ",temp->ptn);
    rv = regcomp(&exp, temp->ptn, REG_EXTENDED);
    if (rv != 0) 
    {
        printf("regcomp failed with %d\n", rv);
    }
    if( match(&exp, text))
    {
    printf("\n>>> Matched %s by %s\n",temp->ptn,text);
    flag =1;
    break;
    }
    temp=temp->next;
  }
  if (flag==0)
    printf(">>> No Match Found\n");
	regfree(&exp);
	return 0;
}
