#include<vector>
#include<queue>
using namespace std;

struct Dir{
    int y;
    int x;
};

int solution(vector<vector<int> > maps)
{
    int answer = 0;
    int moveDir[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}}; // 우, 좌, 상, 하
    int m = maps.size();
    int n = maps[0].size();
    queue<Dir> road;
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    vector<vector<int>> dist(m, vector<int>(n, 0));
    
    road.push({0, 0});
    visited[0][0] = true;
    dist[0][0] = 1;
    
    while(!road.empty()) {
        Dir cur = road.front();
        road.pop();
        
        int y = cur.y;
        int x = cur.x;
        
            for(int i = 0; i < 4; i++) {
                int nextY = y + moveDir[i][0];
                int nextX = x + moveDir[i][1];
            
            
                if(nextY < 0 || nextX < 0 || nextY > m - 1 || nextX > n - 1)
                    continue;
                if(maps[nextY][nextX] == 0)
                    continue;
                if(visited[nextY][nextX])
                    continue;
                
                visited[nextY][nextX] = true;
                road.push({nextY, nextX});
                dist[nextY][nextX] = dist[y][x] + 1;
            }
    }
    
    if(!visited[m - 1][n - 1])
        return -1;
    else
        return dist[m - 1][n - 1];
    
    return answer;
}