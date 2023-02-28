#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    
    sort(dungeons.begin(), dungeons.end());
    
    do{
        int count = 0;
        int current_k = k;
        for(auto& i : dungeons){
            if(current_k >= i[0]){
                current_k -= i[1];
                count++;
            }
        }
        answer = max(answer, count);
    }while (next_permutation(dungeons.begin(), dungeons.end()));
    
    return answer;
}