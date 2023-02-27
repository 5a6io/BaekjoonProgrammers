#include <vector>
#include <iostream>
using namespace std;

int solution(int n) {
    int answer = 0;
    vector<int> cnt(n + 1, 0);
    cnt[1] = 1;
    cnt[2] = 2;
    
    for(int i = 3; i <= n; i++)
        cnt[i] = (cnt[i - 1] + cnt[i - 2]) % 1000000007;
    
    return answer = cnt[n];
}