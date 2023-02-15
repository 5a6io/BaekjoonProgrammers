#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool isPrime(int n){
    for(int i = 2; i < n; ++i)
        if(n % i == 0)
            return false;
    
    return true;
}

int solution(vector<int> nums) {
    int answer = 0;
    vector<bool> check(nums.size());
    fill(check.end() - 3, check.end(), true);
    
    do {
        int sum = 0;
        for(int i = 0; i < nums.size(); ++i)
            if(check[i])
                sum += nums[i];
        
        if(isPrime(sum)){
            cout << sum << endl;
            ++answer;
        }
        
    } while(next_permutation(check.begin(), check.end()));
    
    return answer;
}