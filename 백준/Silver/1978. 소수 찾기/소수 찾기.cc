#include<iostream>
using namespace std;

int main() {
	int a, count = 0, p_num = 0;
	int *b = new int;

	cin >> a;

	for (int i = 0; i < a; i++)
	{
		cin >> b[i];
	}

	for (int i = 0; i < a; i++) {
		for (int j = 1; j <= b[i]; j++)
			if (b[i] % j == 0)
				count++;
		if (count == 2)
			p_num++;
		count = 0;
	}

	cout << p_num << endl;

	return 0;
}