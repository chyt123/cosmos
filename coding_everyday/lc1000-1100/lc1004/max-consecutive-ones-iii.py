class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_pos = [-1]
        for i, n in enumerate(nums):
            if n == 0:
                zero_pos.append(i)

        zero_pos.append(len(nums))

        zero_num = len(zero_pos)

        if zero_num - 2 <= k:
            return len(nums)

        ans = 0
        for start in range(1, zero_num - k):
            end = start + k - 1
            ans = max(ans, zero_pos[end + 1] - zero_pos[start - 1] - 1)

        return ans
# [-1, 3, 4, 5, 10, 11]
# [-1, 0, 1, 4, 5, 9, 12, 13, 14, 19], k = 3