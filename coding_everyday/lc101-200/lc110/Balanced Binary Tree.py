import collections
import math
from typing import List
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lc_tree2list(tree: TreeNode) -> List:
    q = deque()
    q.append(tree)
    ans = []
    while q:
        cur = q.popleft()
        if cur:
            ans.append(cur.val)
            q.extend([cur.left, cur.right])
    return ans


def lc_list2tree(a: List) -> TreeNode:
    if not a:
        return None
    wait_list = []
    l = 0
    while a:
        lim = 2 ** l
        if lim == 1:
            cur = a.pop(0)
            ret = TreeNode(cur)
            wait_list.append(ret)
            l += 1
            continue
        for i in range(lim // 2):
            if not a:
                break
            left = a.pop(0)
            right = None
            if a:
                right = a.pop(0)

            if wait_list:
                cur_p = wait_list.pop(0)
                cur_p.left = TreeNode(left) if left else None
                cur_p.right = TreeNode(right) if right else None
                wait_list.append(cur_p.left)
                wait_list.append(cur_p.right)
        l += 1
    return ret


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            left = helper(node.left)
            right = helper(node.right)
            if abs(left - right) > 1:
                return math.inf
            return max(left, right) + 1
        return helper(root) != math.inf


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [3, 9, 20, None, None, 15, 7],
        [1, 2, 2, 3, 3, None, None, 4, 4],
        [1, None, 2],
        [],
        [1],
    ]
    for i in test_cases:
        print(sol.isBalanced(lc_list2tree(i)))
