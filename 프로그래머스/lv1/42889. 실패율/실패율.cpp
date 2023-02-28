#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<int, double>& a, pair<int, double>& b){
    if(a.second == b.second)
        return a.first < b.first;
    return a.second > b.second;
}

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    vector<pair<int, double>> rate;
    
    for(int i = 1; i <= N; i++){
        double fail = count(stages.begin(), stages.end(), i);
        double reached = count_if(stages.begin(),
                                  stages.end(),
                                  [&i](int n){
                                      return n >= i;
                                  });
        if(reached == 0)
            rate.push_back({i, 0});
        else
            rate.push_back({i, fail/ reached});
    }
    
    sort(rate.begin(), rate.end(), compare);
    
    for(auto it = rate.begin(); it != rate.end(); it++)
        answer.push_back(it->first);
    
    return answer;
}