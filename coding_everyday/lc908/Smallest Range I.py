import collections
import math
from typing import List
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        minn = min(nums)
        maxx = max(nums)
        if minn + k >= maxx - k:
            return 0
        else:
            return maxx - minn - 2 * k


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[1], 0],
        [[0,10], 2],
        [[1,3,6], 3],
    ]
    for i, j in test_cases:
        print(sol.smallestRangeI(i, j))

