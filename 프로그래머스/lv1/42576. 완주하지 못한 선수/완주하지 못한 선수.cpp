#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    map<string, int> table;

    for (auto i = participant.begin(); i != participant.end(); i++)
        table[*i]++;
    
    for(auto i = completion.begin(); i != completion.end(); i++){
        auto it = table.find(*i);
        if(it != table.end()){
            if(it -> second > 1)
                it -> second--;
            else
                table.erase(*i);
            }
    }
    
    for(auto i = table.begin(); i != table.end(); i++)
        answer += i -> first;

    return answer;
}