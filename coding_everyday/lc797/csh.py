class Solution(object):

    def allPathsSourceTarget(self, graph):
        node_stack = list()
        result = list()
        tmp_result = list()
        node_stack.append(0)
        while len(node_stack):
            top = node_stack.pop()
            tmp_result.append(top)
            print tmp_result, result
            if len(graph[top]) > 1:
                tmp_result.append(-1)
            elif not len(graph[top]):
                if top == len(graph) - 1:  # found a path
                    result.append(tmp_result)
                else:  # found a dead end
                    pass
                while tmp_result[-1] >= 0 or node_stack[-1] not in graph[tmp_result[-2]]:
                    tmp_result.pop()
            for i in graph[top]:
                node_stack.append(i)


if __name__ == "__main__":
    sol = Solution()
    # A = [2, 3, 1, 4, 0]
    A = [[1,2],[3,4],[3],[],[5],[]]
    print sol.allPathsSourceTarget(A)

