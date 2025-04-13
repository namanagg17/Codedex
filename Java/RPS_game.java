import java.util.Scanner;
import java.util.Random;

public class RPS_game {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();
        System.out.println("WELCOME TO ROCK,PAPER,SCISSOR GAME!");
        System.out.println(" | Rock=1 | Paper=2 | Scissor=3 | ");
        System.out.print("To play the game enter your input: ");
        int u = sc.nextInt();
        int c = rand.nextInt(3) + 1;
        if (c == 1) {
            System.out.println("Computer choose Rock ");
        } else if (c == 2) {
            System.out.println("Computer choose Paper");
        } else {
            System.out.println("Computer choose Scissor");
        }
        if (u == c) {
            System.out.println("It's a Draw ");
        } else if ((u == 1 && c == 3) || (u == 2 && c == 1) || (u == 3 && c == 2)) {
            System.out.println("You Won ");
        } else {
            System.out.println("Computer Won");
        }
    }
}
