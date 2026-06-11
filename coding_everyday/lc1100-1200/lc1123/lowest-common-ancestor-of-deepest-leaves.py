# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = None
        maxd = 0

        def post_trav(node, depth):
            nonlocal ans
            nonlocal maxd

            ld, rd = 0, 0
            if node.left:
                ld = post_trav(node.left, depth + 1)
            if node.right:
                rd = post_trav(node.right, depth + 1)
            
            d = 0
            if not node.left and not node.right:
                d = depth
                if d >= maxd:
                    maxd = d
                    ans = node
            elif ld == rd:
                d = ld
                if d >= maxd:
                    maxd = d
                    ans = node
            else:
                d = max(ld, rd)
                     
            return d     

        post_trav(root, 0)
        return ans
