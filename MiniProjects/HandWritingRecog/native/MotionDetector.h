/* Motion Detector */
#include "base.h"

class MOTION_DETECTOR
{
private:
POINT *pt_sequence;
DIRECTION * motion_dir;
BOARD * brd;

public:
	MOTION_DETECTOR(){}
	void init( BOARD * b)
	{
	  brd = b;
	  /* Const pt_sequence*/
	  pt_sequence = ( POINT * ) calloc(b->getCount(),sizeof(POINT));
	  for(int i=0;i<b->getCount();i++)
		{ 	pt_sequence[i].x = (b->getRawInputSeq())[i] % (b->getX());
			pt_sequence[i].y = (b->getRawInputSeq())[i] / (b->getX());
		}
	  motion_dir = ( DIRECTION * ) calloc(b->getCount()-1,sizeof(DIRECTION));
	  
	  POINT s = pt_sequence[0];
	  for (int i =1;i<b->getCount();i++)
	  {
	     POINT s1 = pt_sequence[i];
		 motion_dir[i-1] = cmp_pt(s1,s);
		 s=s1;
	  }
	  for(int i=0;i<b->getCount()-1;i++)
	  {
	   printdr(motion_dir[i]);printf("%s","-");
	  }
}
};