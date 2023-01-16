#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(long long n) {
    vector<int> answer;
    string s = to_string(n);
    
    for(auto i = s.begin(); i != s.end(); i++)
        answer.push_back(*i-'0');
    
    reverse(answer.begin(), answer.end());
    
    return answer;
}