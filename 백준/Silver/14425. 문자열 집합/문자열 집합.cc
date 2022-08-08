#include<iostream>
#include<set>
using namespace std;

int main() {
	int n, m, count = 0;
	set<string> a;
	string s;

	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		cin >> s;

		a.insert(s);
	}

	for (int i = 0; i < m; i++) {
		cin >> s;
		set<string>::iterator pos = a.find(s);
		if (pos != a.end())
			count++;
	}

	cout << count << endl;

	
	return 0;
}