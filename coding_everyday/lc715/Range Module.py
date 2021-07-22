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


class RangeModule:

    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        idx = bisect.bisect_left(self.ranges, [left, right])
        if idx > 0 and self.ranges[idx - 1][1] >= left:  # merge left
            self.ranges[idx - 1][1] = max(self.ranges[idx - 1][1], right)
            idx -= 1
        else:
            self.ranges.insert(idx, [left, right])

        while idx < len(self.ranges) - 1 and self.ranges[idx + 1][0] <= right:  # merge right
            self.ranges[idx][1] = max(right, self.ranges[idx + 1][1])
            self.ranges.pop(idx + 1)

        # print('add', left, right, self.ranges)

    def queryRange(self, left: int, right: int) -> bool:
        if not self.ranges:
            return False
        idx = bisect.bisect_left(self.ranges, [left, right])
        # print(left, right, idx)
        if idx > 0 and self.ranges[idx - 1][0] <= left < right <= self.ranges[idx - 1][1]:
            return True
        if idx != len(self.ranges) and self.ranges[idx][0] == left and self.ranges[idx][1] >= right:
            return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        idx = bisect.bisect_left(self.ranges, [left, right])
        if idx > 0 and self.ranges[idx - 1][1] >= left:  # update left
            orig_right = self.ranges[idx - 1][1]
            self.ranges[idx - 1] = [self.ranges[idx - 1][0], left]
            if orig_right > right:  # split range
                self.ranges.insert(idx, [right, orig_right])
        while idx < len(self.ranges) and self.ranges[idx][1] <= right:  # delete right
            self.ranges.pop(idx)
        if idx < len(self.ranges):  # update right
            self.ranges[idx][0] = max(self.ranges[idx][0], right)
        # print('remove', left, right, self.ranges)


if __name__ == "__main__":
    rm = RangeModule()
    # cmds = ["RangeModule","addRange", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
    # vals = [[], [10, 15], [15, 17], [9, 18], [10, 14], [13, 15], [16, 17]]
    cmds = ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
    vals = [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
    # cmds = ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
    # vals = [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
    # cmds = ["RangeModule", "addRange", "addRange", "addRange", "queryRange", "queryRange", "queryRange", "removeRange", "queryRange"]
    # vals = [[], [10, 180], [150, 200], [250, 500], [50, 100], [180, 300], [600, 1000], [50, 150], [50, 100]]
    # cmds = ["RangeModule", "queryRange", "queryRange", "addRange", "addRange", "queryRange", "queryRange", "queryRange",
    #  "removeRange", "addRange", "removeRange", "addRange", "removeRange", "removeRange", "queryRange", "queryRange",
    #  "queryRange", "queryRange", "removeRange", "addRange", "removeRange", "queryRange", "addRange", "addRange",
    #  "removeRange", "queryRange", "removeRange", "removeRange", "removeRange", "addRange", "removeRange", "addRange",
    #  "queryRange", "queryRange", "queryRange", "queryRange", "queryRange", "addRange", "removeRange", "addRange",
    #  "addRange", "addRange", "queryRange", "removeRange", "addRange", "queryRange", "addRange", "queryRange",
    #  "removeRange", "removeRange", "addRange", "addRange", "queryRange", "queryRange", "addRange", "addRange",
    #  "removeRange", "removeRange", "removeRange", "queryRange", "removeRange", "removeRange", "addRange", "queryRange",
    #  "removeRange", "addRange", "addRange", "queryRange", "removeRange", "queryRange", "addRange", "addRange",
    #  "addRange", "addRange", "addRange", "removeRange", "removeRange", "addRange", "queryRange", "queryRange",
    #  "removeRange", "removeRange", "removeRange", "addRange", "queryRange", "removeRange", "queryRange", "addRange",
    #  "removeRange", "removeRange", "queryRange"]
    # vals = [[], [21, 34], [27, 87], [44, 53], [69, 89], [23, 26], [80, 84], [11, 12], [86, 91], [87, 94], [34, 52], [1, 59],
    #  [62, 96], [34, 83], [11, 59], [59, 79], [1, 13], [21, 23], [9, 61], [17, 21], [4, 8], [19, 25], [71, 98], [23, 94],
    #  [58, 95], [12, 78], [46, 47], [50, 70], [84, 91], [51, 63], [26, 64], [38, 87], [41, 84], [19, 21], [18, 56],
    #  [23, 39], [29, 95], [79, 100], [76, 82], [37, 55], [30, 97], [1, 36], [18, 96], [45, 86], [74, 92], [27, 78],
    #  [31, 35], [87, 91], [37, 84], [26, 57], [65, 87], [76, 91], [37, 77], [18, 66], [22, 97], [2, 91], [82, 98],
    #  [41, 46], [6, 78], [44, 80], [90, 94], [37, 88], [75, 90], [23, 37], [18, 80], [92, 93], [3, 80], [68, 86],
    #  [68, 92], [52, 91], [43, 53], [36, 37], [60, 74], [4, 9], [44, 80], [85, 93], [56, 83], [9, 26], [59, 64],
    #  [16, 66], [29, 36], [51, 96], [56, 80], [13, 87], [42, 72], [6, 56], [24, 53], [43, 71], [36, 83], [15, 45],
    #  [10, 48]]

    for i in range(len(cmds)):
        if cmds[i] == 'addRange':
            rm.addRange(vals[i][0], vals[i][1])
        elif cmds[i] == 'removeRange':
            rm.removeRange(vals[i][0], vals[i][1])
        elif cmds[i] == 'queryRange':
            print(rm.queryRange(vals[i][0], vals[i][1]))


