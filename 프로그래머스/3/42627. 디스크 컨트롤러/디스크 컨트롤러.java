import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        
        Arrays.sort(jobs, (o1, o2) -> (o1[0] - o2[0]));
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> (o1[1] - o2[1]));
                
        int task = jobs.length, i = 0, time = 0;
        while (i < task || !pq.isEmpty()) {
            for(; i < task && jobs[i][0] <= time; i++)
                pq.add(jobs[i]);
            
            if(!pq.isEmpty() && pq.peek()[0] <= time){
                time += pq.peek()[1];
                answer += (time - pq.peek()[0]);
                pq.poll();
            }else
                time++;
        }
        
        return answer / task;
    }
}