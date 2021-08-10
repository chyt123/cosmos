import bisect
from copy import deepcopy
from typing import List
from collections import defaultdict
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [True for _ in range(n + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == j == 0:
                    continue
                elif i == 0:
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i - 1]
                else:
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[i + j - 1] or dp[j] and s1[i - 1] == s3[i + j - 1]

        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ["a", "", "a"],
        ["aabcc", "dbbca", "aadbbcbcac"],
        ["aabcc", "dbbca", "aadbbbaccc"],
        ["", "", ""],
    ]
    for i, j, k in test_cases:
        result = sol.isInterleave(i, j, k)
        print(result)
