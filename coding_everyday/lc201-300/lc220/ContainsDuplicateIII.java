import java.util.TreeSet;

public class ContainsDuplicateIII {
    public static boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        TreeSet<Long> values = new TreeSet<>();
        for (int i = 0; i < nums.length; i++) {
            Long floor = values.floor((long) nums[i] + t);
            Long ceiling = values.ceiling((long) nums[i] - t);
            if (floor != null && floor >= nums[i] || ceiling != null && ceiling <= nums[i]) {
                return true;
            }

            values.add((long) nums[i]);
            if (i >= k) {
                values.remove((long) nums[i - k]);
            }
        }
        return false;
    }


    public static void main(String[] args) {
        int[] nums;
        int k;
        int t;

        nums = new int[]{1,2,3,1};
        k = 3;
        t = 0;
        System.out.println(containsNearbyAlmostDuplicate(nums, k, t));

        nums = new int[]{1,0,1,1};
        k = 1;
        t = 2;
        System.out.println(containsNearbyAlmostDuplicate(nums, k, t));

        nums = new int[]{9, 5, 1, 9, 5, 1};
        k = 2;
        t = 3;
        System.out.println(containsNearbyAlmostDuplicate(nums, k, t));

        nums = new int[]{-2147483648,2147483647};
        k = 1;
        t = 1;
        System.out.println(containsNearbyAlmostDuplicate(nums, k, t));

        nums = new int[]{2147483646,2147483647};
        k = 3;
        t = 3;
        System.out.println(containsNearbyAlmostDuplicate(nums, k, t));

        nums = new int[]{-2147483648,-2147483647};
        k = 3;
        t = 3;
        System.out.println(containsNearbyAlmostDuplicate(nums, k, t));
    }
}
