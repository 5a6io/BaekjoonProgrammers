#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, k;
    cin >> n >> k;

    vector<int> candidate(n, 0);

    for (int i = 0; i < n; i++)
        cin >> candidate[i];

    sort(candidate.rbegin(), candidate.rend());

    cout << candidate[k - 1];
}