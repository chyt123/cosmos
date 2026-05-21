# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def construct(pre):
            if not pre:
                return None
            node = TreeNode(pre[0])
            idx = len(pre)
            for i in range(1, len(pre)):
                if pre[i] > pre[0]:
                    idx = i
                    break
            node.left = construct(pre[1:idx])
            node.right = construct(pre[idx:])
            return node

        return construct(preorder)
# Test cases
# 0 Node, 1 Node,
# [8,5,1,7,10,12]


