import java.util.*;
import java.io.*;

public class Main {

    static int n;
    static int[] a;

    public static void main(String[] args) throws IOException {
        BufferedReader r = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter w = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(r.readLine());
        a = new int[n];
        int[] dp = new int[n];

        StringTokenizer st = new StringTokenizer(r.readLine());

        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < n; i++) {
            dp[i] = a[i];
            for (int j = 0; j < n; j++) {
                if (a[i] > a[j] && dp[j] + a[i] > dp[i]) {
                    dp[i] = dp[j] + a[i];
                }
            }
        }

        int max = 0;
        for (int i = 0; i < n; i++) {
            max = Math.max(max, dp[i]);
        }

        System.out.println(max);
    }
}