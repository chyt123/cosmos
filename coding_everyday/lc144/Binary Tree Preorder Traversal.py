import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode, lc_tree2list


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                ans.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)
        return ans

        # def helper(node):
        #     if node:
        #         ans.append(node.val)
        #         helper(node.left)
        #         helper(node.right)
        #
        # helper(root)
        # return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, None, 2, 3],
        [3, 9, 20, None, 15, 7],
    ]
    for i in test_cases:
        print(sol.preorderTraversal(lc_list2tree(i)))
