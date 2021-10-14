import bisect
import collections
import math
import re
from typing import List
from util import TreeNode, lc_list2tree


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        print(graph)
        leaves = []
        for k, v in graph.items():
            if len(v) == 1:
                leaves.append(k)

        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            while leaves:
                cur_leaf = leaves.pop()
                father = graph[cur_leaf][0]
                graph[father].remove(cur_leaf)
                if len(graph[father]) == 1:
                    new_leaves.append(father)
            leaves = new_leaves
        return leaves


if __name__ == "__main__":
    sol = Solution()
    n = 2
    edges = [[0, 1]]
    n = 0
    edges = []
    n = 6
    edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    n = 10
    edges = [[0, 1], [0, 2], [0, 3], [2, 4], [0, 5], [5, 6], [6, 7], [2, 8], [7, 9]]
    print(sol.findMinHeightTrees(n, edges))