import collections
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pnum = [0]
        for i in range(0, len(self.nums)):
            self.pnum.append(self.pnum[i] + self.nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.pnum[right + 1] - self.pnum[left]


if __name__ == "__main__":
    pass
