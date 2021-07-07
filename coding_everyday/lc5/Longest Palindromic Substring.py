import collections
from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        maxx = 0
        for i in range(len(s) * 2):
            if i % 2 == 0:
                l = r = i // 2
                cnt = -1
            else:
                l, r = (i - 1) // 2, (i + 1) // 2
                cnt = 0
            cur = ''
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur = s[l] + cur + s[r] if l != r else s[l]
                cnt += 2
                l -= 1
                r += 1
            if cnt > maxx:
                maxx = cnt
                ans = cur
            maxx = max(maxx, cnt)
        return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        "babad",
        "cbbd",
        "a",
        "ac",
    ]
    for i in test_cases:
        print(sol.longestPalindrome(i))
