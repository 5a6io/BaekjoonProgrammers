#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    vector<pair<int, int>> timeline;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int start, end;
        cin >> start >> end;
        timeline.push_back({end, start});
    }

    sort(timeline.begin(), timeline.end());
    int end = timeline[0].first;
    int cnt = 1;
    for (auto i = 1; i < n; i++) {
        if (end <= timeline[i].second) {
            cnt++;
            end = timeline[i].first;
        }
    }

    cout << cnt;
}