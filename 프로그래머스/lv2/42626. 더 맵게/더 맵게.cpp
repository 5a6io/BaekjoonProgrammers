#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> scale; // minheap
    
    for(auto it = scoville.begin();it != scoville.end(); it++)
        scale.push(*it);
    
    if(scale.top() > K)
        return 0;
    else{
        while(scale.top() < K && !scale.empty()){
            answer++;
            int mix = scale.top();
            scale.pop();
            mix += (scale.top() * 2);
            scale.pop();
            scale.push(mix);
            if(scale.size()==1&&scale.top() < K)
                return -1;
        }
        return answer;
    }
}