# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def trav(node1, node2):
            if not node1 and not node2:
                return True
            if node1 and not node2 or node2 and not node1 or node1.val != node2.val:
                return False
            l = node1.left.val if node1.left else None
            r = node2.right.val if node2.right else None
            if l == r:
                node2.left, node2.right = node2.right, node2.left
            return trav(node1.left, node2.left) and trav(node1.right, node2.right)

        return trav(root1, root2)