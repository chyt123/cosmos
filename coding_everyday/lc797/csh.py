import copy

class Solution(object):

    def dfs(self, node, path, graph, result):
        if node == len(graph) - 1:
            result.append(path)
        for i in graph[node]:
            self.dfs(i, path + [i], graph, result)
        return result
            
    def allPathsSourceTarget(self, graph):
        result = []
        return self.dfs(0, [0], graph, result)

if __name__ == "__main__":
    sol = Solution()
    # A = [[1,2], [3], [3], []]
    # A = [[1,2],[3,4],[3],[],[5],[]]
    A = [[1,2],[3,5],[3],[4],[6],[6],[]]
    # A = [[4,3,1],[3,2,4],[3],[4],[]]
    # A = [[3,1],[4,6,7,2,5],[4,6,3],[6,4],[7,6,5],[6],[7],[]]
    print sol.allPathsSourceTarget(A)

