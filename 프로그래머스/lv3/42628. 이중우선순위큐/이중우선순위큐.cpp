#include <string>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    deque<int> dq;
    
    for (auto i:operations) {
        if (i[0] == 'I')
            dq.push_back(stoi(i.substr(2, i.size() - 2)));
        else if (!dq.empty() && i[0] == 'D') {
            if (i[2] == '1') {
                sort(dq.begin(), dq.end());
                dq.pop_back();
            }
            else {
                sort(dq.begin(), dq.end());
                dq.pop_front();
            }
        }
    }
    
    if(!dq.empty()){
        sort(dq.begin(), dq.end());
        answer.push_back(dq.back());
        answer.push_back(dq.front());
    }
    else{
        answer.push_back(0);
        answer.push_back(0);
    }
    
    return answer;
}