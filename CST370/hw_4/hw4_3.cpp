/*
 * HackerRank link: https://www.hackerrank.com/contests/cst370-su20-hw4/challenges/dfs-4/submissions/code/1323652141
 * Title: 370_hw4_3
 * Abstract: Generate a graph from vertexes and their connections and run DFS
 * Author: Andrew Bell
 * ID: 1138
 * Date: 5/17/2020
 */
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Vertex {
	private:
		//changed to pointers hopefully will update
		vector<Vertex*> connections;
		int label = -1;
		int distance = -1;
	public:
		Vertex() {};
		Vertex(int label) {
			this->label = label;
		}
		int getLabel() const {
			return label;
		}
		int getDistance() const {
			return distance;
		}
		void addConnection(Vertex *v) {
			connections.push_back(v);
		}
		bool operator<(const Vertex &rhs) {
			return this->label < rhs.label;
		}
		void DFS(int &dist) {
			if(distance != -1) return;
			distance = dist;
			//cerr << "Visiting " << label << distance << endl;
			sort(connections.begin(), connections.end());
			for(auto vert : connections) {
				if(vert->getDistance() == -1)
					vert->DFS(++dist);
			}
		}

		friend ostream &operator<<(ostream &outs, Vertex &v);
};
ostream &operator<<(ostream &outs, Vertex &v) {
	outs << "Mark[" << v.label << "]:" << v.distance;
	/*
	outs << v.label;
	for(const Vertex *vert : v.connections) {
		outs << "->" << vert->getLabel();
	}
	*/
	return outs;
}

class Graph {
	private:
		vector<Vertex> vertices;
	public:
		Graph() {}
		Graph(int numVertices) {
			for(int i = 0; i < numVertices; i++) {
				vertices.push_back({i});
			}
		}
		void DFS(size_t start) {
			//if no vertexes dont do anything
			int dist = 1;
			if(start < vertices.size()) 
				vertices.at(start).DFS(dist);
		}
		friend ostream &operator<<(ostream &outs, const Graph &g);
		friend istream &operator>>(istream &ins, Graph &g);
};
ostream &operator<<(ostream &outs, const Graph &g) {
	for(Vertex vert : g.vertices) {
		outs << vert << endl;
	}
	return outs;
}
istream &operator>>(istream &ins, Graph &g) {
	int vert1, vert2;
	ins >> vert1 >> vert2;
	g.vertices.at(vert1).addConnection(&g.vertices.at(vert2));
	return ins;
}

int main() {
	int vertices, edges;
	cin >> vertices >> edges;
	Graph graph(vertices);
	for(int i = 0; i < edges; i++) {
		cin >> graph;
	}
	graph.DFS(0);
	cout << graph;
}
