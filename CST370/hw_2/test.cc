#include <iostream>
using namespace std;

class Test {
	private:
		int x = 0;
		int y = 0;
	public:
		Test() {}
		Test(int x, int y) {
			this->x = x;
			this->y = y;
		}
		void print() {
			cout << "(" << x << "," << y << ")" << endl;
		}
};

int main() {
	string test = "test";
	Test coord;
	coord.print();
	Test xy(5,3);
}
