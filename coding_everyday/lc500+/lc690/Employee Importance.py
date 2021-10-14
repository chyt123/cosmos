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

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ans = 0
        d = dict()
        for e in employees:
            d[e.id] = [e.importance, e.subordinates]
        q = collections.deque([id])
        while q:
            cur = q.popleft()
            ans += d[cur][0]
            q += d[cur][1]
        return ans


if __name__ == "__main__":
    sol = Solution()

