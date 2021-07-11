import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode, lc_tree2list


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        rtn = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        rtn.left = self.buildTree(inorder[:idx], postorder[:idx])
        rtn.right = self.buildTree(inorder[idx + 1:], postorder[idx:len(postorder) - 1])
        return rtn


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[9,3,15,20,7], [9,15,7,20,3]],
    ]
    for i, j in test_cases:
        result = sol.buildTree(i, j)
        print(lc_tree2list(result))

