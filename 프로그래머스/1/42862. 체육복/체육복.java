import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n;
        boolean[] visit = new boolean[n+1];
        int[] b = new int[n+1];
        Arrays.fill(b, 1);
        b[0] = 0;
        
        for(int i = 0; i < reserve.length; i++)
            b[reserve[i]] += 1;
        for(int i = 0; i < lost.length; i++)
            b[lost[i]] -= 1;
        
        for(int i = 1; i <= n; i++){
            if(b[i] == 0){
                if(i-1 > 0 && b[i-1] == 2 && !visit[i-1]){
                    b[i-1]--;
                    b[i]++;
                    visit[i-1] = true;
                }
                else if(n >= i+1 && b[i+1]==2 && !visit[i+1]){
                    b[i+1]--;
                    b[i]++;
                    visit[i+1] = true;
                }
            }
        }
        
        for(int i = 1; i <= n; i++){
            if(b[i] == 0)
                answer--;
        }
        
        
        return answer;
    }
}