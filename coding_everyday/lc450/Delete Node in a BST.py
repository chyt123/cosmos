import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode, lc_tree2list, lc_list2singlelinkedlist, ListNode


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            new_root = root.left
            while new_root.right:
                new_root = new_root.right
            root.val, new_root.val = new_root.val, root.val
            root.left = self.deleteNode(root.left, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[5, 3, 6, 2, 4, None, 7], 3],
        [[5, 3, 6, 2, 4, None, 7], 0],
        [[5, 3, 6, 2, 4, None, 7], 7],
        [[5, 3, 6, 2, 4, None, 7], 5],
    ]
    for i, j in test_cases:
        result = sol.deleteNode(lc_list2tree(i), j)
        print(lc_tree2list(result))


