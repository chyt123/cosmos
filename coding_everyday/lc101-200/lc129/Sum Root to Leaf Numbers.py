import bisect
import math
from typing import List, Optional
from collections import defaultdict
from util import TreeNode, lc_tree2list, lc_list2tree


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def po(node, cur):
            nonlocal ans
            cur += str(node.val)
            if not node.left and not node.right:
                ans += int(cur)
                return
            if node.left:
                po(node.left, cur)
            if node.right:
                po(node.right, cur)
        po(root, '')
        return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 3],
        [4, 9, 0, 5, 1],
    ]
    for i in test_cases:
        print(sol.sumNumbers(lc_list2tree(i)))
