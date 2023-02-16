#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    map<string, int> c_cnt;
    
    for(int i = 0; i < clothes.size(); i++)
        c_cnt[clothes[i][1]]++;
    
    for(auto it = c_cnt.begin(); it != c_cnt.end(); it++)
        answer *= (it->second + 1);
    
    return answer - 1;
}