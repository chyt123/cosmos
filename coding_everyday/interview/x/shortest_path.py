from typing import List
from collections import deque, OrderedDict, defaultdict
import heapq


# class Solution:
#     def find_path(self, start, end, paths):
#         edges = defaultdict(list)
#         for p, q in paths:
#             edges[p].append(q)
#             edges[q].append(p)
#         cnt = 0
#         q = deque()
#         q.append(start)
#         visit = set()
#         visit.add(start)
#         while q:
#             cnt += 1
#             l = len(q)
#             for i in range(l):
#                 cur = q.popleft()
#                 num = len(edges[cur])
#                 for j in range(num):
#                     next_node = edges[cur][j]
#                     if next_node == end:
#                         return cnt
#                     if next_node not in visit:
#                         visit.add(next_node)
#                         q.append(next_node)


class Solution:
    def find_path(self, start, end, paths, stations, charge_time, power):
        charge_time -= 1
        edges = defaultdict(list)
        for p, q in paths:
            edges[p].append(q)
            edges[q].append(p)
        cnt = 0
        cur_power = power
        q = deque()
        q.append((start, 0, power))
        visit = set()
        visit.add((start, cur_power))
        while q:
            cnt += 1
            l = len(q)
            for i in range(l):
                cur, refill_time, cur_power = q.popleft()
                cur_power -= 1
                num = len(edges[cur])
                if cur in stations and refill_time > 0:
                    if (cur, power) not in visit:
                        if refill_time == charge_time:
                            visit.add((cur, power))
                        else:
                            q.append((cur, refill_time - 1, power))
                            continue
                    else:
                        q.append((cur, refill_time - 1, power))
                        continue
                if cur_power < 0:
                    continue
                for j in range(num):
                    next_node = edges[cur][j]
                    if next_node == end:
                        return cnt
                    if (next_node, cur_power) not in visit:
                        refill_time = charge_time if next_node in stations else 0
                        if cur_power >= 0:
                            visit.add((next_node, cur_power))
                            q.append((next_node, refill_time, cur_power))


if __name__ == "__main__":
    sol = Solution()
    start = 1
    end = 3
    path = [[1,2],[2,3]]
    start = 1
    end = 5
    path = [[1, 2], [2, 3], [2, 5], [3, 4], [4, 5]]
    start = 0
    end = 7
    stations = {3}
    charge_time = 0
    power = 4
    path = [[0, 1], [1, 2], [2, 3], [2, 4], [2, 5], [3, 4], [4, 5], [5, 6], [6, 7]]
    print(sol.find_path(start, end, path, stations, charge_time, power))
