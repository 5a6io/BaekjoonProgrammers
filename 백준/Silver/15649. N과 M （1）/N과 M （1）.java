import java.util.*;
import java.io.*;

public class Main {

    static int n;
    static int m;
    static boolean[] visited;
    static ArrayList<Integer> result = new ArrayList<>();

    static BufferedReader r = new BufferedReader(new InputStreamReader(System.in)); // 입력

    static void backtracking() {
        if (result.size() == m) {
            for (int i = 0; i < m; i++) System.out.print(String.valueOf(result.get(i)) + " ");
            System.out.println();
            return;
        }

        for (int i = 1; i <= n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                result.add(i);
                backtracking();
                visited[i] = false;
                result.remove(result.size()-1);
            }
        }
    }

    public static void main(String[] args) throws IOException {

        StringTokenizer st = new StringTokenizer(r.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        visited = new boolean[n + 1];
        Arrays.fill(visited, false);

        backtracking();
    }
}