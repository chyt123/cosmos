from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        indices = [idx for idx, i in enumerate(seats) if i == 1]
        longest = 0
        for i in range(1, len(indices)):
            longest = max(longest, (indices[i] - indices[i - 1]) // 2)
        longest = max(longest, indices[0])
        longest = max(longest, len(seats) - indices[-1] - 1)
        return longest


if __name__ == "__main__":
    sol = Solution()
    seats = [1, 0, 0, 0]
    seats = [1, 0, 0, 0, 1, 0, 1]
    print(sol.maxDistToClosest(seats))
