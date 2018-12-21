# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pre_order(self, root, num_list):
        if root.left:
            self.pre_order(root.left, num_list)
        num_list.append(root.val)
        if root.right:
            self.pre_order(root.right, num_list)

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        num_list = []
        self.pre_order(root, num_list)
        m = float('Inf')
        for i in range(len(num_list) - 1):
            m = min(m, num_list[i + 1] - num_list[i])

        return m


if __name__ == "__main__":
    sol = Solution()
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    tree.right = TreeNode(6)

    print sol.minDiffInBST(tree)

