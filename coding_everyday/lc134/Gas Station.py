import bisect
import collections
import copy
import functools
import math
from typing import List, Optional
from collections import defaultdict
from util import TreeNode, lc_tree2list, lc_list2tree


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)] * 2
        if sum(diff) < 0:
            return -1
        i = cnt = ans = summ = 0
        while i < len(diff):
            if cnt == 0:
                if diff[i] > 0:
                    cnt += 1
                    ans = i
                    summ += diff[i]
            elif cnt == n:
                break
            else:
                summ += diff[i]
                if summ < 0:
                    cnt = 0
                    summ = 0
                else:
                    cnt += 1
            i += 1
        return ans % n


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[1,2,3,4,5], [3,4,5,1,2]],
        [[2,3,4], [3,4,3]],
    ]
    for i, j in test_cases:
        print(sol.canCompleteCircuit(i, j))
