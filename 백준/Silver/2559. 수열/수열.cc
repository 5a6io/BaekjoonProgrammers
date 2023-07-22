#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, k;
    int sum[100001];
    cin >> n >> k;

    for (int i = 1; i <= n; ++i) {
        int temp;
        cin >> temp;
        sum[i] = sum[i - 1] + temp;
    }

    int result = sum[k];
    for (int i = k; i <= n; i++) {
        result = max(result, sum[i] - sum[i - k]);
    }

    cout << result;
}