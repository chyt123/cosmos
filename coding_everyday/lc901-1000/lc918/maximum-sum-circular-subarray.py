from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        special_sum = float('-inf')

        normal_sum = [0] * n
        normal_sum[0] = nums[0]
        for i in range(1, n):
            normal_sum[i] = max(nums[i], normal_sum[i - 1] + nums[i])
        normal_max = max(normal_sum)

        right_max = [0] * n
        right_max[-1] = nums[-1]
        right_sum = nums[-1]
        for i in range(n - 2, -1, -1):
            right_sum += nums[i]
            right_max[i] = max(right_max[i + 1], right_sum)

        left_sum = 0
        for i in range(n - 1):
            left_sum += nums[i]
            special_sum = max(left_sum + right_max[i + 1], special_sum)
        # print(f"normal_sum={normal_sum}, right_max={right_max}")
        return max(normal_max, special_sum)

if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1,-2,3,-2],
        [5,-3,5],
        [10, -2, 20, -3, 30],
        [-3, -2]
    ]
    for i in test_cases:
        print(sol.maxSubarraySumCircular(i))