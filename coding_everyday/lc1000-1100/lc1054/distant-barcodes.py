class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = []
        s = defaultdict(int)
        for i in barcodes:
            s[i] += 1
        
        for k in s:
            freq.append([k, s[k]])

        freq = sorted(freq, key=lambda x: -x[1])

        odd, even = deque(), deque()

        total = []
        for i, f in freq:
            total.extend([i] * f)
        n = len(total)
        for i in range(n):
            # 6: 0-2 3-5
            # 7: 0-3 4-6
            # 8: 0-3 4-7
            if i <= (n + 1) // 2 - 1:
                odd.append(total[i])
            else:
                even.append(total[i])

        # print(odd, even)
        ans = []
        for i in range(n):
            if i % 2 == 0:
                ans.append(odd.popleft())
            else:
                ans.append(even.popleft())
            
        return ans

# 3:2
# 4:2
# 5:2
# 1:1
# 1 2 1 2 1 2 3 4 3 4 5 1 5
