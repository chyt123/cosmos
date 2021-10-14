import bisect
import collections
import copy
import functools
import math
from typing import List, Optional
from collections import defaultdict
from util import TreeNode, lc_tree2list, lc_list2tree


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        nums.extend([math.inf, math.inf])
        for i in range(0, n, 3):
            if nums[i] != nums[i + 1]:
                return nums[i]


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [2,2,3,2],
        [0,1,0,1,0,1,99]
    ]
    for i in test_cases:
        print(sol.singleNumber(i))
