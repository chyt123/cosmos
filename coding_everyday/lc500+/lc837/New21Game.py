class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        pos = [0 for _ in range(N+W+1)]
        for i in range(K, N+1):
            pos[i] = 1
        pos[K-1] = min(1, (N-K+1)/W)
        for i in range(K-2, -1, -1):
            pos[i] = pos[i+1]/W + pos[i+1] - pos[i+1+W]/W
        # print(pos)
        return pos[0]


if __name__ == "__main__":
    sol = Solution()
    N = 21
    # K = 17
    W = 10
    for K in range(11, 22):
        print(sol.new21Game(N, K, W))
