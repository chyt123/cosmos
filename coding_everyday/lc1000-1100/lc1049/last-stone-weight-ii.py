class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        diff = set()
        for s in stones:
            if not diff:
                diff = {s, -s}
                continue
            tmp = set()
            for i in diff:
                tmp.add(i + s)
                tmp.add(i - s)
            diff = tmp
            # print(diff)
 
        ans = float('inf')
        for i in diff:
            ans = min(ans, abs(i))
        return ans
# 21, 26, 31, 33, 40
# 19 26 31 33
# 2 7 4 1 8 1

# 2 -2 
