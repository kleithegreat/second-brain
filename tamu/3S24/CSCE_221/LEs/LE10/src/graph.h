#include <iostream>
#include <vector>
#include <list>
#include <climits>
#include <queue>
#include <unordered_set>
using namespace std;

class Graph {
    private:
        int n;
        typedef pair<int, int> Edge;
        vector<list<Edge>> v;
        
    public:
        Graph(int size = 2) {
            n = size;
            v.resize(n);
        }

        void addEdge(int x, int y, int w) {
            v[x].push_back(make_pair(y, w));
            v[y].push_back(make_pair(x, w));
        }

        void print() {
            for(int i = 0; i < n; i++) {
                cout << "Node " << i << " is connected to: ";
                for (pair<int,int> j : v[i]) {
                    if(j.first != -1){
                        cout << j.first << " : "<< j.second<<", ";
                    }
                }
                cout << endl;
            }
        }

        vector<pair<int, int>> dijkstra(int startNode) {
            vector<pair<int, int>> p(n, make_pair(INT_MAX, -1));
            p[startNode] = make_pair(0, startNode);

            priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
            pq.push(make_pair(0, startNode));

            while (!pq.empty()) {
                int currNode = pq.top().second;
                int currDist = pq.top().first;
                pq.pop();

                if (currDist > p[currNode].first) {
                    continue;
                }

                for (auto neighbor : v[currNode]) {
                    int nextNode = neighbor.first;
                    int nextDist = currDist + neighbor.second;

                    if (nextDist < p[nextNode].first) {
                        p[nextNode] = make_pair(nextDist, currNode);
                        pq.push(make_pair(nextDist, nextNode));
                    }
                }
            }

            return p;
        }

        string printShortestPath(int startNode, int endNode) {
            vector<pair<int, int>> p = dijkstra(startNode);
            if (p[endNode].first == INT_MAX) {
                return "";
            }

            string path = "";
            int currNode = endNode;
            while (currNode != startNode) {
                path = to_string(currNode) + " " + path;
                currNode = p[currNode].second;
            }
            path = to_string(startNode) + " " + path;

            return path;
        }
};



