import java.util.*;
import java.io.*;

public class Main {

    static int n;
    static int m;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        HashMap<Long, Long> A = new HashMap<>();
        for (int i = 0; i < n; i++) {
            long key = Long.parseLong(st.nextToken());
            A.put(key, A.getOrDefault(key, 0l) + 1);
        }

        m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            long key = Long.parseLong(st.nextToken());
            if (A.containsKey(key)) {
                bw.write(A.get(key) + "\n");
            } else {
                bw.write("0\n");
            }
        }

        bw.close();
        br.close();
    }
}