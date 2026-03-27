import bisect
from typing import List
from collections import defaultdict


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cur0 = 1 if s[0] == '0' else 0
        cur1 = 1 - cur0
        ans = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:  # switch
                ans += 1
                if s[i] == '0':
                    cur0 = 1
                else:
                    cur1 = 1
            else:
                if s[i] == '0':
                    cur0 += 1
                    if cur0 <= cur1:
                        ans += 1
                else:
                    cur1 += 1
                    if cur1 <= cur0:
                        ans += 1
        return ans



if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        "00110011",
        "10101",
    ]
    for i in test_cases:
        print(sol.countBinarySubstrings(i))
