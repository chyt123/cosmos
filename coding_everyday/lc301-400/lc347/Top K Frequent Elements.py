import bisect
import collections
import math
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = collections.Counter(nums)
        return [i[0] for i in ct.most_common(k)]


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(sol.topKFrequent(nums, k))


