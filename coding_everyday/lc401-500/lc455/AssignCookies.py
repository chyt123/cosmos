import bisect
import math
from typing import List
from collections import deque, defaultdict, OrderedDict, Counter
from util import (
    TreeNode, lc_list2tree, lc_tree2list,
    ListNode, lc_list2singlelinkedlist
)


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        pts, ptg = 0, 0
        while pts < len(s) and ptg < len(g):
            if s[pts] >= g[ptg]:
                ptg += 1
            pts += 1
        return ptg


if __name__ == "__main__":
    sol = Solution()
    g = [1, 2, 3]
    s = [1, 1]
    g = [1,2]
    s = [1,2,3]
    print(sol.findContentChildren(g, s))