from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        suum = numbers[l] + numbers[r]
        while suum != target:
            if suum > target:
                r -= 1
            elif suum < target:
                l += 1
            suum = numbers[l] + numbers[r]

        return [l + 1, r + 1]


if __name__ == "__main__":
    sol = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    numbers = [2, 3, 4]
    target = 6
    numbers = [-1, 0]
    target = -1
    print(sol.twoSum(numbers, target))
