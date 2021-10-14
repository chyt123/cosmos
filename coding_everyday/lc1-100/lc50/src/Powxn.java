public class Powxn {
    public static void main(String[] args) {
        double x = 2;
        int n = 10;
        Solution sol = new Solution();
        System.out.println(sol.myPow(x, n));
    }
}

class Solution {
    public double myPow(double x, int n) {
        if (n == 0) {return 1;}
        if (x == 1) {return 1;}
        if (x == -1) {return n % 2 == 0 ? 1 : -1;}
        if (n == Integer.MIN_VALUE) {return 0;}
        if (n < 0) {
            x = 1 / x;
            n = -n;
        }
        return n % 2 == 0 ? myPow(x * x, n / 2) : x * myPow(x * x, n / 2);
    }
}