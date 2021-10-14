import bisect
import math
from typing import List
from collections import deque, defaultdict, OrderedDict
from util import TreeNode, lc_list2tree


class Dir:
    def __init__(self):
        self.dir = 0

    def next(self):
        self.dir += 1
        if self.dir == 4:
            self.dir = 0

    def pre(self):
        self.dir -= 1
        if self.dir == -1:
            self.dir = 3


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dir = {
            0: [0, 1],
            1: [1, 0],
            2: [0, -1],
            3: [-1, 0]
        }
        obstacles = set(map(tuple, obstacles))
        cur_dir = Dir()
        cur_xy = [0, 0]
        maxx = 0
        for cmd in commands:
            if cmd == -1:
                cur_dir.next()
            elif cmd == -2:
                cur_dir.pre()
            else:
                step = 0
                while step < cmd:
                    if not (cur_xy[0] + dir[cur_dir.dir][0], cur_xy[1] + dir[cur_dir.dir][1]) in obstacles:
                        cur_xy[0] += dir[cur_dir.dir][0]
                        cur_xy[1] += dir[cur_dir.dir][1]
                        step += 1
                    else:
                        break
                maxx = max(maxx, cur_xy[0] ** 2 + cur_xy[1] ** 2)
        return maxx


if __name__ == "__main__":
    sol = Solution()
    commands = [4, -1, 3]
    obstacles = []
    commands = [-2, -2, 4, -1, 4, -2, 4]
    obstacles = [[0, -3], [2, 4], [3, 4], [-1, 4], [-2, -2]]
    commands = [7, -2, -2, 7, 5]
    obstacles = [[-3, 2], [-2, 1], [0, 1], [-2, 4], [-1, 0], [-2, -3], [0, -3], [4, 4], [-3, 3], [2, 2]]
    commands = [2, 2, 5, -1, -1]
    obstacles = [[-3, 5], [-2, 5], [3, 2], [5, 0], [-2, 0], [-1, 5], [5, -3], [0, 0], [-4, 4], [-3, 4]]
    print(sol.robotSim(commands, obstacles))
