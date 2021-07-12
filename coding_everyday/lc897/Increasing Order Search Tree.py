import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode, lc_tree2list, lc_list2singlelinkedlist, ListNode


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        rtn = cur = TreeNode()

        def inorder(node):
            nonlocal cur
            if node:
                inorder(node.left)
                cur.right = TreeNode(node.val)
                cur = cur.right
                inorder(node.right)

        inorder(root)
        return rtn.right


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9],
        [5, 1, 7],
    ]
    for i in test_cases:
        result = sol.increasingBST(lc_list2tree(i))
        print(lc_tree2list(result))


