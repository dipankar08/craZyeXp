/* Define all Basic String opeartion */
#include<stdio.h>
#include<stdlib.h>
int strlen(char *a){   // Find length of a String.
  int i=0;
  while(*a){ i++;a++;}
  return i;
}
void toLower(char *a){ //convert a string to lower inPlace
  while(*a){
    if(*a>='A' && *a<='Z'){
      *a=*a-'A'+'a';
    }
    a++;
  }
}
char * strcpy(char *a){  //copy a string into one buffer
  char * new =(char*)malloc(sizeof(char)*(strlen(a)+1));
  char *tmp =new;
  while(*a){
    *tmp=*a;
    tmp++;
    a++;
  }
  *tmp=0;
  return new;
}
int strcmp(char *a, char *b){ // same:0, a>b return 1, else -1
  while(*a!= '\0' && *b != '\0'){
    if(*a < *b) return -1;
    if(*a > *b) return +1;
    else{  // when both are same.
      a++;b++; continue;
    }
  }
  if(*a=='\0' && *b =='\0') return 0; //both same
  if(*a =='\0') return -1;
  return +1 ; // here only b is end first
}

char* strdouble(char *a){ // doubeling a string...
  char * new =(char*)malloc(sizeof(char)*(2*strlen(a)+1));
  char *tmp =new;
  char *atmpc=a;
  while(*atmpc){
    *tmp=*atmpc;
    tmp++; atmpc++;
  }
  //copy it again..
  atmpc=a;
  while(*atmpc){
    *tmp=*atmpc;
    tmp++; atmpc++;
  }
  *tmp=0;
  return new;   
}
char *concat(char *a,char*b){ // Concat and return a new joined string..
  char * new =(char*)malloc(sizeof(char)*(strlen(a)+strlen(b)+1));
  char *tmp =new;
  while(*a){
    *tmp=*a;
    tmp++;
    a++;
  }
  while(*b){
    *tmp=*b;
    tmp++;
    b++;
  }
  *tmp=0;
  return new;
}
int matchStart(char *a,char* b){ // is string a start with string b ?
  while(*a && *b){
    if(*a != *b ) return 0;
    a++; b++;
  }
  if(*b == '\0') return 1;
  return 0;
}
int matchEnd(char *a, char *b){ 
  if(strlen(b)> strlen(a)) return 0; // b is bigger than a.
  a= a+ strlen(a) - strlen(b); // setting offset of a to correct postion
  while(*b){
    if(*a != *b) return 0;
    a++;b++;
  }
  return 1;
}
// return index of occ or return -1 if not able to find..
int find(char *a,char *b){ // this is basic find using two loop approach.
  if(strlen(b)> strlen(a)) return -1; // b is bigger than a.
  for(int i=0;i<strlen(a)-strlen(b)+1;i++){
    int flag =1;
    int k  = i;
    for(int j=0;j<strlen(b);j++){
      if(a[k++] != b[j]){ // some char doesnt match,,,
        flag =0;
        break;
      }
    }
    if(flag == 1) return i;
  }
  return -1;
}
// Get Substring by spacifyig data..
char* substr(char *a,int beg,int end){
  if(end >= strlen(a)) return 0;
  char * new =(char*)malloc(sizeof(char)*(end-beg+2));
  char * temp = new;
  int j=0;
  for(int i=beg;i<=end;i++){
    new[j++]=a[i];
  }
  new[j]=0;
  return temp;  
}
void split(char *a,char b){ //<out and n> would be a placeholder of ans
  int count = 0;
  // Fisrt Itr : count the occurance of b
  char *temp =a;
  while(*temp){
    if(*temp == b){
      count++;
    }
    temp++;
  }
  count++;
  //Update ans
  char ** out = malloc(30 * sizeof(char*));
  //Second ITR
  temp =a;
  int i=0;
  out[i++]=a;
  while(*temp){
    if(*temp == b){
      *temp='\0';
      out[i++] = (temp+1);
    }
    temp++;
  }
  printf("\nSplit Ans:");
  for(int i=0;i<count;i++) printf("\n%d:[%s]",i,out[i]);
    
}
char * join( char **a,int n){
  
}

int test(){
  char a[]="DipankAr";
  printf("strlen(%s): %d\n",a,strlen(a));
  toLower(a);printf("toLower: %s\n",a);
  char *b = strcpy(a); printf("Copy is %s\n",b);
  printf("\nstrcmp: %d",strcmp("hellz","aello"));
  printf("\nstrdouble: %s",strdouble("Dipankar"));
  printf("\nconcat: %s",concat("Dipankar","Dutta"));
  printf("\nmatchStart: %d",matchStart("Di","Dip"));
  printf("\nmatchEnd: %d",matchEnd("karr","kar"));
  printf("\nfind: %d",find("Dipankar","ar"));
  printf("\nsubstr: %s",substr("Dipankar",5,7));
  char **out;
  int n;
  char a1[]=":aa::bb:";//Not that is shoud be a const char..
  split(a1,':');
  
  
}

