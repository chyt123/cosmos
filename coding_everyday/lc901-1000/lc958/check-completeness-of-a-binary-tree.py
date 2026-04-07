# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])

        leaf = False
        while len(q):
            p = []
            for i in q:
                p.append(i.val)
            # print(p)
            cur = q.popleft()
            if cur.right and not cur.left: # only r
                # print("only r")
                return False
            if leaf and (cur.left or cur.right): #leaf violation
                # print("leaf vio")
                return False
            if not (cur.right and cur.left): # only l or no child
                leaf = True
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return True
