#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<vector<int> > land)
{
    int answer = 0;
    int sum = 0;
    vector<vector<int>> score(land.size(), vector<int>(4, 0));
    
    for(int i = 0; i < 4; i++)
        score[0][i] = land[0][i];
        
    for(int i = 1; i < land.size(); i++){
        for(int j = 0; j < 4; j++){
            int max = 0;
            for(int k = 0; k < 4; k++){
                if(j != k && max < score[i-1][k])
                    max = score[i-1][k];
            }
            score[i][j] = max + land[i][j];
        }
    }

    return answer = *max_element(score[land.size()-1].begin(), score[land.size()-1].end());
}