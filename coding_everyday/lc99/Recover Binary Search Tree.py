import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode, lc_tree2list


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = None
        m1 = m2 = None

        def inorder(node):
            nonlocal pre, m1, m2
            if node:
                inorder(node.left)
                if pre and node.val < pre.val:
                    if not m1:
                        m1 = pre
                        m2 = node
                    else:
                        m2 = node
                pre = node
                inorder(node.right)

        inorder(root)
        m1.val, m2.val = m2.val, m1.val
        return root


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [50, 17, 76, 54, 23, 9],
        [3, 1, 4, None, None, 2]
    ]
    for i in test_cases:
        result = (sol.recoverTree(lc_list2tree(i)))
        print(lc_tree2list(result))
