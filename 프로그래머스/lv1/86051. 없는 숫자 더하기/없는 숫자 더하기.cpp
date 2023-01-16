#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> numbers) {
    int answer = 0;
    for(auto i = 0;i <= 9; i++)
        if(auto f = find(numbers.begin(), numbers.end(), i); f == numbers.end())
            answer += i;
    
        
    return answer;
}