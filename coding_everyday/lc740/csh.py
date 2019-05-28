import collections

class Solution(object):
    def deleteAndEarn(self, nums):
        if not nums:
            return 0
        count = collections.defaultdict(int)
        for x in nums:
            count[x] += x
        max_num = max(nums)
        rst = [0 for _ in range(max_num + 2)]
        rst[max_num] = count[max_num]
        for i in range(max_num - 1, -1, -1):
            rst[i] = max(count[i] + rst[i + 2], rst[i + 1])

        return rst[0]


if __name__ == "__main__":
    sol = Solution()
#     nums = [71,43,93,55,30,46,48,73,81,97,98,47,41,7,1,44,82,15,76,18,3,93,12,69,76,38,99,33,38,67,87,93,5,61,60,16,96,86,82,64,69,65,79,26,5,16,27,87,41,24,9,51,60,21,98,80,19,18,58,31,22,52,72,29,23,100,53,57,50,77,5,49,88,34,15,58,60,11,77,1,17,71,73,56,43,87,15,87,30,84,88,88,32,60,86,100,20,72,70,4,54,97,42,99,49,38,27,22,29,95,64,28,48,99,32,91,91,31,24,18,30,8,84,40,75,34,47,90,32,72,56,37,80,47,85,77,75,85,86,88,46,50,1,87,9,14,13,28,51,43,86,72,50,55,69,61,97,60,74,99,86,49,20,68,5,34,30,91,95,67,32,12,70,59,100,58,46,24,56,76,21,77,76,86,69,93,68,25,45,87,91,14,26,39,44,4,13,12,97,73,64,97,28,66,4,20,44,72,1,50,30,39,98,66,17,44,80,48,49,78,49,81,61,39,93,62,18,77,89,43,46,5,80,70,76,66,54,16,41,70,28,2,57,11,86,94,7,94,73,16,100,6,47,54,38,50,23,21,55,23,47,60,97,29,53,17,58,77,100,94,4,37,64,36,16,20,22,94,53,45,16,77,24,81,10,38,24,86,43,42,58,3,99,44,63,86,35,93,24,80,84,95,87,53,94,78,10,55,68,69,99,51,53,55,33,9,2,91,42,45,95,88,75,32,38,83,97,82,73,83,34,57,37,31,16,71,12,34,47,46,21,98,27,13,15,34,2,78,84,36,46,67,71,70,48,85,82,33,42,82,2,48,24,16,62,62,33,27,41,63,65,60,78,36,56,24,27,60,24,66,40,47,68,22,84,52,74,44,87,100,18,62,94,56,15,95,17,74,8,2,81,59,5,92,45,82,64,99,93,91,21,55,30,41,82,61,56,83,80,66,96,16,51,89,90,26,58,87,83,46,15,94,43,82,13,97,67,67,91,62,90,60,36,20,37,93,24,82,3,6,28,19,6,64,93,39,50,34,9,37,32,97,29,10,45,18,37,37,10,40,91,15,5,69,57,85,18,76,66,13,11,60,89,49,34,33,35,7,51,11,8,76,21,9,22,8,100,58,62,8]
    nums = [1]
    print sol.deleteAndEarn(nums)
