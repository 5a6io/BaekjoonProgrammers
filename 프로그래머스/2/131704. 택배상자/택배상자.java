import java.util.*;

class Solution {
    public int solution(int[] order) {
        int answer = 0;
        Stack<Integer> s = new Stack<>();
        int idx = 0;
        for(int i = 1; i <= order.length; i++){
            s.add(i);
            while(!s.isEmpty() && s.peek() == order[idx]){
                s.pop();
                answer++;
                idx++;
            }
        }
        
        return answer;
    }
}