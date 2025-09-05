public class InvertedPattern {
    // Method 1: Using nested for loops
    public static void pattern1() {
        int rows = 5;
        for (int i = rows; i > 0; i--) {
            for (int j = i; j > 0; j--) {
                System.out.print(j + " ");
            }
            System.out.println(); // New line after each row
        }
    }

    // Method 2: Using StringBuilder for efficient string concatenation
    public static void pattern2() {
        int rows = 5;
        for (int i = rows; i > 0; i--) {
            StringBuilder line = new StringBuilder();
            for (int j = i; j > 0; j--) {
                line.append(j).append(" ");
            }
            System.out.println(line);
        }
    }

    public static void main(String[] args) {
        System.out.println("Pattern using Method 1:");
        pattern1();
        
        System.out.println("\nPattern using Method 2:");
        pattern2();
    }
}
