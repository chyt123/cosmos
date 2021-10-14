public class BalancedBinaryTree {
    public static void main(String[] args) {
        TreeNode[] tl = new TreeNode[10];
        for (int i = 0; i < 10; i++) {
            tl[i] = new TreeNode(i);
        }
        tl[2].left = tl[3];
        tl[2].right = tl[4];
        tl[0].left = tl[1];
        tl[0].right = tl[2];
//        tl[4].left = tl[6];
//        tl[4].right = tl[7];
//        tl[2].left = tl[4];
//        tl[2].right = tl[5];
//        tl[1].left = tl[2];
//        tl[1].right = tl[3];

        Solution sol = new Solution();
        System.out.println(sol.isBalanced(tl[9]));
    }
}

class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        return cal_root(root) != Integer.MAX_VALUE;
    }

    public int cal_root(TreeNode root) {
        int l = root.left == null ? 0 : cal_root(root.left);
        int r = root.right == null ? 0 : cal_root(root.right);
        if (l == Integer.MAX_VALUE || r == Integer.MAX_VALUE || Math.abs(l - r) > 1) {
            return Integer.MAX_VALUE;
        }
        return 1 + Math.max(l, r);
    }
}