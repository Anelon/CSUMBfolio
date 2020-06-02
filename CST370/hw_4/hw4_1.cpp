/*
 * HackerRank link: https://www.hackerrank.com/contests/cst370-su20-hw4/challenges/tsp-2-1/submissions/code/1323586657
 * Title: 370_hw4_1
 * Abstract: Traveling salesperson problem
 * Author: Andrew Bell
 * ID: 1138
 * Date: 5/14/20
 */
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <climits>
#include <cmath>
using namespace std;

template <class T>
class Vertex {
	private:
		//pair, vertex connection and weight of connection
		std::vector<std::pair<Vertex,int>> connections;
		T label = {};
		bool seen = false;
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
		vector<pair<Vertex,int>>& getConnections() {return connections;}
		//hmm not what I want I think...
		bool TSP(int steps, vector<pair<Vertex,int>> &path) {
			//mark this as seen
			seen = true;
			int min = INT_MAX;
			Vertex next;
			int dist = 0;
			for(auto &conn : connections) {
				if(conn.second < min) {
					min = conn.second;
					next = conn.first;
				}
			}
			if(min == INT_MAX) {
				return steps == 0;
			}
			path.push_back({next, min});
			if(TSP(steps - 1, path)) {
				//successfully found
				return true;
			} else {
				//should try a different one?
				return false;
			}
		}

		void addConnection(Vertex &v, int weight = 1) {
			//std::cout << "Added connection " << v << weight << std::endl;
			connections.push_back({v, weight});
		}

		bool operator<(const Vertex &rhs) {
			return this->label < rhs.label;
		}
		bool operator==(const Vertex &rhs) {
			return this->label == rhs.label;
		}

		static bool sortByLabel(const std::pair<Vertex,int> &a, const std::pair<Vertex,int> &b){
			return a.first.label < b.first.label;
		}

		friend std::ostream& operator<<(std::ostream& outs, Vertex<T>& v) {
			outs << v.label;
			//sort(v.connections.begin(), v.connections.end(), sortByLabel);
			//for(const auto vert : v.connections) {
			//outs << "->" << vert.first.getLabel();
			//}
			return outs;
		}
		void print() {
			std::cout << *this << std::endl;
		}
};


template <class T>
class Graph {
	private:
		std::unordered_map<T, Vertex<T>> vertices;
	public:
		Graph() {}
		Graph(std::vector<Vertex<T>> vertices) {
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
		//void function to do the traveling sales person problem and print path
		void TSP(T start) {
			vector<Vertex<T>> vertVec = makeVec(start);
			vector<Vertex<T>> bestPath;
			vector<int> base;
			for(size_t i = 0; i < vertices.size(); i++) base.push_back(i);

			int bestPathLen = INT_MAX;
			do {
				//only look at paths that start at the first
				if(base.front() != 0) break;
				vector<Vertex<T>> currPath;

				bool validPath = true;
				int pathLen = 0;
				for(size_t i = 0; i < base.size(); i++) {
					Vertex<T> curr = vertVec.at(base.at(i));
					//check if it connects to the next one
					bool connects = false;
					auto connection = curr.getConnections();
					for(auto conn : connection) {
						//if connection can be made
						if(conn.first.getLabel() == vertVec.at(base.at((i+1) % vertices.size())).getLabel()) {
							connects = true;
							pathLen += conn.second;
							currPath.push_back(conn.first);
							break;
						}
					}
					//if no connection can be made exit
					if(!connects) {
						validPath = false;
						break;
					}
				}
				if(validPath) {
					if(pathLen < bestPathLen) {
						bestPathLen = pathLen;
						bestPath = currPath;
					}
				}
			} while (next_permutation(base.begin(), base.end()));

			/*
			for(auto line : pathOptions) {
				for(auto i : line) {
					cout << i << " ";
				}
				cout << endl;
			}
			//vertices.at(start).TSP(vertices.size(), path);
			*/
			if(bestPath.size()) {
				cout << "Path:" << start;
				for(auto &p : bestPath) {
					cout << "->" << p;
				}
				cout << endl;
				cout << "Cost:" << bestPathLen << endl;
			} else {
				cout << "Path:" << endl;
				cout << "Cost:-1" << endl;
			}

		}

		friend std::ostream &operator<<(std::ostream &outs, Graph<T> &g) {
			for(auto &vert : g.vertices) {
				outs << vert.second << std::endl;
			}
			return outs;
		}
		friend std::istream &operator>>(std::istream &ins, Graph<T> &g) {
			T vert1, vert2;
			int weight;
			ins >> vert1 >> vert2 >> weight;
			//std::cout << g.vertices.at(vert1) << std::endl;
			g.vertices.at(vert1).addConnection(g.vertices.at(vert2), weight);
			return ins;
		}
};

template class Graph<std::string>;

int main() {
	int vertices;
	//read number of vertices
	cin >> vertices;
	//make all of the vertices
	vector<Vertex<string>> vertexes;
	string start;
	for(int i = 0; i < vertices; i++) {
		string temp;
		cin >> temp;
		if(i == 0) start = temp;
		vertexes.push_back(temp);
	}
	//construct graph with vertices
	Graph<string> graph(vertexes);
	int edges;
	//read number of edges
	cin >> edges;
	for(int i = 0; i < edges; i++) {
		cin >> graph;
	}
	//cout << graph;
	graph.TSP(start);
}
