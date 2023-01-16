#include <string>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    string s = to_string(n);
    vector<int> arr;

    for(auto i = s.begin(); i != s.end(); i++)
        arr.push_back(*i-'0');

    sort(arr.begin(), arr.end());

    for(auto i = 0; i < arr.size(); i++)
        answer += (arr[i] * pow(10, i));
    
    return answer;
}