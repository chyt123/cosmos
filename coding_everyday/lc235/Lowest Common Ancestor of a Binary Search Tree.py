import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode, lc_tree2list


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        if p.val <= root.val <= q.val:
            return root
        if q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], [2], [8]],
        [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], [2], [4]],
    ]
    for i, p, q in test_cases:
        result = sol.lowestCommonAncestor(lc_list2tree(i), lc_list2tree(p), lc_list2tree(q))
        print(lc_tree2list(result))

