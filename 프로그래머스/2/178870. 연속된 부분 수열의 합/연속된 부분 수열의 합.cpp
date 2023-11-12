#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> sequence, int k) {
    vector<int> answer;
    answer.push_back(0);
    answer.push_back(sequence.size());
    
    int sum = sequence[0];
    int start = 0, end = 0;
    
    while(end < sequence.size()) {
        if(sum < k){
            end++;
            if(end == sequence.size()) break;
            sum += sequence[end];
        }
        else {
            if(sum == k && (answer[1] - answer[0] > end - start)){
                answer[0] = start;
                answer[1] = end;
            }
            sum -= sequence[start];
            start++;
        }
    }
    
    return answer;
}