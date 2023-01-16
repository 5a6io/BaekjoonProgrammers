#include <string>
#include <vector>

using namespace std;

int solution(string t, string p) {
    int answer = 0;
    for(auto i = 0; i <= t.size() - p.size(); i++){
        string temp = t.substr(i, p.size());
        if(stol(p) >= stol(temp))
            answer++;
    }
    return answer;
}