class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ones = []
        for i, n in enumerate(nums):
            if n == 1:
                ones.append(i)
        # print(ones)
        if goal == 0:
            ans = 0
            for i in range(len(ones)):
                if i == 0:
                    zeros = ones[i]
                else:
                    zeros = ones[i] - ones[i - 1] - 1
                ans += (zeros + 1) * zeros // 2

            zeros = len(nums) - ones[-1] - 1 if ones else len(nums)
            ans += (zeros + 1) * zeros // 2
            return ans

        n = len(ones)
        if goal > n:
            return 0

        ans = 0
        for l in range(n - goal + 1):
            r = l + goal - 1
            if l > 0:
                zerosl = ones[l] - ones[l - 1] - 1
            elif l == 0:
                zerosl = ones[l]
            if r < n - 1:
                zerosr = ones[r + 1] - ones[r] - 1
            elif r == n - 1:
                zerosr = len(nums) - ones[r] - 1

            # print(zerosl, zerosr)
            ans += (zerosl + 1) * (zerosr + 1)
        return ans