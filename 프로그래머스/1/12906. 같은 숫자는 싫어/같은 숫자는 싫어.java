import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> answer = new ArrayList<>();
        
        for (int i : arr) {
            if(answer.isEmpty())
                answer.add(i);
            else {
                if(answer.get(answer.size() - 1) != i)
                    answer.add(i);
            }
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }
}