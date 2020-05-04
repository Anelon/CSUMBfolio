/*
 * HackerRank link: https://www.hackerrank.com/contests/cst370-su20-hw1/challenges/common-nums/submissions/code/1323197572
 * Title: 370_hw1_1
 * Abstract: check the intersection of 2 sets
 * Author: Andrew Bell
 * ID: 1138
 * Date: 4/24/20
 */
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int number = 0;
	cin >> number;
	vector<int> set1;
	for (int i = 0; i < number; i++) {
		int temp = 0;
		cin >> temp;
		if(!cin) break;
		set1.push_back(temp);
	}
	int number2 = 0;
	cin >> number2;
	vector<int> set2;
	for (int i = 0; i < number2; i++) {
		int temp = 0;
		cin >> temp;
		if(!cin) break;
		set2.push_back(temp);
	}
	sort(set1.begin(), set1.end());
	sort(set2.begin(), set2.end());

	/*
	size_t x = 0, y = 0;
	int lastPrinted = -100000;
	bool found = false;
	cout << "Answer:";
	while(x != set1.size() && y != set2.size()) {
		if(set1.at(x) < set2.at(y)) {
			x++;
		} else if (set1.at(x) > set2.at(y)) {
			y++;
		} else {
			if(set1.at(x) != lastPrinted) cout << set1.at(x) << " ";
			lastPrinted = set1.at(x);
			x++;
			found = true;
		}
	}
	if(!found) cout << "NONE";
	cout << endl;
	*/

	vector<int> intersection;
	set_intersection(set1.begin(), set1.end(), set2.begin(), set2.end(), back_inserter(intersection));

	cout << "Answer:";
	if(intersection.size() == 0) cout << "NONE";
	else {
		int lastPrinted = -100000; //eww magic number
		for(int x : intersection) {
			if(lastPrinted != x) {
				cout << x << " ";
			}
			lastPrinted = x;
		}
	}
	cout << endl;
}
