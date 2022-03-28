import java.util.ArrayList;
import java.util.Arrays;

public class ProductofArrayExceptSelf {
    public static int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] rtn = new int[n];
        rtn[0] = 1;
        for (int i = 1; i < n; i++) {
            rtn[i] = rtn[i - 1] * nums[i - 1];
        }
        int right = 1;
        for (int i = n - 2; i >= 0 ; i--) {
            rtn[i] *= right * nums[i + 1];
            right *= nums[i + 1];
        }
        return rtn;
    }


    public static void main(String[] args) {
        int[] nums;

        nums = new int[]{1,2,3,4};
        System.out.println(Arrays.toString(productExceptSelf(nums)));

        nums = new int[]{-1, 1, 0, -3, 3};
        System.out.println(Arrays.toString(productExceptSelf(nums)));
   }
}
