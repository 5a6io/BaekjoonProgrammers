import java.util.*;

class Solution {
    
    static int dfs(int[] numbers, int sum, int idx, int target){
        if(idx == numbers.length) {
            if(target == sum)
                return 1;
            else
                return 0;
        }
        
        return dfs(numbers, sum + numbers[idx], idx + 1, target) + dfs(numbers, sum - numbers[idx], idx + 1, target);
    }
    
    public int solution(int[] numbers, int target) {
        int answer = 0;
        
        answer = dfs(numbers, 0, 0, target);
        
        return answer;
    }
}