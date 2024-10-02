import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i = 0; i < scoville.length; i++){
            pq.add(scoville[i]);
        }
        
        while(pq.peek() < K){
            if (pq.peek() < K && pq.size() < 2)
                return -1;
            int min1 = pq.poll();
            int min2 = pq.poll();
            
            int k = min1 + (min2 * 2);
            answer++;
            pq.add(k);
        }
        
        return answer;
    }
}