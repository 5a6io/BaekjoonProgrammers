#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n; // n = 포도잔의 개수
    cin >> n;

    vector<long long> wine(n + 1, 0);
    vector<long long> dp(100000, 0);
    
    for (int i = 1; i <= n; ++i) {
        cin >> wine[i];
    }

    dp[1] = wine[1];
    dp[2] = wine[1] + wine[2];

    for (int i = 3; i <= n; ++i) {
        dp[i] = dp[i - 1] > dp[i - 3] + wine[i] + wine[i - 1] ? dp[i - 1] : dp[i - 3] + wine[i] + wine[i - 1];
        dp[i] = dp[i] < dp[i - 2] + wine[i] ? dp[i - 2] + wine[i] : dp[i];
    }

    cout << dp[n];
}