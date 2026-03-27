import bisect
from typing import List
from collections import defaultdict


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for c in range(0, 2 * n):
            left = c // 2
            right = c // 2 if c % 2 == 0 else c // 2 + 1
            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans

        # def is_palind(start, end):
        #     mid1 = (start + end + 1) // 2
        #     mid2 = (start + end) // 2
        #     return s[start:mid1] == s[end:mid2:-1]
        #
        # n = len(s)
        # dp = [[0 for _ in range(n)] for _ in range(n)]
        # for l in range(n):
        #     for i in range(n - l):
        #         j = i + l
        #         if i == j:
        #             dp[i][j] = 1
        #         else:
        #             dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1] + is_palind(i, j)
        # return dp[0][len(s) - 1]


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        "abc",
        "aaa",
        "ababa"
    ]
    for i in test_cases:
        print(sol.countSubstrings(i))
