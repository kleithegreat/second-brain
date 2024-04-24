#include <iostream>
#include <vector>
#include <list>
#include <climits>
#include <queue>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Graph {
    private:
        unordered_map<int, unordered_map<int, int>> adjList;

    public:
        Graph() {};

        bool contains_vertex(int u) {
            return adjList.find(u) != adjList.end();
        }

        bool contains_edge(int u, int v) {
            if (contains_vertex(u) && contains_vertex(v)) {
                return adjList[u].find(v) != adjList[u].end();
            }
            return false;
        }

        void addVertex(int u) {
            if (!contains_vertex(u)) {
                adjList[u] = unordered_map<int, int>();
            }
        }

        void addEdge(int u, int v, int w) {
            addVertex(u);
            addVertex(v);
            adjList[u][v] = w;
            adjList[v][u] = w;
        }

        void removeEdge(int u, int v) {
            if (contains_edge(u, v)) {
                adjList[u].erase(v);
                adjList[v].erase(u);
            }
        }

        void removeVertex(int id) {
            if (contains_vertex(id)) {
                for (auto neighbor : adjList[id]) {
                    adjList[neighbor.first].erase(id);
                }
                adjList.erase(id);
            }
        }

        int numVertices() {
            return adjList.size();
        }

        int getEdgeWeight(int u, int v) {
            if (contains_edge(u, v)) {
                return adjList[u][v];
            }
            return -1;
        }

        vector<pair<int, int>> primMST() {
            vector<pair<int, int>> p;
            if (numVertices() == 0) {
                return p;
            }

            priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
            unordered_set<int> visited;

            int startVertex = adjList.begin()->first;
            visited.insert(startVertex);

            for (auto neighbor : adjList[startVertex]) {
                pq.push({neighbor.second, {startVertex, neighbor.first}});
            }

            while (!pq.empty() && visited.size() < numVertices()) {
                auto minEdge = pq.top();
                pq.pop();
                int weight = minEdge.first;
                int src = minEdge.second.first;
                int dest = minEdge.second.second;

                if (visited.find(dest) == visited.end()) {
                    visited.insert(dest);
                    p.push_back({src, dest});

                    for (auto neighbor : adjList[dest]) {
                        if (visited.find(neighbor.first) == visited.end()) {
                            pq.push({neighbor.second, {dest, neighbor.first}});
                        }
                    }
                }
            }

            return p;
        }
};