/*
 * HackerRank link: https://www.hackerrank.com/contests/cst370-su20-hw3/challenges/equal-groups/submissions/code/1323537143
 * Title: 370_hw3_3
 * Abstract: check if subsets have same sum
 * Author: Andrew Bell
 * ID: 1138
 * Date: 5/12/20
 */
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

//assumes both strings are same length
bool bitOverlap(string s1, string s2) {
	for(size_t i = 0; i < s1.size(); i++) {
		if(s1.at(i) == s2.at(i)) {
			return true;
		}
	}
	return false;
}

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
	vector<int> elements;
	for(int i = 0; i < number; i++) {
		int temp;
		cin >> temp;
		elements.push_back(temp);
	}

	//sort least to greatest
	sort(elements.begin(), elements.end());

	int bits = pow(2, number);
	vector<string> bitMaps;
	for(int i = 1; i < bits; i++) {
		//use i as bitmap for index of vector
		//figure out how to print int in binary
		string bitStr = toBinaryStr(number, i);
		bitMaps.push_back(bitStr);
	}
	bool foundAny = false;
	for(const string &first : bitMaps) {
		//if smallest number bit is set
		if(first.at(0) == '1') {
			int sum = 0;
			for(size_t i = 0; i < first.size(); i++) {
				if(first.at(i) == '1') {
					sum += elements.at(i);
					//cout << elements.at(i) << " ";
				}
			}
			bool equals = false;
			for(const string &second : bitMaps) {
				//don't look at the same
				if(first == second) continue;
				if(bitOverlap(first,second)) continue;
				int sum2 = 0;
				for(size_t i = 0; i < second.size(); i++) {
					if(second.at(i) == '1') {
						sum2 += elements.at(i);
						//cout << elements.at(i) << " ";
					}
				}
				if(sum == sum2) {
					equals = true;
					break;
				}
			}
			if(equals) {
				foundAny = true;
				cout << "Equal Set:";
				for(size_t i = 0; i < first.size(); i++) {
					if(first.at(i) == '1') {
						//sum += elements.at(i);
						cout << " " << elements.at(i);
					}
				}
				cout << endl;
			}
		}
	}
	if(!foundAny) {
		cout << "Equal Set: 0\n";
	}
}
