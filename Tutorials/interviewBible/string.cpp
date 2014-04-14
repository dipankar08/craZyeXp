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
//#include<conio.h>
#include<stdlib.h>

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

/*******************************************************************************
* Problem 3A:  Print a String in Revrse Order, Without actualy revering it
* Input: 
* Output:
* Algorithms:
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
    



/*******************************************************************************
* Problem 5: Print A sentence with "Reverse Word" order 
* Input:
* Output:
* Algorithms:
*******************************************************************************/


/*******************************************************************************
* Problem 6: Find Length of String 
* Input:
* Output:
* Algorithms:
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
* Algorithms:
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
* Input:
* Output:
* Algorithms:
*******************************************************************************/



/*******************************************************************************
* Problem 20: Check s astring has only unique Charecter or Not ? 
* Input:
* Output:
* Algorithms:
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

void remove(char *a,char *b)
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
* Input:
* Output:
* Algorithms:
*******************************************************************************/

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


/*******************************************************************************
* Problem 45: Determine a String is palindoem or not excuding while space. 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 46: Decode : Print all possible messge genaration of a Nokia Mobile type 
* Input:
* Output:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 47: Count number of word in a String 
* Input:
* Output:
* Algorithms:
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
b)Find the first available position in str, i.e., find the first ‘\0′ in str
c) Let the first position be p. Fill x at p, p+d,.. p+(f-1)d

*******************************************************************************/
struct charFreq{ // Item Set
	char c; int f;
};

void swap(charFreq *x, charfreq *y)
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
* Problem 60: Given a Sentence print all anagram together 
* Input:
* Output:
* Algorithms:
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


/*******************************************************************************
* Problem 75 :  remoev whiel space in Single Iteration in place.
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
}    




/*******************************************************************************
* Problem 75:  Arry to integer
* Input:
* Output:
* Algorithms:
Suppot: +ve or -Ve nymber
Suport Floating number
*******************************************************************************/

float atoi(char *a)
{
    int state =1;
    int sign =0;
    int int_sum=0;
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





#if 0
int main()
{
    printf("**************** Problem of Array **************\n\n");
   // char  str1[],str2[],str3[];
    
    //char str[] ="DIPANKAR";
    //printRev(str);
    //printf("\nLength:%d\n",strlen(str));
    //reverseStr(str);
    //printf("Revrse:%s\n",str);
    //reverse1(str,0,strlen(str)-1);
    //printf("Revrse1:%s\n",str);
    
   // char str1[] ="   I   love    Dipankar   ";
   // revWordInSen(str1);
   // printf("Revrse1:%s\n",str1);

   // char str1[] ="   I   love    Dipankar   ";
   // revWordInSen(str1);
   // printf("Revrse1:%s\n",str1);    
    
    //printf("Is Sub:%d\n",isSubStr("Dipankar","Dip"));
    //char str[]= "DIPANKAR";
    //rotateInplace(str,3);
    //printf("Roate Ans :%s",str);
    
    //char str[]="aab";permute(str,0,strlen(str));
    
    //printf("%f",atoi("-10.228"));
    //char str[]= " I love dipabakr \t]]\t\n";
    //remWhiteSpace(str);
    //printf("\nAns :%s",str);
    //char str[]= " I love dipabakr ";
    //char * str1 = replaceby20(str);
    //printf("\nAns :%s",str1);
    //char str[] ="axyyxb";
    //remRepetative(str);
    //printf("Ans: %s",str);
     // printAllInter("abc","123");
     //printf ("Ans: %d",printLognonrep("abccefghimaamy"));
     
     //char str[]="aaabbbcccdddeeefff";
     //remove(str,"aef");
     //printf("Ans: %s",str);
     
     char str[]="aaaaaaaaaaaaaaabcccccccccccccceeeeeeeeeeefffffggggg";
     encode(str);
     printf("Ans: %s",str);
     
   
       printf("\n\n****************** [ E N D ] *******************\n\n");
//    getch();
}    
#endif
int main()
{ 
return 0;
}
