import bisect
import collections
import copy
import functools
import math
from typing import List, Optional
from collections import defaultdict
from util import TreeNode, lc_tree2list, lc_list2tree, ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def cal(l):
            if not tmp:
                return float('-inf')
            if len(l) == 1 and l[0] < 0:
                return l[0]
            rtn = pre = su = 1
            first_neg = False
            for idx, i in enumerate(l):
                if not first_neg:
                    pre *= i
                else:
                    su *= i
                if i < 0:
                    first_neg = True
                    su = i
                rtn *= i
            if rtn < 0:
                rtn = max(rtn // pre, rtn // su)
            return rtn

        ans = float('-inf')
        tmp = []
        for i in nums:
            if i != 0:
                tmp.append(i)
            else:
                ans = max(ans, cal(tmp))
                tmp = []
        ans = max(ans, cal(tmp))
        return nums[0] if len(nums) == 1 and nums[0] < 0 else max(ans, 0)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [2,3,-2,4],
        [-2,0,-1],
        [2, 3, -2, 0, -4, -8, 4, -8],
        [-2]
    ]
    for i in test_cases:
        result = sol.maxProduct(i)
        print(result)
