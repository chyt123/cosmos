import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class MajorityElementII {
    public static List<Integer> majorityElement(int[] nums) {
        HashMap<Integer, Integer> summary = new HashMap<>();
        int n = nums.length;
        ArrayList<Integer> rtn = new ArrayList<>();
        for (int num : nums) {
            if (summary.containsKey(num)) {
                summary.put(num, summary.get(num) + 1);
            } else {
                summary.put(num, 1);
            }
        }
        summary.forEach((k, v) -> {
            if (v > Math.floorDiv(n, 3)) {
                rtn.add(k);
            }
        });
        return rtn;
    }

    public static void main(String[] args) {
        int[] nums;

        nums = new int[]{3, 2, 3};
        System.out.println(majorityElement(nums));

        nums = new int[]{3, 2, 1};
        System.out.println(majorityElement(nums));

        nums = new int[]{};
        System.out.println(majorityElement(nums));

        nums = new int[]{1, 2};
        System.out.println(majorityElement(nums));
    }
}
