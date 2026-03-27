class Solution:
    def soupServings(self, N: int) -> float:
        q = N // 25
        if q >= 500:
            return 1
        if N - q * 25 > 0:
            q += 1
        self.mem = {}
        return self.dp(q, q)

    def dp(self, x, y):
        if (x, y) not in self.mem:
            if x <= 0 or y <= 0:
                if x <= 0 and y <= 0:
                    ans = 0.5
                elif y > 0:
                    ans = 1.0
                elif x > 0:
                    ans = 0.0
            else:

                dp1 = self.dp(x - 4, y)
                dp2 = self.dp(x - 3, y - 1)
                dp3 = self.dp(x - 2, y - 2)
                dp4 = self.dp(x - 1, y - 3)
                ans = 0.25 * (dp1 + dp2 + dp3 + dp4)
            self.mem[(x, y)] = ans
        return self.mem[(x, y)]


if __name__ == "__main__":
    sol = Solution()
    N = 50
    print(sol.soupServings(N))
