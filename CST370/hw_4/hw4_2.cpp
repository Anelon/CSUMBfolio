/*
 * HackerRank link: https://www.hackerrank.com/contests/cst370-su20-hw4/challenges/bfs-hops/submissions/code/1323615145 
 * Title: 370_hw4_2
 * Abstract: Graph get within steps
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
		int distance = -1;
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
		int getDistance() {
			return distance;
		}
		void setDistance(int newDistance) {
			distance = newDistance;
		}
		vector<pair<Vertex,int>>& getConnections() {return connections;}

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
			return outs;
		}
		void print() {
			cout << label;
			sort(connections.begin(), connections.end(), sortByLabel);
			for(const auto vert : connections) {
				cout << "->" << vert.first.getLabel();
			}
			cout << endl;
		}
};

template <class T>
bool isIn(vector<T> vec, T data) {
	for(T x : vec) {
		if(x == data) return true;
	}
	return false;
	//return find(vec.begin(), vec.end(), data) != vec.end();
}

template <class T>
class Graph {
	private:
		std::unordered_map<T, Vertex<T>> vertices;
	public:
		static bool variableWeight;
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
		vector<Vertex<T>> getWithin(T start, int steps) {
			vertices.at(start).setDistance(0);
			vector<Vertex<T>> proccessing = {vertices.at(start)};
			for(size_t i = 0; i < proccessing.size(); i++) {
				//set up local veriables
				Vertex<T> curr = vertices.at(proccessing.at(i).getLabel());
				int currDist = curr.getDistance();
				//if current distance >= max steps exit
				if(currDist >= steps) break;
				//get all connections
				auto connections = curr.getConnections();
				for(auto conn : connections) {
					//if not already looked at
					if(vertices[conn.first.getLabel()].getDistance() == -1) {
						//update distance
						vertices[conn.first.getLabel()].setDistance(currDist + 1);
						proccessing.push_back(vertices.at(conn.first.getLabel()));
					}
				}
			}
			return proccessing;
		}

		friend std::ostream &operator<<(std::ostream &outs, Graph<T> &g) {
			for(auto &vert : g.vertices) {
				outs << vert.second << std::endl;
			}
			return outs;
		}
		friend std::istream &operator>>(std::istream &ins, Graph<T> &g) {
			T vert1, vert2;
			//terible place for default weight
			int weight = 1;
			ins >> vert1 >> vert2;
			if(variableWeight)
				ins >> weight;
			g.vertices.at(vert1).addConnection(g.vertices.at(vert2), weight);
			return ins;
		}
};
template <class T>
bool Graph<T>::variableWeight = false;

int main() {
	int vertices;
	//read number of vertices
	cin >> vertices;
	//make all of the vertices
	vector<Vertex<string>> vertexes;
	for(int i = 0; i < vertices; i++) {
		string temp;
		cin >> temp;
		vertexes.push_back(temp);
	}
	//construct graph with vertices
	Graph<string> graph(vertexes);
	//make weights all 1
	//graph.setVeriableWeight(false);
	int edges;
	//read number of edges
	cin >> edges;
	for(int i = 0; i < edges; i++) {
		cin >> graph;
	}
	//cout << graph;
	string start;
	cin >> start;
	int depth;
	cin >> depth;
	//graph.TSP(start);
	auto within = graph.getWithin(start, depth);
	sort(within.begin(), within.end());
	Vertex<string> lastPrinted;
	for(Vertex<string> vert : within) {
		//ignore duplicates
		if(lastPrinted == vert) continue;
		lastPrinted = vert;
		cout << vert << endl;
	}
}
