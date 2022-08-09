#include<iostream>
#include<unordered_set>
#include<set>
using namespace std;

int r_count = 0;
int d_count = 0;
int* f = new int;

int fib(int n) {
	if (n == 1 || n == 2) {
		r_count++;
		return 1;
	}
	else {
		return fib(n - 1) + fib(n - 2);
	}
}

int fibonacci(int n) {
	if (n == 1 || n == 2) {
		f[n] = 1;
	}
	else
		for (int i = 3; i <= n; i++) {
			d_count++;
			f[i] = f[i - 1] + f[i - 2];
		}
	return f[n];
}

int main() {
	unsigned int n;
	cin >> n;

	fib(n);
	fibonacci(n);

	cout << r_count << " " << d_count << endl;
	
	return 0;
}