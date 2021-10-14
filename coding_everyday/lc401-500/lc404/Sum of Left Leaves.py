import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode, lc_tree2list


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = 0

        def preorder(node, left):
            nonlocal ans
            if node:
                if not node.left and not node.right and left:
                    ans += node.val
                preorder(node.left, True)
                preorder(node.right, False)
        preorder(root, False)
        return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [3, 9, 20, None, None, 15, 7],
    ]
    for i in test_cases:
        result = sol.sumOfLeftLeaves(lc_list2tree(i))
        print(result)

