MOD = 10**9+7

class Solution:
    def knightDialer(self, n: int) -> int:

        mvt = {
            0:[4,6],
            1:[6,8],
            2:[7,9],
            3:[4,8],
            4:[3,9,0],
            5:[],
            6:[0,1,7],
            7:[2,6],
            8:[1,3],
            9:[2,4]
        }
        cnt = [
            [1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0,0,0],
        ]
        for i in range(1,n):
            cur = i % 2
            pre = (i + 1) % 2
            for j in range(10):
                cnt[cur][j] = 0
                for k in mvt[j]:
                    cnt[cur][j] += cnt[pre][k]

        return sum(cnt[(n + 1) % 2]) % MOD

