from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.UNKNOWN = 0
        self.VISITING = 1
        self.UNSAFE = 2
        self.SAFE = 3
        self.status = [self.UNKNOWN for _ in range(len(graph))]
        ret = []
        for node in range(len(graph)):
            if self.dfs(graph, node) == self.SAFE:
                ret.append(node)
        return ret

    def dfs(self, graph, node):
        if self.status[node] == self.VISITING:
            return self.UNSAFE
        if self.status[node] != self.UNKNOWN:
            return self.status[node]

        self.status[node] = self.VISITING
        for nextNode in graph[node]:
            if self.dfs(graph, nextNode) == self.UNSAFE:
                self.status[node] = self.UNSAFE
                return self.UNSAFE
        self.status[node] = self.SAFE
        return self.SAFE

# TLE
#         rst = []
#         while [] in graph:
#             removed = []
#             for node, nextNodeList in enumerate(graph):
#                 if nextNodeList == []:
#                     rst.append(node)
#                     removed.append(node)
#                     graph[node] = False
#             for node in removed:
#                 for nextNodeList in graph:
#                     if nextNodeList and node in nextNodeList:
#                         nextNodeList.remove(node)
#         rst.sort()
#         return rst


if __name__ == "__main__":
    sol = Solution()
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    print(sol.eventualSafeNodes(graph))
    graph = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
    print(sol.eventualSafeNodes(graph))
    graph = [[1], [2], [3], [1]]
    print(sol.eventualSafeNodes(graph))

