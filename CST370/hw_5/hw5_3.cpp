/*
 * HackerRank link: https://www.hackerrank.com/contests/cst370-su20-hw5/challenges/kahns-topological-sort/submissions/code/1324020601
 * Title: 370_hw5_3
 * Abstract: Khan's algorithm for topological order
 * Author: Andrew Bell
 * ID: 1138
 * Date: 9/2/20
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
		//TODO keep track of number of people connected to me
		set<Vertex> connections;
		T label = {};
		bool seen = false;
		int connected = 0;
	public:
		Vertex() {};
		Vertex(T label) {
			this->label = label;
		}
		T getLabel() const {
			return label;
		}
		bool getSeen() {
			return seen;
		}
		void setSeen(bool newSeen) {
			seen = newSeen;
		}
		set<Vertex>& getConnections() {return connections;}

		void addConnection(Vertex &v) {
			//cout << "Added connection " << v << weight << endl;
			connections.insert(v);
		}
		void addConnected() { connected++; }
		void removeConnected() { connected--; }
		int getConnected() { return connected; }

		bool operator<(const Vertex &rhs) const {
			return this->label < rhs.label;
		}
		bool operator==(const Vertex &rhs) const {
			return this->label == rhs.label;
		}

		static bool sortByLabel(const Vertex &a, const Vertex &b){
			return a.first.label < b.first.label;
		}

		friend ostream& operator<<(ostream& outs, Vertex<T>& v) {
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
		static bool variableWeight;
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

		void khans() {
			for(auto &vert : vertices) {
				cout << "In-degree[" << vert.second.getLabel() << "]:";
				cout << vert.second.getConnected() << endl;
			}
			vector<T> order;
			while(true) {
				vector<Vertex<T>> toRemove;
				for(auto &vert : vertices) {
					if(!vert.second.getSeen() && !vert.second.getConnected()) {
						//cout << vert.second << endl;
						vert.second.setSeen(true);
						order.push_back(vert.second.getLabel());
						toRemove.push_back(vert.second);
					}
				}
				for(size_t i = 0; i < toRemove.size(); i++) {
					auto conn = toRemove.at(i).getConnections();
					for(const Vertex<T> &v: conn) {
						vertices.at(v.getLabel()).removeConnected();
						if(!vertices.at(v.getLabel()).getSeen() and !vertices.at(v.getLabel()).getConnected()) {
							vertices.at(v.getLabel()).setSeen(true);
							order.push_back(vertices.at(v.getLabel()).getLabel());
							toRemove.push_back(vertices.at(v.getLabel()));
						}
					}
				}
				if(order.size() == vertices.size()) break;
				if(!toRemove.size()) {
					order.clear();//toss the order
					break;
				}
			}
			if(order.size()) {
				string orderStr;
				for(auto &vert : order) {
					orderStr += to_string(vert) + "->";
				}
				//remove trailing "->"
				orderStr.pop_back();
				orderStr.pop_back();
				cout << "Order:" << orderStr << endl;
			} else {
				cout << "No Order:" << endl;
			}
		}

		friend ostream &operator<<(ostream &outs, Graph<T> &g) {
			for(auto &vert : g.vertices) {
				outs << vert.second << endl;
			}
			return outs;
		}
		friend istream &operator>>(istream &ins, Graph<T> &g) {
			T vert1, vert2;
			int weight;
			ins >> vert1 >> vert2;
			//cout << g.vertices.at(vert1) << endl;
			g.vertices.at(vert1).addConnection(g.vertices.at(vert2));
			g.vertices.at(vert2).addConnected();
			return ins;
		}
};
template <class T>
bool Graph<T>::variableWeight = false;

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
	graph.khans();
}
