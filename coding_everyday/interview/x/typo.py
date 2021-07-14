from typing import List
from collections import deque, OrderedDict
import heapq


class Solution:
    def typo(self, word: str, dictionary: set) -> list:
        pass




if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ['adple', {'apple', 'banana', 'orange'}],
        ['baiana', {'apple', 'banana', 'orange'}],
        ['cake', {'apple', 'banana', 'orange'}],
    ]
    for i, j in test_cases:
        print(sol.typo(i, j))
