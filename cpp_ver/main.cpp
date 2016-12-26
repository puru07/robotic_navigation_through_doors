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
	
	return a.fcost > b.fcost;
}

//vector<vector<int> > getPath(node& fNode,vector<node>& cList)
void getPath(vector<node>& path,node& fNode,vector<node>& cList)
{
	 path.push_back(fNode);
	 int i = 0;
	 while (1)
	 {
	 	int pkey = fNode.pkey_;
	 	if (pkey == 0){break;}
	 	vector<node>::iterator searchIt = std::find_if(cList.begin(),cList.end(),searchNode(pkey));
	 	fNode = *searchIt;

	 	path.push_back(fNode);

	 }
	
}

int main()
{
	int arena[2] = {100,100};
	int goal[2] = {99,99};
	std::priority_queue<node> pq;
	vector<int> openlist;
	vector<int>::iterator itOpen;
	vector<node> closedlist;
	node startNode = node(goal,0,0,0,0);
	pq.push(startNode);
	openlist.push_back(startNode.key);
	int goalCheck = 0; 
	node currNode = startNode;
	while(pq.size() != 0)
	{
		currNode = pq.top();
		pq.pop();

		//checking if goal is reached
		if ((currNode.x == goal[0]) && (currNode.y == goal[1]))
			{
				cout<<"goal reached!!"<<endl;
				cout << "total cost is "<<currNode.gcost_<<endl;
				goalCheck = 1;
				break;
			}

		// getting the successors
		vector<node> succs = currNode.getSuccs(goal, arena[0],arena[1]);
		
		for (vector<node>::iterator itSuccs = succs.begin(); itSuccs != succs.end(); ++itSuccs)
		{
			int currKey = itSuccs->key;
			//searching in open list
			itOpen = find(openlist.begin(), openlist.end(),currKey);
			if (itOpen != openlist.end())
			{
			//	cout<<"copy" <<endl;
				continue;
			}
			//searching in the closed list
			vector<node>::iterator searchIt = std::find_if(closedlist.begin(), closedlist.end(),searchNode(currKey));
			if (searchIt != closedlist.end()) 
			{
			//	cout<<"copy cl" <<endl;
				continue;
			}
			pq.push(*itSuccs);
			openlist.push_back(itSuccs->key);
		}
		
		// pushing it in closed list :
		closedlist.push_back(currNode);
		//deleting it from openlist
		openlist.erase(remove(openlist.begin(), openlist.end(), currNode.key), openlist.end());
		

	}
	if (goalCheck == 1)
	{

		std::vector<node> path ;
		getPath(path, currNode,closedlist);
		std::vector<node>::iterator row;

		int temp[2];
		int i = 0;
		cout<<path.size()<<endl;
		for (row = path.begin();row != path.end();++row)
		{
			cout<<"--------"<<++i<<"---------"<<endl;
			cout<<row->x<<" "<<row->y<<endl;
		}
	}
	else
	{
		cout<<"goal not found"<<endl;
	}
	
	cout<<"done!!!"<<endl;
	return 0;
}

