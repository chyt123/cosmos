import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode, lc_tree2list


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = collections.deque([root])
        ans = 0
        while q:
            l = len(q)
            for i in range(l):
                cur = q.popleft()
                ans = cur.val
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
        return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [3, 9, 20, None, None, 15, 7],
        [1, 2, 3, 4, None, 5, 6, None, None, 7]
    ]
    for i in test_cases:
        result = sol.findBottomLeftValue(lc_list2tree(i))
        print(result)

