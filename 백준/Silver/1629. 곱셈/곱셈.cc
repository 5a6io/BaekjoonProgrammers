#include <iostream>
using namespace std;

long long divide_and_conquer(long long a, long long b, long long c) {
    if (b == 0) {
        return 1;
    }
    auto temp = divide_and_conquer(a, b / 2, c);
    temp = temp * temp % c;
    return b % 2 == 0 ? temp : temp * a % c;
 }

int main() {
    cin.tie(0); cout.tie(0);
    ios::sync_with_stdio(false);

    long long a, b, c;
    cin >> a >> b >> c;

    cout << divide_and_conquer(a, b, c);
}
