from math import sqrt
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        num = pow(10, 9) + 7
        if not arr:
            return 0
        l = len(arr)
        arr.sort()
        dp = [1 for _ in range(l)]
        index = {x: i for i, x in enumerate(arr)}
        for i in range(1, l):
            for j in range(i):
                if arr[j] > sqrt(arr[i]):
                    break
                if arr[i] % arr[j] == 0:
                    div = arr[i] / arr[j]
                    if div in index:
                        idx = index[int(div)]
                        dp[i] += dp[j] * dp[idx] if j == idx else dp[j] * dp[idx] * 2
                        dp[i] %= num
        return sum(dp) % num


if __name__ == "__main__":
    sol = Solution()

    arr = [2,4,5,10,20]
    # arr = [18,3,6,2]
    print(sol.numFactoredBinaryTrees(arr))
