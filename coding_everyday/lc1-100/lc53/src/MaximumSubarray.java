public class MaximumSubarray {
    public static void main(String[] args) {
//        int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
//        int[] nums = {1};
//        int[] nums = {5,4,-1,7,8};
        int[] nums = {1, 2};
        Solution sol = new Solution();
        System.out.println(sol.maxSubArray(nums));
    }
}

class Solution {
    public int maxSubArray(int[] nums) {
        int sum = nums[0];
        int max = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i] + sum) {
                sum = nums[i];
            } else {
                sum += nums[i];
            }
            max = Math.max(sum, max);
        }
        return max;
    }
}