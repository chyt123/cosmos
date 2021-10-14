import bisect
from copy import deepcopy
from typing import List, Optional
from collections import defaultdict
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes = []

        def inorder(node):
            left = right = True
            if node:
                left = inorder(node.left)
                if nodes and node.val <= nodes[-1]:
                    return False
                nodes.append(node.val)
                right = inorder(node.right)
            return left and right

        return inorder(root)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [2, 1, 3],
        [5, 1, 4, None, None, 3, 6],
        [2, 2, 2]
    ]
    for i in test_cases:
        result = sol.isValidBST(lc_list2tree(i))
        print(result)
