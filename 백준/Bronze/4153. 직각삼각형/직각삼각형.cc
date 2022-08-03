#include<iostream>
#include<cmath>
using namespace std;

int main() {
	int a, b, c;
	
	while (true)
	{
		cin >> a >> b >> c;

		if (a == 0 && b == 0 && c == 0)
			break;

		if (a >= b && a >= c && b + c > a) {
			if (pow(c, 2) + pow(b, 2) == pow(a, 2))
				cout << "right" << endl;
			else if (pow(c, 2) + pow(b, 2) != pow(a, 2))
				cout << "wrong" << endl;
		}
		else if (b > a && b > c && a + c > b) {
			if (pow(c, 2) + pow(a, 2) == pow(b, 2))
				cout << "right" << endl;
			else if (pow(c, 2) + pow(a, 2) != pow(b, 2))
				cout << "wrong" << endl;
		}
		else {
			if (pow(a, 2) + pow(b, 2) == pow(c, 2))
				cout << "right" << endl;
			else if (pow(a, 2) + pow(b, 2) != pow(c, 2))
				cout << "wrong" << endl;
		}
	}

	return 0;
}