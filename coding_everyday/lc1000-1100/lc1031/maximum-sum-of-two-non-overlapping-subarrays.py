class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        # ans = 0
        # n = len(nums)

        # max_sum = 0
        # for i in range(n - firstLen - secondLen + 1):
        #     sum_a = sum(nums[i: i + firstLen])
        #     for j in range(i + firstLen, n - secondLen + 1):
        #         sum_b = sum(nums[j: j + secondLen])
        #         max_sum = max(max_sum, sum_a + sum_b)

        # for i in range(n - firstLen - secondLen + 1):
        #     sum_b = sum(nums[i: i + secondLen])
        #     for j in range(i + secondLen, n - firstLen + 1):
        #         sum_a = sum(nums[j: j + firstLen])
        #         max_sum = max(max_sum, sum_a + sum_b)
        # return max_sum

        def cal_ans(first_len, second_len):
            ans = 0
            n = len(nums)
            lmaxsum = [0] * n
            rmaxsum = [0] * n

            curlsum = sum(nums[:first_len])
            lmaxsum[first_len - 1] = curlsum
            for i in range(first_len, n):
                curlsum += nums[i] - nums[i - first_len]
                lmaxsum[i] = max(lmaxsum[i - 1], curlsum)

            currsum = sum(nums[n - second_len:])
            rmaxsum[n - second_len] = currsum
            for i in range(n - second_len - 1, -1, -1):
                currsum += nums[i] - nums[i + second_len]
                rmaxsum[i] = max(rmaxsum[i + 1], currsum)

            for i in range(first_len - 1, n - second_len):
                ans = max(ans, lmaxsum[i] + rmaxsum[i + 1])

            print(lmaxsum, rmaxsum)
            return ans

        return max(cal_ans(firstLen, secondLen), cal_ans(secondLen, firstLen))