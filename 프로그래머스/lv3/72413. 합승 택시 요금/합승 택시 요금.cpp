#include <algorithm>
#include <vector>

using namespace std;

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    vector<vector<int>> vertex(n + 1, vector<int>(n + 1, 999999));
    int answer = 999999;
    
    for(int i = 1; i <= n; i++)
        vertex[i][i] = 0;
    
    for(int i = 0; i < fares.size(); i++) {
        int x = fares[i][0], y = fares[i][1], w = fares[i][2];
        vertex[x][y] = w;
        vertex[y][x] = w;
    }
    
    for(int k = 1; k <= n; k++)
        for(int i = 1; i <= n; i++)
            for(int j = 1; j <= n; j++){
                if(i == j || i == k || j == k) continue;
                if(vertex[i][k] + vertex[k][j] < vertex[i][j])
                    vertex[i][j] = vertex[i][k] + vertex[k][j];
            }
    
    answer = vertex[s][a] + vertex[s][b];
    
    for(int i = 1; i <= n; i++)
            answer = min(answer, vertex[s][i] + vertex[i][a] + vertex[i][b]);
    
    return answer;
}