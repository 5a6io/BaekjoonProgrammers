#include <string>
#include <vector>

using namespace std;

int binary(int n) {
    int cnt = 0;
    
    while (n > 0) {
        if (n%2 == 1) cnt++;
        n /= 2;
    }
    
    return cnt;
}

int solution(int n) {
    int answer = 0;
    int cnt = binary(n);
    
    for(int i = n+1; i < 1000001; i++) {
        if(cnt == binary(i)){
            answer = i;
            break;
        }
    }
    
    return answer;
}