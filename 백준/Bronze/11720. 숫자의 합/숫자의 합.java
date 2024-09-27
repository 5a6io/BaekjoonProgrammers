import java.util.*;

public class Main {

    static int n;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        String num = sc.next();
        char[] cNum = num.toCharArray();

        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += cNum[i] - '0';
        }

        System.out.println(sum);
    }
}