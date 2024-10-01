import java.util.*;
import java.io.*;

public class Main {

    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader r = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter w = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        Queue<Integer> q = new LinkedList<>();
        int rear = 0;

        n = Integer.parseInt(r.readLine());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(r.readLine());
            String c = st.nextToken();
            if (c.equals("push")){
                rear = Integer.parseInt(st.nextToken());
                q.add(rear);
            }else if(c.equals("pop")){
                w.write(String.valueOf(q.isEmpty() ? -1 : q.poll()) + "\n");
            }else if(c.equals("size")){
                w.write(String.valueOf(q.size()) + "\n");
            } else if (c.equals("empty")) {
                w.write(String.valueOf(q.isEmpty() ? 1 : 0) + "\n");
            } else if (c.equals("front")) {
                w.write(String.valueOf(q.isEmpty() ? "-1" : q.peek()) + "\n");
            } else {
                w.write(String.valueOf(q.isEmpty() ? "-1" : rear) + "\n");
            }
        }
        w.flush();
    }
}