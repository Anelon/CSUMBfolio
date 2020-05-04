/*
 * HackerRank link: https://www.hackerrank.com/contests/cst370-su20-hw2/challenges/adjacency-list/submissions/code/1323249172
 * Title: 370_hw2_3
 * Abstract: Generate a graph from vertexes and their connections
 * Author: Andrew Bell
 * ID: 1138
 * Date: 4/30/20
 */
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Vertex {
	private:
		vector<Vertex> connections;
		int label = -1;
	public:
		Vertex() {};
		Vertex(int label) {
			this->label = label;
		}
		int getLabel() const {
			return label;
		}
		void addConnection(Vertex &v) {
			connections.push_back(v);
		}
		bool operator<(const Vertex &rhs) {
			return this->label < rhs.label;
		}

		friend ostream &operator<<(ostream &outs, Vertex &v);
};
ostream &operator<<(ostream &outs, Vertex &v) {
	outs << v.label;
	sort(v.connections.begin(), v.connections.end());
	for(const Vertex vert : v.connections) {
		outs << "->" << vert.getLabel();
	}
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
	g.vertices.at(vert1).addConnection(g.vertices.at(vert2));
	return ins;
}

int main() {
	int vertices, edges;
	cin >> vertices >> edges;
	Graph graph(vertices);
	for(int i = 0; i < edges; i++) {
		cin >> graph;
	}
	cout << graph;
}
