#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;
    
    vector<vector<int>> tr(n, vector<int>(n, 0));
    int max_num = (n * (n + 1)) / 2;
    int num = 1;
    int top = 0, bottom = n - 1, left = 0, right = 0;
    int state = 0;
    while(num <= max_num) {
        if(state == 0){
            for(int i = top; i <= bottom; i++) tr[i][left] = num++;
            top++;
            left++;
            state = 1;
        }
        if(state == 1){
            for(int i = left; i <= bottom - right; i++) tr[bottom][i] = num++;
            bottom--;
            state = 2;
        }
        if(state == 2){
            for(int i = bottom; i >= top; i--) tr[i][i - right] = num++;
            right++;
            top++;
            state = 0;
        }
    }
    
    for(int i = 0; i < n; i++)
        for(int j = 0; j <= i; j++)
            answer.push_back(tr[i][j]);
    
    return answer;
}