import bisect
import math
from typing import List
from collections import deque, defaultdict, OrderedDict, Counter
from util import (
    TreeNode, lc_list2tree,
    ListNode, lc_list2singlelinkedlist
)


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        bobSet = set(bobSizes)
        aliceSum = sum(aliceSizes)
        bobSum = sum(bobSizes)
        diff = (aliceSum - bobSum) // 2
        for i in aliceSizes:
            if i - diff in bobSet:
                ans = [i, i - diff]
        return ans


if __name__ == "__main__":
    sol = Solution()
    aliceSizes = [1, 1]
    bobSizes = [2, 2]
    aliceSizes = [1, 2, 5]
    bobSizes = [2, 4]
    print(sol.fairCandySwap(aliceSizes, bobSizes))
