#include <string>
#include <vector>

using namespace std;

string solution(string phone_number) {
    string answer = "";
    string temp = phone_number.substr(phone_number.size()-4, 4);
    
    for(auto i = 0; i < phone_number.size()-4; i++)
        answer += "*";
    
    answer += temp;
    
    return answer;
}