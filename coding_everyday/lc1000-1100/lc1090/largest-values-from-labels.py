class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        n = len(values)
        vl = []

        for i in range(n):
            vl.append((values[i], labels[i]))
        
        vl = sorted(vl, key=lambda x: -x[0])

        cnt = 0
        ans = 0
        use = defaultdict(int)
        i = 0
        while cnt < numWanted and i < n:
            label = vl[i][1]
            if use[label] < useLimit:
                use[label] += 1
                ans += vl[i][0]
                cnt += 1
            i += 1
            
        return ans
