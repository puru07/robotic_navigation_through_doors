
#include "astar.hpp"
#include <queue>
#include <vector>
#include <algorithm>

int main()
{
	int weight = 1;
	int start[2] = {0,0};
	int goal[2] = {99,99};
	int arena[2] = {100,100};

	astar problem1 = astar(start, goal, arena, weight);
	std::vector<node> path;
	int goalCheck = problem1.findPath(path);

	return 0;
}
