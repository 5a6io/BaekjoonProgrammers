#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <stack>
#include <map>
using namespace std;

bool compare(vector<string> a, vector<string> b){
    return a[1] < b[1];
}

vector<string> solution(vector<vector<string>> plans) {
    sort(plans.begin(), plans.end(), compare);
    vector<string> answer;
    stack<pair<string, int>> task;
    
    int end = stoi(plans[0][1].substr(0, 2)) * 60 + stoi(plans[0][1].substr(3, 2)) + stoi(plans[0][2]); // index: 0에 있는 과제가 끝나는 시간
    for(int i = 1; i < plans.size(); i++){
        int start = stoi(plans[i][1].substr(0, 2)) * 60 + stoi(plans[i][1].substr(3, 2)); // 과제를 시작하는 시간
        int playtime = stoi(plans[i][2]); // 과제를 하는 시간
        
        if(start >= end){ // 현재 과제 시작까지 시간이 남은 경우
            answer.push_back(plans[i - 1][0]);
            int r_t = start - end;
            while(!task.empty()){
                if(task.top().second <= r_t){
                    answer.push_back(task.top().first);
                    r_t -= task.top().second;
                    task.pop();
                }else{
                    task.top().second -= (start - end);
                    break;
                }
            }
        }
        else {
            task.push({plans[i - 1][0], end - start});
        }
        
        if(plans.size() - 1 == i) {
            answer.push_back(plans[i][0]);
            break;
        }
        end = start + playtime;
    }
    
    
    
    while(!task.empty()){
        answer.push_back(task.top().first);
        task.pop();
    }
    
    return answer;
}