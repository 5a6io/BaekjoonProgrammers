import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = new int[2];
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(); // 최소 힙
        PriorityQueue<Integer> rpq = new PriorityQueue<>(Collections.reverseOrder()); // 최대 힙
        
        for(int i = 0; i < operations.length; i++){
            String[] s = operations[i].split(" ");
            if(s[0].equals("I")){
                pq.add(Integer.parseInt(s[1]));
                rpq.add(Integer.parseInt(s[1]));
            }
            else if(!pq.isEmpty() && !rpq.isEmpty() && s[0].equals("D")){
                if(s[1].equals("1")){
                    int max = rpq.poll();
                    pq.remove(max);
                }
                else{
                    int min = pq.poll();
                    rpq.remove(min);
                }
            }
        }
        
        if(pq.isEmpty() && rpq.isEmpty()){
            answer[0] = 0;
            answer[1] = 0;
        }else{
            answer[0] = rpq.peek();
            answer[1] = pq.peek();
        }
        
        return answer;
    }
}