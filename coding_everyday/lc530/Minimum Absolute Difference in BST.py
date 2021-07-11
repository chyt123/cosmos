import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode, lc_tree2list


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        minn = math.inf
        pre = -math.inf

        def inorder(node):
            nonlocal pre, minn
            if node:
                inorder(node.left)
                minn = min(minn, node.val - pre)
                pre = node.val
                inorder(node.right)
                return node.val
            return None

        inorder(root)
        return minn


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [4, 2, 6, 1, 3],
        [1, 0, 48, None, None, 12, 49],
        [236, 104, 701, None, 227, None, 911]
    ]
    for i in test_cases:
        result = sol.getMinimumDifference(lc_list2tree(i))
        print(result)

