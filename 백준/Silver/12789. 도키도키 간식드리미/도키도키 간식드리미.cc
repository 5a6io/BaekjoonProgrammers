#include <iostream>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;

    cin >> n;

    queue<int> order;

    for (int i = 0; i < n; ++i) {
        int temp;
        cin >> temp;
        order.push(temp);
    }

    stack<int> wait;
    int num = 1;
    while (!order.empty() || !wait.empty()) {
        if (!order.empty() && order.front() == num) {
            order.pop();
            num++;
        } else if (!wait.empty() && wait.top() == num) {
            wait.pop();
            num++;
        } else if (!order.empty()) {
            wait.push(order.front());
            order.pop();
        } else {
            cout << "Sad";
            return 0;
        }
    }

    cout << "Nice";
    return 0;
}