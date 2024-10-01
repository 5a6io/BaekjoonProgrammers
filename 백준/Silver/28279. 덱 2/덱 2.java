import java.util.*;
import java.io.*;

public class Main {

    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        Deque<Integer> dq = new LinkedList<>();

        n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            int c = Integer.parseInt(st.nextToken());
            if (c == 1) {
                dq.addFirst(Integer.parseInt(st.nextToken()));
            } else if (c == 2) {
                dq.addLast(Integer.parseInt(st.nextToken()));
            } else if (c == 3) {
                bw.write(String.valueOf(dq.isEmpty() ? -1 : dq.pollFirst()) + "\n");
            } else if (c == 4) {
                bw.write(String.valueOf(dq.isEmpty() ? -1 : dq.pollLast()) + "\n");
            } else if (c == 5) {
                bw.write(String.valueOf(dq.size()) + "\n");
            } else if (c == 6) {
                bw.write(String.valueOf(dq.isEmpty() ? 1 : 0) + "\n");
            } else if (c == 7) {
                bw.write(String.valueOf(dq.isEmpty() ? -1 : dq.getFirst()) + "\n");
            } else {
                bw.write(String.valueOf(dq.isEmpty() ? -1 : dq.getLast()) + "\n");
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }
}