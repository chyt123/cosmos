import bisect
import collections
import math
import random
from typing import List
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        if n == k:
            return total

        minn = math.inf
        mem = collections.defaultdict()
        for i in range(0, k + 1):
            if (i - 1, i + n - k - 1) in mem:
                summ = mem[i - 1, i + n - k - 1] - cardPoints[i - 1] + cardPoints[i + n - k - 1]
            else:
                summ = sum(cardPoints[i:i + n - k])
            mem[i, i + n - k] = summ
            minn = min(minn, summ)
        return total - minn


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[11,49,100,20,86,29,72], 4],
        [[1, 2, 3, 4, 5, 6, 1], 3],
        [[2, 2, 2], 2],
        [[9, 7, 7, 9, 7, 7, 9], 7],
        [[1, 1000, 1], 1],
        [[1, 79, 80, 1, 1, 1, 200, 1], 3],
    ]
    for i, j in test_cases:
        print(sol.maxScore(i, j))

