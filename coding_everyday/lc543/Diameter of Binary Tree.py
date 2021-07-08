import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        rtn = 0
        if not root or (not root.left and not root.right):
            return 0

        def helper(node):
            nonlocal rtn
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            left = helper(node.left)
            right = helper(node.right)
            rtn = max(rtn, left + right)
            return max(left, right) + 1

        helper(root)
        return rtn


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [3, 9, 20, None, None, 15, 7],
        [1, None, 2],
        [1, 2, None, 3, None],
        [1],
        [2, 1, 4, 3, None, 5],
    ]
    for i in test_cases:
        print(sol.diameterOfBinaryTree(lc_list2tree(i)))
