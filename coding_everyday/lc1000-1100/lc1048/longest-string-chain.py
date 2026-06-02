class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def is_pred(a, b) -> bool:
            # if len(a) != len(b) - 1:
            #     return False
  
            for i in range(len(b)):
                if b[:i] + b[i + 1:] == a:
                    return True
            return False

        n = len(words)
        words = sorted(words, key=lambda x: len(x))

        ans = 1
        dp = [1] * n
        for i in range(1, n):
            for j in range(0, i):
                if len(words[i]) - len(words[j]) != 1:
                    continue

                if is_pred(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
                    ans = max(ans, dp[i])
        return ans

