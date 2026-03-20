from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        l, h = 0, n - 1
        while l < h:
            m = (l + h) // 2
            if (m == 0 and nums[m] > nums[m + 1]) or \
                (m == n - 1 and nums[m] > nums[m - 1]) or \
                (nums[m] > nums[m - 1] and nums[m] > nums[m + 1]):
                return m
            # decide left or right
            if m + 1 < n and nums[m + 1] > nums[m]: # go right
                l = m + 1
            elif m - 1 >= 0 and nums[m - 1] > nums[m]: # go left
                h = m - 1
        return l


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [6,5,4,3,2,3,2],
        [1,2,3,4,5,6],
        [0],
        [0,1],
        [1,0],
        [1,2,3,1],
        [1,2,1,3,5,6,4],
        [1,2,3,4,5,6,3,2,1]
    ]
    for i in test_cases:
        print(sol.findPeakElement(i))
