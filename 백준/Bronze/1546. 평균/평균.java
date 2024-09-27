import java.util.*;

public class Main {

    static int n;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        float[] score = new float[n];

        for (int i = 0; i < n; i++) {
            score[i] = sc.nextInt();
        }

        float m = 0;
        for (int i = 0; i < n; i++) {
            if (score[i] > m) {
                m = score[i];
            }
        }

        float sum = 0;
        for (int i = 0; i < n; i++) {
            score[i] = score[i] / m * 100;
            sum += score[i];
        }

        System.out.println(sum / n);
    }
}