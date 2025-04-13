import java.util.Scanner;

public class cbse_marks {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("subject1");
        int s1 = sc.nextInt();
        System.out.println("subject2");
        int s2 = sc.nextInt();
        System.out.println("subject3");
        int s3 = sc.nextInt();
        int x = s1 + s2 + s3;
        double total = (x / 300.0) * 100;
        System.out.println(total);

    }
}
