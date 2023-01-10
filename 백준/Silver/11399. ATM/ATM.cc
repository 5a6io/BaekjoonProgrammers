#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, total = 0;

    cin >> n;
    vector<int> p(n, 0);

    for(int i = 0; i < n; i++)
        cin >> p[i];

    sort(p.begin(), p.end());

    for (auto i = 0; i < n; i++) {
        total += (p[i] * (p.size() - i));
    }

    cout << total << endl;
}