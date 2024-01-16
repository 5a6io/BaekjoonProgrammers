#include <iostream>
#include <cmath>

using namespace std;

void hanoi(int n, int start, int end) {

    if (n == 1) {
        cout << start << ' ' << end << "\n";
    } else {
        hanoi(n - 1, start, 6 - start - end); // n-1개를 start에서 sub으로 옮겨줘야 함.
        cout << start << ' ' << end << "\n";
        hanoi(n - 1, 6 - start - end, end); // sub에 있는 n-1개를 모두 end로 보내줘야 함.
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n; // 원판의 개수
    cin >> n;

    cout << (int)pow(2, n) - 1 << "\n"; // 하노이탑 최소 이동 횟수 = 2^n - 1
    hanoi(n, 1, 3);
}