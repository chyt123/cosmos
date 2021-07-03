import collections
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        summ = 0
        d = collections.defaultdict()
        d[0] = 1
        cnt = 0

        for i in range(len(nums)):
            summ += nums[i]
            cnt += d.get(summ - k, 0)
            d[summ] = d.get(summ, 0) + 1
        return cnt


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[1, 1, 1], 2],
        [[1, 2, 3], 3],
        [[1, -1, 0], 0]
    ]
    for i, j in test_cases:
        print(sol.subarraySum(i, j))
