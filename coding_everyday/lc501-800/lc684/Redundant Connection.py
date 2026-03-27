from typing import List
from collections import defaultdict


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ufs = UFS(len(edges))
        for i, j in edges:
            if ufs.is_union(i, j):
                return [i, j]
            ufs.union(i, j)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[1, 2], [1, 3], [2, 3]],
        [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]],
    ]
    for i in test_cases:
        print(sol.findRedundantConnection(i))
