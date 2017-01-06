#include <iostream>
#include <math.h>
#include <vector>


class node
{
 private:
	/*  dim of the room */
	static   double door_r_;
	static 	double  * arena_;
	
	// dim of robo
	static  double arm_r_ , rWidth_, rLen_;

	static double dx_,dy_;


public:
	int pkey;
	int gcost_;
	int fcost;
	double x;
	double y;
	int key;

	int d;
	int h;
	int v;


	static void init(double& Door , double * Arena, 
		double& Arm_r, double& RWidth, double& RLen);
	static void init();
	nodenode(int *goal,double X = 0,double Y = 0, int D=0, 
			int H=0, int V=0, int cost = 1, int Pkey = 0);
	~node(){};
	void getSuccs(std::vector<node>& succsNode, int *goal,int& xlim, int& ylim);
	// int getKey(int X, int Y);
	void getFcost( int *goal) ; 
	int getPkey(){return pkey_;};
	int getGcost(){return gcost_;};
};