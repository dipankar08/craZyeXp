/*
  Name: Dynamic Prgramming Program
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
#include<conio.h>
#include<string.h>
#include "lib.h"

#define MAX_LEN 9999



/**************  Common Struuct is define here  ***************/
// DO NOT CHANGE
struct result
{
	int max;
	int l;
	int r;
};


/*******************************************************************************
* Problem 1: Fibonacci Series
* I/O:
* Algorithms: f(i) = f(i-1) + f(i-2)
*******************************************************************************/
int fib(int n)
{
	int cache[MAX_LEN] = {0};
	cache[0]=0;
	cache[1] =1;
	for (int i =2;i<=n;i++)
	  cache[i]= cache[i-1]+cache[i-2];
	return cache[n];	
}


/*******************************************************************************
* Problem 2: Ugly Number
* I/O:
* Algorithms: U[i] =min{ 2*U[x],3*U[y],5*U[z] } whre x, y z are the correct pointer to 2,3,5, multiplier
*******************************************************************************/


int ugly(int n)
{
	int U[MAX_LEN]={0};
	int x,y,z;
	x=y=z=1; 
	U[1]=1; /* We will not use 0th Index. */
	
	for (int i=2;i<=n;i++)
	{
		U[i] = MIN(2*U[x],MIN(3*U[y],5*U[z]));
		
		if (U[i]== 2* U[x]) x++;
		if(U[i] == 3* U[y]) y++;
		if(U[i] == 5* U[z]) z++;
	}
	return U[n];

}

/*******************************************************************************
* Problem 3: Find the count of  N-digit Lucky Number, doesnt conayin 13
* I/O:
* Algorithms:
f(i) : count  of N-digit  lucy number 
f(i) = f(i-1)*10 - f(i-2) # fill i-1  
 
*******************************************************************************/

int luckyCount(int n)
{
	long long f[MAX_LEN]={0};
	
	f[1] = 9; // Donest include ZERo
	f[2] = 100 -10 -1; // Doesnt include 0-9 and 13
	
	for (int i=3;i<=n;i++)
	{
		f[i] = f[i-1] * 10 - f[i-2];
	} 
	return f[n];
}

/*******************************************************************************
* Problem 4:  Count N-digt , K based Valid Number donesnt have TWO consicutive Zero
* I/O:
* Algorithms: 
Z(1) = 1; NZ(1) = k-1;
Z(2) = k-1 ; NZ(2) = k*(k-1)-1;
Z(i) = NZ(i-1)*1
NZ(i) = (k-1)* { Z[i-1] + NZ(i-1) }

*******************************************************************************/

int validNumber(int n, int k)
{
	long Z[MAX_LEN] = {0};
	long NZ[MAX_LEN] = {0};
	
	Z[1]=1;  NZ[1]= k-1;
	Z[2]= k-1; NZ[2]= (k-1)*(k-1);
	for (int i=3;i<=n;i++)
	{
		Z[i] = NZ[i-1];
		NZ[i]= (k-1)*(Z[i-1] + NZ[i-1]);
	}
    return Z[n]+NZ[n];

}

/*******************************************************************************
* Problem 5: Flag Problem, We have a Color strope of RED,WHITE,BLUE, count number of way to make flag having n stipe.
having 1) Stipe of same color cannot be placed next to each other
2) blue must be in White and REd or RED or WHITE
* I/O:
* Algorithms:
1. let f(i,w),f(i,r),f(i,b) be the number of valid i length flag ending with w,r,or b resptectvly
2. Ans = f(n,w)+f(i,r)
3. f(i,w) = ?
*******************************************************************************/

/*******************************************************************************
* Problem 6: [ Minimum Sum of squire ]
Given a sequnece of n number, find the minimum sum of squire of grough of 2,3 and 4 from N number. 
* I/O:
* Algorithms:
f(i) : mimimum SOS a[1...i]
f(1) = 0
f(2) =(a1+a2)2
f(3) =(a1+a2+a3)^2
f(4) = min { (a1+a2)2 +(a3+a4)2 , (a1+a2+a3+a4)2 }
f(i) = min {
       (ai+ai-1+ai-2+ai-3)2+f(i-4),
       (Ai+Ai-1 + Ai-2)2 +f(i-3),
       ..
   }
*******************************************************************************/

/*******************************************************************************
* Problem 7: Tri-Tiling
How many way you can make 3 X N retecgle with 2 X1 rect ? 
* I/O:
* Algorithms: N/A
*******************************************************************************/

/*******************************************************************************
* Problem 8: Count Special Number of from 1 to N, A number is spacial if it's binary donet have equla number 
0 and 1. 
* I/O:
* Algorithms:
1. Let's say N is power of 2, then m is log(N) bit's
2. if m is odd, No solution
3. find number of Special number of t-bit
3a. MST of t-bit should be 1:
3.b how to fill up t-1 bit's by t/2 zero and t-1/2 one. => (t-1)!/(t/2)!*(t/2-1)! =>f(t)
4. find f(t+2) and express it f(t)
5. f(t) = 4*(t-1)/t *f(t-2) with f(2) = 1 ( that is 11 only)
6. Ans = f(2)+f(4)+f(6) ...F(m) 

*******************************************************************************/

/*******************************************************************************
* Problem 9:  Count NDD ( Non-decresing -digits)
find number of NDD of length n, whre digit's are in non-decresing order.
* I/O:
* Algorithms:
1. Say input : <x1,x2,x3...xn>
2. f(i,x) is the count of NDD of length i, ending with x [0,9]
3. f(1,X) = 1  X =[0,9]
4. f(i,j) = sum ( f(i-1,t) ) for t = 0..j
5. Ans = sum(f(n,x)) x=[0,9]
*******************************************************************************/

/*******************************************************************************
* Problem 10: Archer's Traval: Given a chess board M X N. Initilly Archar sit in (1,1)
 Cout the number of way it can visit all the cell in chess board exctly once and back to (1,1)
* I/O:
* Algorithms: N/A
*******************************************************************************/

/*******************************************************************************
* Problem 11: Boolean Parenthesis: Given a extression of T and F with AND, OR, XOR.
count number of way do parethesis haviing a Expression value id True 
* I/O:
* Algorithms:
1. Define T(i,j)/F(i,j) Count of parenthesis of getting True/False of expression<xi,xj>
2. T(i,i) = 1 if xi is True or else 0, same dfor F(i,i) i=[0,n]
3. Define teh rule like ..T(M AND N)= T(M) *T(N)
ex for OR opeator at k location:
T(i,j) = sum (T(i,k) * T(k+1,i) + T(i,k)*F(k+1,j) + F(i,k) *T(k+1,j) ) for k =[i,j-1]
4 Chaninging it of length 1,2,3...N.
4.Ans = T[1,n]
 
*******************************************************************************/

/*******************************************************************************
* Problem 12 : Logest palindrome Substring 
* I/O:
* Algorithms:
1. input <x1...xn>
2. f(i,j) max length palindome inside <ai..aj>
3. f(i,i) = True  ; i=[1,n]
   f(i,i+1) = True if a[i]==a[i+1] else Fase.
   f(i,j) = True if a[i] ==a[j] && f(i+1,j-1) else False
4. keep trace max_len in calculation of length 1->2->3....->n

Algo2: Tricky with O(1) Space.
for(int i==1i<n;i++)
{ 1. Take i as a Mid point and find the max length palindome,
  2. do it for even length;
    left = right =i ; len=0
    while(a[left]==a[right]){len+=2;left--;right++}
  3. do it for odd length.
      left =i-1 right =i+1 ;len=1
    while(a[left]==a[right]){len+=2;left--;right++}
}
*******************************************************************************/

void longestPalSubStr(char *a)
{
	int n = strlen(a);
	//int n;
	//STRLEN(a,n);
	bool Tab[n][n];
	
    struct result res;	
	
	//length 1
	for(int i=0;i<n;i++){
		Tab[i][i]=true; //length 1
		res.max=1;res.l =i;res.r=i;
	}
	// Length 2
	for (int i=0;i<n-1;i++)
	{
		if(a[i]==a[i+1])
		  {
		  	Tab[i][i+1]=true;
		  	res.max=2;res.l =i;res.r=i+1;
		  }
		else
		  Tab[i][i+1]=false;
	}
	//Check all substr for length 3 to length N
	for(int len =3;len<=n;len++)
	{
		for(int i =0;i<=n-len;i++)
		{
			int j = i+len-1; //<i,j> is of len
			if(a[i]== a[j] && Tab[i+1][j-1])
			{
				Tab[i][j] = true;
				res.max=len;res.l =i;res.r=j;
			}
			else
			 Tab[i][j]=false;
		}
	}

	printf("\n Maximum pal in %s is  of length %d [%d:%d].",a,res.max,res.l,res.r);
}



/*******************************************************************************
* Problem 13: Longest palindome Sun-sequences. 
* I/O:
* Algorithms:
1. input <x1...xn>
2. f(i,j) max length palindome sub-sequnece inside <ai..aj>
3. f(i,i) = 1  ; i=[1,n]
   f(i,i+1) = 2 if a[i]==a[i+1] else 2.
   f(i,j) = f(i+1,j-1)+2  if a[i] ==a[j]  
   f(i,j) = max( f(i+1,j) , f(i,j-1)  if a[i] !=a[j]  
4. return f(1,n)
not working**
*******************************************************************************/

void longestPalSubSeq(char *a)
{
	int n = strlen(a);
	bool Tab[n][n];
	
	SET_2D_ARRAY_ZERO(Tab,n,n);
	
	
    struct result res;	
	
	//length 1
	for(int i=0;i<n;i++){
		Tab[i][i]= 1; //length 1
	}
	// Length 2
	for (int i=0;i<n-1;i++)
	{
		if(a[i]==a[i+1])
		  {
		  	Tab[i][i+1] = 2;
		  }
		else
		  Tab[i][i+1]=2;
	}
	//Check all substr for length 3 to length N
	for(int len =3;len<=n;len++)
	{
		for(int i =0;i<=n-len;i++)
		{
			int j = i+len-1; //<i,j> is of len
			if(a[i] == a[j])
			{
				Tab[i][j] = 2 + Tab[i+1][j-1] ;
			}
			else
			 Tab[i][j]= MAX(Tab[i+1][j],Tab[i][j-1]);
		}
	}
    PRINT_2D_ARRAY(Tab,n,n);
	printf("\n Maximum pal in %s is  of length %d ",a,Tab[0][n-1]);
}

/*******************************************************************************
* Problem 14: Maximize an Expreesion having +,*
* I/O:
* Algorithms:
1. input <x1...xn>
2. f(i,j) max value while evalution <ai..aj>
3. f(i,i) = ai
   f(i,i+1) = a[i] Op a[i+1]
   f(i,j) =  max ( f(i,k) op f( k+1,j) ) for k in [i..j-1]
4. return f(1,n)
*******************************************************************************/

/*******************************************************************************
* Problem 14A: Maximize an Expreesion having +,*, - 
* I/O:
* Algorithms:
Only max(i,j) cannot solve the probme.
*******************************************************************************/

/*******************************************************************************
* Problem 15: Maximize chain Devison.
Maximize a1/a2/a3/a4/a4/ 
* I/O:
* Algorithms:
1. input <x1...xn>
2. max(i,j) max value while evalution <ai..aj> 
   min(i,j) find min value.
3. min=max(i,i) = ai
   min = max(i,i+1) = a[i] Op a[i+1]
   max(i,j) =  max ( max(i,k) / min( k+1,j) ) for k in [i..j-1]
   min(i,j) =  min ( min(i,k) / max( k+1,j) ) for k in [i..j-1]
4. return max(1,n)
*******************************************************************************/

/*******************************************************************************
* Problem 16: Matrix Chain Multiplication.
Given a Set of matrix A1, A1, A2....An and arry d[0,n]
Ai having  d[i-1] * d[i]
How to do multipliaction such that minimum scalar matiplication can be done.
* I/O:
* Algorithms:
1. input <x1...xn>
2. f(i,j) min value while evalution <ai..aj> 
3. f(i,i) = 0 // No scalar multiplications
   f(i,i+1) = d[i-1] * d[i]*d[i+1]
   f(i,j) =  min ( f(i,k) + f( k+1,j) +d[i-1] *d[k]*d[j] ) for k in [i..j-1]
4. return f(1,n)
*******************************************************************************/

/*******************************************************************************
* Problem 17: Safe Salutation.
Given 2N persion , in a round table, find number of way to do N-hanskake without cross-over
* I/O:
* Algorithms:
1. Lets we a <a1....aN>
2. Chosse an persion i , it can do handshak to n/2 way such that both size must have even ppl.
3. so while handsaking it devide group like <0,N-2>,<2,N-2>,<N-2,0>
let f(i) be the number of such counts.
f(0) = 0 and f(1) =1.
f(i) = sum {f(i) * f(N-2-i)} for i [0,n-2]
return f(n)
Q. Is there any duplicates?
*******************************************************************************/

/*******************************************************************************
* Problem 18: Count Different Binary Free having N-Node.? 
* I/O:
* Algorithms:
Note : binary Tree + node Level matter + left-right chlid matters
1. Let's have level X=[1,2,3...N]
2. Any one can be root and It devide into two parts.
3. let's f(i) count kind of BT
4. f(0) =1; //it;s a Null Tree.
f(1) = 1
f(2) = 4 // as 
f(i) =sum (f(k) *f(n-1-K) for k [0..n-1]
4. Now We can arrage [1..N] in n! way.
5. Ans : n! * f(n)
*******************************************************************************/

/*******************************************************************************
* Problem 18A: Count the number of BST ? 
* I/O:
* Algorithms: Just like Same but no need to multiplication of n!
3. let's f(i) count kind of BST
4. f(0) =1; //it;s a Null Tree.
f(1) = 1
f(2) = 4 // as 
f(i) =sum (f(k) *f(n-1-K) for k [0..n-1]
*******************************************************************************/

/*******************************************************************************
* Problem 19: Count the number of balace of bracking of with N Parenthesis
* I/O:
* Algorithms:
two Rule
1. there is only one way to get parnethesis when there is no brack => it's null :)
2. if N pairs then We can something like A.(B) where total brack used in A and B is N-1

a. let's say f(i) indicate parenthesi of i pairs.
b. f(0) =1
c. f(i) = sum( f(k) * f(i-1 -k)} k =[0...i-1]
d. return f(n)
*******************************************************************************/

/*******************************************************************************
* Problem 20: Count the number of balace patrebthesif of (),{}, and [] in porper oder that
no [] or {} inside ()
no [] insiide {} 
* I/O:
* Algorithms: NA
*******************************************************************************/

/*******************************************************************************
* Problem 21: repeat the Q20 , where max depth allowed to d. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 20: Count all Binary Brackingthing. 
* I/O: ex. ABC =((AB)C),(A(BC)) =>2
* Algorithms:
b(i) = count of binary brcking when we have i simbol.
b(0) = b(1) =0
b(2) = 1//(AB)
b(i) = sum { b(k) * b(n-K)} , whre k =[1..n-1], we are placing Devition at k position, such that each side at lease 1 Simbols.

*******************************************************************************/

/*******************************************************************************
* Problem 20 A: Count all Non_binary Bracking. 
* I/O:
* Algorithms:
Non-Binary means ATLEASET one operation is Ternary or more. Like ABC => (ABC) =>1 way
a. find b(i) for each i= 0,1,,,,n
b.  let t(i) indicete no-binary bracing.
t(0)=t(1) =t(2) = 0
t(3) = 1

t(i) = Sum {
        b(k) *t(n-k)+  //left bin and righ non-bin
        t(k) *b(n-k)+   // left non-bin and rught bin
        t(k) *t(n-k) +  // both non-bin
      }
      k =1...N-1

*******************************************************************************/

/*******************************************************************************
* Problem 21: Composition Table.
Given a Composition table C[n*n] and a expression <x1...xn>.
  find it is can be reduced to S using composiotion table. 
* I/O:
* Algorithms:
lets; define a fucntion f(i,j,a) = true if x[i..j] can be reduce to a , else False.
1. Crete a table T[N][N][S]={False}
2. Start of chain length 1. 
3. f(i,i+1,s) = True if x[i]*x[i+1] =s else False.
4. f(i,j,s) = True if OR [f(i,k,a) && f(k+1,j,b)] for all production a*b=s // We should crete a map.
5. return f(1,n,S) 

*******************************************************************************/

/*******************************************************************************
* Problem 22: String Reconstractuon. 
We have a senences having all space remove, recotscat it when a dict is given to you. 
* I/O:
* Algorithms:
1. input <x1.x2....xn>
2. f(i,i) = true if xi in DICT
3. f(i,i+1) true if x[i:i+1] in DICT
4. f(i,j) = DICT(x[i:j]) OR [OR{ f(i,k) && f(k+1,j)}] for k = [i..j-1]
5. return f(1,n)
*******************************************************************************/

/*******************************************************************************
* Problem 22 A: Max word String Reconstractuon. 
We have a senences having all space remove, recotscat it with max possble word when a dict is given to you. 
* I/O:
* Algorithms:
1. input <x1.x2....xn>
2. f(i,i) = 1 if xi in DICT
3. f(i,i+1) 1 if x[i:i+1] in DICT
4. f(i,j) = max { 1 if DICT(x[i:j]) , [max { f(i,k) + f(k+1,j)}] for k = [i..j-1]
5. return f(1,n)
*******************************************************************************/

/*******************************************************************************
* Problem 22 B: count the way  word String Reconstractuon.
We have a senences having all space remove, how many way u can recotscat it  when a dict is given to you. 
* I/O:
* Algorithms:
1. input <x1.x2....xn>
2. f(i,i) = 1 if xi in DICT
3. f(i,i+1) 1 if x[i:i+1] in DICT
4. f(i,j) = SUM{ 1 if DICT(x[i:j]) + [SUM { f(i,k) * f(k+1,j)}] for k = [i..j-1]
5. return f(1,n)
*******************************************************************************/

/*******************************************************************************
* Problem 23: Optimal String Cut-Copy 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 24:  CFL Recognizier.
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 25: Minimal Substritution in CFL parser. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 26: Optimal BST 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 27: Minimum Waight Traingulalization
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 28: Transitive Clouse of a Grpahn :Warsal Ago
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 29 : All pair shoretst path : Floyed Algo 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 30: String Conversion using fixed cache. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 31: Arbitarage problems: Stock Exchnage
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 32: Jack Staws Puzzle.
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 33: DOT Games. (NIM game)
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 34: Gold Pickup Games.
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 35: Astrik Problem 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 36 : Recognize Scrambled Strings  
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 37 : Minim Insertion to make palindome. O(n2)
* I/O:
* Algorithms:
1. Let;s say input <a1..an>
2. f(i,j) indicate minimum insertion to make it palindoem.
3. f(i,i) = 0 // no insertion.
4. f(i,i+1) = 0 if a[i]==a[i+1] else 1
5. f(i,j) =  f(i+1,j-1) if a[i] ==a[j]
else     = min(f(i+1,j) ,f(i,j-1) } +1
*******************************************************************************/


/*******************************************************************************
* Problem 38 : Break a String with minimum number of palindromes.O(n3)
* I/O:
* Algorithms:
If the string is palindrome, then we simply return 0; No partion required.
2. Let's input <a1...an>
3. f(i,j) func giving minimum cut.
4. f(i,i) =0
5. f(i,i+1) = 1 if a[i]!=a[j] else 0
6. f(i,j) = min(f(i,k)+f(k+1,j)} k = i to j-1 
7. f(i,j) =0 if <i,j> it self is a pal -> to test it make a table uisng DP before.
subdp. g(i,j) =true if a[i:j] is a pal, Find this bollenan matrix in previous run.O(n2)

- We can join f() and g() calculation using tricky way.
*******************************************************************************/

/*******************************************************************************
* Problem 39: Coin  Chnage problem.
We have a coin of RS1,3, and 7. What is the minimum number of coin require to make N ? 
* I/O:
* Algorithms:
- n type of coin<d1...dn>
-we want to get X
f(x) =0
f(x) = min{1+f(x-d[i]) such that x-d[i] >0 for i [1..n]
*******************************************************************************/

/*******************************************************************************
* Problem 40: Count ,how many way mw can make Rs X with N number of coins.? 
* I/O:
* Algorithms:
- n coin type <d1..dn>
- We want to make X,
Sol 1: 
f(x,i) indicate how many way we can make x with firat i-number of coins.
f(0,0) = 1 //base case.
f(x,i) = f(x,i-1) + f(x -d[i],i) when x-d[i] >=0;
way to make x with i coins = way to make x with i-1 coin, without taking i-th coin +
way to make x-d[i] ,while taking i-th coin.( we can take any number of i-th coin)
Time Complexity(O(n2) Space Complexity O(n2)

Sol 2: Reduce to O(n) space.
1. Table[1:X]=0
Table [0] =1
2. for j = 1 to X:
   { for d =d1 to dn
       table[j] = table[j]+ (table[j-d] when j-d >=0)
   }
3. Return table[x]

*******************************************************************************/

/*******************************************************************************
* Problem 41: Minimum jump to reach End.
Given an arry, where intdiace max jump can made from that point. What is the minim jump you can make to get end ? 
* I/O:
* Algorithms:
Input <a1...an>
f(i) indiace minimum jump from i-th location  to end
f(N) =0;
f(i) = 0 when i >=n
f(i) = min (1 + f(i+j)) whre j in[1,d[j] ] 
Ans: f(1)
*******************************************************************************/

/*******************************************************************************
* Problem 42 : Longest Increasing Subsequence. 
* I/O:
* Algorithms:
L[1] = 1
L[i] =  1+ max (L[j]] such that a[i] > a[j] for j in [0..i]
      = 1 , if no such max found. 
Ans : Max(L[1:n]] , as LIS end any point.
*******************************************************************************/

/*******************************************************************************
* Problem 43:  IN BIG SMARTER.
Given a list of touple, find out LIS of it, when fitest item of touple in increasing but second item in decresaing order.
* I/O:
* Algorithms:
1. Sort the touple based on second element in decending order.
2. find LIS for firest eleent
*******************************************************************************/

/*******************************************************************************
* Problem 44: Max-contigouus sub array  sum .
* I/O:
* Algorithms:
1> 3 loops techniwqe O(n3)
sol2 : Reuse sum calculation.
max =0;
for(int i=0;i<n;i++)
{ sum=0;
{ for (j =i;j<n;j+=) <i...j>
  { sum = sum+ a[i] 
   if sum>max max= sum;
  }
}
Sol 3: Devide and Qunquire and O(nlogn) 
Sol 4:MAX_SO_FAR Technique[ Tricky in O9n)
max_so_far =0
max_upto_hare =0
for i 1..n
{
max_upto_hare = max(0,max_upto_hree+a[i])
max_so_far= max(max_so_far,max_upto_hare);
//is_All_neg =False of a[i] >0
}
if (is_all_neg) retrurn smallest int)

*******************************************************************************/

/*******************************************************************************
* Problem 45:  Max _non_cont_ subarray
* I/O:
* Algorithms:
f(i) = max{ a[i] + max{f(j): j in 1..i-2} , f(i-1) }
f(1) = a[1]
f(2) = max(a[2],a[1])
*******************************************************************************/

/*******************************************************************************
* Problem 46: Minimum windows contaisn all chrater 
* I/O:
* Algorithms: Windows techniews.
TARGET_CHAR [1:126]
Need_To_Cover = target_char
win_start =0
win_end =0
while(win_end <n)
{
  while(need_to_cover is not all_zero or neg) //EXPAND WINDOWS
  {
    win_end ++ and decresing the count in need_to_cover;
  }
  //At this point we conver all chratter
  while( need_to is not gereter than 0) // SHINK WINDOW
  { win_start ++ and increse count such tat it sould  not go up ;; Srinking the windors from left;
  }
  // Now it's optimal.
  max = max( max, win_end-win_start );

}

*******************************************************************************/
/*******************************************************************************
* Problem 47: Largest balance 0/1
* I/O:
* Algorithms: 
Sol1 : use 2 loop keep trace 0th and 1th count
sol 2: Efficinet and tricky 
a) Replace all 0 by -1
b) Determine cumalitive c[i] = sum of 1...i
c) Hash the cumative sume, that is H{x} =<i,j,k> such that c[i] =c[j] = c[k]
d) Find largest bt two rule.
d1) find max i such that c[i] =0 that is <0..i> have balance sum
d2) in Each hash, find max diff of <i,j,k> in step c
*******************************************************************************/

/*******************************************************************************
* Problem 48: Longest String without repetaion 
* I/O:
* Algorithms: WinDows Technique.
a. Use a Visited_Array[256]=0;
b) win_left =0;
c) win_write=0, Visited_Array[win_left] =1
while(win_right <n)
{
  while(visisted_array[] does have all 0 and 1)
  {
    win_right ++; Visited_Array[win_right] =++;
  }
  //When break, keep track max_len
  while(visisted_array[] does become have all 0 and 1)
  {
     Visited_Array[win_left] --;win_left ++;
  }
}

*******************************************************************************/


/*******************************************************************************
* Problem 49: Samllest +ve sum Subaary. that is sum ->0
* I/O:
* Algorithms: Windows technique
Sol1 : find All subarray and find sum and keep minimum +ve sum.=>O(n3)
Sol 2: Change sol1 for calcualtion of sum while two loop. O(n2)
Sol 3: Windows Technique.
NA
*******************************************************************************/

/*******************************************************************************
* Problem 50:  Zig Zag problems
Longest ZigZag sequnecs like +ve, _ve,+ve,-ve...
* I/O:
* Algorithms:
P(i) indicae lingest zipzag seq haveing osatve at end
N(i) -- ve at end.
P(i) = 1 //i-h is the first posative from left
N(i) =1 //same


P(i) =1+ max(N(j) where a[i] is +ve and j =[o..i]
N(i) = 1+ max (P(j)//same

Ans = Max(P(i),N(i) ) for i [1..n]
*******************************************************************************/

/*******************************************************************************
* Problem 51: Wavio sequences having 2n+1 elemnt havding firat nelemnt are LIS and last (n+1) element is LDS
* I/O:
* Algorithms:
a.) I[i] => Find LIS of each elemnt ending with A[i]
b) D[i] = find DS of each elemnt sart with A[i] to right.
c) Find x= Max(min(I[i],D[i])) for i =1..n
d) Ans = 2*x +1
*******************************************************************************/

/*******************************************************************************
* Problem 52: Building bridge problem 
We have a rever horixatially having N cites in Upside and N city is word siide.
each have x cordinate. We want to connect them by bRidges.
Find Number of bridges with out any croos over
* I/O:
* Algorithms: NA
Let Up-City (a1....An)
Down City (b1....bn)
(ai,bi) & (aj,bj) can be connected iff a) ai<=aj and bi<=bj or oprrosite.
Thus Qn Becoem.
Given two Set A and B make a relation R ={(ai,bj): ai(-A and bj (- B} maintaina above properties.

Sol 1: On(n2) Approach
Sol 2: Sort A by corinates.
Sol 2: FIND LIS>
*******************************************************************************/

/*******************************************************************************
* Problem 53: Maximum waighted non-overlapping interval 
Given a set of interval havig a waight each, find out max sum waighted non-overlapping interval
* I/O:
* Algorithms: 
a. Array the Interval based on finish time.<a1,a2...an>, waight <w1....wn>
b) f[i] indicae max sum having not overlapping.
f[0]=0
f[1] =w1.
for (int i=1..n)
{
 >>> Serach a interval havng ending time less then start time of i, say this is j 
 >>> this seach can be done by liner O(n) or O(logn)
  f(i) = max (f(i-1) ,wi + f(j)
}
ans: f(n)
Complexity : O(n2 ) or (nlogn)
*******************************************************************************/


/*******************************************************************************
* Problem 54: Finding busyest period in a interval schedule 
Given a set of interval find max-overlapping interval.
* I/O:
* Algorithms:
Sort all staring and ending point <a1....a2n>
busy_this_time indicaete max overallping at any time.
busy_this_time =0;
for i in 1 to 2N.
{ if i is start : busy_this_time ++; max = max(max,busy_this_time);
   if i is end : busy_this_time --;
}
    
*******************************************************************************/

/*******************************************************************************
* Problem 55: Count numbers having abs diffrenecs. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 56: Count lucky Tickts having Sum of first half = sum of second half. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 57:  Job shop problem. Reduce total complication time of N job havong m task execued in m machibe.
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 58:  Optimal Rod -cutting Algo
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 59: Given a multu-stage graph find sortest path from S to T  
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 60: Find the sortest path in a DAG 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 61:  Given a DFA, find fewest move to make a state trsansition from A to B
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 62:  Given a Tree, find out simple sortest path
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 63: Maximum waightest indipendent set of a Tree 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 64: Given a waightest graph, find max gain havinh k steps move from a give starting point. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 65: Vretex cover problem of a Tree/ 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 66: 2-partition Problem
Given a set of numbers,devide into to set, such that sum of diff is minimum 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 67: 3-Partition Probelm.
Given a set of number, devide into 3 set such that it minimize the maximum sum of all set
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 68: K-Balance Partion.
Generalize the solution for 2-Balanace partition for k sets. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem XX: Egg Drop Puzzle 
* I/O:
* Algorithms: N/A
*******************************************************************************/

/*******************************************************************************
* Problem 69: Storing Books on Slaves
Suppose we have n number of books, having thickness <t1..tn> and height <1..hn> The length of
book-sleaf id length L. how the place the book such that it total height of slef become minimum. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 70: Data Compression. 
Given a cache of m text string having max length K. We want to encode a Striing S, using this cache.
How to encode it with using Minimum number of words.  
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 71: Bitonic TSP problem
Given a set of points Pi = <xi,yi> i=[1..n]. We want to visit each point start from left most point 
and go to strictly right direction and reach right most point and then comeback to left most point, such that all points got visited 
exactly once. How to do it with minimum Cost-distance.
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 72: Bubble Sort Distance.
Give a Arry of n number having no duplicates, Find out the minimum number of swap required to sort this./ Find out the inverston of the arry. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 73.: Squire Country
Given a number N, find out the minimum number of squire addition equla to N
Ex. N=18, then two way we ca get it :
18 = 4^2+ 1^2+1^2 and 3^2+3^2
Ands: min(3,2) =2  
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 74: Box Stacking problem:
Given set of n Box. Bi(wi,hi,di)  How to stack the box, one on another such that total height is minimim.
With the constrains, We can place the B1 on B2 if base of B1 is less than base of B2/ 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 75: Nested Dolls probllem. 
You can given n-dolls with height hi and width wi, wecan put a doll x into doll y iff wi<-wj and hi <hj.
Find out what is the maximum nextest doll can be made ?
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 76:  Generalized box staking  Nesting problem.
We have M box with n-dimentainal. that each box has n-dimention <d1...dn>.
Two box can be bnested, that one can be put into another of if all dim of inside box is less than all dimention of outside box.
that is Bi can be nexted into Bj iff dik < djk  for all k[1..n]
Find out maximum possbile nexting.
* I/O:
* Algorithms: N/A
*******************************************************************************/



/*******************************************************************************
* Problem 77: Tower of Cube.
Suppose we have n cube and each has diffenet waight like <w1..wn> also, each face if color by some color.
we can place one cube on another iff:
a) if adjanct color are same.
b) waight of top cuble is less then waight of base cube.
What is the max cuble can be array in this way. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 78: Murcia's Skyline
Suppose we have n building having width wi and height hi,
we say the skyline is incresing if LIS of the building is heigher than LDS of the building.. 
The length of the sequence of buidling is define as Width of building in the sequence,
Find out the skypline ? 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 79: Histoy Greading.
You are ask to sequenec some historical events in chronological order. Student who order all the event is correct order, he will get a full masrks.
farther, if he can;t , he might get a pertila marks, define by below rules:
a) 1 pint for each evet which ranks match to corect rank.
b) 1 pt for each event in longest sequenec which is correct order, relative to another.
Given a ans find out the marks. ( Node max masks can be 2N) 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 80: Elevator Optimizations
I have a N Store building , it is too tall. I want to go from groud to to floor.
It very fasting when ppl press 13,14,15, the my jouney distrib 3 times, as the lift stop 3 times, Instead it can stop at floor 14, and ppl 
can walk to floor 15 and 13 by walk.
1. ppl first eneter the destnation when they enter in groudl floor.
2. We limit elivator can stop upto k -times.such that it minimize total number of floor ppl wlak.up or down,
3. if they are same up/down, we can break a ties , by stppoing at height floor, as it rewuire less energy for going down.
How what is the mimim cost for ppl walk. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 81: Red Blue Robot 
Red and blue are friendly robot, An eval cmputer has loked them up into separte hallways/
1. There are 100 btn in each hall way. Each btn are 1 mtr apart.
2. both robot are in first btn .
3. Robot can make 3 operations:
a. Move left or right, which take 1 sec.
b. Press a btn which take 1 sec.
c. just stay that side, doent do anything.
Given  a sequenec of btn pressing R2,B1,B2,R4, find out minimum tiem required ?
* I/O:
* Algorithms:

*******************************************************************************/

/*******************************************************************************
* Problem 82: 0/1 Knapsack problem.
We have n object having value  vi and waight wi, We also have a Knapsack which can have item of max waight M. 
Find how you pickup the items such that we earrns max value. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 83: Unbounded knapsack.
Just like knapsack, but we can take a object multiple times. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 84: Multiple Source Knapsack.
We have N object again , but 4 varient each and having different value of each varient,
 we can take only one valrient of an object.  Find max value we can earn 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 85: Multiple destination Knapsake. 
* I/O:
* Algorithms:
We have n songs to store into two tape : T1 and T2. Each store have a length li.,
1. A sogs can be stored either in T1 or T2.
2. Acss time is porpotinal to max(Sum(li),sum(lj)} i store in T1 and j store in t2.
3. Find out optimal assinment wich minimize overall worst case accesstiem.
*******************************************************************************/

/*******************************************************************************
* Problem 86: Old Wine in New Bottle.
You have M lit of wine, which need to put into n btl. 
each btl has a charectersisc that we can put minmim x and max y liter wine , 
that we shuld put atlease<x,y> wine in a btl.
Find out what is the minimum number of btl to be used to fill up teh full wine.
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 87: Sum of Subset
Given a Set of n - number , decide whether there is a subset having sum = S
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 88: Fixed Lenggth Subset
Given a Set of n - number , decide whether there is a subset of length K having sum = S,
The length of subset must be K.
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 89 : Varient of Sum of Subset -I
Given a Set S, length L, and vlaue V, Find How many subset of Length L having sume <=V.
1. Find how many diffrent subset .
2. Having length L
3. Having sum <= V 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 90: Load Balanacing.
We want too build a large Scalabe distributed system, milion of user want to store billions of file.
- One way to design of the system would be hash user lohin rage and partition the hash range into equal zise of bucktes
and store the data fro each buckets of users into one server.
- However if number of user is samll , hashing will not achve a balance parttions. We need to rethibk the soution.
We have n server of uqnique hash : h1,h2...hn
We have m server : 1...m
User i have Bi Byte to Store
We need to partion n user into M group. The target is to minimize the load of maximum loadde server. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 91:  Given a set of Sumber <x1...Xn>, Count number of subset having a prime sum.
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 92: Adjacent Bit-count
Given a N -bit string of 0 and 1, adjBit count can be defien as :
Adj(x) = x0*x1 +x[1]*x[2]......+x[n-1]*x[n]  
Given a N and K find how many string can be formed of length N having Adj Count K
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 93: Given two String X and Y find logest commonest sub sequnecs ?(LCS 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 94: Given Two String , find Sorted Common Super Squences (LSS)
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 95: Find the Logest common sub-equence of 3 String X, Y and Z. (3LCSS) 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 96: DNA Sequence alignmnet.
Given a two DNA sequnece (having a,t,g,c) align these two string by placing "_" such that it's properly alignment.
Find out the minimum "_" to be make proper alignmnet 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 97: Maximum Waight matched sub-sequence ?
Given Two sequence T and P, where each ti maps to waight wi. Find out a common subsequece of T and P having maximum waighed sum. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 98: Logest Commom Sub-String /Longest common sufficex.
Given two String X[1..n] and Y[1..n], find the logest string which a substring x and y both. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 99: Edit Distnace,
Given two string A and B, convert A to by folloing opetayion.
a. Insert a char with cost 1
b. Delete a char with cost 2
c. Change a char with cost 3

Find minmum cost to change A to B. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 100:  Minimum number of swap require to convert one permutation to another.
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 101: Maximum Waighed common Subsequenced.
Given two Integer Arry, find lonest connon Subsequnec having maximum waighted sum. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 102 : Count number of Occurnce of a sequnece of a Sequnec in a String. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 103:  Implement DBMS Like comparism with %, _,[c1..cn] and [^c1..cn] 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 104: Given a boolean Matrix M, find largest rect having all 1. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 105: Given a boolean Matrix M, find largest Dimond having all 1. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 106 : Given a integer Matrix M, find largest rect having maximum sum.
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 107: Maximum Size valid rect
Given a dict of million word, find out largest possible rectangele where each word in row(L2R and col(T2D) are valid word/
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 108: Optimal Line Break Algo
Given a Word documnet (n word , having wi size each), having max-line width is l, break into line such it minimum waster space 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 109: Given N interger, How many ordering is possible with < and = operator
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 110: Maximum gain in Cheaker board Problem.
Given a Integer matrix of MXN, move from <0,0> to <n,n> having maximum sum. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 111: Coount possble path in  Cheaker board Problem.
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 112 : Unidirectinal TSP
Give a matrix of mXN,  find the total sum from first coluon to last column , where you can move left to right in rotate way. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 113: MaximumSum in trangle 
Given a lower left trangle matrix, find max sum from top to btoom
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 114 : Paper cutting
You have L * W papers. you can cut the paper  in such way to get max profit. You have a price catelog <li,wi,Pi> 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 115: Dice Throwing.
Given N dices, how many way you can get a sum Atleast M 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 116: Dice Trowing -II
Given m n-D dices, having 1..n writeen in the face,, How many way we can amke sum S, whne all m dice are thow as smae time. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 117: TSP using Dynamic programming
Given a waighted Graph of n-vertices ,Starting from v1 how you can cover all vertices and back to v1 , with minimal cost. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 118: Garage Sale problem
In a file morning, we have n -garage are in sell. the cost of going gi to gj is dij. 
we start form home(g0) and came back to home. We want to buy only subset of garage. 
Maximize the profit while doing - transport cost.  
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 119: Hamiltoniann path.
Given a unwaighted graph find a path s to t that visit every vertex extactly once.
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 120: Two taxi Traversal.
Given a n cities (c1..cn) in X*Y plane. We satrt two taxi A and B from staring position, having enough food,
how to srevre food from left to right visit each city exitly once with mimum route cost. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 121: Bottle nack TSP problems.
Given a Waighted graph G having n-verrices, find a hamiltonian cycle, such that cost of most expansice edge is minimized/ 
* I/O:
* Algorithms: N/A
*******************************************************************************/

/*******************************************************************************
* Problem 122: Suppose you have keyborad having 4 key, A,ctrl+A,crol+C,Ctr+V,
 if you can have max t press of keyboard , hwo many A can be generated. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 123: Make a String balance.
Given a String having n parenthesis string- which in unbalavced, How many minimun String can be injected to amke it balanaces. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 124: Make a String balance -II.
Given n -parenthesi string, how you can concatente such that resutant String is balace.
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 125: patrren in a matrix. Given a charecter Matrix, find a pattern "Dpankat" is presnt in that matrix.
You can serach hoz./vert./dia./crossdia/ 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 126: Raceing
In a race, n -harse, hwo many race can be complited.
Like if 2 horse can be complted in 3 way:
1) both first
2) H1 first and h2 second.
3) H2 first and h1 second. 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 127: Poligon Fusion.
Given a Polugoon having n-verties and N-edge, edage are the operators and vertiges are operation.
We can merge two vertices with op mentioned in the edge joint them and create new verices with resukted value. 
how you can do a fusion, such that it will return maximum Relut.
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 128: Cout Complete Heap tree.
A complete k-ary tree is a k-degree tree in which all leave are in same level.
Given diff level, how many way you can form k-arry complete tree with d-depth 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 129: Chocolet Break.
Given a chokomar of M* N Size, how many way we can break it such that mn 1 X1 caholet can be generated.
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem 130: ChopStick NA
Mr. Tom has 3 chop stcks ( one pair + 1 Xtra) to get some bg food  
* I/O:
* Algorithms: NA
*******************************************************************************/

/*******************************************************************************
* Problem 131: Laziest Mobile typing.
I have nokia 1600 Mobile. we want to type a number using two finger, having minimum movement, we start from * and # location. 
* I/O:
* Algorithms: N/A
*******************************************************************************/

/*******************************************************************************
* Problem : 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : 
* I/O:
* Algorithms:
*******************************************************************************/

/*******************************************************************************
* Problem : 
* I/O:
* Algorithms:
*******************************************************************************/



int main()
{
    printf("**************** Problem of Array **************\n\n");
    
#if 0
    printf("\n fib(5): %d",fib(5));
    printf("\n fib(10): %d",fib(10));
    printf("\n fib(15): %d",fib(15));
    printf("\n fib(150): %d",fib(150));
    
    printf("\n\n ugly(5): %d",ugly(5));
    printf("\n ugly(10): %d",ugly(10));
    printf("\n ugly(15): %d",ugly(15));
    printf("\n ugly(150): %d",ugly(150));

    printf("\n\n luckyCount(3): %d",luckyCount(3));
    printf("\n luckyCount(10): %d",luckyCount(10));
    printf("\n luckyCount(15): %d",luckyCount(15));
    printf("\n luckyCount(150): %d",luckyCount(150));
    
    
    printf("\n\n validNumber(2,10): %d",validNumber(2,10));
    printf("\n validNumber(10): %d",validNumber(10,4));
    printf("\n validNumber(15): %d",validNumber(15,4));
    printf("\n validNumber(150): %d",validNumber(150,4));
    
    longestPalSubStr("abcabcbadef");
    longestPalSubStr("abcddcba");
    longestPalSubStr("abcabcbadef");
    longestPalSubStr("abcabcbadef");
#endif
    longestPalSubSeq("1m2a3d4a555m6");
    longestPalSubSeq("aa");
    
    
    
    
    
    
    
    
    
    
    
    
    printf("\n\n****************** [ E N D ] *******************\n\n");
    getch();
}    
