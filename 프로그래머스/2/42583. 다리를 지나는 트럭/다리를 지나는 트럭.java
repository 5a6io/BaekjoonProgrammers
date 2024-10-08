import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> q = new LinkedList<>();
        
        for(int i = 0; i < bridge_length; i++)
            q.add(0);
        
        int n = truck_weights.length;
        int total = 0;
        int i = 0;
        
        if(bridge_length == 1)
            return n + 1;
        if(n == 1)
            return bridge_length + 1;
        
        while(i < n){
            total -= q.poll();
            answer++;
            
            if(total + truck_weights[i] <= weight){
                q.add(truck_weights[i]);
                total += truck_weights[i++];
            }else{
                q.add(0);
            }
        }
        
        
        return answer + bridge_length;
    }
}