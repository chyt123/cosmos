import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode, lc_tree2list


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1+idx], inorder[0:idx])
        root.right = self.buildTree(preorder[1+idx:], inorder[idx+1:])
        return root


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]],
    ]
    for i, j in test_cases:
        result = sol.buildTree(i, j)
        print(lc_tree2list(result))
