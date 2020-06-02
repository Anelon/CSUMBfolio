/*
 * HackerRank link: https://www.hackerrank.com/contests/cst370-su20-hw3/challenges/binary-numbs/submissions/code/1323537063
 * Title: 370_hw3_2
 * Abstract: Make all subsets
 * Author: Andrew Bell
 * ID: 1138
 * Date: 5/12/20
 */
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

string toBinaryStr(int bits, int num) {
	if(bits <= 0) return "0";
	string retstr;
	for(int i = bits - 1; i >= 0; i--) {
		if(num & (1 << i)) retstr.push_back('1');
		else retstr.push_back('0');
	}
	return retstr;
}

int main() {
	int number = 0;
	cin >> number;
	vector<string> elements;
	for(int i = 0; i < number; i++) {
		string temp;
		cin >> temp;
		elements.push_back(temp);
	}
	//reverse the vector
	//reverse(elements.begin(), elements.end());

	// should be 2^(n+1) - 1
	int bits = pow(2, number);
	for(int i = 0; i < bits; i++) {
		//use i as bitmap for index of vector
		//figure out how to print int in binary
		string bitStr = toBinaryStr(number, i);
		cout << bitStr << ":";
		if(i == 0) cout << "EMPTY";
		else {
			for(size_t j = 0; j < bitStr.size(); j++) {
				if(bitStr.at(j) == '1') {
					cout << elements.at(j) << " ";
				}
			}
		}
		cout << endl;
	}
}
