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
            return false;
        }

        bool contains_edge(int u, int v) {
            return false;
        }

        void addVertex(int u) {
         
        }

        void addEdge(int u, int v, int w) {
        
        }

        void removeEdge(int u, int v) {
            
        }

        void removeVertex(int id) {
            
        }

        int numVertices() {
            return -1;
        }

        int getEdgeWeight(int u, int v) {
            return -1;
        }

        vector<pair<int, int>> primMST() {
            vector<pair<int, int>> p;
            return p;
        }
};