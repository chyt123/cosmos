import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = collections.deque()
        q.append(root)
        while q:
            l = len(q)
            cmp = []
            for _ in range(l):
                cur = q.popleft()
                if cur:
                    cmp.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
                else:
                    cmp.append(None)
            mid = len(cmp) // 2
            if cmp[:mid] != cmp[len(cmp) - 1:mid - 1:-1]:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 2, 3, 4, 4, 3],
        [1, 2, 2, None, 3, None, 3],
        [1, 2, 2, 3, 4, 4, 3, None, 5, None, None, None, None, 5]
    ]
    for i in test_cases:
        print(sol.isSymmetric(lc_list2tree(i)))
