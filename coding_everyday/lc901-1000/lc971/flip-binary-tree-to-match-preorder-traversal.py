# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        n = len(voyage)
        ans = []
        self.i = 0
        def dfs(node):
            if not node:
                return
            if node.val != voyage[self.i]:
                ans.append(-1)
                return
            self.i += 1
            if self.i < n and node.left and node.left.val != voyage[self.i]:
                ans.append(node.val)
                dfs(node.right)
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        if ans and -1 in ans:
            return [-1]
        return ans