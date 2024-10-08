import java.util.*;

public class Solution {
    public Stack solution(int []arr) {
        Stack<Integer> answer = new Stack<>();
        
        for (int i : arr) {
            if(answer.isEmpty() || answer.peek() != i)
                answer.push(i);
        }

        return answer;
    }
}