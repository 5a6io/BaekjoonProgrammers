#include <vector>
#include <stack>

using namespace std;


int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<bool> visited(n, false);
    
    for(int i = 0; i < n; i++){
        if(visited[i])
            continue;
        else {
            visited[i] = true;
            stack<int> s;
            s.push(i);
            
            while(!s.empty()){
                int cur = s.top();
                s.pop();
                visited[cur] = true;
                
                for(int i = 0; i < n; i++){
                    if(visited[i])
                        continue;
                    if(computers[cur][i] == 0)
                        continue;
                    visited[i] = true;
                    s.push(i);
                }
            }
            answer++;
        }
    }
      
    return answer;
}