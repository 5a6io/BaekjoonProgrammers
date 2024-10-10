import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = new int[2];
        
        List<Integer> dq = new ArrayList<>();
        
        for(int i = 0; i < operations.length; i++){
            String[] s = operations[i].split(" ");
            if(s[0].equals("I")){
                dq.add(Integer.parseInt(s[1]));
            }
            else if(!dq.isEmpty() && s[0].equals("D")){
                if(s[1].equals("1"))
                    dq.remove(0);
                else
                    dq.remove(dq.size() - 1);
            }
            dq.sort((o1, o2) -> (o2 - o1));
        }
        
        if(dq.isEmpty()){
            answer[0] = 0;
            answer[1] = 0;
        }else{
            answer[0] = dq.get(0);
            answer[1] = dq.get(dq.size() - 1);
        }
        
        return answer;
    }
}