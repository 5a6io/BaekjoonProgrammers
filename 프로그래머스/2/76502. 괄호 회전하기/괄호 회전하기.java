import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        int n = s.length();
        
        for(int i = 0; i < n; i++){
            Stack<Character> st = new Stack<>();
            for(int j = i; j < i + n; j++){
                int idx = j % n;
                if(st.isEmpty()) st.push(s.charAt(idx));
                else{
                    if(st.peek() == '(' && s.charAt(idx) == ')') st.pop();
                    else if(st.peek() == '[' && s.charAt(idx) == ']') st.pop();
                    else if(st.peek() == '{' && s.charAt(idx) == '}') st.pop();
                    else st.push(s.charAt(idx));
                }
            }
            if(st.isEmpty())
                answer++;
        }
        
        return answer;
    }
}