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

/*******************************************************************************
* Problem :  Basic Trsing funtinaliries
            1. print String Revrse 
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

int strlen(char *a)
{   int i=0;
    for (i=0;*a;i++,a++);
    return i;
}


/*******************************************************************************
* Problem : Revrse a String with locations
* Input: 
* Output:
* Algorithms:
*******************************************************************************/

void reverse(char *begin, char *end)
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
    
void reverse1(char *a,int start,int end)
{
    if (start<end)
    {   //swap a[strat],a[end]
        char temp =a[start];a[start]=a[end];a[end]=temp;
        reverse1(a,start++,end--);
    }    
}    

/*******************************************************************************
* Problem : Revrsing teh work in a sentances
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
* Problem :  Check SunString Problem
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
* Problem : Rotate A string in K place.
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
* Problem : Print All Permutation of a String
* Input:
* Output:
* Algorithms:
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
* Problem :  Arry to integer
* Input:
* Output:
* Algorithms:
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
* Problem :  remoev whiel space in Single Iteration in place.
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
* Problem :  replace Space by %20 
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
* Problem :  Remove Repetation Curercted in recurion.
* Input:
* Output:
* Algorithms:
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
* Problem : Print All interleaving string
* Input:
* Output:
* Algorithms:
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
* Problem :  Reararnage A1B2C3D4 --> ABCD1234
* Input:
* Output:
* Algorithms:
*******************************************************************************/


void interLeaveRearrange(char *a)
{
return;
}    

/*******************************************************************************
* Problem :  Logest Substring without repetative chracter
* Input:
* Output:
* Algorithms:
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
* Problem :  Minimum windows contains All Character
* Input:
* Output:
* Algorithms:
*******************************************************************************/

void contailsAllChar(char *text,char *all)
{

return;
}    

/*******************************************************************************
* Problem :  Encode String wwwwaaabbc =>w4a3b2c
* Input: 
* Output:
* Algorithms: Scan from Left to right and Keep track the count and print
*******************************************************************************/
void encode(char *a)
{
  char *t =a+1;
  char now =*a;
  a++;
  int count = 1;
  char *int_start;
  while(*a)
  {
    if (*a == now)
    {
      count ++; a++;
    }
    else
    { 
      int_start=t;
      if( count !=1)
      { 
        while(count)
        {
          *t='0'+count % 10;
          t++;
          count=count/10;
        }
        reverse(int_start,t-1);
      }
      count = 0;
      *t++ = *a;
      now = *a;
    }  
  }
  if( count !=1)
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
* Problem :  Find Fast Non -reparation charcter
* Input:
* Output:
* Algorithms: Scan from Right to left and Keep a hash map to keep trace which is occure and keep trace of last repetationg chracter in the Heap. it occure it remove from heap. At last return the root
*******************************************************************************/


/*******************************************************************************
* Problem :  Remove all Charecter from First string whicg occue in second string
* Input:
* Output:
* Algorithms:
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

