import bisect
import collections
import copy
import functools
import math
from typing import List, Optional
from collections import defaultdict
from util import TreeNode, lc_tree2list, lc_list2tree, ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find_min(l, r):
            if nums[l] <= nums[r]:
                return nums[l]
            if l + 1 == r:
                return min(nums[l], nums[r])

            mid = (l + r) // 2
            if nums[l] > nums[mid]:
                return find_min(l, mid)
            return find_min(mid + 1, r)

        n = len(nums)
        return find_min(0, n - 1)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [3,4,5,1,2],
        [4,5,6,7,0,1,2],
        [11,13,15,17],
    ]
    for i in test_cases:
        result = sol.findMin(i)
        print(result)
