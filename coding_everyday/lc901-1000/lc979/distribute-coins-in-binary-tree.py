# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        def post_trav(node):
            val_left = post_trav(node.left) if node.left else 1
            val_right = post_trav(node.right) if node.right else 1
            self.moves += abs(val_left - 1) + abs(val_right - 1)
            return node.val + val_left - 1 + val_right - 1

        post_trav(root)
        return self.moves
