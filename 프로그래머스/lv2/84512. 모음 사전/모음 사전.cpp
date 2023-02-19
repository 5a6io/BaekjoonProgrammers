#include <string>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;


vector<char> vowel = {'A', 'E', 'I', 'O', 'U'};
vector<string> dic;
int order = 0;

void make_word(int target, string s = ""){
    if(s.size() == target)
        dic.push_back(s);
    else
        for(auto i : vowel){
            s += i;
            make_word(target, s);
            s.pop_back();
        }
}

int solution(string word) {
    int answer = 0;
    
    for(int i = 1; i <= 5; i++) make_word(i);
    
    sort(dic.begin(), dic.end());
    
    auto it = find(dic.begin(), dic.end(), word);
    
    return answer = distance(dic.begin(), it) + 1;
}