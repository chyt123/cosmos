from typing import List
from collections import defaultdict


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        pt1, pt2, pos = m - 1, n - 1, m + n - 1
        while pos >= 0:
            print(pt1, pt2)
            if pt1 >= 0 and nums1[pt1] >= nums2[pt2] or pt2 < 0:
                nums1[pos] = nums1[pt1]
                pt1 -= 1
            elif nums1[pt1] < nums2[pt2] or pt1 < 0:
                nums1[pos] = nums2[pt2]
                pt2 -= 1
            pos -= 1
        print(nums1)


if __name__ == "__main__":
    sol = Solution()
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    print(sol.merge(nums1, m, nums2, n))
