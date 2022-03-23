import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class BinaryTreeRightSideView {
    public static List<Integer> rightSideView(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        List<Integer> rtnList = new ArrayList<>();
        LinkedList<TreeNode> treeNodes = new LinkedList<>();
        TreeNode currentTreeNode;
        treeNodes.add(root);
        int level = 1;
        int cnt = 0;
        int right;
        while (!treeNodes.isEmpty()) {
            currentTreeNode = treeNodes.removeFirst();

            right = currentTreeNode.val;
            if (currentTreeNode.left != null) {
                treeNodes.add(currentTreeNode.left);
            }
            cnt += 1;
            if (currentTreeNode.right != null) {
                treeNodes.add(currentTreeNode.right);
            }
            cnt += 1;

            if (cnt == Math.pow(2, level)) {
                cnt = ((int) Math.pow(2, level) - treeNodes.size()) * 2;
                level += 1;
                rtnList.add(right);
            }
        }
        return rtnList;
    }

    public static int countNodes(TreeNode root){
        if (root == null) {
            return 0;
        }
        return 1 + countNodes(root.left) + countNodes(root.right);
    }

    public static void main(String[] args) {
        ArrayList<Integer> arrayList;
        TreeNode treeNode;

        arrayList = new ArrayList<>(
            Arrays.asList(1,2,3,null,5,null,4)
        );
        treeNode = TreeNode.buildTreeFromList(arrayList);
        System.out.println(rightSideView(treeNode));

        arrayList = new ArrayList<>(
            Arrays.asList(1,null,3)
        );
        treeNode = TreeNode.buildTreeFromList(arrayList);
        System.out.println(rightSideView(treeNode));

        arrayList = new ArrayList<>();
        treeNode = TreeNode.buildTreeFromList(arrayList);
        System.out.println(rightSideView(treeNode));

        arrayList = new ArrayList<>(
            Arrays.asList(1,2)
        );
        treeNode = TreeNode.buildTreeFromList(arrayList);
        System.out.println(rightSideView(treeNode));
        arrayList = new ArrayList<>(
            Arrays.asList(6,1,null,null,3,2,5,null,null,4)
        );
        treeNode = TreeNode.buildTreeFromList(arrayList);
        System.out.println(rightSideView(treeNode));
    }
}

