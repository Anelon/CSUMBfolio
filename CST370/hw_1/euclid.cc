#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int mods = 0;
int gcd(int x, int y) {
	//cout << "gcd(" << x << "," << y << ")\n";
	if(x == 0) return y;
	if(y == 0) return x;
	mods++;
	return gcd(y, x % y);
}

int main() {
	int answer = gcd(150,150);
	vector<int> counts;
	//cout << "gcd = " << answer << endl;
	for(int i = 1; i <= 150; i++) {
		for(int j = 1; j <= 150; j++) {
			mods = 0;
			gcd(i,j);
			cout << "gcd(" << i <<"," << j <<")" << mods << endl;
			counts.push_back(mods);
		}
	}
	int max = 0;
	for(int i : counts) {
		if(i > max) max = i;
	}
	cout << "Max mods: " << max << endl;
}
