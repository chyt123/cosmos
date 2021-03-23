from typing import List
from collections import defaultdict
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        l = len(A)
        dp = defaultdict()
        for i in range(0, l):
            dp[i, 1] = sum(A[i:]) / (l-i)

        for i in range(l-2, -1, -1):
            for k in range(2, K + 1):
                dp[i, k] = 0
                for j in range(i, l-k+1):
                    dp[i, k] = max(dp[i, k], sum(A[i:j+1])/(j+1-i) + dp[j+1, k-1])

        return dp[0, K]



if __name__ == "__main__":
    sol = Solution()
    A = [9,1,2,3,9]
    K = 3
    print(sol.largestSumOfAverages(A, K))
