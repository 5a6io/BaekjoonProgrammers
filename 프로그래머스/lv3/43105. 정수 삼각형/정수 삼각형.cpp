#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> triangle) {
    int answer = 0;
    vector<vector<int>> sum(triangle.size(), vector<int>(triangle.size(), 0));
    sum[0][0] = triangle[0][0];
    
    for(int i = 0; i < triangle.size() - 1; i++)
        for(int j = 0; j < triangle[i].size(); j++){
            sum[i+1][j] = max(sum[i+1][j], sum[i][j] + triangle[i+1][j]);
            sum[i+1][j+1] = max(sum[i+1][j+1], sum[i][j] + triangle[i+1][j+1]);
        }
    
    return answer = *max_element(sum[sum.size()-1].begin(), sum[sum.size()-1].end());
}