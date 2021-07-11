import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode, lc_tree2list


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans

        # def inorder(node):
        #     if node:
        #         inorder(node.left)
        #         ans.append(node.val)
        #         inorder(node.right)
        #
        # inorder(root)
        # return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, None, 2, 3],
        [1, 2, 3, None, 4, None, 5]
    ]
    for i in test_cases:
        result = sol.inorderTraversal(lc_list2tree(i))
        print(result)

