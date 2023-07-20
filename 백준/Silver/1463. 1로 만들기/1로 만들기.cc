#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int x;
    cin >> x;

    vector<int> result(x + 1, 0);


    result[1] = 0;
    result[2] = 1;
    result[3] = 1;

    for (int i = 4; i <= x; i++) {
        result[i] = result[i - 1] + 1;
        if (i % 2 == 0) result[i] = min(result[i], result[i / 2] + 1);
        if (i % 3 == 0) result[i] = min(result[i], result[i / 3] + 1);
    }

    cout << result[x];

    return 0;
}