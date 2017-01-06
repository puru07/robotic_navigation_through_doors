#include "node.hpp"
#include <cmath>

node::node(double X = 0,double Y = 0, int D=0, 
			int H=0, int V=0, int cost = 1, int Act = 0,int Pkey = 0)
{
	x = X;
	y = Y;
	//theta = Theta;
	d = D;		// 0: closed, 1: open 2: overlap, door interval
	h = H;		// 0: Outside, 1: inside	, side of the door in contact
	v = V;		// 0: Arm , 1: base , part of robot in contact
	gcost_ = cost + 1;
	key_ =  x*100 + y;
	getFcost(goal);
	pkey = Pkey;
}
	double node::door_r_;
	double * node::arena_;

	// dim of robo
	double node::arm_r_ , node::rWidth_, node::rLen_;

	double node::dx_,node::dy_;
 void node::init()
		{
			 door_r_ = 1.0; 
			 arena_[0] = 2.4;
			 arena_[1] = 2.4; 
			 arm_r_ = 1.0; 
			 rWidth_= 0.4; rLen_ = 0.4;
			 dx_ = rWidth_/4;	
			 dy_ = rLen_/4;
		}
 void node::init(double& Door , double * Arena, 
		double& Arm_r, double& RWidth, double& RLen)
		{
			 door_r_= Door; 
			 arena_ = Arena;
			 arm_r_ =Arm_r; 
			 rWidth_=RWidth;  rLen_ =RLen;
			 dx_ = rWidth_/4;
			 dy_ = rLen_/4;
		}
void node::getFcost( int *goal) 
{
	int h1 = x - goal[0];
	int h2 = y - goal[1];
	int h =  int(fabs(h1) + fabs(h2));
	fcost = gcost_ + h;
}

void node::getSuccs(std::vector<node>& succsNode, int *goal,int& xlim, int& ylim)
{
/*
	transitions in SECOND primitives
	(h,v) ==(0,1) -> NOT possible, holding door by base from outside
	(1,1) -> special case, (1,0)-> final/goal case: arm from inside, 
	(0,0)-> initial state

	the only transition possible when in contact with base from inside
	transition from base to arm 
*/	
	int action;
	if (h == 1 && v == 1 && d == 1){
		int vnew = 0;
		action = 5;
		node tempNode = node(x,y,d,h,vnew, gcost,action, key_);
		succsNode.push_back(tempNode);
		return;
	}

	//transition from arm to base and outside to inside
	//(d,h,v) = (1,0,0) -> (1,1,1)

	if (h == 0 and d == 1 and v == 0):
		if (hypot(self.x,self.y) > door_r - arm_r/2)
		{
			int hnew = 1;
			int vnew = 1;
			tempNode = node(x,y,d,hnew,vnew,gcost,action,key_);
			action1 = 4
			action2 = 5
			if (tempNode.stateIsvalid())
			{
				succsNode.push_back(tempNode);
			}
		}
}
