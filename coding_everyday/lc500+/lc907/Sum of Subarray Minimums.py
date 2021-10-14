import collections
import math
from typing import List
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [0 for _ in range(n + 1)]
        stack = []
        summ = 0
        for i in range(1, n + 1):
            while stack and arr[stack[-1] - 1] >= arr[i - 1]:
                stack.pop()
            pre = stack[-1] if stack else 0
            stack.append(i)
            dp[i] = arr[i - 1] * (i - pre) + dp[pre]
            summ += dp[i]
        return summ % (10 ** 9 + 7)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [3, 1, 2, 4],
        [11, 81, 94, 43, 3],
    ]
    for i in test_cases:
        print(sol.sumSubarrayMins(i))

