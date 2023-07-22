#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n, m, r; // n = 정점의 수, m = 간선의 수, r = 시작 정점.
vector<bool> visited;
vector<int> result;
vector<vector<int>> graph;
int order = 1;

void dfs(int num) {
    visited[num] = true;
    result[num - 1] = order;

    for (int i = 0; i < graph[num].size(); ++i) {
        if (!visited[graph[num][i]]) {
            order++;
            dfs(graph[num][i]);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m >> r;
    graph.resize(n + 1, vector<int>());
    visited.resize(n + 1, 0);
    result.resize(n, 0);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for (int i = 1; i <= n; ++i) {
        sort(graph[i].begin(), graph[i].end());
    }

    dfs(r);

    for (auto i: result) {
        cout << i << "\n";
    }
}