import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        boolean[][] graph = new boolean[n + 1][n + 1];
        int[] dist = new int[n + 1];

        for(int i = 0; i < edge.length; i++){
            int u = edge[i][0], v = edge[i][1];
            graph[u][v] = graph[v][u] = true;
        }

        Queue<Integer> q = new LinkedList<>();

        q.add(1);
        while (!q.isEmpty()) {
            int cur = q.poll();
            for (int i = 2; i <= n; i++) {
                if (graph[cur][i] && dist[i] == 0) {
                    q.add(i);
                    dist[i] += dist[cur] + 1;
                }
            }
        }
        
        Arrays.sort(dist);
        for (int i = n; i > 1; i--)
            if (dist[i] != dist[i - 1])
                return n - i + 1;
        
        return n - 1;
    }
}