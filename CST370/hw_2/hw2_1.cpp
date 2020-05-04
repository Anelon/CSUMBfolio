/*
 * HackerRank link: https://www.hackerrank.com/contests/cst370-su20-hw2/challenges/reverse-number-13/submissions/code/1323248608
 * Title: 370_hw2_1
 * Abstract: Take in a number and reverse it
 * Author: Andrew Bell
 * ID: 1138
 * Date: 4/30/20
 */
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	string input;
	cin >> input;
	reverse(input.begin(), input.end());
	cout << stoi(input) << endl;
}
