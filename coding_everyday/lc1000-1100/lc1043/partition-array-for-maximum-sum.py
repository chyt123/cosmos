class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            maxx = 0
            for j in range(1, k + 1):
                if i - j >= 0:
                    maxx = max(maxx, dp[i - j] + max(arr[i - j: i]) * j)
            dp[i] = maxx
        
        # print(dp)
        return dp[-1]
        
#  [1,4,1, 5, 7, 3, 6, 1, 9, 9, 3 ]
# 0[1,8,12,20,29,34,41,46,65,74,83]

# [0,4,1, 5, 7]
# [0,8,12,18,29]

# [1,2,3,4,5,4,3,1,0]
