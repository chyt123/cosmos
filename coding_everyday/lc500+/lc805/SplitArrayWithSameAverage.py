import collections
import functools
from typing import List


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        @functools.lru_cache()
        def find(target, k, i):
            if k == 0:
                return target == 0
            if target < 0 or k + i > n:
                return False
            return find(target - nums[i], k - 1, i + 1) or find(target, k, i + 1)

        s = sum(nums)
        n = len(nums)
        return any(find(s * k / n, k, 0) for k in range(1, n // 2 + 1) if n * k % n == 0)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    print(sol.splitArraySameAverage(nums))
