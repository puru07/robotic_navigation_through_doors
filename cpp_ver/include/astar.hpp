#include <iostream>
#include "node.hpp"
#include <vector>
class astar
{
public:
	astar(int * Start, int * Goal,int* Arena, int Weight);
	~astar(){};
	void getPath(std::vector<node>& path,node& fNode,std::vector<node>& cList);
	int findPath(std::vector<node>& path);
	int * start;
	int * goal;
	int weight;
	int xlim;
	int ylim;
};