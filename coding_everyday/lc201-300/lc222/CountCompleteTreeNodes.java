import java.util.ArrayList;
import java.util.List;

public class CountCompleteTreeNodes {
    public static int countNodes(TreeNode root) {
        if (root == null) return 0;
        if (root.left == null && root.right == null) return 1;
        String binary = checkTree(root, 0, "");
        return (int) Math.pow(2, binary.length())  + Integer.parseInt(binary, 2);
    }

    private static String checkTree(TreeNode root, int level, String binary) {
        if (root == null) return binary.substring(0, binary.length() - 1);

        int leftHeight = countHeight(root.left);
        int rightHeight = countHeight(root.right);
        if (leftHeight == rightHeight && leftHeight != 0) {
            return checkTree(root.right, level + 1, binary + "1");
        } else {
            return checkTree(root.left, level + 1, binary + "0");
        }
    }

    private static int countHeight(TreeNode root) {
        if (root == null) return 0;
        int leftHeight = 1;
        while (root.left != null) {
            leftHeight ++;
            root = root.left;
        }
        return leftHeight;
    }

    public static void main(String[] args) {
        ArrayList<Integer> root;

        root = new ArrayList<>(List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));
        System.out.println(countNodes(TreeNode.buildTreeFromList(root)));

        root = new ArrayList<>(List.of(1, 2, 3, 4, 5, 6));
        System.out.println(countNodes(TreeNode.buildTreeFromList(root)));

        root = new ArrayList<>();
        System.out.println(countNodes(TreeNode.buildTreeFromList(root)));

        root = new ArrayList<>(List.of(1));
        System.out.println(countNodes(TreeNode.buildTreeFromList(root)));

        root = new ArrayList<>(List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14, 15));
        System.out.println(countNodes(TreeNode.buildTreeFromList(root)));
    }
}
