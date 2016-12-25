#include <iostream>
#include <math.h>
#include <vector>

class node
{
private:
	/* data */
	int pkey_;
	
	int gcost_;
public:
	int fcost;
	int x;
	int y;
	int key;

	node(int *goal,int X,int Y ,int cost , int Pkey );
	~node();
	std::vector<node>  getSuccs(int *goal);
	int getKey(int X, int Y);
	int getFcost( int *goal) ; 
	
};