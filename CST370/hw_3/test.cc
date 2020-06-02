#include <iostream>
#include <vector>
using namespace std;

vector<int> riddle(vector<int> vec) {
	if(vec.size() == 1) return vec;
	else {
		vector<int> temp = vec;
		temp.pop_back();
		temp = riddle(temp);
		if(temp <= vec) return temp;
		else return vec;
	}
}

int main() {
	vector<int> vec = {1,5,10,0,0};
	vec = riddle(vec);
	for(int i : vec) {
		cout << i << ",";
	}
	cout << endl;
}
