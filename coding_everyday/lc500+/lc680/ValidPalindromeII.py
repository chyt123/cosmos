import collections
import math
from typing import List


class Solution:
    def is_palindrome(self, mstring):
        l, r = 0, len(mstring) - 1
        while l <= r:
            if mstring[l] != mstring[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        flag = False
        while l <= r:
            if s[l] != s[r]:
                flag = True
                break
            l += 1
            r -= 1
        if not flag:
            return True
        return self.is_palindrome(s[l:r]) or self.is_palindrome(s[l + 1: r + 1])


if __name__ == "__main__":
    sol = Solution()
    s = "abcdcba"
    s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    s = "abcdedcxba"
    print(sol.validPalindrome(s))


