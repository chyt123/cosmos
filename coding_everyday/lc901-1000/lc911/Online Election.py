import bisect
import collections
import math
from typing import List
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        cnt = collections.Counter()
        self.winning = []
        self.leading = []
        for i in range(len(persons)):
            cnt[persons[i]] += 1
            if not self.leading or cnt[persons[i]] >= self.leading[1]:
                self.leading = [persons[i], cnt[persons[i]]]
            self.winning.append(self.leading[0])

    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.times, t)
        return self.winning[idx - 1]


if __name__ == "__main__":
    cmds = ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
    vals = [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
    tvc = None
    for i in range(len(cmds)):
        c = cmds[i]
        v = vals[i]
        if c == 'TopVotedCandidate':
            tvc = TopVotedCandidate(v[0], v[1])
        elif c == 'q':
            print(tvc.q(v[0]))

