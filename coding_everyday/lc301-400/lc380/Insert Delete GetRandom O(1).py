import bisect
import random
from typing import List
from collections import defaultdict, OrderedDict


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.num = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.d:
            self.num.append(val)
            self.d[val] = len(self.num) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.d:
            return False
        idx = self.d[val]
        self.d.pop(val)
        self.num[idx] = self.num[-1]
        if self.num[-1] != val:
            self.d[self.num[-1]] = idx
        self.num.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.num[random.randrange(len(self.num))]


if __name__ == "__main__":
    cmds = ["RandomizedSet", "remove", "remove", "insert", "getRandom", "remove", "insert"]
    vals = [[], [0], [0], [0], [], [0], [0]]
    cmds = ["RandomizedSet", "insert", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
    vals = [[], [1], [3], [2], [2], [], [1], [2], []]
    cmds = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
    vals = [[], [1], [2], [2], [], [1], [2], []]
    rs = RandomizedSet()
    for idx, i in enumerate(cmds):
        if i == 'insert':
            print(rs.insert(vals[idx][0]))
            # print(rs.num, rs.d)
        if i == 'remove':
            print(rs.remove(vals[idx][0]))
            # print(rs.num, rs.d)
        if i == 'getRandom':
            print(rs.getRandom())
