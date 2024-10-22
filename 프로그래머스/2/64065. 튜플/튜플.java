import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = {};
        
        s = s.replace('{', '\0').replace('}', '\0');
        String[] nums = s.split(",");
        Map<Integer, Integer> m = new HashMap<>();
        
        for(String n : nums){
            int tmp = Integer.parseInt(n.trim());
            m.put(tmp, m.getOrDefault(tmp, 0) + 1);
        }
        
        List<Integer> list = new ArrayList<>(m.keySet());
        list.sort((a, b) -> m.get(b) - m.get(a));
        
        return answer = list.stream().mapToInt(i -> i).toArray();
    }
}