class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens = sorted(tokens)
        n = len(tokens)
        score = 0
        max_score = 0
        l, r = 0, n - 1
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                max_score = max(max_score, score)
                l += 1
            elif score > 0:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break

        return max_score

# 55 71 82 - 54
