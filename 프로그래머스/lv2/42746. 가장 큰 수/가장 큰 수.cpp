#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int compare(string a, string b){
    return a + b > b + a;
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> num;
    
    for(auto i:numbers){
        num.push_back(to_string(i));
    }
    
    sort(num.begin(),num.end(), compare);
    
    for(auto s:num)
        answer += s;
    
    if(answer[0] == '0') return "0";
    
    return answer;
}