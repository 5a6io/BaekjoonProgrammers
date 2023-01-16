#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr, int divisor) {
    vector<int> answer;
    for(auto it = arr.begin(); it != arr.end(); it++) {
        if(*it % divisor == 0)
            answer.push_back(*it);
    }
    
    if(answer.empty())
        answer.push_back(-1);
    else
        sort(answer.begin(), answer.end());
            
    return answer;
}