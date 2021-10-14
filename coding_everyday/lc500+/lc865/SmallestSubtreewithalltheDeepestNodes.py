from typing import List
from collections import deque, defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        lv = []
        e = []
        stack = deque([root, '@'])
        cnt = 0
        while stack:
            cur = stack.popleft()
            if cur == '@':
                lv.append(e)
                if not stack:
                    break
                stack.append('@')
                e = []
            else:
                cnt += 1
                e.append(cur.val)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
        deepest = lv[-1]
        n = len(deepest)
        self.ans = []

        def tran(node: TreeNode):
            l, m, r = 0, 0, 0
            if node.val in deepest:
                m = 1
            if node.left:
                l = tran(node.left)
            if node.right:
                r = tran(node.right)
            if l + m + r == n:
                self.ans.append(node)
            return l + m + r

        tran(root)
        return self.ans[0]


if __name__ == "__main__":
    sol = Solution()
    # root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
    tn = [TreeNode(0)] * 11
    for i in range(11):
        tn[i] = TreeNode(i)

    tn[3].left = tn[5]
    tn[3].right = tn[1]
    tn[5].left = tn[6]
    tn[5].right = tn[2]
    tn[1].left = tn[0]
    tn[1].right = tn[8]
    tn[2].left = tn[7]
    tn[2].right = tn[4]
    tn[6].left = tn[9]
    # tn[8].left = tn[9]
    # tn[8].right = tn[10]
    print(sol.subtreeWithAllDeepest(tn[3]))
