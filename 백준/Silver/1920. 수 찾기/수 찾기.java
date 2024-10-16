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
        HashSet<Long> A = new HashSet<>();
        for (int i = 0; i < n; i++) {
            A.add(Long.parseLong(st.nextToken()));
        }

        m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            if (A.contains(Long.parseLong(st.nextToken()))) {
                bw.write("1\n");
            } else {
                bw.write("0\n");
            }
        }

        bw.close();
        br.close();
    }
}