import collections
from typing import List, Optional
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        def po(node):
            if not node or not node.left and not node.right:
                return node
            right = tmp = po(node.left)
            if right:
                while tmp.right:
                    tmp = tmp.right
                tmp.right = po(node.right)
                node.left = None
                node.right = right
            else:
                po(node.right)
            return node

        po(root)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 5, 3, 4, None, 6],
        [],
        [0]
    ]
    for i in test_cases:
        sol.flatten(lc_list2tree(i))

