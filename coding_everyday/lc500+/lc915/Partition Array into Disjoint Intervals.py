from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:

        # Construct right_min array
        right_min = [0] * len(nums)
        min_num = float('inf')
        for i in range(len(nums) - 1, -1, -1):
            min_num = nums[i] if nums[i] < min_num else min_num
            right_min[i] = min_num


        left_max = -1
        for i in range(len(nums)):
            # cal left max
            left_max = nums[i] if nums[i] > left_max else left_max

            # if left max <= right min, return
            if left_max <= right_min[i + 1]:
                return i + 1
        return 0

if __name__ == "__main__":
    sol = Solution()
    nums = [5,0,3,8,6]
    # nums = [1,1,1,0,6,12]
    print(sol.partitionDisjoint(nums))
