from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # - - | |
        if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]:
            return False
        line1 = [rec1[1], rec1[3], rec1[0], rec1[2]]
        line2 = [rec2[1], rec2[3], rec2[0], rec2[2]]
        if line2[0] >= line1[1] or line2[1] <= line1[0] or line2[2] >= line1[3] or line2[3] <= line1[2]:
            return False
        return True


if __name__ == "__main__":
    sol = Solution()
    rec1 = [0, 0, 2, 2]
    rec2 = [1, 1, 3, 3]
    # rec1 = [0, 0, 1, 1]
    # rec2 = [1, 0, 2, 1]
    # rec1 = [0, 0, 1, 1]
    # rec2 = [2, 2, 3, 3]
    print(sol.isRectangleOverlap(rec1, rec2))
