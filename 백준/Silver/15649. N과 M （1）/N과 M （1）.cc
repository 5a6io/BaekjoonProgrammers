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

    for (int i = 1; i <= n; i++) {
        if (find(result.begin(), result.end(), i) == result.end()) {
            result.push_back(i);
            backtracking();
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
