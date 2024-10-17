import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        Arrays.sort(times);
        long low = times[0];
        long high = (long) n * times[times.length - 1];
        long answer = 0;
        
        while(low <= high){
            long mid = (low + high) / 2;
            long p = 0;
            for(int t : times)
                p += mid / t;
            if(p >= n) {
                answer = mid;
                high = mid - 1;
            }
            else
                low = mid + 1;
        }
        
        return answer;
    }
}