import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode, lc_tree2list, lc_list2singlelinkedlist, ListNode


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0 for _ in graph]  # 0:unvisited, 1, -1: visited
        q = collections.deque()
        cur_color = 1
        for idx, i in enumerate(color):
            if i != 0:
                continue
            q.append(idx)
            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    if color[cur] and color[cur] != cur_color:
                        return False
                    if not color[cur]:
                        color[cur] = cur_color
                        for j in graph[cur]:
                            q.append(j)
                cur_color = - cur_color
        return True


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        # [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]],
        # [[1, 3], [0, 2], [1, 3], [0, 2]],
        [[1], [0], [4], [4], [2, 3]]
    ]
    for i in test_cases:
        print(sol.isBipartite(i))


