import collections
import math
from typing import List
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        even.extend(odd)
        return even


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [3, 1, 2, 4]
    ]
    for i in test_cases:
        print(sol.sortArrayByParity(i))

