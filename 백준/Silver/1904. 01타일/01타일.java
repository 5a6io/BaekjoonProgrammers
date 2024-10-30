import java.io.*;

public class Main {

    static int n;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine());

        long[] dp = new long[1000001];
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 2;
        
        for(int i = 3; i <= n; i++)
            dp[i] = (dp[i - 1] + dp[i - 2]) % 15746;

        bw.write(String.valueOf(dp[n]));
        bw.flush();
        bw.close();
        br.close();
    }
}