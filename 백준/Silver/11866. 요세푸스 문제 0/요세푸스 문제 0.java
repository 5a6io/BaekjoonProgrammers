import java.util.*;
import java.io.*;

public class Main {

    static int n;
    static int k;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            q.add(i);
        }
        int cnt = 0;
        bw.write("<");
        while (q.size() != 1) {
            int cur = q.poll();
            cnt++;
            if (cnt % k == 0) {
                bw.write(String.valueOf(cur) + ", ");
            } else {
                q.add(cur);
            }
        }
        bw.write(String.valueOf(q.poll()) + ">");
        bw.flush();
        bw.close();
        br.close();
    }
}