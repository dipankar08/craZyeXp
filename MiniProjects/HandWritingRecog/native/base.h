/* Define common structure and utility */

/* define cutoffs */
#define CONV_CUTOFF .15
#define CONV_CUTOFF_FIXED 15

/*CR1 Cutiff*/
#define CR1_CUTOFF 7 /* indiacte maximal Mergable waight */
#define CUTOFF_IGNORE_LOW_MID_WT 10 /* We ally 10 ppl in between */


struct POINT{
	int x;
	int y;
};

/* DIRECTION_TYPE: Indicate the elementary motion */
typedef enum {
	U, // moving up
	UR, //moving up to right
	R, // moving right
	RD, // moving right to down
	D, // moving down
	DL, //moving down to left
	L, //moving left
	LU, //moving left to up 
	S,   // no move
	
	INVALID_DIRECTION_TYPE
} DIRECTION_TYPE;

DIRECTION_TYPE cmp_pt(POINT p1, POINT p2)
{
// motion moving from P1 to p2.
/*
	if(p1.x==p2.x && p1.y == p2.y) return S;
	else if(p1.x==p2.x && p1.y < p2.y) return L;
	else if(p1.x==p2.x && p1.y > p2.y) return R;
	else if(p1.x < p2.x && p1.y == p2.y) return U;
	else if(p1.x > p2.x && p1.y == p2.y) return D;
	else if(p1.x > p2.x && p1.y > p2.y) return LU;
	else if(p1.x < p2.x && p1.y < p2.y) return RD;
	else if(p1.x > p2.x && p1.y < p2.y) return DL;
	else if(p1.x < p2.x && p1.y > p2.y) return UR ;
*/
	if(p1.x==p2.x && p1.y == p2.y) return S;
	else if(p1.x==p2.x && p1.y < p2.y) return R;
	else if(p1.x==p2.x && p1.y > p2.y) return L;
	else if(p1.x < p2.x && p1.y == p2.y) return D;
	else if(p1.x > p2.x && p1.y == p2.y) return U;
	else if(p1.x > p2.x && p1.y > p2.y) return UR;
	else if(p1.x < p2.x && p1.y < p2.y) return DL;
	else if(p1.x > p2.x && p1.y < p2.y) return LU;
	else if(p1.x < p2.x && p1.y > p2.y) return RD ;
	
}

void printdr(DIRECTION_TYPE d){
	if(d==U) printf("%s:","U");
	if(d==UR) printf("%s:","UR");
	if(d==R) printf("%s:","R");
	if(d==RD) printf("%s:","RD");
	if(d==D) printf("%s:","D");
	if(d==DL) printf("%s:","DL");
	if(d==L) printf("%s:","L");
	if(d==LU) printf("%s:","LU");
	if(d==S) printf("%s:","S");
}
/*  end of DIRECTION_TYPE */


/* GESTURE: Indicate the motion structure*/
typedef enum {
	LINE_TO_UP,
	LINE_TO_DOWN,
	LINE_TO_LEFT,
	LINE_TO_RIGHT,	
	
	ROTATE_LEFT_UP,	
	ROTATE_RIGHT_UP,	
	ROTATE_LEFT_DOWN,	
	ROTATE_RIGHT_DOWN,
	ROTATE_UP_LEFT,	
	ROTATE_UP_RIGHT,
	ROTATE_DOWN_LEFT,	
	ROTATE_DOWN_RIGHT,
	
	INVALID_GESTURE_TYPE
	
} GESTURE_TYPE;

void PRINT_GESTURE_TYPE(GESTURE_TYPE g){
	if(g == LINE_TO_UP) printf("%s","LINE_TO_UP");
	if(g == LINE_TO_DOWN) printf("%s","LINE_TO_DOWN");
	if(g == LINE_TO_LEFT) printf("%s","LINE_TO_LEFT");
	if(g == LINE_TO_RIGHT) printf("%s","LINE_TO_RIGHT");
	
	if(g == ROTATE_LEFT_UP) printf("%s","ROTATE_LEFT_UP");
	if(g == ROTATE_RIGHT_UP) printf("%s","ROTATE_RIGHT_UP");
	if(g == ROTATE_LEFT_DOWN) printf("%s","ROTATE_LEFT_DOWN");
	if(g == ROTATE_RIGHT_DOWN) printf("%s","ROTATE_RIGHT_DOWN");
	if(g == ROTATE_UP_LEFT) printf("%s","ROTATE_UP_LEFT");
	if(g == ROTATE_UP_RIGHT) printf("%s","ROTATE_UP_RIGHT");
	if(g == ROTATE_DOWN_LEFT) printf("%s","ROTATE_DOWN_LEFT");
	if(g == ROTATE_DOWN_RIGHT) printf("%s","ROTATE_DOWN_RIGHT");
}

struct GESTURE{
	GESTURE_TYPE gt;
	POINT start;
	POINT end;
	int waight; /* how many points in it */
};


