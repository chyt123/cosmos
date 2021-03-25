from typing import List
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        self.back(root)
        if root.val == 0 and root.left is None and root.right is None:
            return None
        return root

    def back(self, node: TreeNode):
        if node.left:
            node.left = self.back(node.left)
        if node.right:
            node.right = self.back(node.right)
        if node.val == 0 and node.left is None and node.right is None:
            return None
        return node

    def front(self, node: TreeNode):
        print(node.val)
        if node.left:
            self.front(node.left)
        if node.right:
            self.front(node.right)

    def middle(self, node: TreeNode):
        if node.left:
            self.middle(node.left)
        print(node.val)
        if node.right:
            self.middle(node.right)


if __name__ == "__main__":
    sol = Solution()
    tr001 = TreeNode(0, TreeNode(0), TreeNode(1))
    root = TreeNode(1, None, tr001)

    tr000 = TreeNode(0, TreeNode(0), TreeNode(0))
    tr101 = TreeNode(1, TreeNode(0), TreeNode(1))
    root = TreeNode(1, tr000, tr101)

    root = TreeNode(0, None, tr000)
    print(sol.pruneTree(root))
