import java.util.ArrayList;
import java.util.List;

public class SpiralMatrix {
    public static void main(String[] args) {
//        int[][] matrix = {{1,2,3},{4,5,6},{7,8,9}};
//        int[][] matrix = {{1,2,3,4},{5,6,7,8},{9,10,11,12}};
//        int[][] matrix = {{1},{5},{9}};
        int[][] matrix = {{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}};
        Solution sol = new Solution();
        System.out.println(sol.spiralOrder(matrix));
    }
}
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ans = new ArrayList<>();
        int h = matrix.length;
        int w = matrix[0].length;
        int n = (h + 1) / 2;
        for (int frame = 0; frame < n; frame++) {
            for (int i = frame; i < w - frame; i++) {
                ans.add(matrix[frame][i]);
            }
            for (int i = frame + 1; i < h - frame; i++) {
                ans.add(matrix[i][w - frame - 1]);
            }
            if (h - frame - 1 != frame) {
                for (int i = w - frame - 2; i >= frame; i--) {
                    ans.add(matrix[h - frame - 1][i]);
                }
            }
            if (frame != w - frame - 1) {
                for (int i = h - frame - 2; i > frame; i--) {
                    ans.add(matrix[i][frame]);
                }
            }
            if (ans.size() == h * w) {
                return ans;
            }
        }
        return ans;
    }
}
