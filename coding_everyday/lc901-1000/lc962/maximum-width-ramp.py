class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        dec = [(nums[0], 0)]
        for i in range(1, n):
            if nums[i] < dec[-1][0]:
                dec.append((nums[i],i))

        r = n - 1
        ans = 0
        while len(dec):
            if nums[r] >= dec[-1][0]:
                val, idx = dec.pop()
                ans = max(r - idx, ans)
            else:
                r -= 1
        return ans

# 9 7 10 5 3 1 8 0

# 9 7 5 3 1 0