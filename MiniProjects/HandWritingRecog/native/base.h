/* Define base structure */

struct POINT{
int x;
int y;
};

typedef enum {
U, UR,R,RD,D,DL,L,LU,S
} DIRECTION;

DIRECTION cmp_pt(POINT p1, POINT p2)
{
  if(p1.x==p2.x && p1.y == p2.y) return S;
  else if(p1.x==p2.x && p1.y <p2.y) return L;
  else if(p1.x==p2.x && p1.y > p2.y) return R;
  else if(p1.x < p2.x && p1.y == p2.y) return U;
  else if(p1.x > p2.x && p1.y == p2.y) return D;
  else if(p1.x > p2.x && p1.y > p2.y) return LU;
  else if(p1.x < p2.x && p1.y < p2.y) return RD;
  else if(p1.x > p2.x && p1.y < p2.y) return DL;
  else if(p1.x < p2.x && p1.y > p2.y) return UR ;
  
}

void printdr(DIRECTION d){
if(d==U) printf("%s","U");
if(d==UR) printf("%s","UR");
if(d==R) printf("%s","R");
if(d==RD) printf("%s","RD");
if(d==D) printf("%s","D");
if(d==DL) printf("%s","DL");
if(d==L) printf("%s","L");
if(d==LU) printf("%s","LU");
if(d==S) printf("%s","S");
}
