import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode, lc_tree2list


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        summ = 0

        def inverted_inorder(node):
            nonlocal summ
            if node:
                inverted_inorder(node.right)
                node.val += summ
                summ = node.val
                inverted_inorder(node.left)
            return node

        inverted_inorder(root)
        return root

        # def inverted_inorder(node, pre):
        #     if not node:
        #         return 0
        #     if node.right:
        #         pre = inverted_inorder(node.right, pre)
        #     node.val += pre
        #     left = 0
        #     if node.left:
        #         left = inverted_inorder(node.left, node.val)
        #     return left if left else node.val
        #
        # inverted_inorder(root, 0)
        # return root


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8],
        [3, 2, 4, 1],
    ]
    for i in test_cases:
        result = sol.convertBST(lc_list2tree(i))
        print(lc_tree2list(result))

