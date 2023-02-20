#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int k, int m, vector<int> score) {
    int answer = 0;
    int i = m - 1;
    
    sort(score.begin(), score.end(), greater<int>());
    
    while(i < score.size()){
        answer += score[i] * m;
        i += m;
    }
    
    return answer;
}