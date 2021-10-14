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


class SnapshotArray:

    def __init__(self, length: int):
        self.d = dict(collections.defaultdict())
        self.cnt = 0

    def set(self, index: int, val: int) -> None:
        if index in self.d:
            self.d[index]['cur'] = val
        else:
            self.d[index] = {'cur': val}

    def snap(self) -> int:
        for i in self.d:
            self.d[i][self.cnt] = self.d[i]['cur']
        self.cnt += 1
        return self.cnt - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.d[index][snap_id] if index in self.d and snap_id in self.d[index] else 0


if __name__ == "__main__":

    snapshot = SnapshotArray(1)
    cmds = ["SnapshotArray", "set", "snap", "snap", "snap", "get", "snap", "snap", "get"]
    vals = [[1], [0, 15], [], [], [], [0, 2], [], [], [0, 0]]
    snapshot = SnapshotArray(4)
    cmds = ["SnapshotArray", "snap", "snap", "get", "set", "snap", "set"]
    vals = [[4], [], [], [3, 1], [2, 4], [], [1, 4]]
    snapshot = SnapshotArray(2)
    cmds = ["SnapshotArray", "snap", "get", "get", "set", "get", "set", "get", "set"]
    vals = [[2], [], [1, 0], [0, 0], [1, 8], [1, 0], [0, 20], [0, 0], [0, 7]]
    snapshot = SnapshotArray(3)
    cmds = ["SnapshotArray", "set", "snap", "set", "get"]
    vals = [[3], [0, 5], [], [0, 6], [0, 0]]
    for i in range(len(cmds)):
        if cmds[i] == 'set':
            snapshot.set(vals[i][0], vals[i][1])
        if cmds[i] == 'snap':
            print(snapshot.snap())
        if cmds[i] == 'get':
            print(snapshot.get(vals[i][0], vals[i][1]))

