#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    int a[100000];
    int sum[100000];

    for(int i = 0; i < n; i++)
        cin >> a[i];

    sum[0] = a[0];
    for(auto i = 1; i <n; i++)
        sum[i] = max(sum[i - 1] + a[i], a[i]);
        
    auto max = -INT64_MAX;
    for(auto i = 0; i < n; i++)
        max = (max < sum[i])?sum[i]:max;

    cout << max << endl;
}