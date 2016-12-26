#include <iostream>
#include <math.h>
#include <vector>

class node
{
private:
	/* data */

public:
	int pkey_;
	
	int gcost_;
	int fcost;
	int x;
	int y;
	int key;

	node(int *goal,int X,int Y ,int cost , int Pkey );
	~node(){};
	void getSuccs(std::vector<node>& succsNode, int *goal,int& xlim, int& ylim);
	// int getKey(int X, int Y);
	void getFcost( int *goal) ; 
	int getPkey(){return pkey_;};
	int getGcost(){return gcost_;};
};