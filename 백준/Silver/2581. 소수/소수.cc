#include <iostream>
#include <vector>
using namespace std;

bool isPrime(int n){
    if(n == 1)
        return false;
    else {
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
    }
    return true;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int m, n, sum = 0;
    vector<int> prime;
    cin >> m >> n;

    for (int i = m; i <= n; i++)
        if(isPrime(i)) {
            prime.push_back(i);
            sum += i;
        }

    if(prime.empty())
        cout << -1 << endl;
    else{
        cout << sum << endl;
        cout << prime[0] << endl;
    }
}
