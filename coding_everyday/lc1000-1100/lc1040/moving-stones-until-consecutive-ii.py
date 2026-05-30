class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        n = len(stones)
        stones.sort()

        l = 0
        r = l

        maxcon = 0
        while r < n:
            if stones[r] - stones[l] < n:
                r += 1
            else:
                l += 1
            maxcon = max(maxcon, r - l)
        
        minimum = n - maxcon

        if ((stones[-2] - stones[0] == n - 2 and stones[-1] - stones[1] > n - 1) or \
            (stones[-1] - stones[1] == n - 2 and stones[-2] - stones[0] > n - 1)) and \
          stones[-1] - stones[0] != n - 1:
            minimum += 1
        
        left_space = stones[1] - stones[0] - 1
        right_space = stones[-1] - stones[-2] - 1
        maximum = stones[-1] - stones[0] - 1 - min(left_space, right_space) - (n - 2)
        return [minimum, maximum]
 
# [4, 7, 9]
# [1, 2, 3, 4, 5]
# [1, 3, 4, 7, 11]
# [3, 4, 5, 6, 10]
# # o . . o . o
# # o o o o . . . o
# # o . o o . . o . . . o
# # o . o . . o . . . o
# # o . . . o . . . o . . . o

# [1, 5, 9, 13]
