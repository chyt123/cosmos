class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [float('inf')] * n
        ans[0] = 0
        sred, sblue = defaultdict(set), defaultdict(set)
        for i, j in redEdges:
            sred[i].add(j)
        for i, j in blueEdges:
            sblue[i].add(j)
        
        # print(sred, sblue)
        start = []
        if 0 in sred:
            start.append((0, True)) # True red, False blue
        if 0 in sblue:
            start.append((0, False)) # True red, False blue
        q = deque()
        for st in start:
            q.append(st) 
            l = 0
            v = set()
            while q:
                for j in range(len(q)):
                    cur_node, cur_color = q.popleft()
                    v.add(cur_node)
                    ans[cur_node] = min(ans[cur_node], l)
                    if cur_color and cur_node in sred:
                        for k in sred[cur_node]:
                            if (cur_node, k, cur_color) not in v:
                                v.add((cur_node, k, cur_color))
                                q.append((k, False))
                    elif not cur_color and cur_node in sblue:
                        for k in sblue[cur_node]:
                            if (cur_node, k, cur_color) not in v:
                                v.add((cur_node, k, cur_color))
                                q.append((k, True))
                l += 1
        
        for i in range(n):
            if ans[i] == float('inf'):
                ans[i] = -1
        return ans





# 0 -> 1 -> 2

# 0 -> 1 <= 2

# 0 -> 1 -> 2 -> 3 -> 4
#        => 2 => 3
#      A        ||
#       ========
