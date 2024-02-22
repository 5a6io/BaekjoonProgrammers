#include <string>
#include <vector>
#include <algorithm>
#define INF 1000000

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
        
    vector<int> dist(n+1, INF);
    
    dist[1] = 0;
    for(int i = 1; i <= n; i++){
        for(int j = 0; j < edge.size(); j++){
            int from = edge[j][0];
            int to = edge[j][1];
            
            if(dist[from] != INF && dist[to] > dist[from] + 1) dist[to] = dist[from] + 1;
            else if(dist[to] != INF && dist[from] > dist[to] + 1) dist[from] = dist[to] + 1;
        }
    }
    
    sort(dist.rbegin(), dist.rend() - 1);
    
    int m = -1;
    for(int i = 1; i < n; i++) {
        if(dist[i] != INF && dist[i] >= m){
            m = dist[i];
            answer++;
        }
    }
        
    return answer;
}