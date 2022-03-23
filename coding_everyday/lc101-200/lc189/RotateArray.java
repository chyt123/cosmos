import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class RotateArray {
    public static void rotate(int[] nums, int k) {
        k = k % nums.length;
        int[] tmp = new int[k];
        System.arraycopy(
            nums, nums.length - k,
            tmp, 0,
            k
        );

        System.arraycopy(
            nums, 0,
            nums, k,
            nums.length - k
        );

        System.arraycopy(
            tmp, 0,
            nums, 0,
            k
        );
    }

    public static void main(String[] args) {
//        int[] nums = new int[]{1,2,3,4,5,6,7};
//        int k = 13;
        int[] nums = new int[]{-1,-100,3,99};
        int k = 2;
        rotate(nums, k);
        System.out.println(Arrays.toString(nums));
    }
}

