#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <regex.h>

#define MAX_ERROR_MSG 0x1000

int main ( int argc, char *argv[] )
{
    char *pattern, *text;  
    if ( argc != 3 ) /* argc should be 2 for correct execution */
    {
        /* We print argv[0] assuming it is the program name */
        printf( "usage: %s filename.\n", argv[0] );
        return 0;
    }
    else 
    {
      pattern = argv[1];
      text = argv[2];
      printf(" Pattern: %s, Text : %s. \n",pattern,text); 
    }
    regex_t r;
    regmatch_t m[1];
    int status = regcomp (&r, pattern, REG_EXTENDED|REG_NEWLINE);
    if (status != 0) {
	char error_message[MAX_ERROR_MSG];
	regerror (status, &r, error_message, MAX_ERROR_MSG);
        printf ("Regex error compiling '%s': %s\n",
                 pattern, error_message);
        return 0;
    }
    int nomatch = regexec (&r, pattern,1, m, 0);
    if (nomatch){
            printf ("No matches.\n");
     }
    else{ 
	printf("Match!!!\n");
	}

return 1;
}
