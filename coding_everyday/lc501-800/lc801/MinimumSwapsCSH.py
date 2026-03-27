from typing import List
from math import inf


class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        keep = [inf for _ in range(len(A))]
        swap = [inf for _ in range(len(A))]
        keep[0] = 0
        swap[0] = 1
        for i in range(1, len(A)):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                # case1, keep both
                keep[i] = keep[i - 1]
                # case2, swap both
                swap[i] = swap[i - 1] + 1
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                # case3, swap former, keep latter
                keep[i] = min(swap[i - 1], keep[i])
                # case4, keep former, swap latter
                swap[i] = min(keep[i - 1] + 1, swap[i])
        return min(keep[-1], swap[-1])


if __name__ == "__main__":
    A = [0,3,4,9,10]
    B = [2,3,7,5,6]
    sol = Solution()
    print(sol.minSwap(A, B))

