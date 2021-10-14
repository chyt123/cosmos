import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = collections.deque()
        q.append(root)
        cnt = 0
        while q:
            cnt += 1
            l = len(q)
            for _ in range(l):
                cur_root = q.popleft()
                if cur_root.left:
                    q.append(cur_root.left)
                if cur_root.right:
                    q.append(cur_root.right)
        return cnt


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [3, 9, 20, None, None, 15, 7],
        [1, None, 2],
        [],
        [1],
    ]
    for i in test_cases:
        print(sol.maxDepth(lc_list2tree(i)))
