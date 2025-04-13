import java.util.Scanner;

public class kilometersTOmiles {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter kilometers: ");
        int km = sc.nextInt();
        double miles = 0.62 * km;
        System.out.println(km + "km = " + miles + " miles");
    }
}
