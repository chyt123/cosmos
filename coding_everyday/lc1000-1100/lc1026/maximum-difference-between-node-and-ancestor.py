# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def post_trav(node):
            if not node:
                return (float('inf'), -1)
            min_left, max_left = post_trav(node.left)
            min_right, max_right = post_trav(node.right)

            if node.left:
                self.ans = max(self.ans, abs(node.val - min_left), abs(node.val - max_left))
            if node.right:
                self.ans = max(self.ans, abs(node.val - min_right), abs(node.val - max_right))

            return (min(node.val, min_left, min_right), max(node.val, max_left, max_right))

        min_val, max_val = post_trav(root)
        # print(min_val, max_val)
        return self.ans