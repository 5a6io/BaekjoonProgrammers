import java.util.*;
import java.io.*;

public class Main {

    static int n;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] a = new int[n];
        for(int i = 0; i < n; i++)
            a[i] = Integer.parseInt(st.nextToken());

        int[] in_dp = new int[n];
        int[] de_dp = new int[n];
        Arrays.fill(in_dp, 1);
        Arrays.fill(de_dp, 1);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (a[i] > a[j])
                    in_dp[i] = Math.max(in_dp[i], in_dp[j] + 1);
            }
        }

        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j > i; j--) {
                if (a[i] > a[j])
                    de_dp[i] = Math.max(de_dp[i], de_dp[j] + 1);
            }
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans = Math.max(ans, in_dp[i] + de_dp[i]);
        }

        bw.write(String.valueOf(ans - 1));
        bw.close();
        br.close();
    }
}