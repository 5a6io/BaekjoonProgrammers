import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        
        Arrays.sort(jobs, Comparator.comparingInt(a -> a[0]));
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        
        int time = 0;
        int idx = 0;
        while(idx < jobs.length || !pq.isEmpty()){
            while (idx < jobs.length && jobs[idx][0] <= time){
                pq.add(jobs[idx++]);
            }
            
            if (pq.isEmpty()){
                time = jobs[idx][0];
                continue;
            }
            
            int[] job = pq.poll();
            time += job[1];
            answer += time - job[0];
        }
        
        answer /= jobs.length;
        return (int) answer;
    }
}