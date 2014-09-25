/* Motion Detector */
#include "base.h"
#include <vector>
// debug : g++ native/DrawBlock.cpp -g -o cmd  && gdb -args ./cmd 

struct OPT_MOTION{
	DIRECTION_TYPE dt;
	int waight;	
	/* Convertion Parms */
	GESTURE_TYPE gt; /*This gesture will be updated based on rules */
	
    OPT_MOTION(DIRECTION_TYPE a, int b){dt=a;waight=b;gt=INVALID_GESTURE_TYPE;}
	
};

class MOTION_DETECTOR
{
private:
POINT *pt_sequence;
int pt_count;
DIRECTION_TYPE * motion_dir;
BOARD * brd;
vector <GESTURE> g_list; /* List of gesture list */

/* board overall Perimeter */
int max_up,max_left,max_right,max_down;
int max_height,max_width;


public:
	MOTION_DETECTOR(){}
	void init( BOARD * b)
	{  /*initilize */	   
	    brd = b;
		max_up=max_left=max_right=max_down=max_height=max_width=0;
	   /* Constricting  pt_sequence*/
	  pt_count = b->getCount();
	  pt_sequence = ( POINT * ) calloc(pt_count,sizeof(POINT));
	  for(int i=0;i<pt_count;i++)
		{ 	pt_sequence[i].x = (b->getRawInputSeq())[i] / (b->getX());
			pt_sequence[i].y = (b->getRawInputSeq())[i] % (b->getX());
			
			/* calculate board overall Perimeter  */
			if(pt_sequence[i].x > max_down ) { max_down= pt_sequence[i].x; }
			else if(pt_sequence[i].x < max_up ) { max_up= pt_sequence[i].x; }
			
			if(pt_sequence[i].y > max_right ) { max_right= pt_sequence[i].y;}
			else if(pt_sequence[i].y < max_left) { max_left= pt_sequence[i].y;}		
			
		}
		
	  cout<<"Print Points\n";
	  for(int i=0;i<pt_count;i++)
		{ 	cout<<"["<< pt_sequence[i].x <<","<<pt_sequence[i].y <<"]";
		}
		
	  cout <<"XXX:"<<max_right<<max_left;
		max_height = max_down - max_up;
		max_width = max_right - max_left;
		
	  /* Contracting motion Sequence */
	  motion_dir = ( DIRECTION_TYPE * ) calloc(pt_count-1,sizeof(DIRECTION_TYPE));	  
	  POINT s = pt_sequence[0];
	  for (int i =1;i<pt_count;i++)
	  {
	     POINT s1 = pt_sequence[i];
		 motion_dir[i-1] = cmp_pt(s,s1); /* Change from s to s1 */
		 s=s1;
	  }
	  cout <<"\n\n Elementary motion :\n";
	  for(int i=0;i<pt_count-1;i++)
	  {
	   printdr(motion_dir[i]);printf("%s","-");
	  }
	  
	  /* Optimizing Motion Sequences */
	  vector <OPT_MOTION *> om_list;
	  OPT_MOTION *start = new OPT_MOTION(motion_dir[0],1);
	  for(int i=1; i< pt_count-1; i++)
	  {
	   if(motion_dir[i] == start->dt )
	   { start->waight++;
	   }
	   else
	   {
	     om_list.push_back(start);
		 start = new OPT_MOTION(motion_dir[i],1);
		}
	  }	  
	  om_list.push_back(start);	  
	  
	  cout <<"\nOPT_MOTION :\n"; for (int i=0;i<om_list.size();i++){ printdr(om_list[i]->dt);cout << om_list[i]->waight <<"--";} cout<<endl;	 
	  
	  /* Constricting Gesture List */
	  
	  int hoz_converstion_cutoff = CONV_CUTOFF_FIXED;//(int) max_width * CONV_CUTOFF;
	  int ver_converstion_cutoff = CONV_CUTOFF_FIXED;//(int) max_height * CONV_CUTOFF ;

	  cout<<"MAX: Height:"<<max_height<<" Width:"<<max_width<<endl; 
	  cout<<"CUTOFF Height:"<<ver_converstion_cutoff<<" Width:"<<hoz_converstion_cutoff<<endl; 
	  
	  /* C Rule 1: Delete node in om_list if some low weight node in between high weight node */
	  int mini_ver_converstion_cutoff=  CR1_CUTOFF;
	  int mini_hoz_converstion_cutoff = CR1_CUTOFF;
	  
	  int track_index = -1;
	  int others_waight = 0;
	  int same_waight=0;
	  for (int i=om_list.size()-1;i>=0;i--) /* chane in vector inside loop */
	  {
		if (((om_list[i]->dt == D || om_list[i]->dt == U) && om_list[i]->waight >= mini_ver_converstion_cutoff  )||
		   ((om_list[i]->dt == L || om_list[i]->dt == R) && om_list[i]->waight >= mini_hoz_converstion_cutoff  ))
		{ 
		   if( track_index == -1)
		   { 
		     track_index = i;
		   }
		   else
		   {
			   //Already we has big one of same DT  && others intermidiate has LOW waight
			   if(( om_list[i]->dt == om_list[track_index]->dt) && others_waight < CUTOFF_IGNORE_LOW_MID_WT )
			   {
			   //delete all node from<track_index..i> and insite simiar node ..
				OPT_MOTION *temp = new OPT_MOTION(om_list[track_index]->dt,om_list[track_index]->waight+same_waight+others_waight+om_list[i]->waight);
				om_list.erase (om_list.begin()+i,om_list.begin()+track_index+1);
				om_list.insert(om_list.begin()+i,temp);
				//cout<<"XXX:";for(int j=0;j<om_list.size();j++){printdr(om_list[j]->dt);} cout<<endl;
				track_index = i ; //As Vector modified start again from track index.. 
		       }
			   else
			   {
			     // with other dt. so try for next items..
				 track_index = i;
			   }		   
		   }
		}
		else if(track_index != -1) /* the process not yet stared,, */
		{
			 // We get some some other low waight node. sum up waight..
			 // add only if it is not have similar track dt
			 if(om_list[i]->dt != om_list[track_index]->dt)
			 {
			   others_waight += om_list[i]->waight; 
			 }
			 else{
			 same_waight += om_list[i]->waight; 
			 }
			 if( others_waight > CUTOFF_IGNORE_LOW_MID_WT) //Opps others own, exceed cutoff
			 {
			   track_index = -1 ;
			   others_waight = 0;
			   same_waight=0;
			 }
		}

	  }	//end of for  
	  
	  cout <<"\n OPT_MOTION (AfterAplying CR1) :\n"; for (int i=0;i<om_list.size();i++){ printdr(om_list[i]->dt);cout << om_list[i]->waight <<"--";} cout<<endl;
		  
	  /* C Rule 1: Delete node in om_list if e-dist(w1,w2) < e ,where w1 and w2 have same waight */
	  
	  /* C Rule 2: Traverse the list and Apply Direct Conversion on Opt Motion List */
	  for (int i=0;i<om_list.size();i++){
		if (om_list[i]->dt == D && om_list[i]->waight >= ver_converstion_cutoff  )
		{
		   om_list[i]->gt = LINE_TO_DOWN; 
		}
		if (om_list[i]->dt == U && om_list[i]->waight >= ver_converstion_cutoff  )
		{
		   om_list[i]->gt = LINE_TO_UP; 
		}
		if (om_list[i]->dt == L && om_list[i]->waight >= hoz_converstion_cutoff  )
		{
		   om_list[i]->gt = LINE_TO_LEFT; 
		}
		if (om_list[i]->dt == R && om_list[i]->waight >= hoz_converstion_cutoff  )
		{
		   om_list[i]->gt = LINE_TO_RIGHT; 
		}
	  }
	  
	  /* C Rule 1: if C1 and C2 are diff gt and Intermediate nodes form a Rotation Event :remove all node and add Rotation Gt  */
	  
	  
	  
	  /* Print conv List */
	  cout <<"\n CONV LIST :\n";
	  for (int i=0;i<om_list.size();i++){
	  if(om_list[i]->gt != INVALID_GESTURE_TYPE){
	  	  PRINT_GESTURE_TYPE(om_list[i]->gt);
		  cout <<"==";
		}
	  }
	  
	  
	  
}
};