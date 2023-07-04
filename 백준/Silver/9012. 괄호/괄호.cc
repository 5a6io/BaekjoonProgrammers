#include <iostream>
#include <stack>
#include <vector>

using namespace std;

vector<string> result;

void test(string &s) {
    stack<char> ps;
    for (auto i:s) {
        if(!ps.empty() && ps.top() == '(' && i == ')'){
            ps.pop();
        } else {
            ps.push(i);
        }
    }

    if (!ps.empty()) {
        result.push_back("NO");
    } else {
        result.push_back("YES");
    }
}

int main() {

    cin.tie(0);

    int n; // 테스트 개수
    cin >> n;

    string s;
    for (int i = 0; i < n; i++) {
        cin >> s;
        test(s);
    }

    for (auto i: result) {
        cout << i << "\n";
    }
}