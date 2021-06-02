import java.util.Arrays;

public class JumpGame {
    public static void main(String[] args) {
//        int[] nums = {3, 2, 1, 0, 4};
//        int[] nums = {2,3,1,1,4};
        int[] nums = {2,0, 0};
        Solution sol = new Solution();
        System.out.println(sol.canJump(nums));
    }
}

class Solution {
    public boolean canJump(int[] nums) {
        int reach = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > reach) { return false;}
            reach = Math.max(reach, nums[i] + i);
        }
        return true;
    }
}
