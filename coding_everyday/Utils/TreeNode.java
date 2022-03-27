import java.util.ArrayList;
import java.util.List;

public class TreeNode {
     int val;
     TreeNode left;
     TreeNode right;
     TreeNode() {}
     TreeNode(int val) { this.val = val; }
     TreeNode(int val, TreeNode left, TreeNode right) {
         this.val = val;
         this.left = left;
         this.right = right;
     }
     public static TreeNode buildTreeFromList(List<Integer> inputList) {
         if (inputList.isEmpty()) {
             return null;
         }
         if (inputList.size() == 1) {
             return new TreeNode(inputList.get(0));
         }

         ArrayList<TreeNode> treeNodes = new ArrayList<>();
         for (Integer i : inputList) {
             if (i != null) {
                 treeNodes.add(new TreeNode(i));
             } else {
                 treeNodes.add(null);
             }
         }

         int slow = 0;
         int fast = 1;
         TreeNode currentTreeNode;
         TreeNode leftTreeNode;
         TreeNode rightTreeNode;
         do {
             currentTreeNode = treeNodes.get(slow);
             if (currentTreeNode != null) {
                 leftTreeNode = treeNodes.get(fast);
                 if (leftTreeNode != null) {
                     currentTreeNode.left = leftTreeNode;
                 }
                 fast++;

                 if (fast == treeNodes.size()) break;

                 rightTreeNode = treeNodes.get(fast);
                 if (rightTreeNode != null) {
                     currentTreeNode.right = rightTreeNode;
                 }
                 fast++;
             }
             slow ++;
         } while (fast < treeNodes.size());
         return treeNodes.get(0);
     }

}