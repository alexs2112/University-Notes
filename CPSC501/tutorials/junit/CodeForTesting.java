import java.util.*;
public class CodeForTesting {

    public static int fibonacci(int n) {
        if (n <= 0) {
            throw new IllegalArgumentException("Input must be a positive integer.");
        }
        if (n == 1 || n==2) {
            return 1;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 3; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static List<String> reverseStrings(List<String> strings) {
        if (strings == null) {
            throw new IllegalArgumentException("Input list of strings cannot be null.");
        }

        List<String> reversedStrings = new ArrayList<>();

        for (String str : strings) {
            if (str == null) {
                throw new IllegalArgumentException("Input string cannot be null.");
            }

            StringBuilder reversed = new StringBuilder();
            for (int i = str.length() - 1; i >= 0; i--) {
                reversed.append(str.charAt(i));
            }
            reversedStrings.add(reversed.toString());
        }

        return reversedStrings;
    }

    public static double calculateCircleArea(double radius) {
        if (radius < 0) {
            throw new IllegalArgumentException("Radius cannot be negative.");
        }
        return Math.PI * radius * radius;
    }
}
