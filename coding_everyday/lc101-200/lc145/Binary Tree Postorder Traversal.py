import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode, lc_tree2list


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                ans.append(cur.val)
                stack.append(cur.left)
                stack.append(cur.right)
        return ans[::-1]


        # def postorder(node):
        #     if node:
        #         postorder(node.left)
        #         postorder(node.right)
        #         ans.append(node.val)
        #
        # postorder(root)
        # return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 3, 4, 5, 6, 7],
        [1, None, 2, 3],
        [1, 2, 3, None, 4, None, 5]
    ]
    for i in test_cases:
        result = sol.postorderTraversal(lc_list2tree(i))
        print(result)

