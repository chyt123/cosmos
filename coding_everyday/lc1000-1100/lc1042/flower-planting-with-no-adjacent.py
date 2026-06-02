class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        for fr, to in paths:
            adj[fr].add(to)
            adj[to].add(fr)

        colors = [0] * (n + 1)

        for i in range(1, n + 1):
            neib_set = set()
            for neib in adj[i]:
                neib_set.add(colors[neib])
            
            for j in range(1, 5):
                if j not in neib_set:    
                    colors[i] = j
                    break
        
        return colors[1:]
