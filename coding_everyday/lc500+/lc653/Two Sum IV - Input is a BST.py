import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode, lc_tree2list, lc_list2singlelinkedlist, ListNode


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        sorted_l = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_l.append(node.val)
            inorder(node.right)

        inorder(root)
        l, r = 0, len(sorted_l) - 1
        while l < r:
            if sorted_l[l] + sorted_l[r] == k:
                return True
            if sorted_l[l] + sorted_l[r] > k:
                r -= 1
            if sorted_l[l] + sorted_l[r] < k:
                l += 1
        return False


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[5, 3, 6, 2, 4, None, 7], 9],
        [[5, 3, 6, 2, 4, None, 7], 28],
        [[1], 2]
    ]
    for i, j in test_cases:
        result = sol.findTarget(lc_list2tree(i), j)
        print(result)


