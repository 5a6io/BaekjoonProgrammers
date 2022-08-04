#include<iostream>
#include<cmath>
using namespace std;

int factorial(int a) {
	if (a == 0 || a == 1)
		return 1;
	else
		return a * factorial(a - 1);
}

int main() {
	int n, k;

	cin >> n >> k;

	cout << factorial(n) / (factorial(k) * factorial(n - k)) << endl;

	return 0;
}