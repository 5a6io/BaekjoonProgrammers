import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int n = nums.length;
        
        HashSet<Integer> k = new HashSet<>();
        
        for(int i = 0; i < n; i++){
            if(k.size() < n/2)
                k.add(nums[i]);
        }
        
        return answer = k.size();
    }
}