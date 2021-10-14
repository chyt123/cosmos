from typing import List, Optional
from collections import deque
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(arr):
            if not arr:
                return None
            mid = len(arr) // 2
            rtn = TreeNode(arr[mid])
            rtn.left = helper(arr[:mid])
            rtn.right = helper(arr[mid + 1:])
            return rtn

        return helper(nums)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [-10, -3, 0, 5, 9],
        [1, 3],
        [5]
    ]
    for i in test_cases:
        result = sol.sortedArrayToBST(i)
        print(lc_tree2list(result))

