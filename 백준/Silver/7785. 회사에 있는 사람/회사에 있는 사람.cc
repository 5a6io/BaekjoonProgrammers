#include <iostream>
#include <set>

using namespace std;

int main() {
    cin.tie(0);

    int n;
    cin >> n;

    string name, inout;
    set<string, greater<string>> p;
    for (int i = 0; i < n; i++) {
        cin >> name >> inout;
        cin.ignore();
        if (inout == "enter") {
            p.insert(name);
        } else {
            p.erase(name);
        }
    }

    for (auto i: p) {
        cout << i << "\n";
    }

    return 0;
}