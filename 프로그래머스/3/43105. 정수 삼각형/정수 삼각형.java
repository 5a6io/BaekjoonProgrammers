import java.util.Arrays;

class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        int n = triangle.length;
        int[][] dp = new int[n][n];
        dp[0][0] = triangle[0][0];
        
        for(int i = 0; i < n - 1; i++){
            for(int j = 0; j < triangle[i].length; j++){
                dp[i + 1][j] = Math.max(dp[i][j] + triangle[i + 1][j], dp[i + 1][j]);
                dp[i + 1][j + 1] = Math.max(dp[i][j] + triangle[i + 1][j + 1], dp[i + 1][j +  1]);
            }
        }
        
        return answer = Arrays.stream(dp[n - 1]).max().orElse(0);
    }
}