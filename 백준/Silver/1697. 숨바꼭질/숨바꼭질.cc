#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

	int n, k;
    cin >> n >> k;

    queue<pair<int, int>> q;
    vector<bool> visited(100001, 0);
    q.push({n, 0});

    while (!q.empty()) {
        int cur = q.front().first;
        int cnt = q.front().second;
        q.pop();

        if (cur == k) {
            cout << cnt;
            break;
        }

        if (cur + 1 >= 0 && cur + 1 < 100001) {
            if (!visited[cur + 1]) {
                visited[cur + 1] = true;
                q.push({cur + 1, cnt + 1});
            }
        }

        if (cur - 1 >= 0 && cur - 1 < 100001) {
            if (!visited[cur - 1]) {
                visited[cur - 1] = true;
                q.push({cur - 1, cnt + 1});
            }
        }

        if (cur * 2 >= 0 && cur * 2 < 100001) {
            if (!visited[cur * 2]) {
                visited[cur * 2] = true;
                q.push({cur * 2, cnt + 1});
            }
        }
    }

	return 0;
}