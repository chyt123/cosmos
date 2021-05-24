import bisect
import math
import re
from typing import List


class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.chairs = []

    def seat(self) -> int:
        ans = 0
        if not self.chairs:
            self.chairs.append(0)
            return 0
        if self.chairs == [0]:
            ans = self.n - 1
            self.chairs.append(self.n - 1)
            return ans
        maax = 0

        if self.chairs[0] > maax:
            maax = self.chairs[0]
            ans = 0

        for i in range(1, len(self.chairs)):
            min_dist = (self.chairs[i] - self.chairs[i - 1]) // 2
            if min_dist > maax:
                maax = min_dist
                ans = (self.chairs[i] + self.chairs[i - 1]) // 2

        if self.n - self.chairs[-1] - 1 > maax:
            ans = self.n - 1

        bisect.insort_left(self.chairs, ans)
        return ans

    def leave(self, p: int) -> None:
        self.chairs.remove(p)
        return


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)


if __name__ == "__main__":
    cmd = ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "leave", "seat"]
    arg = [[4], [], [], [], [], [1], [3], []]
    cmd = ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
    arg = [[10], [], [], [], [], [4], []]
    cmd = ["ExamRoom", "seat", "leave", "seat", "leave", "seat", "leave", "seat", "leave", "seat", "leave"]
    arg = [[1000000000], [], [0], [], [0], [], [0], [], [0], [], [0]]
    cmd = ["ExamRoom", "seat", "seat", "seat", "leave", "leave", "seat", "seat", "seat", "seat", "seat", "seat", "seat",
           "seat", "seat", "leave", "leave", "seat", "seat", "leave", "seat", "leave", "seat", "leave", "seat", "leave",
           "seat", "leave", "leave", "seat", "seat", "leave", "leave", "seat", "seat", "leave"]
    arg = [[10], [], [], [], [0], [4], [], [], [], [], [], [], [], [], [], [0], [4], [], [], [7], [], [3], [], [3], [],
           [9],
           [], [0], [8], [], [], [0], [8], [], [], [2]]
    for idx, i in enumerate(cmd):
        if i == 'ExamRoom':
            er = ExamRoom(arg[idx][0])
        elif i == 'leave':
            print(er.leave(arg[idx][0]))
        else:
            print(er.seat())