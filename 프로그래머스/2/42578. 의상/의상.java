import java.util.HashMap;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        HashMap<String, Integer> m = new HashMap<>();
        
        for(int i = 0; i < clothes.length; i++)
            m.put(clothes[i][1], m.getOrDefault(clothes[i][1], 0) + 1);
        
        for(String i : m.keySet())
            answer *= (m.get(i) + 1);
        
        
        return answer - 1;
    }
}