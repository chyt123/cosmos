import math
from typing import List
from collections import defaultdict


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp = [0 for _ in s]
        dp[0] = 1 if s[0] != '0' else 0
        num = 10 * int(s[0]) + int(s[1])
        if s[1] == '0' and num > 26:
            return 0
        if 10 < num < 20 or 20 < num <= 26:
            dp[1] = 2
        else:
            dp[1] = 1
        # print(dp)
        n = len(s)
        for i in range(2, n):
            num = 10 * int(s[i - 1]) + int(s[i])
            if s[i] == '0' and (num > 26 or num == 0):
                return 0
            if s[i] == '0':
                dp[i] = dp[i - 2]
            elif 10 < num <= 26 and s[i - 1] != '0':
                dp[i] = dp[i - 2] + dp[i - 1]
            else:
                dp[i] = dp[i - 1]
        # print(dp)
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    s = '10'
    s = '11106'
    s = '10011'
    s = '207'
    s = '230'
    s = '1010'
    print(sol.numDecodings(s))
