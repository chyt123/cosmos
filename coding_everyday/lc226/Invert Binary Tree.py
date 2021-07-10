import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode, lc_tree2list


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                cur.left, cur.right = cur.right, cur.left
                stack += cur.left, cur.right
        return root
        # if not root:
        #     return None
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [4, 2, 7, 1, 3, 6, 9],
        [2, 1, 3]
    ]
    for i in test_cases:
        result = sol.invertTree(lc_list2tree(i))
        print(lc_tree2list(result))

