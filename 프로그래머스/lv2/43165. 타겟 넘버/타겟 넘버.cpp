#include <string>
#include <vector>

using namespace std;

int answer = 0;

void dfs(vector<int> numbers, int index, int target, int sum){
    if(index == numbers.size()) {
        if(sum == target)
            answer++;
        return;
    }
    
    dfs(numbers, index + 1, target, sum + numbers[index]);
    dfs(numbers, index + 1, target, sum - numbers[index]);
}

int solution(vector<int> numbers, int target) {
    dfs(numbers, 0, target, 0);
    
    return answer;
}