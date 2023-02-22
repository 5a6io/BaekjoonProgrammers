#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

bool compare(const pair<int, int>& a, pair<int, int>& b) {
    return a.second > b.second;
}

int solution(int k, vector<int> tangerine) {
    int answer = 0;
    map<int, int> kind;
    
    sort(tangerine.begin(), tangerine.end());
    
    for(auto i : tangerine)
        kind[i]++;
    
    vector<pair<int, int>> kind_count(kind.begin(), kind.end());
    
    sort(kind_count.begin(), kind_count.end(), compare);
    
    for(auto it = kind_count.begin(); it != kind_count.end(); it++){
        if(k > 0){
            k -= it->second;
            answer++;
        }
    }
    
    
    return answer;
}