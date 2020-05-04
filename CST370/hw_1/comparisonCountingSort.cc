#include <iostream>
#include <vector>
using namespace std;

int main() {
	vector<int> A = {9,3,3,9,3,6};
	vector<int> count(A.size());
	vector<int> S(A.size());
	for(int i = 0; i < A.size(); i++) {
		count[i] = 0;
	}
	for(int i = 0; i < A.size() - 1; i++) {
		for(int j = i + 1; j < A.size(); j++) {
			//cout << A[i] << "<" << A[j] << endl;
			if(A.at(i) < A.at(j)) {
				count[j]++;
				//cout << A[j] << " bigger" << endl;
			} else {
				count[i]++;
				//cout << A[i] << " bigger" << endl;
			}
		}
	}
	for(int i = 0; i < A.size(); i++) {
		S[count[i]] = A[i];
	}

	cout << "A[";
	for(int i : A) cout << i << ",";
	cout << "]" << endl;
	cout << "S[";
	for(int i : S) cout << i << ",";
	cout << "]" << endl;
	cout << "count[";
	for(int i : count) cout << i << ",";
	cout << "]" << endl;
}
