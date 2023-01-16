#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    auto i = min_element(arr.begin(), arr.end());
    arr.erase(i);
    if(arr.empty())
        answer.push_back(-1);
    else
        answer = arr;
    
    return answer;
}