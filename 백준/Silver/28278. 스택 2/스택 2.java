import java.util.*;
import java.io.*;

public class Main {

    static int n;
    
    static BufferedReader r = new BufferedReader(new InputStreamReader(System.in)); // 입력

    public static void main(String[] args) throws IOException {

        n = Integer.parseInt(r.readLine());

        Stack<Integer> stack = new Stack<>();

        StringTokenizer st;
        while (n-- > 0) {
            st = new StringTokenizer(r.readLine());
            String c = st.nextToken();
            if (c.equals("1")) {
                stack.push(Integer.parseInt(st.nextToken()));
            } else if (c.equals("2")) {
                System.out.println(stack.empty() ? -1 : stack.pop());
            } else if (c.equals("3")) {
                System.out.println(stack.size());
            } else if (c.equals("4")) {
                System.out.println(stack.empty() ? 1 : 0);
            } else {
                System.out.println(stack.empty() ? -1 : stack.peek());
            } 
        }
    }
}