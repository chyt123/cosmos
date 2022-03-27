import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class CombinationSumIII {
    public static List<List<Integer>> combinationSum3(int k, int n) {
        int[] digits = new int[9];
        for (int i = 0; i < 9; i++) {
            digits[i] = i + 1;
        }
        List<List<Integer>> rtn = new ArrayList<>();
        combinationSum(k, n, 0, digits, rtn, null);
        return rtn;
    }

    private static void combinationSum(int k, int n, int curPos, int[] digits, List<List<Integer>> rtn, LinkedList<Integer> internal) {
        if (k == 0 && n == 0) {
            LinkedList<Integer> add = new LinkedList<>(internal);
            rtn.add(add);
            return;
        }
        if (k == 0 || n < 0 || curPos == 9 || digits[curPos] > n) return;

        if (internal == null) {
            internal = new LinkedList<>();
        }

        internal.add(digits[curPos]);
        combinationSum(k - 1, n - digits[curPos], curPos + 1, digits, rtn, internal);

        internal.removeLast();
        combinationSum(k, n, curPos + 1, digits, rtn, internal);
    }


    public static void main(String[] args) {
        int k;
        int n;

        k = 3;
        n = 7;
        System.out.println(combinationSum3(k, n));

        k = 3;
        n = 9;
        System.out.println(combinationSum3(k, n));

        k = 4;
        n = 1;
        System.out.println(combinationSum3(k, n));
    }
}

