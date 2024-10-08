import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        Queue<Integer> q = new LinkedList<>();
        int n = progresses.length;
        
        for (int i = 0; i < n; i++) {
            int remain = 100 - progresses[i];
            int day = remain / speeds[i];
            if(remain % speeds[i] != 0)
                day++;
            q.add(day);
        }
        
        int cnt = 1;
        int cur = q.poll();
        while(!q.isEmpty()){
            if(q.peek() <= cur){
                cnt++;
                q.poll();
            }
            else {
                answer.add(cnt);
                cnt = 1;
                cur = q.poll();
            }
        }
        answer.add(cnt);
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}