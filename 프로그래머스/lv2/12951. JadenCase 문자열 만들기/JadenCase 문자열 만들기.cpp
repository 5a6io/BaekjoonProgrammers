#include <string>
#include <vector>
#include <cctype>

using namespace std;

string solution(string s) {
    string answer = "";
    char prev;
    
    for(auto i = 0; i < s.size(); i++){
        if(i == 0)
            answer += toupper(s[i]);
        else if(isspace(prev))
            answer += toupper(s[i]);
        else
            answer += tolower(s[i]);
        prev = s[i];
    }
    
    return answer;
}