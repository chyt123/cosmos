import collections
import math
from typing import List
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        incr = None
        for i in range(1, len(nums)):
            if incr is None:
                if nums[i] > nums[i - 1]:
                    incr = True
                elif nums[i] < nums[i - 1]:
                    incr = False
                continue

            if incr and nums[i] < nums[i - 1] or (not incr and nums[i] > nums[i - 1]):
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 2, 3],
        [6, 5, 4, 4],
        [1, 3, 2],
        [1, 2, 4, 5],
        [1, 1, 1],
    ]
    for i in test_cases:
        print(sol.isMonotonic(i))

