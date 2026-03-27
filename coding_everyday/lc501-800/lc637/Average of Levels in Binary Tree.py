import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q = collections.deque([root])
        ans = []
        while q:
            summ = 0
            l = len(q)
            for _ in range(l):
                cur = q.popleft()
                if cur:
                    summ += cur.val
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            ans.append(summ/l)
        return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [3],
        [3, 9, 20, None, 15, 7],
        [3, 9, 20, None, None, 15, 7],
    ]
    for i in test_cases:
        print(sol.averageOfLevels(lc_list2tree(i)))
