import collections
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        maxx = 0
        for i in nums:
            if i in set_nums:
                cnt = 1
                set_nums.remove(i)
                forw = i + 1
                backw = i - 1
                while forw in set_nums:
                    cnt += 1
                    set_nums.remove(forw)
                    forw += 1
                while backw in set_nums:
                    cnt += 1
                    set_nums.remove(backw)
                    backw -= 1
                maxx = max(maxx, cnt)
        return maxx


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [100,4,200,1,3,2],
        [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
    ]
    for i in test_cases:
        print(sol.longestConsecutive(i))
