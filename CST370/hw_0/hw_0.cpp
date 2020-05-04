/*
 * hackerrank link: https://www.hackerrank.com/contests/cst370-su20-hw0/challenges/370-hw0-1/submissions/code/1323100670
 * Title: hw0_1.cpp
 * Abstract: Reads user input and conducts sum or difference depending on command input.
 * Name: Andrew Bell
 * ID: 1138
 * Date: 4/27/2020
 */
#include <iostream>
using namespace std;

int main() {
    while (true) {
        int select = 0;
        cin >> select;
        if(select == 9) break;
        int num1 = 0, num2 = 0;
        cin >> num1 >> num2;
        if(select == 1) {
            cout << num1 + num2 << endl;
        } else if (select == 2) {
            cout << abs(num1 - num2) << endl;
        }
    }
}
