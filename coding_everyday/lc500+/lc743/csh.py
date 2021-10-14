from collections import defaultdict, deque


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        dist = {node: float('inf') for node in xrange(1, N+1)}

        def dfs(node, elapsed):
            if elapsed >= dist[node]: return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed + time)

        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1


if __name__ == "__main__":
    # words = ["apple", "aasdfe"]
    # [prefix, suffix] = ["a","e"]
    sol = Solution()
    times = [[2,1,1],[2,3,1],[3,4,1]]
    N = 4
    K = 2
    print sol.networkDelayTime(times, N, K)
