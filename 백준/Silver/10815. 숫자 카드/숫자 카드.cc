#include <iostream>
#include <set>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, m, k;
    cin >> n;

    set<int> a;

    for (int i = 0; i < n; i++) {
        cin >> k;
        a.insert(k);
    }

    cin >> m;

    for (int i = 0; i < m; i++) {
        cin >> k;
        if(a.find(k) != a.end())
            cout << "1 ";
        else
            cout << "0 ";
    }

}