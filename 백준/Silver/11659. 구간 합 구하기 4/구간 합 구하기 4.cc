#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<int> sum(n + 1, 0);

    for (int i = 1; i <= n; i++) {
        int temp;
        cin >> temp;
        sum[i] = sum[i - 1] + temp;
    }

    for (int k = 0; k < m; k++) {
        int i, j;
        cin >> i >> j;
        cout << sum[j] - sum[i - 1] << "\n";
    }

}