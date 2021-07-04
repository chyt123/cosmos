from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        n = len(needle)
        for i in range(0, len(haystack) - n + 1):
            if haystack[i:i + n] == needle:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ["hello", "ll"],
        ["aaaaa", "bba"],
        ["", ""],
        ["a", "a"]
    ]
    for i, j in test_cases:
        print(sol.strStr(i, j))
