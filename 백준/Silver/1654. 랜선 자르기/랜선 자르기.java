import java.util.*;
import java.io.*;

public class Main {

    static int n;
    static int k;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        k = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        long[] lan = new long[k];
        for (int i = 0; i < k; i++) {
            lan[i] = Long.parseLong(br.readLine());
        }

        long low = 1;
        long high = Arrays.stream(lan).max().getAsLong();

        while (low <= high) {
            long mid = (low + high) / 2;
            long l = 0;
            for (long i : lan)
                l += i / mid;

            if(l >= n)
                low = mid + 1;
            else
                high = mid - 1;
        }

        bw.write(String.valueOf(high));
        bw.close();
        br.close();
    }
}