from collections import defaultdict
from typing import List
from math import inf


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        self.graph = defaultdict(list)
        for [son, father] in richer:
            self.graph[father].append(son)
        self.qest = [inf] * len(quiet)
        self.ans = [i for i in range(len(quiet))]
        self.visit = [False] * len(quiet)
        for node in list(self.graph):
            if not self.visit[node]:
                qdps, ndps = self.dps(node, quiet)
                if qdps < self.qest[node]:
                    self.qest[node], self.ans[node] = qdps, ndps
        return self.ans

    def dps(self, node, q):
        self.visit[node] = True
        print(node, '----------')
        for son in list(self.graph[node]):
            print('son:', son)
            if not self.visit[son]:
                qdps, ndps = self.dps(son, q)
            else:
                qdps, ndps = self.qest[son], self.ans[son]
            if qdps < self.qest[node]:
                self.qest[node], self.ans[node] = qdps, ndps

        if q[node] < self.qest[node]:
            self.qest[node], self.ans[node] = q[node], node
        print(node, self.qest[node], self.ans[node])
        return self.qest[node], self.ans[node]


if __name__ == "__main__":
    sol = Solution()
    richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
    quiet = [3, 2, 5, 4, 6, 1, 7, 0]
    # richer = []
    # quiet = [0, 1]
    # richer = [[0, 1], [0, 2]]
    # quiet = [0, 1, 2]
    print(sol.loudAndRich(richer, quiet))
