import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode, lc_tree2list


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 and not root2:
            return None
        new_tree = TreeNode(0)
        n1 = root1 if root1 else TreeNode(0)
        n2 = root2 if root2 else TreeNode(0)
        new_tree.val = n1.val + n2.val
        new_tree.left = self.mergeTrees(n1.left, n2.left)
        new_tree.right = self.mergeTrees(n1.right, n2.right)
        return new_tree


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[1,3,2,5], [2,1,3,None,4,None,7]],
        [[1], [1,2]],
    ]
    for i, j in test_cases:
        result = sol.mergeTrees(lc_list2tree(i), lc_list2tree(j))
        print(lc_tree2list(result))

