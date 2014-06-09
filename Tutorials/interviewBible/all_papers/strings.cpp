/*
  Name: String Problem
  Copyright: Interview Bible
  Author: 
  Date: 07/03/14 22:58
  Description:  All linkedlist prgram in place
  
  Table of Contents:
      1. Convert Arry to list
      2.
      3.
      
*/


#include<stdio.h>
#include<stdlib.h>
#include "lib.h"

int strlen(char *a);

/*******************************************************************************
* Problem 1: Edit Distance: Convert One String To another with minimum Change
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem 2: ->42
* Problem 3 Print a String In revrese order  
* Input:
* Output:
* Algorithms:
Sol1 : Use recustion
Sol2 : Iteration
*******************************************************************************/

void reverse(char *begin, char *end) /* Reverse a String By Location */
{
  char temp;
  while (begin < end)
  {
    temp = *begin;
    *begin = *end;
    *end = temp;
    begin++;end--;
  }
}    
void reverseStr( char *a)
{
   reverse(a,a+strlen(a)-1);   
}
    
void reverse1(char *a,int start,int end) /* Recustion */
{
    if (start<end)
    {   //swap a[strat],a[end]
        char temp =a[start];a[start]=a[end];a[end]=temp;
        reverse1(a,start++,end--);
    }    
}    
void test_reverse()
{
 char str[100];
 printf("Enter the string :");
 gets(str);
 reverse(str,str+strlen(str));
 printf("Ans: %s",str);
}

/*******************************************************************************
* Problem 3A:  Print a String in Revrse Order, Without actualy revering it
* Input: 
* Output:
* Algorithms: Use recusrsion
*******************************************************************************/
void printRev(char *a)
{
    if (*a)
    { printRev(a+1);
      printf("%c",*a);
    }
}




/*******************************************************************************
* Problem 4: Revrsing teh work in a sentances
* Input: I am Dipankar
* Output: Dipankar I am
* Algorithms:
    1. Revrse the Each Word
    2. Revser the full sentances
*******************************************************************************/

void revWordInSen(char *a)
{
    char *word_beg = a;
    char *upto =a;
    while(*upto)
    {
        if( *upto ==' ')
        { char* word_end= upto-1;
          if(word_end>word_beg)
          {
              reverse(word_beg,word_end);
          }
          word_beg = upto + 1;
        }
        upto++;            
    }
    reverse(word_beg,upto-1); // For the last Word
        
    reverse(a,a+strlen(a)-1); // Revrese the fill Sentences
}
    
void test_revWordInSen()
{
 char str[100];
 printf("Enter the string :");
 gets(str);
 revWordInSen(str);
 printf("Ans: %s",str);
}

/*******************************************************************************
* Problem 5: Print A sentence with "Reverse Word" order 
* Input:
* Output:
* Algorithms: Same as prob 4 , just dont revrse at end
*******************************************************************************/


/*******************************************************************************
* Problem 6: Find Length of String 
* Input:
* Output:
* Algorithms: Iterations
*******************************************************************************/
int strlen(char *a)
{   int i=0;
    for (i=0;*a;i++,a++);
    return i;
}

/*******************************************************************************
* Problem 7: Convert a String into Lower case 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem 8: Copy a string 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem 9: Double a String 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem 10: Perform String Concatenations 
* Input:
* Output:
* Algorithms:
*******************************************************************************/



/*******************************************************************************
* Problem 11: Do Lexicograpic Compare of two String 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem 12: Get A substring 
* Input:
* Output:
* Algorithms:
*******************************************************************************/



/*******************************************************************************
* Problem 13: Check Substring or Not ? 
* Input:
* Output:
* Algorithms: Interation with falgs
*******************************************************************************/

bool isSubStr(char *a, char *b)
{
    if (strlen(a)<strlen(b)) return 0;
    
    while(strlen(a)>=strlen(b))
    {
        char *t1 = a;
        char *t2 = b;
        int flag =1;
        while(*t2)
        {
            if (*t1++ != *t2++) {flag=0;break;}
        }
        if (flag == 1) // Total Match DOne 
         return true;
        
        a++;     
    }
    return false;    
}
    
void test_isSubStr()
{
 char str1[100],str2[100];
 printf("Enter the long string :");
 gets(str1);

 printf("Enter the 2nd string :");
 gets(str2);
 
 printf("Ans: %s",isSubStr(str1,str2)?"True":"False");
} 



/*******************************************************************************
* Problem 14: Match with End 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 15 : Rotate A string in K place.
* Input:
* Output:
* Algorithms:
*******************************************************************************/
void rotateInplace( char *a, int k)
{
    for (int i=0;i<k;i++)
    {
        char t = *a;
        for (int j=0;j<strlen(a)-1;j++)
          a[j]=a[j+1];
        a[strlen(a)-1]=t;
    }        
} 

void test_rotateInplace()
{
 char str1[100];
 printf("Enter the long string :");
 gets(str1);
 int i;
 printf("Enter the count :");
 scanf("%d",&i);
 rotateInplace(str1,i);
 printf("Ans: %s",str1);
}  
/*******************************************************************************
* Problem 16: Print Allpermuation of a String 
* Input:
* Output:
* Algorithms:
Pular Algo: SWap and Recurursion.
*******************************************************************************/

void permute(char *a, int start, int len)
{
    if( start==len-1)
     { 
         printf("\n%s",a);
         return;
     }
     for (int i=start;i<len;i++)
     {
         if( a[start] == a[i] &&  i != start) // Remove duplicates 
           continue;
         else
         {
             char temp;
             temp =a[start];a[start]=a[i];a[i]=temp;
             permute(a,start+1,len);
             temp =a[start];a[start]=a[i];a[i]=temp;
         }    
     }        
}    

void test_permute()
{
 char str1[100];
 printf("Enter the long string :");
 gets(str1);
 
 permute(str1,0,strlen(str1));
 //printf("Ans: %s",str1);
} 

/*******************************************************************************
* Problem 17: Print All combination of  a String 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem 18 : Print All poweset of a String 
* Input:
* Output:
* Algorithms:
*******************************************************************************/



/*******************************************************************************
* Problem 18: Given Two String S and T , find if S has all chartet set as T 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem 19: Design Trim Functions 
* Input: <     hell        > => <hell>
* Output:
* Algorithms: Scan from left
*******************************************************************************/
#define IS_WHITE(s) (s == ' ' || s =='\t' || s == '\n')

char *trim (char * in)
{
	char *a = in;
	while(IS_WHITE(*a)) a++;
	
	int n =strlen(in)-1;
	while(n>=0 && IS_WHITE(in[n])) 
	{
		n --;
	}
	in[++n]='\0';
	return a;

}

void test_trim()
{
 char str1[100];
 printf("Enter the long string :");
 gets(str1);
 printf("Ans: %s",trim(str1));
}

/*******************************************************************************
* Problem 20: Check s astring has only unique Charecter or Not ? 
* Input:
* Output:
* Algorithms: Use Bitpams
*******************************************************************************/


/*******************************************************************************
* Problem 21: Remove dupliactes from a string without additinal space. 
* Input:
* Output:
* Algorithms:
*******************************************************************************/



/*******************************************************************************
* Problem 22: Check Two String anagram or Not ! 
* Input:
* Output:
* Algorithms:
Sol1 : Sort two String and Match O(nlogn )+ O(n)
sol2 : Use two counterer 
a. Scan the firat Arry and fill the bitmap with count value.
b. Scan the second arry and decement the count bit map.
c) if anytime goeses negetive return false
d) Can the Bit map and if all zero return True.
*******************************************************************************/


/*******************************************************************************
* Problem 23: Remove all space by %20 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

char * replaceby20(char *a)
{
    // Step 1 :count the space
    char * t =a;
    int count =0;
    while(*t)
    {
        if( *t == ' ') count ++;
        t++;
    }
    char * nw =(char*) malloc(strlen(a)+count *2 +1);
    t =a;
    while(*a)
    {
        if (*a == ' ')
        {
            *t++='%';*t++='2';*t++='0';
            a++;
        }
        else
        {
            *t++ = *a++;
        }    
            
    } 
    *t='\0';
    return nw;   
    
}    

void test_replaceby20()
{
 char str1[100];
 printf("Enter the long string :");
 gets(str1);
 printf("Ans: %s",replaceby20(str1));
}


/*******************************************************************************
* Problem 24: Check a String of a rotation of anotehr of not 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 25:  Find Minium lexicographic Rotation of A string
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 27: Write a Program to Recognize an IP. 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 28: Sort a String in Lexicographic order 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 29: Find Lexicographic samll IDEAL string of length n 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 31.  Find Next Non-repetationg Chrater of a String
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 32: Find logest palindrome of a String 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 33: Find Minimum Insertion required to a make string to be a palindome.
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 34:  Check a string is palindrome or not , The Sixe if Big.
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 35: Remove Spacfic chrater in S , which occue in T inplace.
* Input:
* Output:
* Algorithms:
Sol1: Twoo Loop.
Sol 2: USe Bit Map.
*******************************************************************************/

void removeOccInAnother(char *a,char *b)
{
  int map[256]={0};
  while(*b)
  {
    map[*b]=1;
    b++;
  }
  char *t =a;
  while(*a)
  {
    if (map[*a] ==1)
      { a++; continue;}
    *t =*a;
    t++;a++;
  }
  *t='\0';
}

void test_removeOccInAnother()
{
 char str1[100],str2[100];
 printf("Enter the long string :");
 gets(str1);
 printf("Enter the Second string :");
 gets(str2);
 removeOccInAnother(str1,str2);
 printf("Ans: %s",str1);
}

/*******************************************************************************
* Problem 37: Given a Paragram find max occure words. 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 38: Given a Word and DICT, find next word in dict 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 40: matching a string with a Pattern T having * , ?  
* Input: <P,S>
* Output:
* Algorithms:
a. if both are NULL => TRUe
b. if *P == *s or *p == *  and *s != '0' => match(p+1,s+1)
c. if  *p == * and *p+1 = '\0'&& *second ==ANYTHING  =>True
d. if  *p == * and *(p+1) != NULL && *second ='\0'=> FALSe
e. if *p ==* , then call  match(p+1,s) or match(p,s+1)
f. else false
*******************************************************************************/
bool match(char *first, char * second)
{
    // If we reach at the end of both strings, we are done
    if (*first == '\0' && *second == '\0')
        return true;

    // Make sure that the characters after '*' are present in second string.
    // This function assumes that the first string will not contain two
    // consecutive '*' 
    if (*first == '*' && *(first+1) != '\0' && *second == '\0')
        return false;

    // If the first string contains '?', or current characters of both 
    // strings match
    if (*first == '?' || *first == *second)
        return match(first+1, second+1);

    // If there is *, then there are two possibilities
    // a) We consider current character of second string
    // b) We ignore current character of second string.
    if (*first == '*')
        return match(first+1, second) || match(first, second+1);
    return false;
}
void test_match()
{
 char str1[100],str2[100];
 printf("Enter the long string :");
 gets(str1);
 printf("Enter the Second string(ptn) :");
 gets(str2);
 printf("Ans: %s",match(str2,str1)?"True":"False");
}
/*******************************************************************************
* Problem 42: Reduce a String if Adjacents are same 
* Input:
azxxzy -> ay
caaabbbaacdddd -> Empty
acaaabbbacdddd -> acac
* Output:
* Algorithms:
Sol1 : A simple approach would be to run the input string through multiple passes. 
In every pass remove all adjacent duplicates from left to right. 
Stop running passes when there are no duplicates.
The worst time complexity of this method would be O(n^2).

Sol2: Efficient but Tricky : O(n)
1. Start from the leftmost character and remove duplicates at left corner if there are any.
2. The first character must be different from its adjacent now. Recur for string of length n-1 (string without first character). 
3. Let the string obtained after reducing right substring of length n-1 be rem_str .
 There are three possible cases
 a) If first character of rem_str matches with the first character of original string, remove the first character from rem_str 
 b) Else if the last removed character in recursive calls is same as the first character of the original string. Ignore the first character of original string and return rem_str
 c) Else, append the first character of the original string at the beginning of rem_str .
4. Return rem_str .

*******************************************************************************/

/*******************************************************************************
* Problem 43: Given a Strng S find the minumum substring/Windoes , which cover all Strng IN T 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 44: Encode /Compress a String aaaabbbbcccd -> a5b4c3d 
* Input:
* Output:
* Algorithms:
Scan from Left and keep count of adjucent reetaiong chraterr
*******************************************************************************/
void encode(char *a)
{
  char *t =a+1;
  char now =*a; // Now which charter and which is the count 
  a++;
  int count = 1;
  char *int_start; // Whre to store
  while(*a)
  {
    if (*a == now)
    {
      count ++; a++;
    }
    else
    { 
      int_start=t;
      if( count !=1) // Convert count to digit 1555 --> 5,5,5,1
      { 
        while(count)
        {
          *t='0'+count % 10;
          t++;
          count=count/10;
        }
        reverse(int_start,t-1); // Revrse to get 5,5,5,1 -->1555
      }
      count = 0;
      *t++ = *a;
      now = *a;
    }  
  }
  if( count !=1) // last case to convert .. String = aaaaaaaa => We should get a10
  { 
    int_start=t;
    while(count)
    {
      *t='0'+count % 10;
      t++;
      count=count/10;
    }
    reverse(int_start,t-1);
  }
  *t='\0';
}

void test_encode()
{
 char str1[100],str2[100];
 printf("Enter the long string :");
 gets(str1);
  encode(str1);
 printf("Ans: %s",str1);
}
/*******************************************************************************
* Problem 45: Determine a String is palindoem or not excuding while space. 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 46: Mobile1 : Print all possible messge genaration of a Nokia Mobile type 
* Input:
* Output:
* Algorithms:
*******************************************************************************/
char * mobilePad[10]={" ","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
void printMobileMsg(char *in,char *out,int i)
{
	/* Base case */
	if(! *in)
	{
		out[i]='\0';
		printf("%s\n",out);
	}
	else /* If some more digit left */
	{
		char *key = mobilePad[(*in -'0')];
		while(*key)
		{   out[i]=*key;
			printMobileMsg(in+1,out,i+1);
			key++;
		}
	}
}

void test_printMobileMsg()
{
	char in[]="1234";
	char out[10];
	printMobileMsg(in,out,0);
}


/*******************************************************************************
* Problem 46: Mobile2 : Print a perfact message while typing a number in Nokia Mobile
* Input:
* Output:
* Algorithms: 222 => will print c where as 2<Space>22 indigate ab ; space indiacte wait time.
*******************************************************************************/

void printMobileInboxMsg(char *in, char *out)
{   
    int pre= -1;
    char *ans = out;
    char *key;
	while(*in)
	{   
	   /*  While First Key */
	   if(pre ==-1)
	    {
	       pre= *in-'0';	   
	       key =  mobilePad[pre];	
	    }
	    /* If Space */
		else if(*in == ' ')
		{
			*out = *key; out ++;
			pre =-1;
		}
		/* if rept get the Next charrecter in that key*/
		else if ((*in-'0')== pre)
		{
			key ++; 
			if(!key)
			  key = mobilePad[pre];
		}
		/*if not same */
		else if ((*in-'0')!= pre)
		{
		  *out = *key; out ++;
		   pre= *in-'0';
		   key =  mobilePad[pre];
		}
		in++;
		
	}
	//for last charetcet
	if(pre != -1)
	  {
	  *out = *key; out++;	
	  }
	*out ='\0';
	
	/* Print msg */
	puts(ans);
	  	
}

void test_printMobileInboxMsg()
{
	char in[]="2233345 55";
	char out[10];
	printMobileInboxMsg(in, out);
}


/*******************************************************************************
* Problem 46: Mobile3 : FInd the Integer STrig to be type in a mobile to print the Name " Dipankar Dutta"
* Input:
* Output:
* Algorithms: revrese Algorithm of the previous Question
*******************************************************************************/

/*******************************************************************************
* Problem 47: Count number of word in a String 
* Input:
* Output:
* Algorithms: State Machine Approach.
====================================
The idea is to maintain two states: IN and OUT. 
The state OUT indicates that a separator is seen. 
State IN indicates that a word character is seen. 
We increment word count when previous state is OUT and next character is a word character.

*******************************************************************************/

/*******************************************************************************
* Problem 48: Given a Dict, find given Word S can be formed by any two ord in Dict. 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 49: Given 3 String , S1,S2.S3, find if S1 is interleaved with S1 or S2 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 50: Find Out of order charter in a string 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 51:-> 35
* Problem 52 : Reorsert string as same charter are d-distace appart
* Input:
* Output:
* Algorithms:
Sol 1: This is a gready Approach
Step 1: Traverse the string and find out the Chrater frequnecy list
step 2:  Make the max heap of this list based on frequency
Step 3: Do While maxheap is not empty.
a) Extract the Most frequent character. Let the extracted character be x and its frequency be f. 
b)Find the first available position in str, i.e., find the first ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¹Ã…â€œ\0ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â² in str
c) Let the first position be p. Fill x at p, p+d,.. p+(f-1)d

*******************************************************************************/
#if 0
struct charFreq{ // Item Set
	char c; int f;
};

void swap(charFreq *x, charFreq *y)
{
	charFreq z = *x;
	*x=*y;
	*y=z;
}

//Heap functions ..O(log n)
void maxHeapify( charFeq set[],int i, int heap_size)
{
	int l = i*2+1;
	int r = i*2+2;
	int largest = i;
	
	if( l < heap_size && set[l].f > set[i].f )
	  largest = l;
	if ( r <heap_size && set[r].f > set[largest].f)
	  largest = r;
	
	if (largest ! =i)
	{
		swap(&set[i], &set[largest]);
        maxHeapify(set, largest, heap_size);
	}  
	
}
//buid heap
void buildHeap(charFreq set[], int n)
{
    int i = (n - 1)/2;
    while (i >= 0)
    {
        maxHeapify(set, i, n);
        i--;
    }
}
charFreq extractMax(charFreq set[], int heap_size)
{
    charFreq root = set[0];
    if (heap_size > 1)
    {
        set[0] = set[heap_size-1];
        maxHeapify(set, 0, heap_size-1);
    }
    return root;
}

#endif
/*******************************************************************************
* Problem 53: In a String replace x by a given pattern. 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 54: Given a String squence 0123456789101112131415 .. Find The Index of 150 ? 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 55: Found if an Integer is palindrome or Not ! 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 57: Concatente given words to form a Lexicogramic smallest string 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 59: Rearrage Number to form bigest number 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 60: Given a sequence of words, print all anagrams together 
* Input:
* Output:
* Algorithms:
Sol 1:  Hash Map.
Sol1 : Scan the list and for given word , sort the word and put into a hash map to check anagram
Sol 2: Scan the list and for given word, use bitmap to decide angarma or not
Sol3: Tricky and interesting.
USE Lexicographic tree or ties.
1) Create an empty Trie 
2) One by one take all words of input sequence. Do following for each word 
a) Copy the word to a buffer. 
b) Sort the buffer 
c) Insert the sorted buffer and index of this word to Trie.
 Each leaf node of Trie is head of a Index list. The Index list stores index of words in original sequence. If sorted buffe is already present, we insert index of this word to the index list. 
3) Traverse Trie. While traversing, if you reach a leaf node, traverse the index list. And print all words using the index obtained from Index list.
*******************************************************************************/

/*******************************************************************************
* Problem 61: Convert a1b2c3 --> 1bc123 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 62: Swich all odd then Even,
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 63: Given A string print all dupliacte with count
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 64: Devide a String into n equal parts
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 65: Find first Non-Repetaong chater 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 66:  print list of item, conatis all cahter in S
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 67: Find longest string without repetating chratrers 
* Input:
* Output:
* Algorithms:
>>> Use Windoes Technique.
*******************************************************************************/
int  printLognonrep(char *a)
{
int map[256]={-1};
int max_len =0;
int cur_len =0;
int start=0;
int end =0;
  while(*a)
  {
    if (map[*a] ==-1) //not occue before
      {
        cur_len ++;
        map[*a]=1;
      }
    else //occurated before
      {
        if(cur_len > max_len)
        {
         max_len= cur_len;
        }
        for (int i=0;i<256;i++) {map[i]=-1;}
      }
    a++;
  }
return max_len;
}    

void test_printLognonrep()
{
 char str1[100],str2[100];
 printf("Enter the long string :");
 gets(str1);
 printf("Ans: %d",printLognonrep(str1));
}
/*******************************************************************************
* Problem 69: Print all Interleving String 
* Input:
* Output:
* Algorithms: 
Use Recustion.
*******************************************************************************/

void printAllInter_int(char *a,char *b,char *res,int pos)
{
  if (! *a && ! *b) { res[pos]='\0';printf("%s\n",res);}
  if (*a)
     { 
       res[pos]=*a;
       printAllInter_int(a+1,b,res,pos+1);
     }
  if (*b)
    {
      res[pos]=*b;
      printAllInter_int(a,b+1,res,pos+1);
    }
}
void printAllInter(char *a,char *b)
{
   char *res=(char *) malloc(strlen(a)+strlen(b)+1);
   printAllInter_int(a,b,res,0);
}    
void test_printAllInter()
{
 char str1[100],str2[100];
 printf("Enter the Firest string :");
 gets(str1);
 printf("Enter the second string :");
 gets(str2);
 printf("Ans:");
 printAllInter(str1,str2);
}

/*******************************************************************************
* Problem 70:  Print Lexicograic rank of a String
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 71: print all permuation in sorted order 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 72: Find Lexicogrampic previous number 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 74: recursively Delete All Retative  Chrater? 
* Input:
* Output:
* Algorithms: abbcbbcd ==>ad
Sol1 :  R
*******************************************************************************/

void remRepetative(char *a)
{
    if (!*a)
      return;
     char *t;
     while( a[0] && a[1] && a[0] == a[1])
     { char *t = a+1;
       while(*t) {*(t-1) =*t;} *(t-1) ='\0';
     }
     remRepetative(a+1);
     
     if ( a[0] && a[1] && a[0] == a[1])
     { char *t = a+1;
       while(*t) {*(t-1) =*t;} *(t-1) ='\0';
     }   
}    

void test_remRepetative()
{
 char str1[100],str2[100];
 printf("Enter the Firest string :");
 gets(str1);
 remRepetative(str1);
 printf("Ans:%s",str1);
 
}
/*******************************************************************************
* Problem 75 :  remoev whiel space in Single Iteration in place. Just Like trim
* Input:
* Output:
* Algorithms:
*******************************************************************************/

void remWhiteSpace(char *a)
{
    char *t=a;
    while(*a)
    {
        if( *a ==' ' || *a =='\n' || *a =='\t')
         { a++; continue;}
        *t++ =*a++;
    }   
    *t ='\0'; 
}    


void test_remWhiteSpace()
{
 char str1[100],str2[100];
 printf("Enter the Firest string :");
 gets(str1);
 remWhiteSpace(str1);
 printf("Ans:%s",str1);
 
}

/*******************************************************************************
* Problem 75:  Arry to integer
* Input:
* Output:
* Algorithms:
Suppot: +ve or -Ve nymber
Suport Floating number
*******************************************************************************/

float my_atoi(char *a)
{
    int state =1;
    int sign =0;
    float int_sum=0;
    float f_sum =0;
    float mult=1;
    while(*a)
    {    
        //validation..
        if (*a !='+' || *a !='-' || *a!='.' || !(*a>'0' && *a<'9')) 
          { a++;continue;}
        else if ( *a =='+')
        {
            sign = 1;a++;continue;
        }
        else if (*a =='-')
        { sign = -1;a++;continue;
        }
        else if(*a=='.')
        {
            state = 2, a++; continue; //Mode to float State
        }          
        if( state == 1)
        { int_sum = int_sum*10+ (*a-'0');a++;continue;
        }
        if (state == 2)
        {   mult =mult/10;
            f_sum = f_sum + (*a-'0')/mult;a++;continue;
        }          
        
    }
    return sign*(int_sum+f_sum);    
}    

void test_my_atoi()
{
 char str1[100],str2[100];
 printf("Enter the First string :");
 gets(str1);
 printf("Ans:%f",my_atoi(str1));

}

/*******************************************************************************
* Problem 76 : String to Integer 
* Input: 
* Output:
* Algorithms:

*******************************************************************************/
int strToInt(char *a)
{
	int isPos = 1;
	if (*a =='-')
	   { 
	      isPos = -1; a++;
	   }
	int res =0;
	while(*a)
	{   if(IS_DIGIT(*a))
		  res = res *10 + *a-'0';
		  a++;
	}
	return isPos *res;
}

void test_strToInt()
{
	printf("%d",strToInt("--10u1"));
}

/*******************************************************************************
* Problem 76 : Integer to String
* Input: 
* Output:
* Algorithms:

*******************************************************************************/
void IntToStr(int a,char *out)
{
	int i =0;
	/* IF the number is Negetive*/
	if (a < 0) {
	  out[i++]='-';	
	  a = -a;
	}
	/* Making 120 --> 021 */
	while(a)
	{
		out[i++] = '0'+ (a%10) ;
		a =  a/10; 
	}
	out[i]='\0';
	
	/* Revrsing 021 to 120 */
	if (out[0]=='-')
	  reverse(out+1,out+i-1);
	else
	  reverse(out,out+i-1);	
}

void test_IntToStr()
{
	char out[10]={0};
	IntToStr(-1200001,out);
	printf("%s",out);
}
/*******************************************************************************
* Problem 76 : Decode a String In place  
* Input: ab3d4 -> abbbdddd
* Output:
* Algorithms:

*******************************************************************************/

char * decode( char *in)
{
	int total_count=0;
	char *a = in;
	
	int count =0;
	
	// Step 1 Fine the count .
	while(*a)
	{
		if(IS_CHAR(*a))
		{
			total_count += count;
			a++;
			count =0;
		}
		else
		{   
			count += count *10 + CHAR_TO_DIGIT(*a);
			a++;
		}
	}
	total_count += count;
	//printf("\n Total Char: %d",total_count );
	// Step 2: Cretae a space for that.
	char * out = (char *)malloc((total_count+1)*sizeof(char));	
	
	//Step 3: Scan Again and Replace.
	a = in;
	char *b = out;
	char track = *in;
	count = 0;
    while(*a)
	{
		if(IS_CHAR(*a))
		{   while(count)
		    {
				*b = track;
				 b++; count --;
		    }    
			track = *a;
			count =0;
			a++;
		}
		else
		{   
			count += count *10 + CHAR_TO_DIGIT(*a);
			a++;
		}

	}
	while(count)
	{
	 *b = track;
	  b++; count --;
	}
	*b ='\0';
	
	return out;
	
}

void test_decode()
{
 char str1[100],str2[100];
 printf("Enter the First string :");
 gets(str1);
 printf("Ans:%s",decode(str1));

}


/*******************************************************************************
* Problem 77: Find the first non-repeating character from a stream of characters(G$G) 
* Input:
* Output:
* Algorithms:
Point 1. Non-re
Point 2: Strems of chrater
Sol 1: Use Heap and Hash
a) get a char and push it into stack based on time stamp. old timestap will be in top.
b) read next char
 b1. Serach in hash if found retun not found.
 b2. if not found in hash , serach in Heap
 b3. if found in heap, move into hash.
 b4. if not found push it heap.
c. At any point, if you want to find the dupliacted return TOP of the heap. 

Sol 2: Double Linked List ( front contains the latest one )+ Visited BitMap. O(1)Insert, remove, Lookup

1) Create an empty DLL. Also create two arrays inDLL[] and repeated[] of size 256. 
   inDLL is an array of pointers to DLL nodes. repeated[] is a boolean array, 
   repeated[x] is true if x is repeated two or more times, otherwise false. 
   inDLL[x] contains pointer to a DLL node if character x is present in DLL, 
   otherwise NULL. 

2) Initialize all entries of inDLL[] as NULL and repeated[] as false.

3) To get the first non-repeating character, return character at head of DLL.

4) Following are steps to process a new character 'x' in stream.
  a) If repeated[x] is true, ignore this character (x is already repeated two
      or more times in the stream)
  b) If repeated[x] is false and inDLL[x] is NULL (x is seen first time)
     Append x to DLL and store address of new DLL node in inDLL[x].
  c) If repeated[x] is false and inDLL[x] is not NULL (x is seen second time)
     Get DLL node of x using inDLL[x] and remove the node. Also, mark inDLL[x] 
     as NULL and repeated[x] as true.
- We use the inDLL to make fast lookup for DLL pointers for deletion
- We use fast lookup for repeted.
*******************************************************************************/



/*******************************************************************************
* Problem 78 :  Remove all b and ac from a string recusrively.
* Input:
* Output:
acbac   ==>  ""
aaac    ==>  aa
ababac  ==>   aa
bbbbd   ==>   d

Sol1: SCAN AND WRITE in OUTPUT in Place
a) Initiliaze twovaliriable i, j ; i for input scan and j is for output.
b. read input one by one doing doing i++
c1. if a[i] is b then i++, just ignore
c2. if a[i] is a then a[j++] = a[i++]
c3. if a[i] is c , if a[j] is a then, Vanish AC, i++,j--
c4. if a[i] is c and a[j] is  not a , theen a[j++] =a[i++]
c5. if a[i] is somethig other , just copy input to output.

Sol 2: Algorithms: State Machine Approach : SInagle Pass
The approach is to use two index variables i and j.
We move forward in string using �i� and add characters using index j except �b� and �ac�. 
The trick here is how to track �a� before �c�. An interesting approach is to use a two state machine.
The state is maintained to TWO when previous character is �a�, otherwise state is ONE.
 
1) If state is ONE, then do NOT copy the current character to output if one of the following conditions is true 
� a) Current character is �b� (We need to remove �b�) 
� b) Current character is �a� (Next character may be �c�) 
2) If state is TWO and current character is not �c�, we first need to make sure that we copy the previous character �a�. 
Then we check the current character, if current character is not �b� and not �a�, then we copy it to output.
*******************************************************************************/

char * remove_a_bc(char *in)
{
	int j =-1; //end of output
	char *a = in;
	while(*a)
	{
		if (*a == 'b')
		{
			a++; //ignore b
		}
		else if (j == -1)
		{
			in[++j] = *a; a++;
		}
		
		else if (*a =='a')
		{
			in[++j]=*a;a++;
		}
		else if (*a =='c')
		{
			if (in[j] == 'a')
			{
				j--; a++ ;// ac found hence vanish ac
			}
			else
			{
				in[++j] =*a; a++;
			}
		}
		else
		{
			in[++j] =*a;a++;
		}
	}
	in[++j]='\0';
	//printf("%s",in);
	return in;
}


/*******************************************************************************
* Problem 79:  Pattern match with * and ? , where * is the 0 or more repitation of prev charcter
* Input: a*b --> b,ab,aaaab,aaaaab,
a? =>ac,ad.aa etc,
* Output:
* Algorithms: 
a. if both Null => True
b. if ptn is ?, then next simbol is not null and do recusrsion.
b. if last simbol and next char is not a *, then definate match
c. if next is *, then * match logic
*******************************************************************************/

bool ptn_serach(char *p,char *s)
{
	if (*p == '\0' && *s =='\0') return true;
	
	else if( *p == '?')
	{
		if (*s =='\0') return false;
		else return ptn_serach(p+1,s+1);
	}
	else if (*(p+1) =='\0' || *(p+1) !='*') //exect matchs
	{
		if (*p == *s) return ptn_serach(p+1,s+1);
		else return false;
	}
	else if (*(p+1) =='*') // Start match
	{
		if (*s =='\0') return ptn_serach(p+2,s);
		if (*s == *p) return ptn_serach(p,s+1);
		else return ptn_serach(p+2,s);
	}

}


/*******************************************************************************
* Problem 80: Given a continuous stream of strings, maintain strings such that duplicate are eliminated on the fly.
* The interviewer wanted working code. So coded the solution during the interview and emailed it to him 10 mins after.  
* Input:
* Output:
* Algorithms:
* Solution 1: use List and a Hash Map.
* a. Create hash map and Empty List.
* b. read a string from the stream.
* c. Process the String as below:
*   1. Sort the String in O(mlogm)
*   2. Do a Lookup on Hash map ( if Exist egnore the string)
*   3. if Doenst exits, also insert in list
* d. Print the list Anytime if you want to get the non-dupliacte string appers till now.
* 
* Solution 2: You can use Lexicographic tree, rather than a Hash to detect duplicates.
*******************************************************************************/


/*******************************************************************************
* Problem :  Given a String convert base b1 to b2 .
* Input:
* Output:
* Algorithms:
COnvert the base1 => Decimal => base2
*******************************************************************************/


void convertBase(char *in,char *out,int b1,int b2)
{
	int ans =0; // This will store decimal.
	int p =0;
	for (int i = strlen(in)-1;i>=0;i--)
	{
		ans += CHAR_TO_DIGIT(in[i])*pow(b1,p);
		p++;
	}
	
	for(int i=0;ans;i++)
	{
		out[i]=DIGIT_TO_CHAR(ans % b2);
		ans =ans/b2;
	}
	reverse(out,out+strlen(out)-1);
}

void test_convertBase()
{
	char in[10]="A";
	char out[10]={0};
	convertBase(in,out,16,2);
	puts(out);
	
	
}

/*******************************************************************************
* Problem : 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem : 
* Input:
* Output:
* Algorithms:
*******************************************************************************/




/*******************************************************************************
* Problem : 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem : 
* Input:
* Output:
* Algorithms:
*******************************************************************************/



#if UNIT_TEST
int main()
{
    test();
}    
#endif















