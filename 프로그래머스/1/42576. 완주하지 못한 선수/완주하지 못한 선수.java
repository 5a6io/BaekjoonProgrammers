import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        HashMap<String, Integer> m = new HashMap<>();
        
        for(int i = 0; i < participant.length; i++){
            m.put(participant[i], m.getOrDefault(participant[i],0)+1);
        }
        
        for(int i = 0; i < completion.length; i++){
            m.put(completion[i], m.get(completion[i]) - 1);
            if(m.get(completion[i]) == 0)
                m.remove(completion[i]);
        }
        
        Iterator<String> i = m.keySet().iterator();
        
        return answer = i.next();
    }
}