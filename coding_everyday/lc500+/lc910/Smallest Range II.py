import collections
import math
from typing import List
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 0
        nums.sort()
        minn, maxx = nums[0], nums[-1]
        ans = maxx - minn
        for i in range(n - 1):
            ans = min(ans, max(nums[i] + k, maxx - k) - min(minn + k, nums[i + 1] - k))
        return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[1], 0],
        [[0,10], 2],
        [[1,3,6], 3],
        [[2,7,2], 1],
        [[1, 4, 6, 4], 3],
        [[4, 1, 8, 10], 3]
    ]
    for i, j in test_cases:
        print(sol.smallestRangeII(i, j))

