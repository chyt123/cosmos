import collections
import math
from typing import List
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        arr = [0]
        for i, row in enumerate(board[::-1]):
            arr += row[::-1] if i % 2 else row

        q = collections.deque([1])
        lv = 0
        visited = set([1])
        while q:
            l = len(q)
            for _ in range(l):
                cur = q.popleft()
                if cur == n * n:
                    return lv
                for i in range(1, 7):
                    if cur + i <= n * n and cur + i not in visited:
                        visited.add(cur + i)
                        q.append(cur + i if arr[cur + i] == -1 else arr[cur + i])
            lv += 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 35, -1, -1, 13, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 15, -1, -1, -1, -1]],
        [[-1, -1],
         [-1, 3]],
        [[1, 1, -1],
         [1, 1, 1],
         [-1, 1, 1]],
    ]
    for i in test_cases:
        print(sol.snakesAndLadders(i))

