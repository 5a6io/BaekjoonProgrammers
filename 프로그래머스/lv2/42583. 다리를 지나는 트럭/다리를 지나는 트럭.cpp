#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    queue<int> bridge;
    int left_w = weight;
    
    for(int i = 0; i < bridge_length; i++)
        bridge.push(0);
    
    while(!truck_weights.empty()){
        answer++;
        auto it = truck_weights.begin();
        if(*it <= left_w) {
            bridge.pop();
            bridge.push(*it);
            left_w -= bridge.back();
            truck_weights.erase(it);
        }
        else {
            bridge.pop();
            bridge.push(0);
        }
        left_w += bridge.front();
    }
    
    return answer += bridge_length; //마지막 트럭이 빠지고 건너는 시간을 다리 길이만큼 더함.
}