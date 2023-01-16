#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    vector<char> temp;
    
    for(auto i = s.begin(); i != s.end(); i++){
        if(isspace(*i) || i == s.end() - 1){
            temp.push_back(*i);
            for(auto j = 0; j < temp.size(); j++){
                if(j%2 == 0)
                    answer += toupper(temp[j]);
                else
                    answer += tolower(temp[j]);
            }
            temp.clear();
        }
        else
            temp.push_back(*i);
    }
    
    return answer;
}