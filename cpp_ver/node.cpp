#include "node.hpp"

node::node(int *goal,int X = 0,int Y = 0,int cost = 1, int Pkey = 0)
{
	x = X;
	y = Y;
	gcost_ = cost + 1;
	key = getKey(x,y);
	fcost = getFcost(goal);
	pkey_ = Pkey;
}
node::~node(){
	
}
int node::getKey(int X , int Y )
{
	return Y*100 + X;
}

int node::getFcost( int *goal) 
{
	int h1 = x - goal[0];
	int h2 = y - goal[1];
	int h =  int(fabs(h1) + fabs(h2));
	return gcost_ + h;
}

std::vector<node> node::getSuccs(int *goal)
{
 	int x1 = x+1;
 	int x2 = x-1;
 	int y2 = y-1;
 	int y1 = y+1;
 	std::vector<node> succsNode ;
 	succsNode.push_back( node(goal,x1,y1,gcost_,pkey_));
	succsNode.push_back(node(goal,x1,y2,gcost_,pkey_));
	succsNode.push_back( node(goal,x2,y1,gcost_,pkey_));
	succsNode.push_back( node(goal,x2,y2,gcost_,pkey_));
	return succsNode;
}
