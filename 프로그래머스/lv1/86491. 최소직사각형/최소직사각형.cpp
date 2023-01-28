#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) { // sizes 배열을 모두 탐색하여 각 명함의 긴 길이를 앞에 짧은 길이는 뒤에
    int answer = 0;
    
    for(int i = 0; i < sizes.size(); i++){
        if(sizes[i][0] < sizes[i][1]){
            int temp = sizes[i][0];
            sizes[i][0] = sizes[i][1];
            sizes[i][1] = temp;
        }
    }
    
    int w = sizes[0][0], h = sizes[0][1];
    for(int i = 0; i < sizes.size(); i++) {
        w = max(w, sizes[i][0]);
        h = max(h, sizes[i][1]);
    }
    
    return answer = w * h;
}