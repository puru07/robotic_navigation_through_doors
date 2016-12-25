#include "node.hpp"
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

class searchNode
{
public: 
	searchNode (const int& KeyToSearch)
	: _key(KeyToSearch)
	{}
	bool operator()(const node& TheNode)
	{
		return _key == TheNode.key;
	}
private:
	int _key;

};
bool operator<(const node& a, const node& b) 
{
	
	return a.fcost < b.fcost;
}

int main()
{
	int goal[2] = {99,99};
	std::priority_queue<node> pq;
	vector<int> openlist;
	vector<int>::iterator itOpen;
	vector<node> closedlist;
	node startNode = node(goal,0,0,0,0);
	pq.push(startNode);
	openlist.push_back(startNode.key);
	closedlist.push_back(startNode);

	while(pq.size() != 0)
	{
		node currNode = pq.top();
		pq.pop();
		itOpen = find(openlist.begin(), openlist.end(),currNode.key);
		if (itOpen == openlist.end())
		{
			continue;
		}
		
		//checking if goal is reached
		if (currNode.x == goal[0] && currNode.y == goal[1])
			{
				cout<<"goal reached!!"<<endl;
				break;
			}

		// getting the successors
		vector<node> succs = currNode.getSuccs(goal);
		
		for (vector<node>::iterator itSuccs = succs.begin(); itSuccs != succs.end(); ++itSuccs)
		{
			int currKey = itSuccs->key;
			vector<node>::iterator searchIt = std::find_if(closedlist.begin(), closedlist.end(),searchNode(currKey));
			if (searchIt == closedlist.end()) 
			{
				continue;
			}
			pq.push(*itSuccs);
			openlist.push_back(itSuccs->key);
		}
		
		// pushing it in closed list :
		closedlist.push_back(currNode);
		//delting it from openlist
		openlist.erase(remove(openlist.begin(), openlist.end(), currNode.key), openlist.end());
		

	}
	cout<<"done!!!"<<endl;
	return 0;
}

