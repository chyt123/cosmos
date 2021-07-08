import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        ans = []

        def helper(node):
            if not node:
                return None
            left = helper(node.left)
            right = helper(node.right)
            if node.val in to_delete:
                ans.append(left)
                ans.append(right)
                return None
            # if node.left and node.left in to_delete:
            node.left = left
            # if node.right and node.right in to_delete:
            node.right = right
            return node

        ans.append(helper(root))
        return [i for i in ans if i is not None]


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[1, 2, 3, 4, 5, 6, 7], [3, 5]],
        [[1, 2, 4, None, 3], [3]],
    ]
    for i, j in test_cases:
        result = (sol.delNodes(lc_list2tree(i), j))
        print(result)
