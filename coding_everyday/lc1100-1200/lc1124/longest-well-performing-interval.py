class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        presum = [0] * (n + 1)
        for i in range(n):
            hours[i] = 1 if hours[i] > 8 else -1 
            presum[i + 1] += presum[i] + hours[i]

        ma = 0
        for i in range(1, n + 1):
            for j in range(i):
                if presum[j] < presum[i]:
                    ma = max(ma, i - j)
                    break
        # print(presum)
        return ma


#  [9,9,6 ,6 ,0 ,9,6 ,6 ,9 ,9 ,6,9]
#  [1,1,-1,-1,-1,1,-1,-1, 1,1,-1,1]
# 0[1,2,1, 0, -1,0,-1,-2,-1,0,-1,0]

# 0[-1,-1,1,1]
# 0[-1,-2,-1,0]
