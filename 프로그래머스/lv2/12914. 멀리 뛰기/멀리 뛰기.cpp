#include <string>
#include <vector>

using namespace std;

int count = 0;

long long solution(int n) {
    long long answer = 0;
    vector<int> long_jump(2, 1);
    
    for(int i = 2; i <= n; i++)
        long_jump.push_back((long_jump[i-1] + long_jump[i-2]) % 1234567);
        
    return answer = long_jump[n];
}