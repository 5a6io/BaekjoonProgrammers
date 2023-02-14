#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    unordered_map<char, int> str;
    
    for(int i = 0; i < s.size(); i++){
        auto it = str.find(s[i]);
        if(it != str.end())
            answer.push_back(i - it->second);
        else
            answer.push_back(-1);
        
        str[s[i]] = i;
    }
    
    return answer;
}