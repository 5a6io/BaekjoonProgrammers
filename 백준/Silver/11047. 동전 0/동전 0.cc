#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, k, min = 0;

    cin >> n >> k;
    vector<int> coin(n, 0);

    for(int i = 0; i < n; i++)
        cin >> coin[i];

    for (int i = n - 1; i >= 0; i--) {
        if (k >= coin[i]) {
            min += (k / coin[i]);
            k %= coin[i];
        }
    }

    cout << min << endl;
}