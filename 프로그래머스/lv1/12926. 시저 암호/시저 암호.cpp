#include <string>
#include <vector>

using namespace std;

string solution(string s, int n) {
    string answer = "";
    
    for(auto i:s){
        if(!isspace(i)){
            if(isupper(i))
                answer += ((i - 'A' + n) % 26 + 'A');
            else
                answer += ((i - 'a' + n) % 26 + 'a');
        }
        else
            answer += i;
    }
    return answer;
}