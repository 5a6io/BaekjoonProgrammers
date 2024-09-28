import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        
        Queue<Integer> q = new LinkedList<>();
        
        for(int i : prices)
            q.offer(i);
        
        int i = 0;
        while(!q.isEmpty()){
            int current = q.poll();
            
            for(int x : q){
                answer[i]++;
                if(current > x) break;
            }
            
            i++;
        }
        
        return answer;
    }
}