import collections
import math
from typing import List
from collections import deque, OrderedDict
import heapq


class Solution:
    def find_path(self, edges, start, end, lockdown):
        path = []
        graph = collections.defaultdict(list)
        dij = collections.defaultdict()  # (min_lockdown_num, min_path_len, father_note)
        dij[start] = (0, 0, None) if start not in lockdown else (1, 0, None)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = set()
        q = collections.deque()
        q.append(start)
        while q:
            cur = q.popleft()
            cur_lockdown_num, cur_path_len, _ = dij[cur]
            while graph[cur]:
                cur_son = graph[cur].pop()
                graph[cur_son].remove(cur)
                if cur_son not in visited:
                    q.append(cur_son)
                    (son_lockdown_num, son_path_len, _) = dij[cur_son] if cur_son in dij else (math.inf, math.inf, None)
                    new_lockdown_num = cur_lockdown_num + 1 if cur_son in lockdown else cur_lockdown_num
                    new_path_len = cur_path_len + 1
                    if new_lockdown_num < son_lockdown_num or \
                            new_lockdown_num == son_lockdown_num and new_path_len < cur_path_len:
                        dij[cur_son] = (new_lockdown_num, new_path_len, cur)
            visited.add(cur)

        cur = end
        while cur is not None:  # while has father
            path.append(cur)
            cur = dij[cur][2]
        return path[::-1]


if __name__ == "__main__":
    sol = Solution()
    edges = [[0,1],[0,3],[3,2],[3,5],[2,100],[1,4],[4,5],[5,100]]
    start = 0
    end = 100
    lockdown = {1, 2, 3}
    print(sol.find_path(edges, start, end, lockdown))
