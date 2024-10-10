import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        
        List<String> snum = new ArrayList<>();
        for(int i : numbers)
            snum.add(String.valueOf(i));
        
        snum.sort((o1, o2) -> ((o2 + o1).compareTo(o1 + o2)));
            
        for(int i = 0; i < numbers.length; i++)
            answer += snum.get(i);
        
        return answer.charAt(0) == '0' ? "0" : answer;
    }
}