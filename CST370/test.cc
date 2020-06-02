#include <iostream>
using namespace std;

int q(int n) {
	if (n <= 1) {
		return 1;
	}
	return q(n - 1) + 2 * n - 1;
}

int main() {
	for(int i = 1; i < 11; i++) {
		cout << "q(" << i << ")" << q(i) << endl;
	}
	//cout << "q(1)" << q(1) << endl;
	//cout << "q(2)" << q(2) << endl;
	//cout << "q(3)" << q(3) << endl;
}
