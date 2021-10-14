import math
from typing import List
from collections import deque, defaultdict, OrderedDict
from util import TreeNode, lc_list2tree


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.leaves = ''

        def find_leaves(node: TreeNode) -> None:
            if node:
                find_leaves(node.left)
                find_leaves(node.right)
                if not (node.left or node.right):
                    self.leaves += str(node.val) + ','

        find_leaves(root1)
        l1 = self.leaves
        self.leaves = ''
        find_leaves(root2)
        return l1 == self.leaves


if __name__ == "__main__":
    sol = Solution()
    root1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
    root2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
    root1 = [1]
    root2 = [1]
    root1 = [1]
    root2 = [2]
    root1 = [1, 2, 3]
    root2 = [1, 3, 2]
    root1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 14]
    root2 = [3, 5, 1, 6, 71, 4, 2, None, None, None, None, None, None, 9, 8]
    root1 = lc_list2tree(root1)
    root2 = lc_list2tree(root2)
    print(sol.leafSimilar(root1, root2))
