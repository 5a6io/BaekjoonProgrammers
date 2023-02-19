#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer(prices.size(), 0);
    stack<int> rise;
    
    for(int i = 0; i < prices.size(); i++){
        while (!rise.empty() && prices[rise.top()] > prices[i]) {
            answer[rise.top()] = i - rise.top();
            rise.pop();
        }
        rise.push(i);
    }
    
    while(!rise.empty()) {
        answer[rise.top()] = prices.size() - 1 - rise.top();
        rise.pop();
    }
    
    return answer;
}