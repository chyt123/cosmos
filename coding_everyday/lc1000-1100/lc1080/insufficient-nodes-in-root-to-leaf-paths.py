# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def pre_trav(node: TreeNode, pre_sum: int) -> None:
            node.val = (node.val, node.val + pre_sum)
            if node.left:
                pre_trav(node.left, node.val[1])
            if node.right:
                pre_trav(node.right, node.val[1])

        def post_trav(node: TreeNode) -> int:
            if not node:
                return float('-inf')
            if not node.left and not node.right: # leaf
                v = node.val[1]
                node.val = node.val[0]
                return v
            vl = post_trav(node.left)
            if vl < limit:
                node.left = None
            vr = post_trav(node.right)
            if vr < limit:
                node.right = None
            v = max(vl, vr)
            node.val = node.val[0]
            return v

        pre_trav(root, 0)
        v = post_trav(root)

        print(v)
        return None if v < limit else root
