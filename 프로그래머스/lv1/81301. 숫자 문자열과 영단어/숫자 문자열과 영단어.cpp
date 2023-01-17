#include <string>
#include <map>
#include <vector>
#include <cmath>

using namespace std;

int solution(string s) {
    int answer = 0;
    vector<int> num;
    map<string, int> n_word = {{"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3}, {"four", 4},
                             {"five", 5}, {"six", 6}, {"seven", 7}, {"eight", 8}, {"nine", 9}};
    char lexical[100];
    int len = 0;
    
    for(auto i:s){
        if(isalpha(i)){
            lexical[len++] = i;
            lexical[len] = '\0';
            auto it = n_word.find(lexical);
            if(it != n_word.end()){
                num.push_back(it->second);
                len = 0;
            }
            
        }
        else if(isdigit(i))
            num.push_back(i-'0');
    }
    
    for(int i = 0; i < num.size(); i++){
        int count = num.size() - 1 - i;
        answer += (num[i] * powl(10, count));
    }
    
    return answer;
}