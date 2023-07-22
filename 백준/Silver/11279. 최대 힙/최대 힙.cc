#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    cin >> n;

    priority_queue<int> q;
    for (int i = 0; i < n; ++i) {
        int temp;
        cin >> temp;
        if (temp == 0) {
            if (q.empty()) {
                cout << "0\n";
            } else {
                cout << q.top() << "\n";
                q.pop();
            }
        } else {
            q.push(temp);
        }
    }
}