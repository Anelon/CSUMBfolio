/*
 * HackerRank link: https://www.hackerrank.com/contests/cst370-su20-hw5/challenges/partitioning-numbers/submissions/code/1324019850
 * Title: 370_hw5_2
 * Abstract: 2 different partition methouds
 * Author: Andrew Bell
 * ID: 1138
 * Date: 6/2/20
 */
#include <iostream>
#include <vector>
using namespace std;

void partition(vector<int>& numbers) {
	if(numbers.size() <= 1) return;
	size_t i = 0, j = numbers.size() - 1;
	while(i != j) {
		if(numbers.at(i) > 0) {
			if(numbers.at(j) < 0) {
				swap(numbers.at(i), numbers.at(j));
			} else j--;
		} else i++;
	}
}

void partition2(vector<int>& numbers) {
	if(numbers.size() <= 1) return;
	size_t i = 0, j = 1;
	while(i < numbers.size() and j < numbers.size()) {
		if(numbers.at(i) > 0) {
			if(j < i) j = i + 1;
			if(numbers.at(j) < 0) {
				swap(numbers.at(i), numbers.at(j));
			} else j++;
		} else i++;
	}
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

	vector<int> numCopy(numbers);
	partition(numbers);
	for(int i : numbers) {
		cout << i << " ";
	}
	cout << endl;
	partition2(numCopy);
	for(int i : numCopy) {
		cout << i << " ";
	}
	cout << endl;
}
