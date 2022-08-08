#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	int n, a;
	vector<int>s;

	vector<int>::iterator it;

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> a;
		s.push_back(a);
	}

	sort(s.begin(), s.end());

	s.erase(unique(s.begin(), s.end()), s.end());

	for (it = s.begin(); it != s.end(); ++it)
		cout << *it << endl;
	
	return 0;
}