class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for n in nums:
            even_sum += n if n % 2 == 0 else 0

        ans = list()
        for v, idx in queries:
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]
            nums[idx] += v
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]

            ans.append(even_sum)

        return ans
