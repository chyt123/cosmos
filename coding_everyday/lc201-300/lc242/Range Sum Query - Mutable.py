import bisect
import collections
from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ["anagram", "nagaram"],
        ["rat", "car"],
    ]
    for i, j in test_cases:
        print(sol.isAnagram(i, j))
