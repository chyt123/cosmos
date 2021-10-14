import java.util.*;

public class MergeIntervals {
    public static void main(String[] args) {
//        int[][] intervals = {{1,3},{2,6},{8,10},{15,18}};
        int[][] intervals = {{1,4},{4,5}};
        Solution sol = new Solution();
        System.out.println(Arrays.deepToString(sol.merge(intervals)));
    }
}

class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                Integer i1 = o1[0];
                Integer i2 = o2[0];
                return i1.compareTo(i2);
            }
        });
        List<int[]> rst = new ArrayList<>();
        int[] cur_int = intervals[0];
        for (int[] inter:intervals) {
            if (cur_int[0] <= inter[0] && inter[0] <= cur_int[1]){
                cur_int[1] = Math.max(cur_int[1], inter[1]);
            } else {
                rst.add(cur_int);
                cur_int = inter;
            }
        }
        rst.add(cur_int);
        return rst.toArray(new int[rst.size()][]);
    }
}
