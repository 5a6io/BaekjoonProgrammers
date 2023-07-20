#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    cin >> n;

    int s[301]; // 계단 점수
    for (int i = 1; i <= n; i++) {
        cin >> s[i];;
    }

    int dp[301]; // 누적된 점수
    dp[1] = s[1];
    dp[2] = s[1] + s[2];
    dp[3] = max(s[1] + s[3], s[2] + s[3]);
    for (int i = 4; i <= n; i++) {
        dp[i] = max(s[i] + s[i - 1] + dp[i - 3], s[i] + dp[i - 2]);
    }

    cout << dp[n];
}