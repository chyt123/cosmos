import bisect
import collections
import heapq
import math
import random
from typing import List
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:

    def __init__(self, w: List[int]):
        self.arr = []
        self.total = 0
        cur = 0
        for i in range(len(w)):
            self.arr.append(cur)
            cur += w[i]
            self.total += w[i]

    def pickIndex(self) -> int:
        r = random.randrange(self.total)
        idx = bisect.bisect_right(self.arr, r)
        return idx - 1


if __name__ == "__main__":
    sol = Solution([1, 3])
    cmds = ["Solution", "pickIndex", "pickIndex", "pickIndex", "pickIndex", "pickIndex"]
    vals = [[[1, 3]], [], [], [], [], []]
    for i in range(len(cmds)):
        if cmds[i] == 'pickIndex':
            print(sol.pickIndex())

