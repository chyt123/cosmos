
public class MinimumSizeSubarraySum {
    public static int minSubArrayLen(int target, int[] nums) {
        int left = 0;
        int right = 0;
        int rtn = Integer.MAX_VALUE;
        int currentSum = nums[0];
        while (true) {
            if (currentSum < target) {
                right ++;
                if (right == nums.length) break;
                currentSum += nums[right];
            } else if (currentSum == target) {
                rtn = Math.min(rtn, right - left + 1);
                left ++;
                right ++;
                if (right == nums.length) break;
                currentSum = currentSum - nums[left - 1] + nums[right];
            } else {
                rtn = Math.min(rtn, right - left + 1);
                left ++;
                if (left == nums.length) break;
                currentSum -= nums[left - 1];
            }
        }
        return rtn == Integer.MAX_VALUE ? 0 : rtn;
    }

    public static void main(String[] args) {
        int target;
        int[] nums;

//        target = 7;
//        nums = new int[]{2,3,1,2,4,3};
//        System.out.println(minSubArrayLen(target, nums));
//
//        target = 4;
//        nums = new int[]{1, 4, 4};
//        System.out.println(minSubArrayLen(target, nums));
//
//        target = 11;
//        nums = new int[]{1,1,1,1,1,1,1,1};
//        System.out.println(minSubArrayLen(target, nums));
//
//        target = 15;
//        nums = new int[]{1,1,1,1,10, 1,1,1,1,1, 7, 8};
//        System.out.println(minSubArrayLen(target, nums));

        target = 15;
        nums = new int[]{1, 2, 3, 4, 5};
        System.out.println(minSubArrayLen(target, nums));
    }
}

