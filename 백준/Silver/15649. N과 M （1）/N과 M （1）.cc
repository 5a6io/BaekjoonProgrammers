#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, m; // 1 <= m <= n <= 8
vector<int> result;

void backtracking() {
    if (result.size() == m) {
        for (int i = 0; i < m; i++)
            cout << result[i] << " ";
        cout << "\n";
        return;
    }

    vector<bool> visit(n+1, false);
    for (int i = 1; i <= n; i++) {
        if (!visit[i] && find(result.begin(), result.end(), i) == result.end()) {
            visit[i] = true;
            result.push_back(i);
            backtracking();
            visit[i] = false;
            result.pop_back();
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;

    backtracking();
}