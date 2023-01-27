#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> A, vector<int> B)
{
    int answer = 0;
    
    sort(A.begin(), A.end());
    sort(B.rbegin(), B.rend());
    
    auto i = A.begin();
    auto j = B.begin();
    while(i != A.end() && j != B.end()){
        answer += (*i * *j);
        i++;
        j++;
    }
    
    return answer;
}