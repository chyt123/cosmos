import bisect
import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for i, j in sorted(tickets)[::-1]:
            graph[i].append(j)
        ans = []
        def dfs(dept):
            while graph[dept]:
                dfs(graph[dept].pop())
            ans.append(dept)
        dfs('JFK')
        return ans[::-1]


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
        [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]],
        [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]],
    ]
    for i in test_cases:
        print(sol.findItinerary(i))
