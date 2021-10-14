import bisect
import math
from typing import List
from collections import defaultdict


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for i in s:
            if i.isalnum():
                new_s += i.lower()
        l = len(new_s)
        if not new_s:
            return True
        for i in range(0, l // 2 + 1):
            if new_s[i] != new_s[l - i - 1]:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
        "ab",
        "0P"
    ]
    for i in test_cases:
        print(sol.isPalindrome(i))
