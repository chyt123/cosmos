class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        if n <= 1:
            return 0

        ans = 0
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                diff = nums[i - 1] - nums[i] + 1
                ans += diff
                nums[i] += diff
        return ans

# 1 1 2 2 3 7
# 1 2 3 4 5 7