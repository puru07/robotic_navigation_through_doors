#include <iostream>
#include "node.hpp"
#include <vector>
class astar
{
	int * start_;
	int xlim_;
	int ylim_;
public:
	astar(int * Start, int * Goal,int* Arena, int Weight);
	~astar(){};
	void getPath(std::vector<node>& path,node& fNode,std::vector<node>& cList);
	int findPath(std::vector<node>& path);
	
	int * goal;
	int weight;

};