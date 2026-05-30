# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        summ = 0

        def inverted_inorder(node):
            nonlocal summ

            if not node:
                return
            inverted_inorder(node.right)
            summ += node.val
            node.val = summ
            inverted_inorder(node.left)

        inverted_inorder(root)
        return root
