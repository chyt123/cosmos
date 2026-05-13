# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = 'z' * 8000
        self.cur = ''

        def dfs(node):
            self.cur += chr(node.val + ord('a'))
            if not node.left and not node.right:
                # print(self.cur) 
                self.ans = min(self.ans, self.cur[::-1])
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            self.cur = self.cur[:-1]

        dfs(root)
        return self.ans