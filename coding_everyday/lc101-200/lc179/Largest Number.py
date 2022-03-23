import bisect
import collections
import copy
import functools
import math
from typing import List, Optional
from collections import defaultdict
from util import TreeNode, lc_tree2list, lc_list2tree, ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sorted_nums = sorted(nums, key=functools.cmp_to_key(self.sort_by_str))
        rtn = ""
        for i in sorted_nums:
            rtn += str(i)
        zero = True
        for i in rtn:
            if i != '0':
                zero = False
                break
        return '0' if zero else rtn

    def sort_by_str(self, x1, x2):
        s1 = str(x1) + str(x2)
        s2 = str(x2) + str(x1)
        for i in range(len(s1)):
            if s1[i] > s2[i]:
                return -1
            if s1[i] < s2[i]:
                return 1
        return 0


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [10, 2],
        [3, 30, 34, 5, 9],
        [3, 30, 34, 33, 5, 9],
        [34, 344, 343],
        [0, 0]
    ]
    for i in tests:
        result = sol.largestNumber(i)
        print(result)
