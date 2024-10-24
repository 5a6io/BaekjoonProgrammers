import java.util.*;

class Solution {
    public int solution(int[] order) {
        int answer = 0;
        Stack<Integer> s = new Stack<>();
        Queue<Integer> q = new LinkedList<>();
        
        for(int i = 1; i <= order.length; i++){
            q.add(i);
        }
        
        int i = 0;
        while(!q.isEmpty()){
            int o = q.poll();
            if(o != order[i]){
                s.push(o);
            }
            else {
                i++;
                answer++;
                while(!s.isEmpty() && s.peek() == order[i]){
                    s.pop();
                    answer++;
                    i++;
                }
            }
        }
        
        return answer;
    }
}