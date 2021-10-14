from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        post = {i: [] for i in range(numCourses)}
        visit = [0 for _ in range(numCourses)]
        for i, j in prerequisites:
            post[j].append(i)

        ans = []
        self.ispossible = True

        def dfs(node):
            if not self.ispossible:
                return
            visit[node] = 1
            for i in post[node]:
                if visit[i] == 0:
                    dfs(i)
                if visit[i] == 1:
                    self.ispossible = False
            visit[node] = 2
            ans.append(node)

        for i in post:
            if visit[i] == 0:
                dfs(i)

        return ans[::-1] if self.ispossible else []


if __name__ == "__main__":
    sol = Solution()
    numCourses = 6
    prerequisites = [[0,1],[2,0],[0,3],[1,2],[1,3],[2,4],[2,5]]
    numCourses = 2
    prerequisites = [[1, 0]]
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(sol.findOrder(numCourses, prerequisites))
