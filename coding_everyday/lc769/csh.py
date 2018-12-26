class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        orig = sorted(arr)
        cnt = 0
        sum_orig = sum_arr = 0
        while arr:
            sum_orig += orig.pop(0)
            sum_arr += arr.pop(0)
            if sum_orig == sum_arr:
                cnt += 1
                sum_orig = sum_arr = 0

        # for idx, i in enumerate(arr):
        #     sum_orig += orig[idx]
        #     sum_arr += i
        #     if sum_orig == sum_arr:
        #         cnt += 1
        #         sum_orig = sum_arr = 0

        return cnt


if __name__ == "__main__":
    sol = Solution()
    arr = [1,0,2,3,4]
    print sol.maxChunksToSorted(arr)
