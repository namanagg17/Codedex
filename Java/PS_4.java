import java.util.Random;
import java.util.Scanner;

public class PS_4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // PROBLEM 1
        // int a = 10;
        // if (a = 11) {
        // System.out.println("I am 11");
        // } else {
        // System.out.println("I am not 11");
        // }

        // PROBLEM 2
        // byte s1, s2, s3;
        // System.out.print("Subject 1: ");
        // s1 = sc.nextByte();
        // System.out.print("Subject 2: ");
        // s2 = sc.nextByte();
        // System.out.print("Subject 3: ");
        // s3 = sc.nextByte();
        // float avg = (s1 + s2 + s3) / 3.0f;
        // System.out.println("Your percentage is " + avg + "%");
        // if (avg > 40 && s1 > 33 && s2 > 33 && s3 > 33) {
        // System.out.println("you passed all subs");
        // } else {
        // System.out.println("you failed");
        // }

        // // PROBLEM 3
        // // System.out.println("Enter your income in Lakhs per annum");
        // // float tax = 0;
        // // float income = sc.nextFloat();
        // // if (income <= 2.5) {
        // // tax = tax + 0;
        // // } else if (income > 2.5f && income <= 5f) {
        // // tax = tax + 0.05f * (income - 2.5f);
        // // } else if (income > 5f && income <= 10.0f) {
        // // tax = tax + 0.05f * (5.0f - 2.5f);
        // // tax = tax + 0.2f * (income - 5f);
        // // } else if (income > 10.0f) {
        // // tax = tax + 0.05f * (5.0f - 2.5f);
        // // tax = tax + 0.2f * (10.0f - 5f);
        // // tax = tax + 0.3f * (income - 10.0f);
        // // }

        // System.out.println("The total tax paid by the employee is: " + tax);

        // PROBLEM 4
        // int day = sc.nextInt();
        // switch (day){
        // case 1 -> System.out.println("Monday");
        // case 2 -> System.out.println("Tuesday");
        // case 3 -> System.out.println("Wednesday");
        // case 4 -> System.out.println("Thursday");
        // case 5 -> System.out.println("Friday");
        // case 6 -> System.out.println("Saturday");
        // case 7 -> System.out.println("Sunday");
        // }

        // PROBLEM 5
        String website = sc.next();
        if (website.endsWith(".org")) {
            System.out.println("This is an organizational website");
        } else if (website.endsWith(".com")) {
            System.out.println("This is a Commercial website");
        } else if (website.endsWith(".in")) {
            System.out.println("This is an Indian website");
        }
    }
}
