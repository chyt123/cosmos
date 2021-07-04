import collections
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        set_s = set()
        l, r = 0, 0
        set_s.add(s[l])
        maxx = 0
        while r < n - 1:
            if s[r + 1] in set_s:  # move window
                set_s.remove(s[l])
                l += 1
            else:  # expand
                r += 1
                set_s.add(s[r])
            maxx = max(maxx, r - l + 1)
        return maxx


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        "dvdf",
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        ""
    ]
    for i in test_cases:
        print(sol.lengthOfLongestSubstring(i))
