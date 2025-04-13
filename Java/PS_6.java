public class PS_6 {
    public static void main(String[] args) {

        // Problem 1
        // float[] num = { 10.6f, 20.f, 30, 40, 50 };
        // float sum = 0;
        // for (int i = 0; i < num.length; i++) {
        // sum = sum + num[i];
        // // System.out.println(num[0] + num[1] + num[2] + num[3] + num[4]);
        // }
        // System.out.println(sum);

        // Problem 2
        // int[] num = { 2, 5, 3, 8, 7 };
        // int a = 50;
        // boolean isIn = false;
        // for (int element : num) {
        // if (a == element) {
        // isIn = true;
        // break;
        // }
        // }
        // if (isIn) {
        // System.out.println("Present");
        // } else {
        // System.out.println("Not Present");
        // }

        // Problem 3
        // int[] num = { 2, 5, 3, 8, 7 };
        // int sum = 0;
        // for (int element : num) {
        // sum = sum + element;
        // }
        // System.out.println(sum / num.length);

        // Problem 4
        int[][] m1 = { { 1, 2, 3 },
                { 4, 5, 6 } };
        int[][] m2 = { { 1, 1, 1 },
                { 1, 1, 1 } };
        int[][] result = new int[m1.length][m1[0].length];

        for (int i = 0; i < m1.length; i++) {
            for (int j = 0; j < m1[i].length; j++) {
                result[i][j] = m1[i][j] + m2[i][j];
                System.out.print(result[i][j] + " "); // Print updated values
            }
            System.out.println(); // Move to the next line after each row
        }

        // Problem 5
        int[] marks = { 98, 76, 89, 65, 87 };
        for (int i = marks.length - 1; i >= 0; i--) {
            System.out.println(marks[i]);
        }
    }
}
