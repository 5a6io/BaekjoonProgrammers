#include <iostream>
#include <vector>
#define MOD 1000000000

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    vector<vector<int>> dp(n + 1, vector<int>(10, 0));
    for (int i = 1; i < 10; ++i) {
        dp[1][i] = 1;
    }
    for (int i = 2; i <= n; ++i) {
        for (int j = 0; j < 10; ++j) {
            if (j == 0) {
                dp[i][j] = dp[i - 1][j + 1];
            } else if (j == 9) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1];
            }
            dp[i][j] %= MOD;
        }
    }

    int answer = 0;
    for (int i = 0; i < 10; ++i) {
        answer += dp[n][i];
        answer %= MOD;
    }

    cout << answer;
}