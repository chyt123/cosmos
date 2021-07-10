import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode, lc_tree2list


class Solution:
    def same_tree(self, node, subnode):
        if not node and not subnode:
            return True
        if not node or not subnode:
            return False
        if subnode.val == node.val:
            return self.same_tree(node.left, subnode.left) and self.same_tree(node.right, subnode.right)
        return False

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return False
        if self.same_tree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[3, 4, 5, 1, 2], [4, 1, 2]],
        [[3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2]],
        [[1, None, 1, None, 1, None, 1, 2],
        [1, None, 1, 2]],
    ]
    for i, j in test_cases:
        result = sol.isSubtree(lc_list2tree(i), lc_list2tree(j))
        print(result)

