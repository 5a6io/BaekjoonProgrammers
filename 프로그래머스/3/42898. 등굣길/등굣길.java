import java.util.*;

class Solution {
    
    static final int MOD = 1000000007;
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        int[][] dp = new int[n][m];
        
        for (int[] p : puddles){
            dp[p[1]-1][p[0]-1] = -1;
        }
        
        if (dp[0][0] == -1) return 0;
        
        dp[0][0] = 1;
        
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (dp[i][j] == -1){
                    dp[i][j] = 0;
                    continue;
                } 
                if (i > 0) dp[i][j] = (dp[i][j] + dp[i-1][j])%MOD;
                if (j > 0) dp[i][j] = (dp[i][j] + dp[i][j-1])%MOD;
            }
        }
        
        answer = dp[n-1][m-1];
        return answer;
    }
}