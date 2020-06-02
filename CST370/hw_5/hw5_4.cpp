/*
 * HackerRank link: https://www.hackerrank.com/contests/cst370-su20-hw5/challenges/connect-components/submissions/code/1324020704
 * Title: 370_hw5_4
 * Abstract: Find nodes that aren't connected and connect them
 * Author: Andrew Bell
 * ID: 1138
 * Date: 6/2/20
 */
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <climits>
#include <cmath>
#include <set>
using namespace std;

template <class T>
class Vertex {
	private:
		set<Vertex> connections;
		T label = {};
		bool seen = false;
		int connected = 0;
	public:
		Vertex() {};
		Vertex(T label) { this->label = label; }
		T getLabel() const { return label; }
		bool getSeen() const { return seen; }
		void setSeen(bool newSeen) { seen = newSeen; }
		set<Vertex>& getConnections() {return connections;}

		void addConnection(Vertex &v) {
			connections.insert(v);
		}
		void addConnected() { connected++; }
		void removeConnected() { connected--; }
		int getConnected() const { return connected; }

		bool operator<(const Vertex &rhs) const {
			return this->label < rhs.label;
		}
		bool operator==(const Vertex &rhs) const {
			return this->label == rhs.label;
		}

		static bool sortByLabel(const Vertex &a, const Vertex &b) {
			return a.first.label < b.first.label;
		}

		friend ostream& operator<<(ostream& outs, const Vertex<T>& v) {
			outs << v.label;
			for(auto vert : v.connections)
				outs << " " << vert.getLabel();
			return outs;
		}
		void print() {
			cout << *this << endl;
		}
};


template <class T>
class Graph {
	private:
		map<T, Vertex<T>> vertices;
	public:
		Graph() {}
		Graph(vector<Vertex<T>> vertices) {
			for(const Vertex<T> &vert : vertices) {
				this->vertices.insert({vert.getLabel(), vert});
			}
		}
		vector<Vertex<T>> makeVec(T start) {
			vector<Vertex<T>> retVec;
			retVec.push_back(vertices.at(start));
			for(auto vert : vertices) {
				if(vert.first != start) retVec.push_back(vert.second);
			}
			return retVec;
		}

		void makeConnected() {
			bool addedConnection = false;

			//start at 0
			vertices.at(0).setSeen(true);
			size_t seenCount = 1;
			vector<Vertex<T>> proccessing = {vertices.at(0)};
			Vertex<T> lastAdded = vertices.at(0);
			while(seenCount < vertices.size()) {
				for(size_t i = 0; i < proccessing.size(); i++) {
					//set up local veriables    
					Vertex<T> curr = vertices.at(proccessing.at(i).getLabel());    
					//get all connections    
					auto connections = curr.getConnections();    
					for(auto conn : connections) {
						//if not already looked at    
						if(!vertices[conn.getLabel()].getSeen()) {    
							//tag seen
							seenCount++;
							vertices[conn.getLabel()].setSeen(true);    
							proccessing.push_back(vertices.at(conn.getLabel()));    
						}
					}
				}
				//clear to make room for different graph
				proccessing.clear();

				if(seenCount < vertices.size()) {
					for(auto &vert : vertices) {
						//if it hasn't been seen
						if(!vert.second.getSeen()) {
							vertices.at(vert.first).setSeen(true);
							seenCount++;
							proccessing.push_back(vert.second);
							//should probably actually keep track / add these connections
							cout << "Edge: " << lastAdded.getLabel() << "-" << vert.first << endl;
							lastAdded = vert.second;
							addedConnection = true;
							break;
						}
					}
				}
			}

			if(!addedConnection) cout << "No new edge:" << endl;
		}

		friend ostream &operator<<(ostream &outs, Graph<T> &g) {
			for(auto &vert : g.vertices) {
				outs << vert.second << endl;
			}
			return outs;
		}
		friend istream &operator>>(istream &ins, Graph<T> &g) {
			T vert1, vert2;
			ins >> vert1 >> vert2;
			//cout << g.vertices.at(vert1) << endl;
			g.vertices.at(vert1).addConnection(g.vertices.at(vert2));
			g.vertices.at(vert2).addConnected();
			return ins;
		}
};

int main() {
	int numVerts = 0;
	cin >> numVerts;
	vector<Vertex<int>> verts;
	for(int i = 0; i < numVerts; i++) {
		verts.push_back(i);
	}
	Graph<int> graph(verts);
	int edges = 0;
	cin >> edges;
	for(int i = 0; i < edges; i++) {
		cin >> graph;
	}
	//cout << graph;
	graph.makeConnected();
}
