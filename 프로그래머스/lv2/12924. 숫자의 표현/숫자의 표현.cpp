#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    
    for(auto i = 1; i <= n / 2; i++){
        int sum = i;
        for(auto j = i + 1; sum < n; j++){
            sum += j;
            if(sum == n)
                answer++;
        }
    }
    
    return answer + 1;
}