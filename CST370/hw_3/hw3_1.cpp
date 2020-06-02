/*
 * HackerRank link: https://www.hackerrank.com/contests/cst370-su20-hw3/challenges/palindrome-check-10/submissions/code/1323537035
 * Title: 370_hw3_1
 * Abstract: recursive palendrome checker
 * Author: Andrew Bell
 * ID: 1138
 * Date: 5/12/20
 */
#include <iostream>
#include <vector>
using namespace std;

string cleanString(string s) {
	string retStr;
	for(char c : s) {
		if(isalpha(c)) retStr.push_back(toupper(c));
		if(isdigit(c)) retStr.push_back(c);
	}
	return retStr;
}

bool palendrome(string s, size_t index) {
	//cout << index << endl;
	if(index >= s.size() / 2) return true;
	if(s.at(index) == s.at(s.size()-1 - index)) {
		return palendrome(s, ++index);
	} else {
		return false;
	}
}


int main() {
	string str;
	getline(cin, str);
	str = cleanString(str);
	//cout << str << endl;
	if(palendrome(str, 0)) {
		cout << "TRUE" << endl;
	} else {
		cout << "FALSE" << endl;
	}
}
