#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    vector<int> nums;
    
    for(int i = 1; i < n; i++)
        if(n%i == 1)
            nums.push_back(i);
    answer = nums[0];
    
    return answer;
}