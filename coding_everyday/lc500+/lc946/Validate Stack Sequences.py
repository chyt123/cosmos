import bisect
import collections
import heapq
import math
import random
from typing import List
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        push_pt = pop_pt = 0
        while push_pt < len(pushed) and pop_pt < len(popped):
            while push_pt < len(pushed) and (not stack or stack[-1] != popped[pop_pt]):
                stack.append(pushed[push_pt])
                push_pt += 1
            while pop_pt < len(popped) and stack and stack[-1] == popped[pop_pt]:
                stack.pop()
                pop_pt += 1
        return not stack


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[1, 2, 3, 4, 5], [4, 5, 3, 2, 1]],
        [[1, 2, 3, 4, 5], [4, 3, 5, 1, 2]],
        [[1, 0], [1, 0]],
    ]
    for i, j in test_cases:
        print(sol.validateStackSequences(i, j))

