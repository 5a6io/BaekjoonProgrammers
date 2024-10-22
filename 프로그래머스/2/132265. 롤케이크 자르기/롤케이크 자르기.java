import java.util.*;

class Solution {
    
    public int solution(int[] topping) {
        int answer = 0;
        int e = topping.length;
        
        HashMap<Integer, Integer> m = new HashMap<>();
        HashSet<Integer> c = new HashSet<>();
        for(int i = 0; i < e; i++){
            c.add(topping[i]);
            m.put(i, c.size());
        }
        
        HashSet<Integer> b = new HashSet<>();
        for(int i = e - 1; i > 0; i--){
            b.add(topping[i]);
        
            if(m.get(i - 1) == b.size()) answer++;
        }
        
        
        return answer;
    }
}