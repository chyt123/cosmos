import bisect
import collections
import math
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mem = collections.deque([-10**4-1 for _ in range(k)])
        for i in nums:
            if i > mem[0]:
                mem.popleft()
                bisect.insort_left(mem, i)
        return mem[0]


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(sol.findKthLargest(nums, k))


