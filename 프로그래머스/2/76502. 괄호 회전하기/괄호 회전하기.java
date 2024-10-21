import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        char[] c = s.toCharArray();
        int n = c.length;
        for(int i = 0; i < n; i++){
            Stack<Character> st = new Stack<>();
            for(int j = i; j < i + n; j++){
                int idx = j % n;
                if(st.isEmpty()) st.push(c[idx]);
                else{
                    if(st.peek() == '(' && c[idx] == ')') st.pop();
                    else if(st.peek() == '[' && c[idx] == ']') st.pop();
                    else if(st.peek() == '{' && c[idx] == '}') st.pop();
                    else st.push(c[idx]);
                }
            }
            if(st.isEmpty())
                answer++;
        }
        
        return answer;
    }
}