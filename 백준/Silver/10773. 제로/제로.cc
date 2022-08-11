#include<iostream>
#include<stack>
using namespace std;

int main() {
	int k, n;
	stack<int> a;

	cin >> k;

	for (auto i = 0; i < k; i++) {
		cin >> n;
		if (n != 0)
			a.push(n);
		else if(n ==0 && !a.empty())
			a.pop();
	}


	int sum = 0;
	while (!a.empty()) {
		sum = sum + a.top();
		a.pop();
	}

	cout << sum << endl;

	return 0;
}