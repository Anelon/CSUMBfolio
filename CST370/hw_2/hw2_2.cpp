/*
 * HackerRank link: https://www.hackerrank.com/contests/cst370-su20-hw2/challenges/time-difference-2/submissions/code/1323248817
 * Title: 370_hw2_2
 * Abstract: Difference between 2 times
 * Author: Andrew Bell
 * ID: 1138
 * Date: 4/30/20
 */
#include <iostream>
#include <iomanip>
#include <utility>
#include <algorithm>
#include <sstream>
using namespace std;

class TimeStamp {
	private:
		int hour = 0;
		int mins = 0;
		int secs = 0;
	public:
		TimeStamp() {}
		TimeStamp(string timeStamp) {
			stringToTime(timeStamp);
		}
		void stringToTime(string timeStamp) {
			stringstream ss(timeStamp);
			string temp;
			getline(ss,temp,':');
			hour = stoi(temp);
			getline(ss,temp,':');
			mins = stoi(temp);
			getline(ss,temp,':');
			secs = stoi(temp);
		}
		TimeStamp* operator=(const TimeStamp &right) {
			this->hour = right.hour;
			this->mins = right.mins;
			this->secs = right.secs;
			return this;
		}
		TimeStamp operator-(const TimeStamp &right) const {
			TimeStamp retVal;
			TimeStamp left = *this;

			if(left.secs < right.secs) {
				left.secs += 60;
				retVal.mins = -1;
			}
			retVal.secs = left.secs - right.secs;
			if(left.mins < right.mins) {
				left.mins += 60;
				retVal.hour = -1;
			}
			retVal.mins += left.mins - right.mins;
			if(left < right) {
				left.hour += 24; //roll the time around to the next day
			}
			retVal.hour += left.hour - right.hour;
			return retVal;
		}
		bool operator<(const TimeStamp &rhs) const {
			if(this->hour == rhs.hour) {
				if(this->mins == rhs.mins) {
					return this->secs < rhs.secs;
				}
				return this->mins < rhs.mins;
			}
			return this->hour < rhs.hour;
		}
		friend ostream &operator<<(ostream &outs, const TimeStamp &ts);
		friend istream &operator>>(istream &ins, const TimeStamp &ts);

};
ostream &operator<<(ostream &outs, const TimeStamp &ts) {
	outs << setfill('0') << setw(2);
	outs << ts.hour << ":";
	outs << setfill('0') << setw(2);
	outs << ts.mins << ":";
	outs << setfill('0') << setw(2);
	outs << ts.secs;
	return outs;
}

istream &operator>>(istream &ins, TimeStamp& ts) {
	string temp;
	ins >> temp;
	ts.stringToTime(temp);
	return ins;
}

int main() {
	TimeStamp time1, time2;
	cin >> time1 >> time2;
	//cout << time1 << endl;
	//cout << time2 << endl;
	cout << (time2 - time1) << endl;
}
