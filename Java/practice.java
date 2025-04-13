import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class practice {
    private static final Map<String, User> users = new HashMap<>();
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        while (true) {
            System.out.println("\n🔐 User Authentication System:");
            System.out.println("1️⃣ Register");
            System.out.println("2️⃣ Login");
            System.out.println("3️⃣ Exit");
            System.out.print("👉 Choose an option: ");

            if (!scanner.hasNextInt()) {
                System.out.println("❌ Invalid input! Please enter a number.");
                scanner.next();
                continue;
            }

            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1 -> registerUser();
                case 2 -> loginUser();
                case 3 -> {
                    System.out.println("👋 Exiting... Stay secure!");
                    return;
                }
                default -> System.out.println("❌ Invalid choice! Please try again.");
            }
        }
    }

    // ✅ Secure User Registration
    private static void registerUser() {
        System.out.print("🆕 Enter Username: ");
        String username = scanner.nextLine().trim();

        System.out.print("📧 Enter Email: ");
        String email = scanner.nextLine().trim();

        if (!isValidEmail(email)) {
            System.out.println("❌ Invalid email format! Try again.");
            return;
        }

        System.out.print("🔒 Enter Password (min 6 characters): ");
        String password = scanner.nextLine().trim();

        if (password.length() < 6) {
            System.out.println("❌ Password too short! Must be at least 6 characters.");
            return;
        }

        if (users.containsKey(username)) {
            System.out.println("⚠ Username already exists! Try a different one.");
        } else {
            String hashedPassword = hashPassword(password);
            users.put(username, new User(username, email, hashedPassword));
            System.out.println("✅ Registration successful! Now you can log in.");
        }
    }

    // ✅ Secure User Login
    private static void loginUser() {
        System.out.print("👤 Enter Username: ");
        String username = scanner.nextLine().trim();

        System.out.print("🔑 Enter Password: ");
        String password = scanner.nextLine().trim();

        User user = users.get(username);
        if (user != null && user.getPassword().equals(hashPassword(password))) {
            System.out.println("✅ Login successful! Welcome back, " + user.getUsername() + "!");
        } else {
            System.out.println("❌ Invalid username or password. Try again.");
        }
    }

    // ✅ Hash Password using SHA-256
    private static String hashPassword(String password) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hash = md.digest(password.getBytes());
            StringBuilder hexString = new StringBuilder();
            for (byte b : hash) {
                hexString.append(String.format("%02x", b));
            }
            return hexString.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("Error hashing password", e);
        }
    }

    // ✅ Email Validation Method
    private static boolean isValidEmail(String email) {
        return email.matches("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$");
    }

    // ✅ User Class with Secure Password Storage
    static class User {
        private final String username;
        private final String email;
        private final String password;

        public User(String username, String email, String password) {
            this.username = username;
            this.email = email;
            this.password = password;
        }

        public String getUsername() {
            return username;
        }

        public String getEmail() {
            return email;
        }

        public String getPassword() {
            return password; // Storing hashed password
        }
    }
}