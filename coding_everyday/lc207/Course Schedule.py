from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0 for _ in range(numCourses)]  # 0:not visited, 1:in progress, 2:finished
        graph = defaultdict(list)
        for i, j in prerequisites:
            graph[j].append(i)

        def dfs(node):
            if not visited[node]:
                visited[node] = 1
                if node in graph:
                    for i in graph[node]:
                        if visited[i] == 1 or not dfs(i):
                            return False
                visited[node] = 2
            return True

        for i in graph:
            if not visited[i] and not dfs(i):
                return False
        return True

        # graph = defaultdict(list)
        # in_deg = [0 for _ in range(numCourses)]
        # mem = []
        #
        # for i, j in prerequisites:
        #     graph[i].append(j)
        #     in_deg[j] += 1
        # for idx, i in enumerate(in_deg):
        #     if i == 0:
        #         mem.append(idx)
        #
        # for node in mem:
        #     for i in graph[node]:
        #         in_deg[i] -= 1
        #         if in_deg[i] == 0:
        #             mem.append(i)
        #
        # return len(mem) == numCourses


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [5, [[1, 0], [2, 1], [0, 2], [4, 1], [3, 4], [3, 1]]],
        [2, [[1, 0]]],
        [2, [[1, 0], [0, 1]]],
    ]
    for i, j in test_cases:
        print(sol.canFinish(i, j))
