import bisect
import math
from typing import List
from collections import deque, defaultdict, OrderedDict, Counter
from util import (
    TreeNode, lc_list2tree, lc_tree2list,
    ListNode, lc_list2singlelinkedlist
)


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        i = 1
        cnt = 0
        nums.insert(0, -10**5)
        n = len(nums)
        nums.append(10**5)
        print(nums)
        while i < n:
            if nums[i] < nums[i - 1]:
                cnt += 1
                if not (nums[i - 2] <= nums[i - 1] <= nums[i + 1] or nums[i - 2] <= nums[i] <= nums[i + 1]) or cnt == 2:
                    return False
            i += 1
        return True


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 2, 1]
    nums = [1,5,4,6,7,10,8,9]
    nums = [3, 4, 2, 3]
    nums = [5, 7, 1, 8]
    print(sol.checkPossibility(nums))