import bisect
import collections
import math
import re
from typing import List
from util import TreeNode, lc_list2tree


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []

        def dfs(node, s):
            if node:
                s += f'->{node.val}'
                if not node.left and not node.right:
                    ans.append(s[2:])
                dfs(node.left, s)
                dfs(node.right, s)

        dfs(root, '')
        return ans


if __name__ == "__main__":
    root = [1, 2, 3, None, 5]
    root = lc_list2tree(root)
    sol = Solution()
    print(sol.binaryTreePaths(root))