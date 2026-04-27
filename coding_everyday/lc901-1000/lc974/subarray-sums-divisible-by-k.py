class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = [0] * k
        count[0] = 1

        n = len(nums)
        pre_mod = 0
        for i in range(n):
            pre_mod = (pre_mod + nums[i]) % k
            count[pre_mod] += 1

        ans = 0
        for i in count:
            if i > 1:
                ans += i * (i - 1) // 2
        return ans