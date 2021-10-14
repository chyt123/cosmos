import bisect
import math
from typing import List
from collections import deque, defaultdict, OrderedDict, Counter
from util import (
    TreeNode, lc_list2tree, lc_tree2list,
    ListNode, lc_list2singlelinkedlist
)


class Solution:
    def candy(self, ratings: List[int]) -> int:
        cand = [1 for _ in ratings]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                cand[i] = cand[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and cand[i] <= cand[i + 1]:
                cand[i] = cand[i + 1] + 1
        return sum(cand)


if __name__ == "__main__":
    sol = Solution()
    ratings = [1, 2, 5, 2, 4, 2, 1]
    ratings = [1, 2, 5, 4, 3, 2, 1]
    ratings = [1, 2, 2]
    ratings = [1, 0, 2]

    print(sol.candy(ratings))