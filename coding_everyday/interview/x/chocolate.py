from typing import List
from collections import deque, OrderedDict
import heapq


class Solution:
    def split_chocolate(self, choco: list, k: int) -> list:
        l, r = 0, sum(choco)
        if k == 1:
            return r
        while l <= r:
            mid = (l + r) // 2
            summ = 0
            portion = 1
            fail = False
            for idx, i in enumerate(choco):
                summ += i
                if portion > k:
                    break
                if summ >= mid and idx != len(choco) - 1:
                    summ = 0
                    portion += 1
                elif idx == len(choco) - 1 and summ < mid:
                    fail = True

            if portion < k or fail:  # mid too large
                r = mid - 1
            else:
                l = mid + 1
        return r


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[1, 2, 3, 3, 2, 4, 4], 3],
        [[6, 3, 2, 8, 7, 5], 3],
        [[99, 1, 2], 3]
    ]
    for i, j in test_cases:
        print(sol.split_chocolate(i, j))
