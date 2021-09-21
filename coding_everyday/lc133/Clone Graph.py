import bisect
import collections
import copy
import functools
import math
from typing import List, Optional
from collections import defaultdict
from util import TreeNode, lc_tree2list, lc_list2tree


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        rtn = Node(node.val)
        mem = dict()

        def dfs(cur, cp):
            mem[cur.val] = cp
            for i in cur.neighbors:
                if i.val not in mem:
                    new_cp = Node(i.val)
                    mem[i.val] = new_cp
                    cp.neighbors.append(new_cp)
                    new_cp.neighbors.append(cp)
                    dfs(i, new_cp)
                else:
                    if mem[i.val] not in cp.neighbors:
                        cp.neighbors.append(mem[i.val])
                        mem[i.val].neighbors.append(cp)

        dfs(node, rtn)
        return rtn


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[2,4],[1,3],[2,4],[1,3]],
    ]
    # for i in test_cases:
        # print(sol.cloneGraph(i))
