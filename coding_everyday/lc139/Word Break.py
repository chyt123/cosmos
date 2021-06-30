from typing import List
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        for i in range(1, n + 1):
            for word in wordDict:
                l = len(word)
                if i >= l and s[i - l:i] == word:
                    dp[i] = dp[i] or dp[i - l]
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    s = 'catsandog'
    wordDict = ['cats', 'cat', 'and', 'sando', 'og']
    s = "dogs"
    wordDict = ["dog", "s", "gs"]
    print(sol.wordBreak(s, wordDict))
