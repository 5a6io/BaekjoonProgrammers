#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

string solution(string s) {
    string answer = "";
    vector<int> num;
    string temp = "";
    for(auto i:s){
        if(isspace(i)){
            num.push_back(stoi(temp));
            temp = "";
        }
        else 
            temp += i;
    }
    
    num.push_back(stoi(temp));
    
    sort(num.begin(), num.end());
    
    return answer = to_string(num[0]) +" "
        + to_string(num[num.size()-1]);
}