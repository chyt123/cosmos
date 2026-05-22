class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        max_number = 0

        for i in values:
            max_score = max(max_score, max_number + i)
            max_number = max(max_number, i) - 1

        return max_score
