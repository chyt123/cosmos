import bisect
from copy import deepcopy
from typing import List
from collections import defaultdict
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def numTrees(self, n: int) -> int:
        mem = {0: 1, 1: 1}

        def cal_num(num):
            if num in mem:
                return mem[num]
            ans = 0
            for i in range(1, num + 1):
                ans += cal_num(i - 1) * cal_num(num - i)
            mem[num] = ans
            return ans

        return cal_num(n)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        1, 2, 3
    ]
    for i in test_cases:
        result = sol.numTrees(i)
        print(result)
