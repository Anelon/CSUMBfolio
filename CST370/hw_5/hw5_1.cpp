/*
 * HackerRank link: https://www.hackerrank.com/contests/cst370-su20-hw5/challenges/divide-and-conquer-max/submissions/code/1324019825
 * Title: 370_hw5_1
 * Abstract: find Max in vector using divide and conquer
 * Author: Andrew Bell
 * ID: 1138
 * Date: 6/2/20
 */
#include <iostream>
#include <vector>
using namespace std;

int findMax(const vector<int>& numbers) {
	if(numbers.size() == 1) return numbers.at(0);
	const size_t half = numbers.size() / 2;
	vector<int> low(numbers.begin(), numbers.begin() + half);
	vector<int> high(numbers.begin() + half, numbers.end());
	int lowMax = findMax(low);
	int highMax = findMax(high);
	if(highMax > lowMax) return highMax;
	return lowMax;
}

int main() {
	vector<int> numbers;
	int number = 0;
	cin >> number;
	for(int i = 0; i < number; i++) {
		int num = 0;
		cin >> num;
		numbers.push_back(num);
	}
	cout << findMax(numbers) << endl;

}
