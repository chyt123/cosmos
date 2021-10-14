import collections
import math
from typing import List
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = collections.deque(encoding)

    def next(self, n: int) -> int:
        while self.encoding and self.encoding[0] < n:
            cur = self.encoding.popleft()
            _ = self.encoding.popleft()
            n = n - cur
        if not self.encoding:
            return -1
        self.encoding[0] -= n
        return self.encoding[1]


if __name__ == "__main__":
    rle = RLEIterator([3, 8, 0, 9, 2, 5])
    cmds = ["RLEIterator", "next", "next", "next", "next"]
    vals = [[[3, 8, 0, 9, 2, 5]], [2], [1], [1], [2]]
    for i in range(len(cmds)):
        if cmds[i] == 'next':
            print(rle.next(vals[i][0]))

