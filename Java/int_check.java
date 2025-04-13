import java.util.Scanner;

public class int_check {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a integer: ");
        if (sc.hasNextInt()) {
            int num = sc.nextInt();
            System.out.println("The number " + num + " is valid");
        } else {
            System.out.println("Not an Integer");
        }
    }

}
