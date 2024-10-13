import java.util.Arrays;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        int n = citations.length;
        Arrays.sort(citations);
        
        int max = 0;
        for(int i = 0; i < n; i++){
            int min = Math.min(citations[i], n - i);
            max = max < min ? min : max;
        }
        
        return answer = max;
    }
}