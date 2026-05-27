class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # dp[i][diff] the max seen at index i with diff diff

        n = len(nums)

        dp = [{} for _ in range(n)]
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                diff = nums[j] - nums[i]
                dp[j][diff] = dp[i].get(diff, 1) + 1
                ans = max(ans, dp[j][diff])

        return ans
