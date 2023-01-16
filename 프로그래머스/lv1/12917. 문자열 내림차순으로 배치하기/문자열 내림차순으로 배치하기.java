import java.util.Arrays;

class Solution {
    public String solution(String s) {
        String answer = "";
        char a[] = s.toCharArray();
        Arrays.sort(a);
        for(int i = s.length()-1;i>=0;i--)
            answer += Character.toString(a[i]);
        return answer;
    }
}