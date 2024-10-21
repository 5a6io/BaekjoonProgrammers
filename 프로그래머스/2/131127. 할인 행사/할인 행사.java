import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        int days = 10;
        HashMap<String, Integer> m = new HashMap<>();
        for(int i = 0; i < want.length; i++)
            m.put(want[i], number[i]);
        
        for(int i = 0; i < discount.length - 9; i++){
            HashMap<String, Integer> d = new HashMap<>();
            for(int j = 0; j < 10; j++){
                d.put(discount[i + j], d.getOrDefault(discount[i + j], 0) + 1);
            }
            
            int sign = 0;
            for(Map.Entry<String, Integer> e : m.entrySet())
                if(d.containsKey(e.getKey()) && e.getValue() <= d.get(e.getKey())) sign++;
            
            answer += sign == want.length ? 1 : 0;
        }
        
        return answer;
    }
}