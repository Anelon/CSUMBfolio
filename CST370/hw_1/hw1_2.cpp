/*
 * HackerRank link: https://www.hackerrank.com/contests/cst370-su20-hw1/challenges/max-events/submissions/code/1323198015
 * Title: 370_hw1_2
 * Abstract: Check maximum overlapping events
 * Author: Andrew Bell
 * ID: 1138 
 * Date: 4/28/20
 */
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int number = 0;
	cin >> number;
	vector<pair<int,int>> times;
	for (int i = 0; i < number; i++) {
		int start = 0, end = 0;
		cin >> start >> end;
		times.push_back({start,end});
	}
	sort(times.begin(), times.end());
	//int lastEnd = -1, lastStart = -1;
	vector<int> overlaps;
	for(auto time : times) {
		int overlap = 0;
		for(auto time2 : times) {
			if(time.first <= time2.first && time.second >= time2.first) {
				overlap++;
			}
		}
		overlaps.push_back(overlap);
		//cout << time.first << " " << time.second << endl;
	}
	int overlap = *max_element(overlaps.begin(), overlaps.end());
	cout << "Answer:" << overlap << endl;
}
