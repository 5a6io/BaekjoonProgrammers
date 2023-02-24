#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <numeric>

using namespace std;

int solution(vector<int> queue1, vector<int> queue2) {
    int answer = 0;
    long long sum1 = accumulate(queue1.begin(), queue1.end(), 0);
    long long sum2 = accumulate(queue2.begin(), queue2.end(), 0);
    queue<int> q1, q2;
    int s1 = queue1.size(), s2 = queue2.size();
    
    if((sum1 + sum2) % 2 != 0) return -1;
    
    for(int i = 0; i < s1; i++){
        q1.push(queue1[i]);
        q2.push(queue2[i]);
    }
    
    while(sum1 != sum2){
        if(answer > s1 + s2 + 2) return -1; // 다시 생각하기
        else if(sum1 > sum2){
            sum1 -= q1.front();
            sum2 += q1.front();
            q2.push(q1.front());
            q1.pop();
            answer++;
        }
        else {
            sum2 -= q2.front();
            sum1 += q2.front();
            q1.push(q2.front());
            q2.pop();
            answer++;
        }
    }
    
    return answer;
}