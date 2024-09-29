import java.util.*;
import java.io.*;

public class Main {

    static int n;
    static int min = Integer.MAX_VALUE;
    static int[][] s;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader r = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(r.readLine());
        s = new int[n][n];
        visited = new boolean[n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(r.readLine(), " ");
            for (int j = 0; j < n; j++) {
                s[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        backtracking(0, 0);
        System.out.println(min);
    }

    static void backtracking(int len, int idx) {
        if (len == n / 2) {
            compare();
            return;
        }

        for (int i = idx; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                backtracking(len + 1, i + 1);
                visited[i] = false;
            }
        }
    }

    static void compare() {
        int start = 0;
        int link = 0;

        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (visited[i] && visited[j]) {
                    start += s[i][j] + s[j][i];
                } else if (!visited[i] && !visited[j]) {
                    link += s[i][j] + s[j][i];
                }
            }
        }

        min = Math.min(min, Math.abs(start - link));
    }
}