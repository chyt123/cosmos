import bisect
import collections
import math
import random
from typing import List
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(arr, s, e):
            if s >= e:
                return
            if s - e == 1 and arr[s] > arr[e]:
                arr[s], arr[e] = arr[e], arr[s]
                return
            m = (s + e) // 2
            arr[m], arr[s] = arr[s], arr[m]
            pivot = arr[s]
            l, r = s, e
            while l < r:
                while arr[r] >= pivot and l < r:
                    r -= 1
                arr[l] = arr[r]
                while arr[l] <= pivot and l < r:
                    l += 1
                arr[r] = arr[l]
            arr[l] = pivot
            quick_sort(arr, s, l - 1)
            quick_sort(arr, l + 1, e)

        quick_sort(nums, 0, len(nums) - 1)
        return nums


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [5, 7, 8, 3, 2, 4, 6],
        [5, 1, 1, 2, 0, 0],
    ]
    for i in test_cases:
        print(sol.sortArray(i))

