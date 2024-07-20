#include<iostream>
using namespace std;

int main() {
	int n, m, sum = 0;
	int *A = new int;

	cin >> n >> m;
	for (int i = 0; i < n; i++)
		cin >> A[i];

	
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			for (int k = 0; k < n; k++)
				if (i != j && j != k && k != i)
					if (sum < A[i] + A[j] + A[k] && A[i] + A[j] + A[k] <= m) {
						sum = A[i] + A[j] + A[k];
					}

	cout << sum << endl;

	return 0;
}