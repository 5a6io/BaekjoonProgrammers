#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int n, long long left, long long right) {
    vector<int> answer;
    
    for(long long i=left; i<=right; i++)
        answer.push_back(max(i/n,i%n)+1);  /*i를 배열의 길이로 나누면 행, 배열의 길이의 나머지를 구하면 열
                                             이 중 큰 값에 1을 더하면 해당 위치에 들어갈 값을 알 수 있음*/
    
    return answer;
}