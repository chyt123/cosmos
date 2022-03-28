import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class KthSmallestElementInABST {
    public static int kthSmallest(TreeNode root, int k) {
        ArrayList<Integer> treeNodes = new ArrayList<>();
        inOrderTraversal(root, treeNodes);
        return treeNodes.get(k - 1);
    }

    private static void inOrderTraversal(TreeNode node, ArrayList<Integer> treeNodes) {
        if (node == null) {
            return;
        }
        inOrderTraversal(node.left, treeNodes);
        treeNodes.add(node.val);
        inOrderTraversal(node.right, treeNodes);
    }


    public static void main(String[] args) {
        ArrayList<Integer> arrayList;
        int k;

        arrayList = new ArrayList<>(Arrays.asList(3,1,4,null,2));
        k = 1;
        System.out.println(kthSmallest(TreeNode.buildTreeFromList(arrayList), k));

        arrayList = new ArrayList<>(Arrays.asList(5,3,6,2,4,null,null,1));
        k = 3;
        System.out.println(kthSmallest(TreeNode.buildTreeFromList(arrayList), k));
   }
}
