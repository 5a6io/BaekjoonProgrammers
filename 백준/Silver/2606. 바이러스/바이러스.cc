#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n, m;
	cin >> n >> m;

	int s = 1;
	vector<vector<bool>> graph(n + 1, vector<bool>(n + 1, false));
	vector<bool> visited(n + 1, false);
	queue<int> q;

	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		graph[a][b] = true;
		graph[b][a] = true;
	}
	
	visited[s] = true;
	q.push(s);

	int cnt = 0;
	while (!q.empty()) {
		int cur = q.front();
		q.pop();

		for (int i = 1; i <= n; i++) {
			if (graph[cur][i] == true && !visited[i]) {
				q.push(i);
				visited[i] = true;
				cnt++;
			}
		}
	}

	cout << cnt;
}